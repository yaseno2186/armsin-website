/* Armsin homepage: the 3D retro PC in the hero.
   Model, lighting bake, shadow and poster come from Blender (assets/home/).
   This file is a small WebGL renderer, no library: baked light + live specular
   on the plastic, and a CRT shader on the glass (eyes, blink, scanlines, power-on).
   The scroll push (camera flies into the screen) reads --k from the hero.
   Public API: window.PC3D = { ready: Promise<boolean>, power(), setProgress(k), look(x,y) } */
(function () {
  'use strict';
  var canvas = document.getElementById('pc-canvas');
  var resolveReady, PC3D = window.PC3D = { ready: new Promise(function (r) { resolveReady = r; }) };
  function fail(why) { if (window.console && why) console.info('PC3D fallback:', why); var h = document.documentElement; h.classList.remove('pc-live'); h.classList.add('pc-fallback'); resolveReady(false); }
  if (!canvas) return fail('no canvas');
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var gl = canvas.getContext('webgl', { alpha: true, antialias: true, premultipliedAlpha: true, powerPreference: 'high-performance' });
  if (!gl) return fail('no webgl');

  /* ---------- tiny mat4 helpers (column-major) ---------- */
  function persp(fovy, asp, n, f) { var t = 1 / Math.tan(fovy / 2), nf = 1 / (n - f);
    return [t / asp, 0, 0, 0, 0, t, 0, 0, 0, 0, (f + n) * nf, -1, 0, 0, 2 * f * n * nf, 0]; }
  function sub(a, b) { return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]; }
  function cross(a, b) { return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]; }
  function norm(a) { var l = Math.hypot(a[0], a[1], a[2]) || 1; return [a[0] / l, a[1] / l, a[2] / l]; }
  function dot(a, b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }
  function lookAt(e, c, up) { var z = norm(sub(e, c)), x = norm(cross(up, z)), y = cross(z, x);
    return [x[0], y[0], z[0], 0, x[1], y[1], z[1], 0, x[2], y[2], z[2], 0, -dot(x, e), -dot(y, e), -dot(z, e), 1]; }
  function mul(a, b) { var o = new Array(16); for (var i = 0; i < 4; i++) for (var j = 0; j < 4; j++) {
    o[j * 4 + i] = a[i] * b[j * 4] + a[4 + i] * b[j * 4 + 1] + a[8 + i] * b[j * 4 + 2] + a[12 + i] * b[j * 4 + 3]; } return o; }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function lerp3(a, b, t) { return [lerp(a[0], b[0], t), lerp(a[1], b[1], t), lerp(a[2], b[2], t)]; }
  function clamp(x, a, b) { return Math.min(b, Math.max(a, x)); }
  function ease(x) { return x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; }

  /* ---------- shaders ---------- */
  var VS = 'attribute vec3 aP;attribute vec3 aN;attribute vec2 aU;uniform mat4 uMVP;uniform mat4 uM;uniform vec3 uLo;uniform vec3 uHi;' +
    'varying vec3 vN;varying vec3 vW;varying vec2 vU;void main(){vec3 p=uLo+(aP*.5+.5)*(uHi-uLo);vec4 w=uM*vec4(p,1.);vW=w.xyz;' +
    'vN=normalize(mat3(uM)*aN);vU=aU;gl_Position=uMVP*vec4(p,1.);}';
  var COMMON = 'precision mediump float;varying vec3 vN;varying vec3 vW;varying vec2 vU;uniform vec3 uEye;' +
    'vec3 L1=normalize(vec3(-3.6,-3.,4.)),L2=normalize(vec3(2.5,4.5,2.4)),L3=normalize(vec3(4.4,-2.8,.8));' +
    'float spec(vec3 N,vec3 V,vec3 L,float s){return pow(max(dot(N,normalize(L+V)),0.),s);}' +
    'vec3 tone(vec3 c){c*=1.05;c=c*(2.51*c+.03)/(c*(2.43*c+.59)+.14);return pow(clamp(c,0.,1.),vec3(1./2.2));}';
  var FS_BODY = COMMON + 'uniform sampler2D uT;void main(){vec3 N=normalize(vN);vec3 V=normalize(uEye-vW);' +
    'vec3 b=pow(texture2D(uT,vec2(vU.x,1.-vU.y)).rgb,vec3(2.2));' +
    'float f=pow(1.-max(dot(N,V),0.),5.);' +
    'vec3 s=vec3(1.,.95,.88)*spec(N,V,L1,70.)*.55+vec3(1.,.9,.8)*spec(N,V,L2,40.)*.35+vec3(.85,.92,1.)*spec(N,V,L3,30.)*.08;' +
    'vec3 c=b*1.0+s+f*vec3(.05,.055,.05);gl_FragColor=vec4(tone(c),1.);}';
  var FS_SCREEN = COMMON + 'uniform float uT;uniform float uBlink;uniform vec2 uLook;uniform float uPower;uniform float uPush;' +
    'float cap(vec2 p,vec2 c,float h,float r){p-=c;p.y=max(abs(p.y)-h,0.);return length(p)-r;}' +
    'void main(){vec2 uv=vU;vec2 p=(uv-.5)*vec2(1.54,1.16);vec3 N=normalize(vN);vec3 V=normalize(uEye-vW);' +
    'vec3 col=vec3(.022,.05,.036);' +
    'float h=.155*uBlink;vec2 o=uLook*vec2(.045,.03);' +
    'float d=min(cap(p,vec2(-.2,.02)+o,h,.065),cap(p,vec2(.2,.02)+o,h,.065));' +
    'vec3 eye=vec3(.23,1.,.31);float fill=smoothstep(.006,-.004,d);float glow=exp(-max(d,0.)*16.)*.42;' +
    'col+=eye*glow*(1.-uPush)+eye*fill*(1.-uPush)*(.9+.1*sin(uT*3.));' +
    /* push: screen becomes a lit terminal page */
    'vec2 g=abs(fract(p*vec2(14.,10.5))-.5);float grid=smoothstep(.47,.5,max(g.x,g.y));' +
    'col=mix(col,vec3(.07,.16,.11)+vec3(.12,.4,.2)*grid*.35,uPush);' +
    'float sl=.9+.1*sin(gl_FragCoord.y*2.1);col*=sl;' +
    'vec2 q=abs(uv-.5)*2.;float vig=1.-pow(max(q.x,q.y),6.)*.55;col*=vig;' +
    /* glass: key-light reflection + soft top sheen */
    'col+=vec3(1.)*pow(max(dot(N,normalize(L1+V)),0.),220.)*.6+vec3(.6,.7,.65)*smoothstep(.0,.9,uv.y-uv.x*.35)*.05;' +
    /* power-on: a bright line opens into the picture */
    'float open=smoothstep(0.,.5,uPower);float band=abs(uv.y-.5)*2.;' +
    'float vis=step(band,max(open,.012));col=mix(vec3(0.),col,vis);' +
    'col+=vec3(.75,1.,.85)*(1.-smoothstep(0.,.02,abs(uv.y-.5)))*(1.-smoothstep(.3,.7,uPower))*step(abs(uv.x-.5),.5*smoothstep(0.,.25,uPower));' +
    'gl_FragColor=vec4(col,1.);}';
  var VS_SH = 'attribute vec2 aQ;uniform mat4 uMVP;uniform float uS;varying vec2 vQ;void main(){vQ=aQ*.5+.5;gl_Position=uMVP*vec4(aQ*uS*.5,.002,1.);}';
  var FS_SH = 'precision mediump float;varying vec2 vQ;uniform sampler2D uT;uniform float uA;void main(){float a=texture2D(uT,vec2(vQ.x,1.-vQ.y)).a*uA;gl_FragColor=vec4(0.,0.,0.,a);}';

  function prog(vs, fs) {
    function sh(t, s) { var o = gl.createShader(t); gl.shaderSource(o, s); gl.compileShader(o);
      if (!gl.getShaderParameter(o, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(o)); return o; }
    var p = gl.createProgram(); gl.attachShader(p, sh(gl.VERTEX_SHADER, vs)); gl.attachShader(p, sh(gl.FRAGMENT_SHADER, fs));
    gl.linkProgram(p); if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p));
    var u = {}, n = gl.getProgramParameter(p, gl.ACTIVE_UNIFORMS);
    for (var i = 0; i < n; i++) { var a = gl.getActiveUniform(p, i); u[a.name] = gl.getUniformLocation(p, a.name); }
    return { p: p, u: u, a: { P: gl.getAttribLocation(p, 'aP'), N: gl.getAttribLocation(p, 'aN'), U: gl.getAttribLocation(p, 'aU'), Q: gl.getAttribLocation(p, 'aQ') } };
  }
  function tex(img) { var t = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, t);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, img); gl.generateMipmap(gl.TEXTURE_2D);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR); return t; }
  function loadImg(src) { return new Promise(function (ok, no) { var i = new Image(); i.onload = function () { ok(i); }; i.onerror = no; i.src = src; }); }

  var base = canvas.getAttribute('data-base') || 'assets/home/';
  Promise.all([fetch(base + 'pc.bin').then(function (r) { if (!r.ok) throw new Error('bin ' + r.status); return r.arrayBuffer(); }),
    loadImg(base + 'pc-bake.webp'), loadImg(base + 'pc-shadow.webp')]).then(function (res) { start(res[0], res[1], res[2]); })
    .catch(function (e) { fail(e && e.message); });

  function start(buf, bakeImg, shImg) {
    var S;
    try {
      var hl = new DataView(buf).getUint32(0, true), head = JSON.parse(new TextDecoder().decode(new Uint8Array(buf, 4, hl))), bin = buf.slice(4 + hl);
      var P = { body: prog(VS, FS_BODY), screen: prog(VS, FS_SCREEN), sh: prog(VS_SH, FS_SH) };
      var meshes = {};
      head.meshes.forEach(function (m) {
        var vb = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, vb); gl.bufferData(gl.ARRAY_BUFFER, new Uint8Array(bin, m.vo, m.nv * head.stride), gl.STATIC_DRAW);
        var ib = gl.createBuffer(); gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, ib); gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(bin, m.io, m.ni), gl.STATIC_DRAW);
        meshes[m.name] = { vb: vb, ib: ib, n: m.ni };
      });
      var quad = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, quad); gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW);
      S = { head: head, P: P, m: meshes, quad: quad, tBake: tex(bakeImg), tSh: tex(shImg) };
    } catch (e) { return fail(e.message); }
    canvas.addEventListener('webglcontextlost', function (e) { e.preventDefault(); running = false; fail('context lost'); });
    run(S);
  }

  /* ---------- state driven from outside ---------- */
  var k = 0, lookT = [0, 0], look = [0, 0], power = reduce ? 1 : 0, powerT0 = -1, running = true, visible = true;
  PC3D.setProgress = function (v) { k = clamp(v, 0, 1); };
  PC3D.look = function (x, y) { lookT = [clamp(x, -1, 1), clamp(y, -1, 1)]; };
  PC3D.power = function () { if (powerT0 < 0) powerT0 = performance.now(); };

  function run(S) {
    var h = S.head, cam0 = h.cam.pos, tgt0 = h.cam.target, fov = 2 * Math.atan(h.cam.sensor / 2 / h.cam.lens);
    var scrC = [0, h.screen.y, (h.screen.z0 + h.screen.z1) / 2];
    var W = 0, H = 0, dpr = 1, scale = 1, nextBlink = 1.5, blinkT = -1, hopT = -1, nextHop = 4.5, t0 = performance.now(), frames = 0, slow = 0, first = true;
    function size() {
      var r = canvas.getBoundingClientRect(); dpr = Math.min(window.devicePixelRatio || 1, innerWidth < 900 ? 1.5 : 1.75) * scale;
      W = Math.max(1, Math.round(r.width * dpr)); H = Math.max(1, Math.round(r.height * dpr));
      if (canvas.width !== W || canvas.height !== H) { canvas.width = W; canvas.height = H; }
    }
    addEventListener('resize', size); size();
    if ('IntersectionObserver' in window) new IntersectionObserver(function (e) { visible = e[0].isIntersecting; if (visible) loop(); }).observe(canvas);
    document.addEventListener('visibilitychange', function () { if (!document.hidden) loop(); });

    // where the PC sits in the viewport (in css px): desktop right, mobile top-right
    function frame() {
      var w = W / dpr, hh = H / dpr, m = w < 900;
      if (m) { var s = Math.min(w * .5, hh * .3); return { cx: w - s * .42, cy: 140 + s * .5, s: s }; }
      var s2 = Math.min(w * .5, hh * .98); return { cx: w * .74, cy: hh * .52, s: s2 };
    }
    var raf = 0;
    function loop() { if (!raf && running) raf = requestAnimationFrame(draw); }
    function draw(now) {
      raf = 0; if (!running) return;
      var t = (now - t0) / 1000, dt;
      // performance guard: if frames are slow, drop resolution once, then fall back to the poster
      frames++; if (S.last) { dt = now - S.last; if (!document.hidden && frames > 8 && frames < 90 && dt > 34 && dt < 250) slow++; }  // ignore throttled (background) frames
      S.last = now;
      if (slow > 30) { if (scale > .7) { scale = .66; slow = 0; frames = 0; size(); } else { running = false; return fail('slow device'); } }
      if (powerT0 >= 0) power = clamp((now - powerT0) / 900, 0, 1);
      look[0] += (lookT[0] - look[0]) * .08; look[1] += (lookT[1] - look[1]) * .08;
      // blink
      var blink = 1;
      if (!reduce) { if (t > nextBlink) { blinkT = t; nextBlink = t + 2.8 + Math.random() * 2.4; }
        var bk = (t - blinkT) / .16; if (bk >= 0 && bk < 1) blink = Math.max(.06, Math.abs(1 - 2 * bk)); }
      // hop with squash and stretch (it hops, never walks)
      var hz = 0, sq = 1;
      if (!reduce && k < .02) {
        if (power >= 1 && t > nextHop) { hopT = t; nextHop = t + 6 + Math.random() * 3; }
        var hk = (t - hopT) / .55;
        if (hk >= 0 && hk < 1) { if (hk < .14) sq = 1 - .13 * Math.sin(hk / .14 * Math.PI); else if (hk > .86) sq = 1 - .1 * Math.sin((hk - .86) / .14 * Math.PI);
          else { hz = Math.sin((hk - .14) / .72 * Math.PI) * .45; sq = 1.05; } }
      }
      // camera: idle sway + pointer, then push into the screen with scroll
      var kz = ease(clamp(k / .78, 0, 1));
      var sway = reduce ? 0 : Math.sin(t * .35) * .035;
      var yaw = (look[0] * .16 + sway) * (1 - kz), pitch = look[1] * .08 * (1 - kz);
      var rel = sub(cam0, tgt0), cy = Math.cos(yaw), sy = Math.sin(yaw);
      var e0 = [tgt0[0] + rel[0] * cy - rel[1] * sy, tgt0[1] + rel[0] * sy + rel[1] * cy, tgt0[2] + rel[2] + pitch * 2];
      var e1 = [scrC[0], scrC[1] - 1.05, scrC[2]];
      var eye = lerp3(e0, e1, kz), tgt = lerp3(tgt0, scrC, kz);
      var F = frame(), vw = W / dpr, vh = H / dpr;
      var fc = { cx: lerp(F.cx, vw / 2, kz), cy: lerp(F.cy, vh / 2, kz), s: lerp(F.s, Math.max(vw, vh) * 1.02, kz) };
      var proj = persp(fov, 1, .05, 60);
      var sx = fc.s / vw, syy = fc.s / vh, ox = 2 * fc.cx / vw - 1, oy = 1 - 2 * fc.cy / vh;
      var post = [sx, 0, 0, 0, 0, syy, 0, 0, 0, 0, 1, 0, ox, oy, 0, 1];
      var VP = mul(post, mul(proj, lookAt(eye, tgt, [0, 0, 1])));
      var M = [2 - sq, 0, 0, 0, 0, 2 - sq, 0, 0, 0, 0, sq, 0, 0, 0, hz, 1];
      var MVP = mul(VP, M);

      gl.viewport(0, 0, W, H); gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
      // shadow (fades and shrinks while hopping)
      gl.disable(gl.DEPTH_TEST); gl.enable(gl.BLEND); gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);
      var ps = S.P.sh; gl.useProgram(ps.p); gl.bindBuffer(gl.ARRAY_BUFFER, S.quad);
      gl.enableVertexAttribArray(ps.a.Q); gl.vertexAttribPointer(ps.a.Q, 2, gl.FLOAT, false, 0, 0);
      var shS = 7 * (1 - hz * .25); gl.uniformMatrix4fv(ps.u.uMVP, false, VP); gl.uniform1f(ps.u.uS, shS); gl.uniform1f(ps.u.uA, (1 - hz * .9) * (1 - kz));
      gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, S.tSh); gl.uniform1i(ps.u.uT, 0);
      gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4); gl.disableVertexAttribArray(ps.a.Q);
      gl.disable(gl.BLEND); gl.enable(gl.DEPTH_TEST);
      function mesh(pp, m) {
        gl.useProgram(pp.p); gl.bindBuffer(gl.ARRAY_BUFFER, m.vb); gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, m.ib);
        gl.enableVertexAttribArray(pp.a.P); gl.vertexAttribPointer(pp.a.P, 3, gl.SHORT, true, 14, 0);
        gl.enableVertexAttribArray(pp.a.N); gl.vertexAttribPointer(pp.a.N, 3, gl.BYTE, true, 14, 6);
        if (pp.a.U >= 0) { gl.enableVertexAttribArray(pp.a.U); gl.vertexAttribPointer(pp.a.U, 2, gl.UNSIGNED_SHORT, true, 14, 10); }
        gl.uniformMatrix4fv(pp.u.uMVP, false, MVP); gl.uniformMatrix4fv(pp.u.uM, false, M);
        gl.uniform3fv(pp.u.uLo, h.lo); gl.uniform3fv(pp.u.uHi, h.hi); gl.uniform3fv(pp.u.uEye, eye);
      }
      mesh(S.P.body, S.m.body); gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, S.tBake); gl.uniform1i(S.P.body.u.uT, 0);
      gl.drawElements(gl.TRIANGLES, S.m.body.n, gl.UNSIGNED_SHORT, 0);
      var sp = S.P.screen; mesh(sp, S.m.screen);
      gl.uniform1f(sp.u.uT, t); gl.uniform1f(sp.u.uBlink, blink); gl.uniform2fv(sp.u.uLook, look);
      gl.uniform1f(sp.u.uPower, power); gl.uniform1f(sp.u.uPush, clamp((k - .55) / .25, 0, 1));
      gl.drawElements(gl.TRIANGLES, S.m.screen.n, gl.UNSIGNED_SHORT, 0);
      if (first) { first = false; resolveReady(true); document.documentElement.classList.add('pc-live'); }
      // keep animating while visible; reduced motion draws only when something changes
      if (visible && !document.hidden && (!reduce || Math.abs(lookT[0] - look[0]) > .001)) loop();
    }
    PC3D.redraw = loop;
    var _sp = PC3D.setProgress; PC3D.setProgress = function (v) { _sp(v); loop(); };
    loop();
  }
})();
