/*!
 * <slim-monitor> — a 3D slim monitor with a glowing screen layer behind glass.
 * No dependencies. Drop this file into your site and use:
 *
 *   <script src="slim-monitor.js" defer></script>
 *   <slim-monitor src="images/screen.jpg"></slim-monitor>
 *
 * Armsin edit: aria-label text is German (see _applyAll).
 *
 * Attributes (all optional):
 *   src         Image shown on the screen (PNG/JPG, 16:9 works best, e.g. 1920x1080).
 *               Leave it out to show the placeholder.
 *   alt         Description of the screen image for screen readers.
 *   glow        Glow colour as hex (default #BFE3FF). Used when auto-glow can't read the image.
 *   auto-glow   "false" to always use the `glow` colour instead of sampling the image.
 *   strength    Glow strength 0–1.6 (default 1).
 *   shell       Body colour as hex (default #EAE3D6).
 *   scanlines   Add the attribute to show subtle scanlines.
 *   rx, ry      Starting angle in degrees (default -12 and -32).
 *   static      Add the attribute to disable drag/keyboard rotation.
 *   no-floor    Armsin addition: hide the floor shadow/glow under the monitor.
 */
(function () {
  if (customElements.get('slim-monitor')) return;

  var W = 620, H = 470, D = 56;          // body size (px, before scaling)
  var SCENE_W = 620, SCENE_H = 492;      // body + plinth
  var STAGE_W = 780, STAGE_H = 660;      // design size of the whole stage

  var css = `
  :host{display:block;width:100%;max-width:${STAGE_W}px;margin-inline:auto;color-scheme:dark}
  *{box-sizing:border-box}
  [hidden]{display:none!important}
  .stage{position:relative;width:100%;overflow:hidden;touch-action:none;user-select:none;-webkit-user-select:none;cursor:grab;outline:none}
  .stage.dragging{cursor:grabbing}
  :host([static]) .stage{cursor:default;touch-action:auto}
  .stage:focus-visible{box-shadow:inset 0 0 0 2px rgba(250,246,240,.8);border-radius:12px}
  .fit{position:absolute;left:50%;top:0;width:${STAGE_W}px;height:${STAGE_H}px;transform-origin:50% 0;perspective:1900px;perspective-origin:50% 42%}
  .wall{position:absolute;inset:0;pointer-events:none}
  .floor,.floorglow{position:absolute;left:50%;border-radius:50%;pointer-events:none}
  :host([no-floor]) .floor,:host([no-floor]) .floorglow{display:none}
  .floor{top:560px;width:760px;height:150px;margin-left:-380px;background:radial-gradient(ellipse at center,rgba(0,0,0,.55) 0%,rgba(0,0,0,.25) 40%,rgba(0,0,0,0) 70%)}
  .floorglow{top:520px;width:620px;height:140px;margin-left:-310px}
  .scene{position:absolute;left:${(STAGE_W - SCENE_W) / 2}px;top:50px;width:${SCENE_W}px;height:${SCENE_H}px;transform-style:preserve-3d;will-change:transform}
  .scene.anim{transition:transform .7s cubic-bezier(.2,.7,.2,1)}
  .p3{position:absolute;transform-style:preserve-3d}
  .f{position:absolute}
  .img{width:512px;height:288px;display:block;border-radius:8px;object-fit:cover;filter:saturate(1.08) brightness(1.06);transition:opacity .5s ease}
  .ph{width:512px;height:288px;border-radius:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;background:linear-gradient(160deg,#3A5C4D 0%,#2F4A3E 45%,#1C2530 100%);transition:opacity .5s ease;font-family:'Inter',-apple-system,system-ui,sans-serif;color:#FAF6F0}
  .ph b{font:500 30px/36px 'Fraunces',Georgia,serif}
  .ph span{font-size:13px;line-height:20px;opacity:.82}
  .glass{background-image:linear-gradient(112deg,rgba(255,255,255,0) 30%,rgba(255,255,255,.13) 44%,rgba(255,255,255,.03) 52%,rgba(255,255,255,0) 60%),radial-gradient(ellipse 90% 60% at 30% 0%,rgba(255,255,255,.10) 0%,rgba(255,255,255,0) 60%);background-size:320% 100%,100% 100%;box-shadow:inset 0 0 36px rgba(0,0,0,.55),inset 0 0 2px rgba(255,255,255,.18)}
  .scan{background:repeating-linear-gradient(0deg,rgba(0,0,0,.16) 0 1px,rgba(0,0,0,0) 1px 3px)}
  .vent{background:repeating-linear-gradient(90deg,rgba(20,22,25,.62) 0 4px,rgba(0,0,0,0) 4px 11px);border-radius:4px}
  .btn3{border-radius:14px;width:14px;height:14px;background:radial-gradient(circle at 40% 35%,#EFEBE3,#A9A295)}
  .power{position:absolute;left:524px;top:33px;width:40px;height:40px;border-radius:10px;border:0;padding:0;cursor:pointer;background:linear-gradient(180deg,#2A2D31 0%,#16181B 100%);box-shadow:0 2px 3px rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center}
  .power:focus-visible{outline:2px solid #FAF6F0;outline-offset:3px}
  .label{position:absolute;left:230px;top:60px;margin:0;font:600 11px/16px 'Inter',-apple-system,system-ui,sans-serif;letter-spacing:.16em;color:#5A564F}
  .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
  @media (prefers-reduced-motion:reduce){.scene.anim{transition:none}.img,.ph{transition:none}}
  `;

  var html = `
  <div class="stage" part="stage" tabindex="0" role="img" aria-roledescription="3D model">
    <div class="fit">
      <div class="wall"></div>
      <div class="floor"></div>
      <div class="floorglow"></div>
      <div class="scene">
        <div class="p3" style="left:0;top:0;width:${W}px;height:${H}px">
          <div class="f" style="left:34px;top:34px;width:552px;height:328px;background:#050607;transform:translateZ(11px)"></div>
          <div class="f screen" style="left:54px;top:54px;width:512px;height:288px;border-radius:8px;background:#07090A;transform:translateZ(12px)">
            <img class="img" alt="" hidden>
            <div class="ph"><b>Your image here</b><span>PNG or JPG · 16:9</span></div>
          </div>
          <div class="f glass" style="left:54px;top:54px;width:512px;height:288px;border-radius:8px;transform:translateZ(17px)"></div>
          <div class="f scan" hidden style="left:54px;top:54px;width:512px;height:288px;border-radius:8px;transform:translateZ(16px)"></div>
          <div class="f" style="left:34px;top:26px;width:552px;height:16px;background:#0F1113;transform:translateZ(20px) rotateX(90deg)"></div>
          <div class="f" style="left:34px;top:354px;width:552px;height:16px;background:#15181B;transform:translateZ(20px) rotateX(90deg)"></div>
          <div class="f" style="left:26px;top:34px;width:16px;height:328px;background:#121417;transform:translateZ(20px) rotateY(90deg)"></div>
          <div class="f" style="left:578px;top:34px;width:16px;height:328px;background:#121417;transform:translateZ(20px) rotateY(90deg)"></div>
          <div class="f" style="left:34px;top:34px;width:552px;height:328px;border:20px solid #16181B;border-radius:28px;transform:translateZ(22px)"></div>
          <div class="f spill" style="left:54px;top:54px;width:512px;height:288px;border-radius:8px;transform:translateZ(22.5px)"></div>
          <div class="f shell-border" style="left:0;top:0;width:${W}px;height:${H}px;border-style:solid;border-width:34px 34px 108px 34px;border-radius:6px;transform:translateZ(28px)"></div>
          <div class="f" style="left:0;top:0;width:${W}px;height:${H}px;border-radius:6px;transform:translateZ(28.2px);background:linear-gradient(180deg,rgba(255,255,255,.10) 0%,rgba(255,255,255,0) 18%,rgba(0,0,0,0) 80%,rgba(0,0,0,.08) 100%);clip-path:polygon(0 0,100% 0,100% 100%,0 100%,0 0,34px 34px,34px 362px,586px 362px,586px 34px,34px 34px)"></div>
          <div class="f" style="left:0;top:362px;width:${W}px;height:108px;transform:translateZ(28.6px)">
            <div class="f" style="left:40px;top:28px;width:150px;height:52px;border-radius:4px;background:repeating-linear-gradient(90deg,rgba(20,22,25,.78) 0 4px,rgba(0,0,0,0) 4px 10px)"></div>
            <div class="f" style="left:230px;top:50px;width:160px;height:2px;border-radius:2px;background:rgba(20,22,25,.18)"></div>
            <p class="label">MODEL 01</p>
            <div class="f" style="left:452px;top:30px;width:46px;height:46px;border-radius:46px;background:radial-gradient(circle at 35% 30%,#F4F1EB 0%,#CFC8BB 55%,#9E978A 100%);box-shadow:0 2px 4px rgba(0,0,0,.35),inset 0 -2px 3px rgba(0,0,0,.18)"></div>
            <div class="f" style="left:473px;top:34px;width:4px;height:12px;border-radius:2px;background:#5A564F"></div>
            <button class="power" type="button" aria-label="Turn screen off" aria-pressed="true">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#CFC8BB" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M12 3v8"/><path d="M6.3 6.8a8 8 0 1 0 11.4 0"/></svg>
            </button>
            <div class="f led" style="left:541px;top:20px;width:6px;height:6px;border-radius:6px"></div>
          </div>
          <div class="f shell side-r" style="left:${(W - D) / 2}px;top:0;width:${D}px;height:${H}px;transform:rotateY(90deg) translateZ(${W / 2}px)">
            <div class="f btn3" style="left:21px;top:360px"></div>
            <div class="f btn3" style="left:21px;top:388px"></div>
            <div class="f btn3" style="left:21px;top:416px"></div>
          </div>
          <div class="f shell side-l" style="left:${(W - D) / 2}px;top:0;width:${D}px;height:${H}px;transform:rotateY(-90deg) translateZ(${W / 2}px)"></div>
          <div class="f shell top" style="left:0;top:${(H - D) / 2}px;width:${W}px;height:${D}px;transform:rotateX(90deg) translateZ(${H / 2}px)">
            <div class="f" style="left:150px;top:10px;width:320px;height:18px;background:repeating-linear-gradient(90deg,rgba(20,22,25,.55) 0 3px,rgba(0,0,0,0) 3px 9px)"></div>
          </div>
          <div class="f" style="left:0;top:${(H - D) / 2}px;width:${W}px;height:${D}px;background:#1F2023;transform:rotateX(-90deg) translateZ(${H / 2}px)"></div>
          <div class="f shell back" style="left:0;top:0;width:${W}px;height:${H}px;border-radius:6px;transform:rotateY(180deg) translateZ(${D / 2}px)">
            <div class="f vent" style="left:130px;top:60px;width:360px;height:110px"></div>
            <div class="f" style="left:230px;top:220px;width:160px;height:80px;border-radius:4px;background:#24272B"></div>
            <div class="f" style="left:250px;top:244px;width:120px;height:3px;background:rgba(250,246,240,.28)"></div>
            <div class="f" style="left:250px;top:256px;width:90px;height:3px;background:rgba(250,246,240,.2)"></div>
            <div class="f" style="left:250px;top:268px;width:104px;height:3px;background:rgba(250,246,240,.2)"></div>
            <div class="f" style="left:70px;top:380px;width:34px;height:22px;border-radius:4px;background:#24272B"></div>
            <div class="f" style="left:116px;top:380px;width:22px;height:22px;border-radius:22px;background:#24272B"></div>
          </div>
        </div>
        <div class="p3" style="left:80px;top:${H}px;width:460px;height:22px">
          <div class="f" style="left:0;top:0;width:460px;height:22px;background:#232427;transform:translateZ(22px)"></div>
          <div class="f" style="left:0;top:0;width:460px;height:22px;background:#1A1B1D;transform:rotateY(180deg) translateZ(22px)"></div>
          <div class="f" style="left:208px;top:0;width:44px;height:22px;background:#1C1D20;transform:rotateY(90deg) translateZ(230px)"></div>
          <div class="f" style="left:208px;top:0;width:44px;height:22px;background:#18191B;transform:rotateY(-90deg) translateZ(230px)"></div>
          <div class="f" style="left:0;top:-11px;width:460px;height:44px;background:#111214;transform:rotateX(-90deg) translateZ(11px)"></div>
        </div>
      </div>
    </div>
    <span class="sr" aria-live="polite"></span>
  </div>`;

  function hexToRgb(hex, fallback) {
    var h = String(hex || '').trim().replace('#', '');
    if (h.length === 3) h = h.split('').map(function (c) { return c + c; }).join('');
    if (!/^[0-9a-f]{6}$/i.test(h)) return fallback;
    var n = parseInt(h, 16);
    return ((n >> 16) & 255) + ', ' + ((n >> 8) & 255) + ', ' + (n & 255);
  }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }

  class SlimMonitor extends HTMLElement {
    static get observedAttributes() { return ['src', 'alt', 'glow', 'auto-glow', 'strength', 'shell', 'scanlines', 'rx', 'ry']; }

    constructor() {
      super();
      var root = this.attachShadow({ mode: 'open' });
      root.innerHTML = '<style>' + css + '</style>' + html;
      var q = function (s) { return root.querySelector(s); };
      this.$ = {
        stage: q('.stage'), fit: q('.fit'), scene: q('.scene'), wall: q('.wall'), floorglow: q('.floorglow'),
        img: q('.img'), ph: q('.ph'), glass: q('.glass'), scan: q('.scan'), spill: q('.spill'),
        border: q('.shell-border'), shells: root.querySelectorAll('.shell'), power: q('.power'), led: q('.led'), live: q('.sr')
      };
      this.state = { rx: -12, ry: -32, on: true, sampled: null };
      this.drag = null;
      this._bind();
    }

    connectedCallback() {
      var self = this;
      this.state.rx = this._num('rx', -12);
      this.state.ry = this._num('ry', -32);
      this._ro = new ResizeObserver(function () { self._fit(); });
      this._ro.observe(this);
      this._fit();
      this._applyAll();
    }
    disconnectedCallback() { if (this._ro) this._ro.disconnect(); }

    attributeChangedCallback(name) {
      if (!this.isConnected) return;
      if (name === 'src') this.state.sampled = null;
      if (name === 'rx' || name === 'ry') { this.state.rx = this._num('rx', -12); this.state.ry = this._num('ry', -32); }
      this._applyAll();
    }

    /* public API */
    setView(rx, ry, animate) {
      this.state.rx = clamp(rx, -65, 40); this.state.ry = ry;
      this.$.scene.classList.toggle('anim', animate !== false);
      this._applyTransform();
    }
    get on() { return this.state.on; }
    set on(v) { this.state.on = !!v; this._applyAll(); }

    _num(attr, d) { var v = parseFloat(this.getAttribute(attr)); return isNaN(v) ? d : v; }

    _fit() {
      var w = this.clientWidth || STAGE_W;
      var s = Math.min(1, w / STAGE_W);
      this.$.fit.style.transform = 'translateX(-50%) scale(' + s + ')';
      this.$.stage.style.height = Math.round(STAGE_H * s) + 'px';
    }

    _applyTransform() {
      var s = this.state;
      this.$.scene.style.transform = 'rotateX(' + s.rx + 'deg) rotateY(' + s.ry + 'deg)';
      this.$.glass.style.backgroundPosition = (50 + clamp(s.ry, -60, 60) * 0.9) + '% 0, 0 0';
    }

    _applyAll() {
      var $ = this.$, s = this.state;
      var src = this.getAttribute('src');
      var shell = this.getAttribute('shell') || '#EAE3D6';
      var on = s.on;
      var strength = clamp(this._num('strength', 1), 0, 1.6) * (on ? 1 : 0);
      var auto = this.getAttribute('auto-glow') !== 'false';
      var rgb = (auto && src && s.sampled) ? s.sampled : hexToRgb(this.getAttribute('glow'), '191, 227, 255');

      // screen
      if (src) {
        if ($.img.getAttribute('src') !== src) $.img.src = src;
        $.img.alt = this.getAttribute('alt') || '';
        $.img.hidden = false; $.ph.hidden = true;
      } else {
        $.img.hidden = true; $.img.removeAttribute('src'); $.ph.hidden = false;
      }
      $.img.style.opacity = on ? 1 : 0;
      $.ph.style.opacity = on ? 1 : 0;
      $.scan.hidden = !this.hasAttribute('scanlines');

      // glow
      $.spill.style.boxShadow = '0 0 ' + Math.round(30 * Math.max(strength, .01)) + 'px ' + Math.round(5 * strength) + 'px rgba(' + rgb + ',' + (0.42 * strength).toFixed(3) + ')';
      $.wall.style.background = 'radial-gradient(ellipse 60% 55% at 50% 40%, rgba(' + rgb + ',' + (0.16 * strength).toFixed(3) + ') 0%, rgba(0,0,0,0) 70%)';
      $.floorglow.style.background = 'radial-gradient(ellipse at center, rgba(' + rgb + ',' + (0.30 * strength).toFixed(3) + ') 0%, rgba(' + rgb + ',0) 70%)';

      // body colour + face shading
      $.border.style.borderColor = shell;
      var shades = { 'side-r': 'linear-gradient(90deg,rgba(0,0,0,.10),rgba(0,0,0,.18))', 'side-l': 'linear-gradient(90deg,rgba(0,0,0,.26),rgba(0,0,0,.18))', 'top': 'linear-gradient(0deg,rgba(255,255,255,.14),rgba(255,255,255,.04))', 'back': 'linear-gradient(180deg,rgba(0,0,0,.14),rgba(0,0,0,.24))' };
      $.shells.forEach(function (el) {
        el.style.backgroundColor = shell;
        for (var k in shades) if (el.classList.contains(k)) el.style.backgroundImage = shades[k];
      });

      // power
      $.led.style.background = on ? '#7FE0A0' : '#5A564F';
      $.led.style.boxShadow = on ? '0 0 8px #7FE0A0' : 'none';
      $.power.setAttribute('aria-pressed', String(on));
      $.power.setAttribute('aria-label', on ? 'Turn screen off' : 'Turn screen on');
      // Armsin: German label (the site is German-first).
      $.stage.setAttribute('aria-label', (src && this.getAttribute('alt') ? this.getAttribute('alt') : 'Monitor') + (this.hasAttribute('static') ? '' : '. Zum Drehen ziehen oder Pfeiltasten nutzen.'));

      this._applyTransform();
    }

    _sample() {
      try {
        var img = this.$.img, c = document.createElement('canvas');
        c.width = c.height = 8;
        var ctx = c.getContext('2d');
        ctx.drawImage(img, 0, 0, 8, 8);
        var d = ctx.getImageData(0, 0, 8, 8).data, r = 0, g = 0, b = 0, n = 0;
        for (var i = 0; i < d.length; i += 4) { r += d[i]; g += d[i + 1]; b += d[i + 2]; n++; }
        r /= n; g /= n; b /= n;
        var k = Math.min(2.2, 235 / Math.max(r, g, b, 1));
        this.state.sampled = Math.round(r * k) + ', ' + Math.round(g * k) + ', ' + Math.round(b * k);
      } catch (e) {
        this.state.sampled = null; // cross-origin image without CORS: fall back to `glow`
      }
      this._applyAll();
    }

    _bind() {
      var self = this, $ = this.$;
      $.img.addEventListener('load', function () { self._sample(); });
      $.power.addEventListener('click', function (e) {
        e.stopPropagation();
        self.state.on = !self.state.on;
        self._applyAll();
      });
      $.power.addEventListener('pointerdown', function (e) { e.stopPropagation(); });

      $.stage.addEventListener('pointerdown', function (e) {
        if (self.hasAttribute('static')) return;
        try { $.stage.setPointerCapture(e.pointerId); } catch (err) {}
        self.drag = { x: e.clientX, y: e.clientY, rx: self.state.rx, ry: self.state.ry };
        $.scene.classList.remove('anim');
        $.stage.classList.add('dragging');
      });
      $.stage.addEventListener('pointermove', function (e) {
        if (!self.drag) return;
        self.state.rx = clamp(self.drag.rx - (e.clientY - self.drag.y) * 0.3, -65, 40);
        self.state.ry = self.drag.ry + (e.clientX - self.drag.x) * 0.4;
        self._applyTransform();
      });
      var end = function () { self.drag = null; $.stage.classList.remove('dragging'); };
      $.stage.addEventListener('pointerup', end);
      $.stage.addEventListener('pointercancel', end);
      $.stage.addEventListener('dblclick', function () {
        if (self.hasAttribute('static')) return;
        self.setView(self._num('rx', -12), self._num('ry', -32));
      });
      $.stage.addEventListener('keydown', function (e) {
        if (self.hasAttribute('static')) return;
        var step = e.shiftKey ? 30 : 10, s = self.state;
        if (e.key === 'ArrowLeft') self.setView(s.rx, s.ry - step);
        else if (e.key === 'ArrowRight') self.setView(s.rx, s.ry + step);
        else if (e.key === 'ArrowUp') self.setView(s.rx - step, s.ry);
        else if (e.key === 'ArrowDown') self.setView(s.rx + step, s.ry);
        else if (e.key === 'Home') self.setView(self._num('rx', -12), self._num('ry', -32));
        else return;
        e.preventDefault();
      });
    }
  }

  customElements.define('slim-monitor', SlimMonitor);
})();
