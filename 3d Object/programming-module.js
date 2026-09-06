import * as THREE from 'three';

const stage = document.querySelector('three-d-stage');
await stage.ready;

/* ---------- palette (site tokens) ---------- */
const M = {
  case:      new THREE.MeshStandardMaterial({ name: 'case',      color: '#FAF6F0', roughness: 0.62, metalness: 0.04 }),
  caseShade: new THREE.MeshStandardMaterial({ name: 'caseShade', color: '#E4DCD0', roughness: 0.65 }),
  caseDark:  new THREE.MeshStandardMaterial({ name: 'caseDark',  color: '#6E6A63', roughness: 0.6 }),
  ink:       new THREE.MeshStandardMaterial({ name: 'ink',       color: '#1C2530', roughness: 0.5, metalness: 0.1 }),
  screen:    new THREE.MeshStandardMaterial({ name: 'screen',    color: '#182028', roughness: 0.22, metalness: 0.05 }),
  key:       new THREE.MeshStandardMaterial({ name: 'key',       color: '#EFE8DE', roughness: 0.7 }),
  keyAccent: new THREE.MeshStandardMaterial({ name: 'keyAccent', color: '#C1592B', roughness: 0.6 }),
  accent:    new THREE.MeshStandardMaterial({ name: 'accent',    color: '#C1592B', roughness: 0.45 }),
  accentDark:new THREE.MeshStandardMaterial({ name: 'accentDark',color: '#A34620', roughness: 0.5 }),
  green:     new THREE.MeshStandardMaterial({ name: 'green',     color: '#2F4A3E', roughness: 0.5 }),
  greenLit:  new THREE.MeshStandardMaterial({ name: 'greenLit',  color: '#3C5C4D', roughness: 0.5 }),
  glowGreen: new THREE.MeshStandardMaterial({ name: 'glowGreen', color: '#7FBF9A', roughness: 0.4, emissive: '#2F4A3E', emissiveIntensity: 0.6 }),
  paperLine: new THREE.MeshStandardMaterial({ name: 'paperLine', color: '#FAF6F0', roughness: 0.55 }),
  mutedLine: new THREE.MeshStandardMaterial({ name: 'mutedLine', color: '#A9A49B', roughness: 0.55 }),
};

/* ---------- helpers ---------- */
function roundedRectShape(w, h, r) {
  const s = new THREE.Shape();
  const x = -w / 2, y = -h / 2;
  s.moveTo(x + r, y);
  s.lineTo(x + w - r, y);
  s.quadraticCurveTo(x + w, y, x + w, y + r);
  s.lineTo(x + w, y + h - r);
  s.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
  s.lineTo(x + r, y + h);
  s.quadraticCurveTo(x, y + h, x, y + h - r);
  s.lineTo(x, y + r);
  s.quadraticCurveTo(x, y, x + r, y);
  return s;
}

function slab(w, h, d, r, mat, name) {
  const bevel = Math.min(d * 0.3, r * 0.6);
  const geo = new THREE.ExtrudeGeometry(roundedRectShape(w, h, r), {
    depth: d - bevel * 2, bevelEnabled: true, bevelThickness: bevel,
    bevelSize: bevel, bevelSegments: 3, curveSegments: 12,
  });
  geo.translate(0, 0, -(d - bevel * 2) / 2);
  const m = new THREE.Mesh(geo, mat);
  m.name = name;
  m.castShadow = true; m.receiveShadow = true;
  return m;
}

let seed = 20260904;
const rnd = () => ((seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff);

// rows of code-like bars on a face (local XY, extruded toward +z)
function codeLines(w, h, opts = {}) {
  const g = new THREE.Group();
  g.name = opts.name || 'codeLines';
  const lh = opts.lineH || 0.007;
  const gap = opts.gap || 0.0055;
  const indentStep = opts.indent ?? 0.012;
  const rows = Math.floor((h + gap) / (lh + gap));
  const hot = opts.hot ?? 0.22;
  const baseMat = opts.base || M.paperLine;
  const dimMat = opts.dim || M.mutedLine;
  const hotMat = opts.hotMat || M.accent;
  let y = h / 2 - lh / 2;
  for (let i = 0; i < rows; i++) {
    const indent = indentStep * (rnd() < 0.45 ? 1 : 0);
    let x = -w / 2 + indent;
    const segs = rnd() < 0.35 ? 2 : 1;
    let avail = w - indent - (segs - 1) * 0.008;
    for (let s = 0; s < segs; s++) {
      const frac = 0.3 + rnd() * (segs === 1 ? 0.62 : 0.38);
      const len = Math.max(0.008, avail * frac);
      const mat = rnd() < hot ? hotMat : (rnd() < 0.5 ? baseMat : dimMat);
      const bar = slab(len, lh, 0.004, lh / 2, mat, 'codeBar');
      bar.position.set(x + len / 2, y, 0.003);
      g.add(bar);
      x += len + 0.008;
      avail -= len;
    }
    y -= lh + gap;
  }
  return g;
}

function codeTagChip(size, name, body = M.case, ink = M.ink, bar = M.accent) {
  const g = new THREE.Group();
  g.name = name;
  g.add(slab(size, size, 0.016, size * 0.24, body, name + 'Body'));
  const inset = slab(size * 0.9, size * 0.9, 0.004, size * 0.20, M.caseShade, name + 'Inset');
  inset.position.z = 0.008;
  g.add(inset);
  const z = 0.012;

  // lowercase "a" — bowl, stem, and a short foot
  const glyph = new THREE.Group();
  glyph.name = 'logoGlyph';
  glyph.position.set(-size * 0.13, -size * 0.02, z);
  g.add(glyph);

  const bowl = new THREE.Mesh(
    new THREE.TorusGeometry(size * 0.105, size * 0.030, 14, 40, Math.PI * 1.72), ink);
  bowl.name = 'logoBowl';
  bowl.rotation.z = -0.42;
  bowl.position.set(-size * 0.03, -size * 0.055, 0);
  bowl.castShadow = true;
  glyph.add(bowl);

  const arch = new THREE.Mesh(
    new THREE.TorusGeometry(size * 0.105, size * 0.030, 14, 40, Math.PI * 0.95), ink);
  arch.name = 'logoArch';
  arch.position.set(-size * 0.03, size * 0.075, 0);
  arch.castShadow = true;
  glyph.add(arch);

  const stem = slab(size * 0.052, size * 0.30, 0.008, size * 0.026, ink, 'logoStem');
  stem.position.set(size * 0.052, size * 0.028, 0);
  glyph.add(stem);

  const foot = slab(size * 0.075, size * 0.050, 0.008, size * 0.024, ink, 'logoFoot');
  foot.position.set(size * 0.048, -size * 0.10, 0);
  glyph.add(foot);

  // terracotta block
  const block = slab(size * 0.150, size * 0.44, 0.010, size * 0.008, bar, 'logoBlock');
  block.position.set(size * 0.165, -size * 0.01, z);
  g.add(block);
  return g;
}

function ventGrille(w, lines, spacing, len, mat, name) {
  const g = new THREE.Group();
  g.name = name;
  for (let i = 0; i < lines; i++) {
    const b = slab(len, 0.0045, 0.004, 0.002, mat, 'vent');
    b.position.set(0, -i * spacing, 0.002);
    g.add(b);
  }
  g.position.y = ((lines - 1) * spacing) / 2;
  return g;
}

/* ---------- the retro PC ---------- */
const model = new THREE.Group();
model.name = 'retroPCModule';

const pc = new THREE.Group();
pc.name = 'desktopPC';
model.add(pc);

/* --- horizontal system unit (pedestal) --- */
const UW = 0.42, UD = 0.32, UH = 0.075;
const unit = new THREE.Group();
unit.name = 'systemUnit';
unit.position.set(0, 0, 0);
pc.add(unit);

const unitBody = slab(UW, UD, UH, 0.008, M.case, 'unitBody');
unitBody.rotation.x = -Math.PI / 2;
unitBody.position.y = UH / 2;
unit.add(unitBody);

// front fascia detail (front face is +z)
const fascia = new THREE.Group();
fascia.name = 'unitFascia';
fascia.position.set(0, UH / 2, UD / 2 + 0.0005);
unit.add(fascia);

const floppy = slab(0.11, 0.013, 0.006, 0.002, M.ink, 'floppySlot');
floppy.position.set(-0.11, 0.012, 0.002);
fascia.add(floppy);
const floppyEject = slab(0.012, 0.008, 0.006, 0.002, M.caseDark, 'floppyEject');
floppyEject.position.set(-0.042, 0.012, 0.003);
fascia.add(floppyEject);

const cdTray = slab(0.13, 0.010, 0.006, 0.002, M.caseShade, 'driveSlot');
cdTray.position.set(-0.10, -0.014, 0.002);
fascia.add(cdTray);

const powerBtn = new THREE.Mesh(new THREE.CylinderGeometry(0.009, 0.009, 0.006, 24), M.caseShade);
powerBtn.name = 'powerButton';
powerBtn.rotation.x = Math.PI / 2;
powerBtn.position.set(0.155, 0.008, 0.003);
powerBtn.castShadow = true;
fascia.add(powerBtn);

const led = new THREE.Mesh(new THREE.SphereGeometry(0.0042, 18, 14), M.accent);
led.name = 'powerLED';
led.position.set(0.155, -0.017, 0.003);
fascia.add(led);

const unitVents = ventGrille(0.05, 3, 0.009, 0.05, M.caseShade, 'unitVents');
unitVents.position.set(0.075, -0.002, 0.002);
fascia.add(unitVents);

/* --- CRT monitor --- */
const mon = new THREE.Group();
mon.name = 'crtMonitor';
mon.position.set(0, UH, -0.005);
mon.rotation.x = -0.05;
pc.add(mon);

const MW = 0.32, MH = 0.27, MD = 0.235;
const monBody = slab(MW, MH, MD, 0.026, M.case, 'monitorBody');
monBody.position.set(0, MH / 2, -MD / 2 + 0.12);
mon.add(monBody);

// tapered back of the tube
const monBack = new THREE.Mesh(new THREE.BoxGeometry(0.20, 0.17, 0.07), M.caseShade);
monBack.name = 'tubeBack';
monBack.position.set(0, MH / 2 + 0.005, -MD + 0.10);
monBack.castShadow = true;
mon.add(monBack);

// deep bezel + recessed screen
const bezel = slab(0.265, 0.195, 0.022, 0.020, M.caseShade, 'bezel');
bezel.position.set(0, MH / 2 + 0.026, 0.118);
mon.add(bezel);

const glass = slab(0.222, 0.154, 0.014, 0.022, M.screen, 'screenGlass');
glass.position.set(0, MH / 2 + 0.026, 0.1265);
mon.add(glass);

const screenContent = new THREE.Group();
screenContent.name = 'screenContent';
screenContent.position.set(0, MH / 2 + 0.026, 0.1345);
mon.add(screenContent);

// glowing green eyes
function eye(name) {
  const g = new THREE.Group();
  g.name = name;
  const white = slab(0.030, 0.072, 0.006, 0.014, M.glowGreen, name + 'Shape');
  g.add(white);
  const pupil = slab(0.013, 0.028, 0.004, 0.006, M.screen, name + 'Pupil');
  pupil.position.set(0, -0.002, 0.005);
  g.add(pupil);
  return g;
}
const eyeGlow = new THREE.PointLight('#7FBF9A', 0.9, 0.55, 2);
eyeGlow.name = 'screenGlow';
eyeGlow.position.set(0, 0, 0.06);
screenContent.add(eyeGlow);

const eyeL = eye('eyeLeft');
eyeL.position.set(-0.038, 0.004, 0);
screenContent.add(eyeL);
const eyeR = eye('eyeRight');
eyeR.position.set(0.038, 0.004, 0);
screenContent.add(eyeR);

// brand strip below the screen
const strip = slab(0.09, 0.010, 0.006, 0.003, M.accent, 'brandStrip');
strip.position.set(-0.078, 0.036, 0.121);
mon.add(strip);

const monVents = ventGrille(0.06, 3, 0.008, 0.06, M.caseShade, 'monitorVents');
monVents.position.set(0.082, 0.034, 0.121);
mon.add(monVents);

const knobA = new THREE.Mesh(new THREE.CylinderGeometry(0.007, 0.007, 0.008, 20), M.caseDark);
knobA.name = 'brightnessKnob';
knobA.rotation.x = Math.PI / 2;
knobA.position.set(0.016, 0.032, 0.122);
knobA.castShadow = true;
mon.add(knobA);
const knobB = knobA.clone();
knobB.name = 'contrastKnob';
knobB.position.x = 0.040;
mon.add(knobB);

/* --- keyboard + mouse --- */
const kbd = new THREE.Group();
kbd.name = 'keyboard';
kbd.position.set(-0.03, 0.006, 0.30);
kbd.rotation.x = -0.06;
model.add(kbd);

const KBW = 0.30, KBD_ = 0.115;
const kbdBody = slab(KBW, KBD_, 0.016, 0.006, M.case, 'keyboardBody');
kbdBody.rotation.x = -Math.PI / 2;
kbdBody.position.y = 0.008;
kbd.add(kbdBody);

const cols = 15, rows = 5, ks = 0.0158, kg = 0.0026;
const gridW = cols * ks + (cols - 1) * kg;
for (let r = 0; r < rows; r++) {
  for (let c = 0; c < cols; c++) {
    const isAccent = (r === 0 && c === 0) || (r === 2 && c === 14) || (r === 4 && c === 0);
    const key = slab(ks, ks * 0.9, 0.007, 0.0018, isAccent ? M.keyAccent : M.key, 'key');
    key.rotation.x = -Math.PI / 2;
    key.position.set(-gridW / 2 + c * (ks + kg) + ks / 2, 0.0175, -0.041 + r * (ks * 0.9 + kg));
    kbd.add(key);
  }
}
const spacebar = slab(ks * 6, ks * 0.9, 0.007, 0.0018, M.key, 'spacebar');
spacebar.rotation.x = -Math.PI / 2;
spacebar.position.set(-0.005, 0.0175, 0.043);
kbd.add(spacebar);

const mouse = new THREE.Group();
mouse.name = 'mouse';
mouse.position.set(0.215, 0, 0.30);
mouse.rotation.y = -0.16;
model.add(mouse);
const mouseBody = slab(0.045, 0.062, 0.020, 0.014, M.case, 'mouseBody');
mouseBody.rotation.x = -Math.PI / 2;
mouseBody.position.y = 0.010;
mouse.add(mouseBody);
const mouseBtn = slab(0.030, 0.022, 0.006, 0.004, M.caseShade, 'mouseButton');
mouseBtn.rotation.x = -Math.PI / 2;
mouseBtn.position.set(0, 0.0205, -0.016);
mouse.add(mouseBtn);

// coiled-ish cables
function cable(pts, name, radius = 0.0022) {
  const curve = new THREE.CatmullRomCurve3(pts.map(p => new THREE.Vector3(...p)));
  const m = new THREE.Mesh(new THREE.TubeGeometry(curve, 60, radius, 8, false), M.caseDark);
  m.name = name;
  m.castShadow = true;
  return m;
}
model.add(cable([
  [-0.03, 0.006, 0.243], [-0.02, 0.004, 0.215], [0.01, 0.004, 0.19], [0.0, 0.006, UD / 2 - 0.005],
], 'keyboardCable'));
model.add(cable([
  [0.215, 0.006, 0.268], [0.19, 0.004, 0.235], [0.12, 0.004, 0.20], [0.09, 0.006, UD / 2 - 0.005],
], 'mouseCable'));

/* ---------- floating code UI ---------- */
const ui = new THREE.Group();
ui.name = 'floatingUI';
model.add(ui);

// window above the monitor
const win = new THREE.Group();
win.name = 'browserWindow';
win.position.set(0.015, 0.50, 0.06);
win.rotation.y = -0.05;
ui.add(win);
const WW = 0.27, WH = 0.185;
win.add(slab(WW, WH, 0.018, 0.012, M.green, 'windowBody'));
const tabBar = slab(WW - 0.028, 0.022, 0.008, 0.005, M.greenLit, 'tabBar');
tabBar.position.set(0, WH / 2 - 0.024, 0.010);
win.add(tabBar);
const searchBar = slab(WW - 0.028, 0.026, 0.008, 0.006, M.greenLit, 'searchBar');
searchBar.position.set(0, WH / 2 - 0.055, 0.010);
win.add(searchBar);
const dot = new THREE.Mesh(new THREE.SphereGeometry(0.0045, 20, 16), M.accent);
dot.name = 'searchDot';
dot.position.set(-WW / 2 + 0.026, WH / 2 - 0.055, 0.017);
win.add(dot);
const winCode = codeLines(WW - 0.044, WH - 0.096, { name: 'windowCode', hot: 0.08 });
winCode.position.set(0, -0.028, 0.010);
win.add(winCode);

// tall panel, upper left
const left = new THREE.Group();
left.name = 'codePanelLeft';
left.position.set(-0.315, 0.44, -0.01);
left.rotation.set(0.05, 0.42, 0.04);
ui.add(left);
left.add(slab(0.155, 0.245, 0.016, 0.012, M.green, 'leftPanelBody'));
const leftTag = codeTagChip(0.05, 'leftTag');
leftTag.position.set(-0.040, 0.086, 0.008);
leftTag.scale.setScalar(0.85);
left.add(leftTag);
const leftCode = codeLines(0.118, 0.165, { name: 'leftCode', hot: 0.30 });
leftCode.position.set(0, -0.030, 0.009);
left.add(leftCode);

// slim panel, right
const right = new THREE.Group();
right.name = 'codePanelRight';
right.position.set(0.30, 0.40, 0.03);
right.rotation.set(0.04, -0.46, -0.05);
ui.add(right);
right.add(slab(0.095, 0.175, 0.014, 0.011, M.green, 'rightPanelBody'));
const rightTag = codeTagChip(0.042, 'rightTag');
rightTag.position.set(-0.018, 0.060, 0.008);
rightTag.scale.setScalar(0.8);
right.add(rightTag);
const rightCode = codeLines(0.068, 0.10, { name: 'rightCode', hot: 0.34, lineH: 0.006, gap: 0.005, indent: 0.008 });
rightCode.position.set(0, -0.024, 0.008);
right.add(rightCode);

// folder, top centre
const folder = new THREE.Group();
folder.name = 'folder';
folder.position.set(-0.05, 0.72, 0.01);
folder.rotation.set(0.06, 0.16, -0.03);
ui.add(folder);
const fTab = slab(0.052, 0.024, 0.028, 0.007, M.accent, 'folderTab');
fTab.position.set(-0.027, 0.052, 0);
folder.add(fTab);
folder.add(slab(0.125, 0.09, 0.030, 0.009, M.accent, 'folderBack'));
const fFront = slab(0.125, 0.078, 0.014, 0.009, M.accentDark, 'folderFront');
fFront.position.set(0, -0.006, 0.014);
folder.add(fFront);
const folderTag = codeTagChip(0.040, 'folderTag');
folderTag.position.set(0, -0.004, 0.020);
folder.add(folderTag);

// free chips
const chipA = codeTagChip(0.07, 'chipA');
chipA.position.set(0.245, 0.72, -0.02);
chipA.rotation.set(0.05, -0.34, 0.07);
ui.add(chipA);

const chipB = codeTagChip(0.055, 'chipB');
chipB.position.set(-0.335, 0.20, 0.14);
chipB.rotation.set(-0.04, 0.55, -0.10);
ui.add(chipB);

// floppy disk floating, right low
const disk = new THREE.Group();
disk.name = 'floppyDisk';
disk.position.set(0.335, 0.14, 0.20);
disk.rotation.set(0.12, -0.5, 0.18);
ui.add(disk);
disk.add(slab(0.075, 0.075, 0.008, 0.004, M.ink, 'diskBody'));
const shutter = slab(0.030, 0.024, 0.005, 0.002, M.caseDark, 'diskShutter');
shutter.position.set(0.010, 0.024, 0.006);
disk.add(shutter);
const diskLabel = slab(0.055, 0.030, 0.004, 0.002, M.case, 'diskLabel');
diskLabel.position.set(0, -0.016, 0.006);
disk.add(diskLabel);


/* keep the renderer matched to the host every frame (stage can init at 1x1) */
function refit() {
  const r = stage._renderer, c = stage._camera;
  if (!r || !c) return;
  const w = stage.clientWidth, h = stage.clientHeight;
  if (w < 2 || h < 2) return;
  const cv = r.domElement;
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  if (cv.width === Math.round(w * dpr) && cv.height === Math.round(h * dpr)) return;
  r.setPixelRatio(dpr);
  r.setSize(w, h, true);
  c.aspect = w / h;
  c.updateProjectionMatrix();
}

/* ---------- blinking, roving eyes ---------- */
const eyeGroups = [eyeL, eyeR];
const pupils = eyeGroups.map(g => g.children[1]);
const t0 = performance.now();
let nextBlink = 1.4;
let blinkStart = -1;
const BLINK_DUR = 0.16;
let gaze = { x: 0, y: 0 };
let target = { x: 0, y: 0 };
let nextSaccade = 0.9;

function tick() {
  refit();
  pinLeftMiddle();
  const t = (performance.now() - t0) / 1000;

  if (blinkStart < 0 && t > nextBlink) blinkStart = t;
  let lid = 1;
  if (blinkStart >= 0) {
    const k = (t - blinkStart) / BLINK_DUR;
    if (k >= 1) {
      blinkStart = -1;
      nextBlink = t + 1.5 + Math.random() * 3.0;
    } else {
      lid = Math.max(0.05, Math.abs(Math.cos(k * Math.PI)));
    }
  }

  if (t > nextSaccade) {
    target.x = (Math.random() - 0.5) * 0.008;
    target.y = (Math.random() - 0.5) * 0.024;
    nextSaccade = t + 0.7 + Math.random() * 1.8;
  }
  gaze.x += (target.x - gaze.x) * 0.16;
  gaze.y += (target.y - gaze.y) * 0.16;
  const drift = Math.sin(t * 1.1) * 0.0025;

  eyeGroups.forEach((g, i) => {
    g.scale.set(1, lid, 1);
    pupils[i].position.set(gaze.x + drift, gaze.y - 0.002, 0.005);
  });
  eyeGlow.intensity = (0.75 + Math.sin(t * 2.4) * 0.12) * (0.25 + lid * 0.75);
  requestAnimationFrame(tick);
}
tick();

/* 2x scale, pinned to the left-middle of the canvas */
model.scale.setScalar(2);
stage.setObject(model);

function pinLeftMiddle() {
  const cam = stage._camera;
  const w = stage.clientWidth, h = stage.clientHeight;
  if (!cam || w < 2 || h < 2) return;
  const fullW = w * 1.7; // >1 shifts the object left; higher = further left
  cam.setViewOffset(fullW, h, fullW - w, 0, w, h);
  cam.updateProjectionMatrix();
}


