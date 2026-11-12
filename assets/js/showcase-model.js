// Renders the retro workstation (same GLB as the hero, so the browser has
// usually cached it already) into #showcase-model for the "Was ich baue"
// section: a 3/4 view, turned to the left like a product shot, with a real
// project (Youroma) shown on its CRT screen instead of the hero's code loop.
// Gentle float + pointer tilt; only renders while the section is on screen.
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

function initShowcaseModel() {
  var container = document.getElementById('showcase-model');
  if (!container) return;

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var canHover = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  container.appendChild(renderer.domElement);

  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(30, 1, 0.1, 100);

  // Same two lighting moods as the hero model (dark: green CRT key,
  // light: neutral daylight).
  var hemi = new THREE.HemisphereLight(0xd6e8dd, 0x0a0e0c, 1.1);
  var key = new THREE.DirectionalLight(0x39d97a, 1.4);
  key.position.set(3, 4, 5);
  var fill = new THREE.DirectionalLight(0xe0a458, 0.5);
  fill.position.set(-4, 2, -3);
  scene.add(hemi, key, fill);
  var LIGHTS = {
    dark:  { sky: 0xd6e8dd, ground: 0x0a0e0c, hemi: 1.1, key: 0x39d97a, keyI: 1.4, fill: 0xe0a458, fillI: 0.5 },
    light: { sky: 0xffffff, ground: 0x9aa89c, hemi: 1.5, key: 0xfff1de, keyI: 2.1, fill: 0xcfe0ff, fillI: 0.7 }
  };
  function applyThemeLights() {
    var t = LIGHTS[document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark'];
    hemi.color.setHex(t.sky); hemi.groundColor.setHex(t.ground); hemi.intensity = t.hemi;
    key.color.setHex(t.key); key.intensity = t.keyI;
    fill.color.setHex(t.fill); fill.intensity = t.fillI;
  }
  applyThemeLights();
  new MutationObserver(applyThemeLights).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });

  var pivot = new THREE.Group();   // pointer tilt + float
  scene.add(pivot);

  function fit() {
    var w = container.clientWidth || 1;
    var h = container.clientHeight || 1;
    renderer.setSize(w, h);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }
  fit();
  new ResizeObserver(fit).observe(container);

  var targetX = 0, targetY = 0;
  if (canHover && !reduceMotion) {
    window.addEventListener('pointermove', function (e) {
      targetX = (e.clientX / window.innerWidth - 0.5) * 2;
      targetY = (e.clientY / window.innerHeight - 0.5) * 2;
    });
  }

  var clock = new THREE.Clock();
  var BASE_YAW = -0.55;            // turned so the screen faces the pills on the left
  var SCREEN_SCALE = 1.1;          // screen face size vs. the model's original
  function isShown(o) { for (var p = o; p; p = p.parent) { if (!p.visible) return false; } return true; }
  function frame() {
    var dt = clock.getDelta();
    var t = clock.elapsedTime;
    if (!reduceMotion) {
      var lerp = 1 - Math.pow(0.001, dt);
      var yaw = BASE_YAW + (canHover ? targetX * 0.12 : Math.sin(t * 0.35) * 0.06);
      var pitch = canHover ? targetY * 0.06 : Math.sin(t * 0.27 + 1.3) * 0.03;
      pivot.rotation.y += (yaw - pivot.rotation.y) * lerp;
      pivot.rotation.x += (pitch - pivot.rotation.x) * lerp;
      pivot.position.y = Math.sin(t * 0.8) * 0.015;
    }
    if (screenTick) screenTick(t);
    renderer.render(scene, camera);
  }

  var visible = false;
  function setVisible(v) {
    visible = v;
    renderer.setAnimationLoop(v ? frame : null);
    if (v) clock.getDelta();
  }
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) { setVisible(entries[0].isIntersecting); }).observe(container);
  } else {
    setVisible(true);
  }

  // CRT screen: a live re-creation of the Youroma homepage hero (the project
  // shown on the screen, source: github.com/yaseno2186/Youroma,
  // components/HeroBottle.jsx + app/globals.css). Big "YOUROMA" in Bodoni,
  // the flacon floating and tilted in front of it with a pulsing gold aura,
  // orbiting embers and a light glint sweeping over the glass. Same timings
  // as the real site (float 7s, aura 5s, glint 6s, orbits 9-24s). Drawn on a
  // 728x556 canvas that fills the whole screen, plus faint CRT scanlines.
  // Reduced motion: one still frame.
  var screenTick = null;
  function paintScreen(screenFace) {
    var src = container.getAttribute('data-screen');
    if (!src) return;
    var W = 728, H = 556;
    var c = document.createElement('canvas');
    c.width = W; c.height = H;
    var cx = c.getContext('2d');
    var tex = new THREE.CanvasTexture(c);
    tex.colorSpace = THREE.SRGBColorSpace;
    tex.anisotropy = 4;

    var img = new Image();
    var font = new FontFace('Bodoni Moda', 'url(assets/fonts/bodoni-moda-latin-400.woff2)');
    var bottleLayer = document.createElement('canvas');
    var bx = bottleLayer.getContext('2d');

    // Embers (radius in screen px, duration s, delay s, direction, colour).
    var EMBERS = [
      [5, 92, 16, 0, 1, '#FF5A36'], [3, 72, 11, -2, -1, '#FF7A45'], [4, 112, 21, -6, 1, '#E8341C'],
      [2, 58, 9, -1, -1, '#FF9A4D'], [4, 98, 18, -9, -1, '#E8341C'], [3, 80, 13, -4, 1, '#FF5A36'],
      [2, 125, 24, -12, 1, '#FF7A45']
    ];
    var easeInOut = function (x) { return 0.5 - Math.cos(Math.PI * x) / 2; };

    function draw(t) {
      // background + soft gold wash (radial, like the site's section glow)
      cx.fillStyle = '#0E1512';
      cx.fillRect(0, 0, W, H);
      var g = cx.createRadialGradient(W / 2, H * 0.52, 0, W / 2, H * 0.52, W * 0.62);
      g.addColorStop(0, 'rgba(200,169,106,0.16)');
      g.addColorStop(1, 'rgba(200,169,106,0)');
      cx.fillStyle = g;
      cx.fillRect(0, 0, W, H);

      // eyebrow + badge (top corners)
      cx.fillStyle = 'rgba(200,169,106,0.9)';
      cx.fillRect(W * 0.1, H * 0.15, 28, 1);
      cx.font = '500 11px Inter, sans-serif';
      cx.textBaseline = 'middle';
      cx.fillText('E A U   D E   P A R F U M', W * 0.1 + 38, H * 0.15);
      cx.textAlign = 'right';
      cx.fillStyle = 'rgba(237,230,216,0.55)';
      cx.fillText('Y O U R O M A', W * 0.9, H * 0.15);
      cx.textAlign = 'center';

      // big wordmark
      cx.fillStyle = 'rgba(237,230,216,0.94)';
      cx.font = '400 150px "Bodoni Moda", Didot, "Times New Roman", serif';
      cx.textBaseline = 'middle';
      cx.fillText('YOUROMA', W / 2, H * 0.53, W * 0.9);

      // aura: pulses 5s (opacity .75 -> 1, scale 1 -> 1.08)
      var ap = easeInOut((Math.sin(t * Math.PI * 2 / 5 - Math.PI / 2) + 1) / 2);
      var ar = 150 * (1 + ap * 0.08);
      cx.save();
      cx.translate(W / 2, H * 0.53);
      cx.scale(1, 1.4);
      var a = cx.createRadialGradient(0, 0, 0, 0, 0, ar);
      var k = 0.75 + ap * 0.25;
      a.addColorStop(0, 'rgba(200,169,106,' + (0.5 * k).toFixed(3) + ')');
      a.addColorStop(0.35, 'rgba(200,169,106,' + (0.22 * k).toFixed(3) + ')');
      a.addColorStop(0.68, 'rgba(200,169,106,0)');
      cx.fillStyle = a;
      cx.fillRect(-ar, -ar, ar * 2, ar * 2);
      cx.restore();

      // bottle: float 7s (14px), tilted 8deg, glint every 6s (masked to the glass)
      if (img.naturalWidth) {
        var bh = H * 0.66, bw = bh * img.naturalWidth / img.naturalHeight;
        var fy = -7 * (1 - Math.cos(t * Math.PI * 2 / 7));
        bottleLayer.width = Math.ceil(bw); bottleLayer.height = Math.ceil(bh);
        bx.clearRect(0, 0, bw, bh);
        bx.globalCompositeOperation = 'source-over';
        bx.drawImage(img, 0, 0, bw, bh);
        var gp = (t % 6) / 6;                     // glint: sweeps between 12% and 32% of the cycle
        if (gp > 0.12 && gp < 0.32) {
          var q = (gp - 0.12) / 0.2;
          var op = q < 0.4 ? q / 0.4 : 1 - (q - 0.4) / 0.6;
          var gx = -bw + q * bw * 3;
          var lg = bx.createLinearGradient(gx, 0, gx + bw, bh);
          lg.addColorStop(0.42, 'rgba(255,246,224,0)');
          lg.addColorStop(0.5, 'rgba(255,246,224,' + (0.85 * op).toFixed(3) + ')');
          lg.addColorStop(0.58, 'rgba(255,246,224,0)');
          bx.globalCompositeOperation = 'source-atop';
          bx.fillStyle = lg;
          bx.fillRect(0, 0, bw, bh);
        }
        cx.save();
        cx.translate(W / 2, H * 0.53 + fy);
        cx.rotate(8 * Math.PI / 180);
        cx.shadowColor = 'rgba(0,0,0,0.6)';
        cx.shadowBlur = 30;
        cx.shadowOffsetY = 22;
        cx.drawImage(bottleLayer, -bw / 2, -bh / 2);
        cx.restore();
      }

      // embers orbit the bottle and twinkle
      EMBERS.forEach(function (e) {
        var ang = e[4] * ((t - e[3]) / e[2]) * Math.PI * 2;
        var tw = (Math.sin(((t - e[3] / 2) / (e[2] / 2.4)) * Math.PI * 2) + 1) / 2;
        var x = W / 2 + Math.cos(ang) * e[1];
        var y = H * 0.53 + Math.sin(ang) * e[1];
        cx.globalAlpha = 0.2 + tw * 0.8;
        cx.fillStyle = e[5];
        cx.shadowColor = 'rgba(255,60,20,0.8)';
        cx.shadowBlur = 8;
        cx.beginPath();
        cx.arc(x, y, (e[0] / 2) * (0.7 + tw * 0.45), 0, Math.PI * 2);
        cx.fill();
        cx.shadowBlur = 0;
        cx.globalAlpha = 1;
      });

      // CRT scanlines
      cx.fillStyle = 'rgba(0,0,0,0.12)';
      for (var y2 = 0; y2 < H; y2 += 3) cx.fillRect(0, y2, W, 1);
      tex.needsUpdate = true;
    }

    var last = -1;
    function start() {
      screenFace.material = new THREE.MeshBasicMaterial({ map: tex, toneMapped: false });
      draw(1.5);
      if (reduceMotion) { if (!visible) renderer.render(scene, camera); return; }
      screenTick = function (t) {
        if (t - last < 1 / 30) return;            // ~30 fps is plenty for the screen
        last = t;
        draw(t);
      };
      if (!visible) renderer.render(scene, camera);
    }
    var pending = 2;
    function ready() { if (--pending === 0) start(); }
    img.onload = ready;
    img.onerror = ready;
    img.src = src;
    font.load().then(function (f) { document.fonts.add(f); ready(); }, ready);
  }

  new GLTFLoader().load(
    container.getAttribute('data-model'),
    function (gltf) {
      var object = gltf.scene;
      pivot.add(object);

      // Monitor + system unit only: no keyboard, mouse or mouse cord here.
      // screen_light* are point lights baked into the model that paint the
      // green glow ring around the picture; off here so the screen reads clean.
      ['keyboard', 'mouse', 'mouse_cord', 'screen_light', 'screen_light_core', 'screen_halo_1', 'screen_halo_2'].forEach(function (n) {
        var o = object.getObjectByName(n);
        if (o) o.visible = false;
      });
      // Bigger picture: scale the screen face up around its own centre so
      // it fills the bezel opening.
      ['screen_code_face'].forEach(function (n) {
        var m = object.getObjectByName(n);
        if (!m || !m.geometry) return;
        m.geometry = m.geometry.clone();
        m.geometry.computeBoundingBox();
        var c = m.geometry.boundingBox.getCenter(new THREE.Vector3());
        m.geometry.translate(-c.x, -c.y, -c.z);
        m.geometry.scale(SCREEN_SCALE, SCREEN_SCALE, 1);
        m.geometry.translate(c.x, c.y, c.z);
      });

      // Fit off the physical geometry only (skip oversized glow planes).
      var box = new THREE.Box3();
      object.traverse(function (o) {
        if (o.isMesh && !/halo|glow/i.test(o.name) && isShown(o)) box.expandByObject(o);
      });
      if (box.isEmpty()) box.setFromObject(object);
      var sphere = box.getBoundingSphere(new THREE.Sphere());
      // Wide layout: centre on the SCREEN, not the whole PC, so the screen
      // lands exactly in the middle of the canvas box. style.css centres that
      // box on the golden spiral's eye. Phones: centre on the whole PC.
      var wide = window.matchMedia('(min-width: 900px)').matches; // same breakpoint as style.css
      var face = object.getObjectByName('screen_code_face');
      var centre = sphere.center.clone();
      if (wide && face) new THREE.Box3().setFromObject(face).getCenter(centre);
      object.position.sub(centre);
      object.updateMatrixWorld(true);

      var halfFov = (camera.fov * Math.PI) / 360;
      // Zoom: data-zoom on wide screens (bigger number = PC smaller),
      // phones pull in closer because the canvas is square and narrow.
      var zoom = wide ? parseFloat(container.getAttribute('data-zoom') || '1.1') : 0.95;
      var dist = sphere.radius / Math.tan(halfFov) * zoom;
      var elev = 14 * Math.PI / 180;
      camera.position.set(0, dist * Math.sin(elev), dist * Math.cos(elev));
      camera.lookAt(0, 0, 0);
      pivot.rotation.y = BASE_YAW;

      var screenFace = object.getObjectByName('screen_code_face');
      if (screenFace) paintScreen(screenFace);

      renderer.render(scene, camera);
      container.classList.add('is-loaded');
    },
    undefined,
    function () { container.classList.add('is-failed'); }
  );
}

// Start the 3D scene late so it never delays the first paint: wait for the
// page's load event, then for an idle moment. Weak devices (data saver,
// <= 2 GB RAM or <= 2 CPU cores) get a still picture instead (.is-poster in
// style.css), as do browsers without WebGL.
function canRun3D() {
  var n = navigator;
  if (n.connection && n.connection.saveData) return false;
  if (n.deviceMemory && n.deviceMemory <= 2) return false;
  if (n.hardwareConcurrency && n.hardwareConcurrency <= 2) return false;
  try {
    var c = document.createElement('canvas');
    if (!(c.getContext('webgl2') || c.getContext('webgl'))) return false;
  } catch (e) { return false; }
  return true;
}
function whenIdleAfterLoad(fn) {
  var idle = window.requestIdleCallback || function (f) { return setTimeout(f, 300); };
  var go = function () { idle(fn, { timeout: 2500 }); };
  if (document.readyState === 'complete') go();
  else window.addEventListener('load', go, { once: true });
}

// The showcase sits further down the page: only start it once it comes
// within ~600px of the screen (after load + idle as above).
(function () {
  var el = document.getElementById('showcase-model');
  if (!el) return;
  if (!canRun3D()) { el.classList.add('is-poster', 'is-loaded'); return; }
  if (!('IntersectionObserver' in window)) { whenIdleAfterLoad(initShowcaseModel); return; }
  var io = new IntersectionObserver(function (entries) {
    if (!entries[0].isIntersecting) return;
    io.disconnect();
    whenIdleAfterLoad(initShowcaseModel);
  }, { rootMargin: '600px 0px' });
  io.observe(el);
})();
