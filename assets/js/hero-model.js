// Renders the hero's 3D retro-workstation (assets/models/retro-workstation.glb)
// into #hero-model via three.js. Loaded through the pinned importmap in
// index.html's <head> — no npm/build step, just a versioned CDN module.
//
// Motion (see .claude/skills/animate for the reasoning):
//   - Entrance: the model is invisible (`.hero-model { opacity: 0 }` in
//     style.css) until the GLB decodes, then fades in over 400ms — bridges
//     the async load instead of popping in.
//   - Idle: none — the model sits fixed until the pointer moves it.
//   - Pointer: desktop-with-a-mouse only, the model eases toward a tilt
//     derived from cursor position, independent of (but numerically
//     consistent with) the CSS tilt already driving the two code-float
//     panels in initHeroParallax (assets/js/site.js).
// Reduced motion: the model still fades in, but skips the pointer tilt —
// fewer/gentler, not zero.
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
      // Fixed in place — no idle turntable. Only the pointer-driven tilt moves it.
      var lerp = 1 - Math.pow(0.001, dt); // frame-rate-independent ease toward target
      modelGroup.rotation.y += (targetX * 0.35 - modelGroup.rotation.y) * lerp;
      modelGroup.rotation.x += (targetY * -0.18 - modelGroup.rotation.x) * lerp;
    }
    renderer.render(scene, camera);
  });

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
    },
    undefined,
    function (err) {
      console.warn('hero-model: failed to load retro-workstation.glb', err);
    }
  );
})();
