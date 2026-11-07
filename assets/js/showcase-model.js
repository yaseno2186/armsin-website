// Renders the retro workstation (same GLB as the hero, so the browser has
// usually cached it already) into #showcase-model for the "Was ich baue"
// section: a 3/4 view, turned to the left like a product shot, with a real
// project (Youroma) shown on its CRT screen instead of the hero's code loop.
// Gentle float + pointer tilt; only renders while the section is on screen.
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

(function initShowcaseModel() {
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

  // Paint a project screenshot onto the CRT face ("cover" crop to the
  // screen's 728x556 canvas, plus faint scanlines so it still reads as CRT).
  function paintScreen(screenFace) {
    var src = container.getAttribute('data-screen');
    if (!src) return;
    var img = new Image();
    img.onload = function () {
      var W = 728, H = 556;
      var c = document.createElement('canvas');
      c.width = W; c.height = H;
      var cx = c.getContext('2d');
      var s = Math.max(W / img.width, H / img.height);
      var dw = img.width * s, dh = img.height * s;
      cx.fillStyle = '#0a0e0c';
      cx.fillRect(0, 0, W, H);
      cx.drawImage(img, (W - dw) / 2, 0, dw, dh);
      cx.fillStyle = 'rgba(0,0,0,0.12)';
      for (var y = 0; y < H; y += 3) cx.fillRect(0, y, W, 1);
      var tex = new THREE.CanvasTexture(c);
      tex.colorSpace = THREE.SRGBColorSpace;
      tex.anisotropy = 4;
      screenFace.material = new THREE.MeshBasicMaterial({ map: tex, toneMapped: false });
      if (!visible) renderer.render(scene, camera);
    };
    img.src = src;
  }

  new GLTFLoader().load(
    container.getAttribute('data-model'),
    function (gltf) {
      var object = gltf.scene;
      pivot.add(object);

      // Fit off the physical geometry only (skip oversized glow planes).
      var box = new THREE.Box3();
      object.traverse(function (o) {
        if (o.isMesh && !/halo|glow/i.test(o.name)) box.expandByObject(o);
      });
      if (box.isEmpty()) box.setFromObject(object);
      var sphere = box.getBoundingSphere(new THREE.Sphere());
      object.position.sub(sphere.center);
      object.updateMatrixWorld(true);

      var halfFov = (camera.fov * Math.PI) / 360;
      // Phones: the canvas is square and narrow, so pull in closer.
      var dist = sphere.radius / Math.tan(halfFov) * (container.clientWidth < 700 ? 0.68 : 0.92);
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
})();
