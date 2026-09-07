// Renders the hero's 3D retro-workstation (assets/models/retro-workstation.glb)
// into #hero-model via three.js. Loaded through the pinned importmap in
// index.html's <head> — no npm/build step, just a versioned CDN module.
//
// Motion (see .claude/skills/animate for the reasoning):
//   - Entrance: the model is invisible (`.hero-model { opacity: 0 }` in
//     style.css) until the GLB decodes, then fades in over 400ms — bridges
//     the async load instead of popping in.
//   - Idle: the monitor screen (mesh "screen_code_face") runs a live
//     CanvasTexture loop — code typing itself out with a CRT scanline/glow
//     composite, ported from the Claude Design source. This runs regardless
//     of pointer/hover state.
//   - Pointer (hover-capable devices): the model eases toward a tilt
//     derived from cursor position, on-axis with the cursor on both X and Y
//     (moving the mouse down tilts the model down, not up) — a direct
//     pointer-follow, not an inverted/orbit-camera feel.
//   - Idle sway (touch/coarse-pointer devices, i.e. no cursor to react to):
//     a slow sinusoidal rotation (Float, see .claude/skills/animation-vocabulary)
//     so the model still reads as alive on mobile, matching the always-on
//     hero-float/code-float drift already running in style.css.
// Reduced motion: the model still fades in, but skips both the pointer tilt
// and the idle sway — fewer/gentler, not zero.
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

(function initHeroModel() {
  var container = document.getElementById('hero-model');
  if (!container) return;

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var canHover = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  container.appendChild(renderer.domElement);

  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(35, 1, 0.1, 100);

  // The model bakes its own screen glow (screen_light/screen_light_core
  // nodes), so scene lighting stays neutral/modest here rather than adding
  // more — a second light source on top of that geometry over-exposed it
  // to a blown-out white blob.
  scene.add(new THREE.HemisphereLight(0xd6e8dd, 0x0a0e0c, 1.1));
  var key = new THREE.DirectionalLight(0x39d97a, 1.4);
  key.position.set(3, 4, 5);
  scene.add(key);
  var fill = new THREE.DirectionalLight(0xe0a458, 0.5);
  fill.position.set(-4, 2, -3);
  scene.add(fill);

  var modelGroup = new THREE.Group();
  scene.add(modelGroup);

  function fit() {
    var w = container.clientWidth || 1;
    var h = container.clientHeight || 1;
    renderer.setSize(w, h);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }
  fit();
  new ResizeObserver(fit).observe(container);

  var targetX = 0;
  var targetY = 0;
  if (canHover && !reduceMotion) {
    window.addEventListener('pointermove', function (e) {
      targetX = (e.clientX / window.innerWidth - 0.5) * 2;
      targetY = (e.clientY / window.innerHeight - 0.5) * 2;
    });
  }

  var clock = new THREE.Clock();

  renderer.setAnimationLoop(function () {
    var dt = clock.getDelta();
    if (!reduceMotion) {
      var lerp = 1 - Math.pow(0.001, dt); // frame-rate-independent ease toward target
      if (canHover) {
        // Direct pointer-follow tilt: same sign as cursor movement on both
        // axes, so the model leans the way the cursor actually moved.
        modelGroup.rotation.y += (targetX * 0.35 - modelGroup.rotation.y) * lerp;
        modelGroup.rotation.x += (targetY * 0.18 - modelGroup.rotation.x) * lerp;
      } else {
        // No pointer to react to (touch/coarse input) — a slow, gentle
        // idle sway (Float, per animation-vocabulary) so the model reads as
        // alive instead of frozen, matching the CSS hero-float/code-float
        // drift already running elsewhere in this hero on mobile.
        var t = clock.elapsedTime;
        modelGroup.rotation.y += (Math.sin(t * 0.35) * 0.10 - modelGroup.rotation.y) * lerp;
        modelGroup.rotation.x += (Math.sin(t * 0.27 + 1.3) * 0.05 - modelGroup.rotation.x) * lerp;
      }
    }
    renderer.render(scene, camera);
  });

  // Ported from the Claude Design source (retro-workstation.html) that built
  // this model. The GLB only ever carries a static baked snapshot of this
  // canvas (glTF export can't capture a setInterval-driven texture), so the
  // typing/CRT loop has to be re-created here at runtime against the mesh
  // the GLB already ships (`screen_code_face`) — same content, same look,
  // just swapping its material from the baked PNG to a live CanvasTexture.
  function startScreenAnimation(screenFace) {
    var SC_W = 728, SC_H = 556;
    var scr = document.createElement('canvas');
    scr.width = SC_W; scr.height = SC_H;
    var cx = scr.getContext('2d');
    var buf = document.createElement('canvas');
    buf.width = SC_W; buf.height = SC_H;
    var bx = buf.getContext('2d');
    var scrTex = new THREE.CanvasTexture(scr);
    scrTex.colorSpace = THREE.SRGBColorSpace;
    scrTex.anisotropy = 4;

    var HEADER = [
      '// Armsin — portfolio pipeline',
      '// author: Yass',
      'package com.armsin.portfolio;',
      '',
      'public class ArmsinPortfolio {',
      '  final String company = "Armsin";',
      '  final String dev = "Yass";',
      '  final List<Project> work = list();',
      '  final List<String> roadmap = list();',
      '  void add(String t) {',
      '    work.add(new Project(t));',
      '  }',
      '  void goal(String g) {',
      '    roadmap.add(g);',
      '  }',
      '',
      '  public static void main(String[] a) {',
      '    new ArmsinPortfolio().publish();',
      '  }',
      '',
      '  void publish() {',
    ];
    var P1 = ['Atlas', 'Orbit', 'Harbor', 'Nimbus', 'Vertex', 'Lumen', 'Quartz', 'Beacon', 'Cinder',
      'Delta', 'Ember', 'Falcon', 'Grid', 'Helix', 'Ion', 'Junction', 'Kilo', 'Lattice', 'Meridian'];
    var P2 = ['Ledger', 'Console', 'Router', 'Pipeline', 'Studio', 'Gateway', 'Engine', 'Vault',
      'Dashboard', 'Scheduler', 'Registry', 'Compiler', 'Monitor', 'Kernel', 'Bridge'];
    var GOALS = [
      'More reach for our clients',
      'Faster shipment, every time',
      'More efficient delivery',
      'Improve with every release',
      'Cleaner code, fewer bugs',
      'Answer clients the same day',
      'Automate the boring parts',
      'Ship weekly, not yearly',
      'Raise the quality bar',
      'Grow the Armsin team',
    ];
    var cycle = 0;
    function buildCycle() {
      var lines = HEADER.slice();
      for (var i = 0; i < 10; i++) {
        var k = cycle * 10 + i;
        lines.push('    add("' + P1[k % P1.length] + ' ' + P2[(k * 5 + 2) % P2.length] + '");');
      }
      lines.push('  }', '', '  void goals() {');
      GOALS.forEach(function (g) { lines.push('    goal("' + g + '");'); });
      lines.push('  }', '}', '');
      cycle++;
      return lines;
    }
    var queue = buildCycle(), qi = 0;
    function nextLine() { return qi < queue.length ? queue[qi++] : ''; }

    var APERTURE = 0.78;
    var LINE_H = 46, PAD_X = 40, PAD_Y = 34, MAX_LINES = Math.floor((SC_H - PAD_Y * 2) / LINE_H);
    var done = [];
    var cur = nextLine(), ci = 0, wait = 0, scrollOff = 0;

    function drawLine(text, y) {
      var chw = bx.measureText('M').width;
      var x = PAD_X;
      var tokens = text.split(/(\b|(?=[.,;(){}<>:]))/);
      var inStr = false;
      for (var t = 0; t < tokens.length; t++) {
        var tok = tokens[t];
        if (!tok) continue;
        var col = '#7dff89';
        if (tok.indexOf('"') !== -1) inStr = !inStr;
        if (inStr || tok.indexOf('"') !== -1) col = '#e6ffa0';
        else if (/^(public|private|class|static|void|new|final|import|return)$/.test(tok)) col = '#d3ffdb';
        else if (/^(String|List|ArrayList|ArmsinPortfolio|Project|System|Armsin|Yass)$/.test(tok)) col = '#8fe3ff';
        else if (/^[.,;(){}<>:]+$/.test(tok)) col = '#57c463';
        bx.fillStyle = col;
        bx.shadowColor = 'rgba(90,255,110,0.55)';
        bx.shadowBlur = 9;
        bx.fillText(tok, x, y);
        bx.shadowBlur = 0;
        x += tok.length * chw;
      }
    }
    function paintScreen() {
      bx.fillStyle = '#08170c';
      bx.fillRect(0, 0, SC_W, SC_H);
      bx.font = '33px "SFMono-Regular", "Menlo", "Consolas", monospace';
      bx.textBaseline = 'top';
      bx.save();
      bx.translate(SC_W / 2, SC_H / 2);
      bx.scale(APERTURE, APERTURE);
      bx.translate(-SC_W / 2, -SC_H / 2);

      var visible = done.slice(scrollOff);
      visible.forEach(function (t, i) { drawLine(t, PAD_Y + i * LINE_H); });

      var y = PAD_Y + visible.length * LINE_H;
      var partial = cur.slice(0, ci);
      drawLine(partial, y);
      var chw = bx.measureText('M').width;
      bx.fillStyle = '#9dffa6';
      bx.fillRect(PAD_X + partial.length * chw, y + 3, chw * 0.85, LINE_H - 12);
      bx.restore();
    }

    var CORNER = 26;
    function roundPath(c, x, y, w, hh, r) {
      c.beginPath();
      c.moveTo(x + r, y);
      c.arcTo(x + w, y, x + w, y + hh, r);
      c.arcTo(x + w, y + hh, x, y + hh, r);
      c.arcTo(x, y + hh, x, y, r);
      c.arcTo(x, y, x + w, y, r);
      c.closePath();
    }

    function composite(t) {
      cx.clearRect(0, 0, SC_W, SC_H);
      cx.fillStyle = '#08170c';
      cx.fillRect(0, 0, SC_W, SC_H);

      var STRIP = 4;
      for (var y = 0; y < SC_H; y += STRIP) {
        var p = y / SC_H;
        var dx = Math.sin(t * 0.0016 + p * 7.2) * 3.4 + Math.sin(t * 0.0041 + p * 19) * 1.3;
        var sy = 1 + Math.sin(t * 0.0013 + p * 5.0) * 0.012;
        cx.drawImage(buf, 0, y, SC_W, STRIP, dx, y, SC_W, STRIP * sy);
      }

      var rollY = ((t * 0.055) % (SC_H + 260)) - 130;
      var rg = cx.createLinearGradient(0, rollY - 90, 0, rollY + 90);
      rg.addColorStop(0, 'rgba(90,255,110,0)');
      rg.addColorStop(0.5, 'rgba(120,255,140,0.13)');
      rg.addColorStop(1, 'rgba(90,255,110,0)');
      cx.fillStyle = rg;
      cx.fillRect(0, rollY - 90, SC_W, 180);

      cx.globalAlpha = 0.10;
      cx.fillStyle = '#000';
      for (var yy = 0; yy < SC_H; yy += 6) cx.fillRect(0, yy, SC_W, 3);
      cx.globalAlpha = 1;

      cx.globalCompositeOperation = 'lighter';
      var bg = cx.createRadialGradient(SC_W / 2, SC_H / 2, 0, SC_W / 2, SC_H / 2, SC_H * 0.72);
      bg.addColorStop(0, 'rgba(58,255,96,0.10)');
      bg.addColorStop(0.55, 'rgba(46,220,80,0.045)');
      bg.addColorStop(1, 'rgba(30,160,60,0)');
      cx.fillStyle = bg;
      cx.fillRect(0, 0, SC_W, SC_H);
      cx.globalCompositeOperation = 'source-over';

      var vg = cx.createRadialGradient(SC_W / 2, SC_H / 2, SC_H * 0.22, SC_W / 2, SC_H / 2, SC_H * 0.80);
      vg.addColorStop(0, 'rgba(0,0,0,0)');
      vg.addColorStop(1, 'rgba(0,0,0,0.32)');
      cx.fillStyle = vg;
      cx.fillRect(0, 0, SC_W, SC_H);

      cx.globalCompositeOperation = 'destination-in';
      roundPath(cx, 2, 2, SC_W - 4, SC_H - 4, CORNER);
      cx.fillStyle = '#fff';
      cx.fill();
      cx.globalCompositeOperation = 'source-over';

      scrTex.needsUpdate = true;
    }

    var last = 0;
    function typeTick(t) {
      if (t - last < 42) return;
      last = t;
      if (wait > 0) { wait--; paintScreen(); return; }
      if (ci < cur.length) {
        ci += 1 + (Math.random() < 0.35 ? 1 : 0);
        if (ci > cur.length) ci = cur.length;
      } else {
        done.push(cur);
        wait = cur === '' ? 0 : 3;
        if (qi >= queue.length) {
          wait = 30; done = []; scrollOff = 0; queue = buildCycle(); qi = 0;
          cur = nextLine(); ci = 0;
          paintScreen(); return;
        }
        cur = nextLine(); ci = 0;
        if (done.length - scrollOff > MAX_LINES - 1) scrollOff++;
      }
      paintScreen();
    }

    screenFace.material = new THREE.MeshBasicMaterial({
      map: scrTex, toneMapped: false, transparent: true, depthWrite: false,
    });

    if (reduceMotion) {
      // Static resting screen — fewer/gentler, not zero, matching the
      // pointer-tilt's reduced-motion behavior above.
      paintScreen();
      composite(0);
      return;
    }

    var clock2 = 0;
    setInterval(function () {
      clock2 += 40;
      typeTick(clock2);
      composite(clock2);
    }, 40);
  }

  new GLTFLoader().load(
    'assets/models/retro-workstation.glb',
    function (gltf) {
      var object = gltf.scene;
      modelGroup.add(object);

      // Glow/halo meshes (named "*halo*"/"*glow*") are oversized bloom
      // planes meant to bleed past the physical case — including them in
      // the auto-fit box would skew both the centering and the camera
      // distance. Fit off the physical geometry only; the glow still renders.
      var box = new THREE.Box3();
      var glowNamePattern = /halo|glow/i;
      object.traverse(function (o) {
        if (o.isMesh && !glowNamePattern.test(o.name)) {
          box.expandByObject(o);
        }
      });
      if (box.isEmpty()) box.setFromObject(object);
      var sphere = box.getBoundingSphere(new THREE.Sphere());
      object.position.sub(sphere.center);

      // 1.6x padding (not just enough to touch the frame edges) — this
      // model's bounding sphere is dominated by the compact monitor, so a
      // tight fit crops the keyboard/base below the visible fold.
      var dist = sphere.radius / Math.tan((camera.fov * Math.PI) / 360) * 1.6;
      camera.position.set(0, sphere.radius * 0.15, dist);
      camera.lookAt(0, 0, 0);
      // Entrance fade+scale and the resting size (--model-scale) live in
      // style.css (.hero-model.is-loaded) so the mobile override and the
      // reduced-motion variant stay in one place instead of forking here.
      container.classList.add('is-loaded');

      var screenFace = object.getObjectByName('screen_code_face');
      if (screenFace) startScreenAnimation(screenFace);
    },
    undefined,
    function (err) {
      console.warn('hero-model: failed to load retro-workstation.glb', err);
    }
  );
})();
