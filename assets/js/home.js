/* Armsin homepage script (index.html only). No libraries.
   Contact data lives here, once. */
(function () {
  'use strict';
  var WA_NUMBER = '4917662625699';            // shown as 0176 62625699
  var WA_DISPLAY = '0176 62625699';
  var WA_TEXT = 'Hallo Yass, ich interessiere mich für eine kostenlose Demo-Website für meinen Betrieb.';
  var CAL_URL = 'https://cal.com/yass-almardoud/onehour';
  var EMAIL = 'yass.almardoud@armsin.de';

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var clamp = function (x, a, b) { return Math.min(b, Math.max(a, x)); };
  var ease = function (x) { return x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
  var html = document.documentElement;
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = matchMedia('(hover: hover) and (pointer: fine)').matches;

  /* ---------- where the PC sits (css px); the 3D renderer uses the same numbers ---------- */
  window.armsinPcFrame = function (w, hh) {
    if (w < 900) { var t = w >= 600, s = Math.min(w * (t ? .46 : .74), hh * (t ? .3 : .34)); return { cx: w / 2, cy: 80 + s * .5, s: s }; }
    var s2 = Math.min(w * .5, hh * .98); return { cx: w * .74, cy: hh * .52, s: s2 };
  };
  var pcBox = $('.pc'), poster = $('.pc-poster'), hero = document.getElementById('top');
  function placePoster() { if (!pcBox || !poster) return; var r = pcBox.getBoundingClientRect(), f = window.armsinPcFrame(r.width, r.height);
    poster.style.left = (f.cx - f.s / 2).toFixed(1) + 'px'; poster.style.top = (f.cy - f.s / 2).toFixed(1) + 'px'; poster.style.width = f.s.toFixed(1) + 'px';
    hero.style.setProperty('--pc-bottom', (f.cy - f.s / 2 + f.s * .88).toFixed(0) + 'px'); }
  placePoster();

  /* ---------- contact links ---------- */
  function waHref(text) { return 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(text || WA_TEXT); }
  $$('[data-wa]').forEach(function (a) { a.href = waHref(); });
  $$('[data-wa-num]').forEach(function (e) { e.textContent = WA_DISPLAY; });
  $$('[data-cal]').forEach(function (a) { a.href = CAL_URL; });

  /* in-page jumps: render all sections first, so the browser knows the real distances */
  document.addEventListener('click', function (e) { var a = e.target.closest && e.target.closest('a[href^="#"]'); if (a && html.classList.contains('cv')) { html.classList.remove('cv'); offCache = {}; } }, true);

  /* ---------- nav: mobile dropdown + sliding hover highlight (as on the previous site) ---------- */
  var burger = $('#burger'), nav = $('#nav');
  function closeNav() { nav.classList.remove('nav-open'); burger.setAttribute('aria-expanded', 'false'); burger.setAttribute('aria-label', t('nav.menu', 'Menü öffnen')); }
  burger.addEventListener('click', function () {
    var open = nav.classList.toggle('nav-open'); burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? t('nav.close', 'Menü schließen') : t('nav.menu', 'Menü öffnen'));
    if (open) { var f = $('#nav-panel a'); if (f) f.focus(); }
  });
  $$('#nav-panel a').forEach(function (a) { a.addEventListener('click', closeNav); });
  document.addEventListener('click', function (e) { if (nav.classList.contains('nav-open') && !nav.contains(e.target)) closeNav(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('nav-open')) { closeNav(); burger.focus(); } });
  var swY = null;
  nav.addEventListener('touchstart', function (e) { swY = e.touches[0].clientY; }, { passive: true });
  nav.addEventListener('touchend', function (e) { if (swY === null) return; var dy = e.changedTouches[0].clientY - swY; swY = null;
    var open = nav.classList.contains('nav-open');
    if ((dy > 24 && !open) || (dy < -24 && open)) burger.click(); }, { passive: true });
  var links = $('.nav-links'), ind = $('.nav-indicator');
  if (fine) $$('.nav-links a').forEach(function (a) {
    a.addEventListener('mouseenter', function () { links.style.setProperty('--ix', a.offsetLeft + 'px'); links.style.setProperty('--iw', a.offsetWidth + 'px'); links.classList.add('is-tracking'); });
  });
  if (links) links.addEventListener('mouseleave', function () { links.classList.remove('is-tracking'); });

  /* ---------- scroll engine: one rAF, sets --k / --p on pinned sections ---------- */
  var problem = $('#problem'), loesung = $('#loesung'), fuer = $('#fuer-wen'), ablauf = $('#ablauf'), kontakt = $('#kontakt');
  var pins = [hero, problem, loesung, fuer, ablauf];
  var M = {}, vh = innerHeight, vw = innerWidth, lastY = scrollY, barOn = false, ticking = false;
  function measure() {
    vh = innerHeight; vw = innerWidth;
    pins.concat([kontakt]).forEach(function (s) { var t = 0, e = s; while (e) { t += e.offsetTop; e = e.offsetParent; } M[s.id] = { top: t, h: s.offsetHeight }; });
    if (R || routeReady) buildRoute();
  }
  function prog(s) { var m = M[s.id]; return m ? clamp((scrollY - m.top) / Math.max(1, m.h - vh), 0, 1) : 0; }

  var oldBits = $$('#loesung .old .ob'), newScr = $('#loesung .new'), nbs = $$('#loesung .new .nb'), acts = $$('#loesung .act');
  var cards = $$('#fuer-wen .tcard');
  var railLinks = $$('.rail a'), railIds = railLinks.map(function (a) { return a.getAttribute('data-ch'); });
  var mbar = $('#mbar'), bubble = $('.wa-bubble');
  var sq = $('.s-q'), sqText = sq ? sq.getAttribute('data-q') : '', sqN = -1, phoneNew = $('#phone-new');

  // Smoothing: every scroll animation follows the scroll position with a short, soft delay
  // (critically damped, time-based), so wheel steps and finger flicks glide instead of snap.
  var SM = { k: 0, p1: 0, p2: 0, p3: 0, p5: 0 }, snap = true, lastT = 0;
  var TAU = fine ? 75 : 110; // ms
  function update(now) {
    ticking = false;
    var y = scrollY;
    now = now || performance.now();
    var dt = lastT ? Math.min(64, now - lastT) : 16; lastT = now;
    var a = (reduce || snap) ? 1 : 1 - Math.exp(-dt / TAU); snap = false;
    var T = { k: reduce ? 0 : prog(hero), p1: prog(problem), p2: prog(loesung), p3: prog(fuer), p5: prog(ablauf) }, moving = false;
    for (var key in T) { SM[key] += (T[key] - SM[key]) * a; if (Math.abs(T[key] - SM[key]) > .0004) moving = true; else SM[key] = T[key]; }
    if (moving) { ticking = true; requestAnimationFrame(update); }
    // 00 hero push
    var k = SM.k;
    hero.style.setProperty('--k', k.toFixed(4));
    if (window.PC3D && PC3D.setProgress) PC3D.setProgress(k);
    if (sq) { var n = Math.round(clamp((k - .7) / .12, 0, 1) * sqText.length); if (n !== sqN) { sqN = n; sq.textContent = sqText.slice(0, n); } }
    if (reduce) return chrome(y);
    // 01
    problem.style.setProperty('--p', SM.p1.toFixed(4));
    // 02 old site breaks apart, clean one builds, actions tick green
    var p2 = SM.p2; loesung.style.setProperty('--p', p2.toFixed(4));
    var br = ease(clamp((p2 - .12) / .26, 0, 1));
    oldBits.forEach(function (o, i) { var a = i * 2.4, d = br * (260 + i * 30);
      o.style.transform = 'translate(' + (Math.cos(a) * d).toFixed(1) + 'px,' + (Math.sin(a) * d).toFixed(1) + 'px) rotate(' + ((i % 2 ? 1 : -1) * br * (25 + i * 9)).toFixed(1) + 'deg)';
      o.style.opacity = 1 - br; });
    newScr.classList.toggle('on', p2 > .28); phoneNew.classList.toggle('is-new', p2 > .28);
    nbs.forEach(function (n, i) { n.classList.toggle('on', p2 > .3 + i * .045); });
    acts.forEach(function (a, i) { a.classList.toggle('done', p2 > .58 + i * .09); });
    // 03 cards fly over the pinned word
    var p3 = SM.p3; fuer.style.setProperty('--p', p3.toFixed(4));
    var mob = vw < 900;
    cards.forEach(function (c, i) {
      var q = clamp((p3 - .04 - i * .19) / .36, 0, 1), u = 1 - 2 * q, yy = Math.sign(u) * Math.pow(Math.abs(u), 2.2) * vh * .82;
      var xs = (i % 2 ? 1 : -1) * (mob ? vw * .05 : vw * .17), rot = (i % 2 ? 1 : -1) * 6 * u;
      c.style.transform = 'translate(calc(-50% + ' + xs.toFixed(1) + 'px), calc(-50% + ' + yy.toFixed(1) + 'px)) rotate(' + rot.toFixed(2) + 'deg)';
      c.style.opacity = q <= 0 || q >= 1 ? 0 : 1;
      c.style.visibility = q <= 0 || q >= 1 ? 'hidden' : 'visible';
    });
    // 05 route
    drawRoute(SM.p5);
    chrome(y);
  }
  var hdr = $('.site-header'), navY = scrollY;
  function chrome(y) {
    // phones: hide the nav on scroll down, show it on scroll up (never at the top or with the menu open)
    if (vw < 900 && !nav.classList.contains('nav-open') && y > 90) { if (Math.abs(y - navY) > 8) { hdr.classList.toggle('nav-hide', y > navY); navY = y; } }
    else { hdr.classList.remove('nav-hide'); navY = y; }
    // chapter rail
    var a = 0; railIds.forEach(function (id, i) { var el = document.getElementById(id); if (el && y + vh * .45 >= offTop(el)) a = i; });
    railLinks.forEach(function (l, i) { l.classList.toggle('on', i === a); if (i === a) l.setAttribute('aria-current', 'true'); else l.removeAttribute('aria-current'); });
    // mobile bar: after the hero, hide on scroll down, show on scroll up, hide at the contact section
    var afterHero = y > (M.top ? M.top.top + M.top.h - vh * .6 : 600), atContact = M.kontakt && y + vh > M.kontakt.top + 120;
    if (Math.abs(y - lastY) > 6) { var down = y > lastY; barOn = afterHero && !atContact && (!down || y < 40); lastY = y; }
    if (!afterHero || atContact) barOn = false;
    mbar.classList.toggle('on', barOn);
    bubble.classList.toggle('on', afterHero && !atContact);
  }
  var offCache = {};
  function offTop(el) { if (offCache[el.id] == null) { var t = 0, e = el; while (e) { t += e.offsetTop; e = e.offsetParent; } offCache[el.id] = t; } return offCache[el.id]; }
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(update); } }
  addEventListener('scroll', onScroll, { passive: true });

  /* desktop: mouse-wheel steps glide with soft inertia. Touchpads (small deltas), keyboard,
     scrollbar, ctrl+zoom and scrollable fields keep the browser's own scrolling. */
  if (fine && !reduce) {
    var ty = 0, cy = 0, gliding = false, gT = 0;
    var maxY = function () { return document.documentElement.scrollHeight - innerHeight; };
    function glide(now) {
      if (!gliding) return;
      var dt = Math.min(64, now - gT); gT = now;
      cy += (ty - cy) * (1 - Math.exp(-dt / 140));
      if (Math.abs(ty - cy) < .5) { cy = ty; gliding = false; }
      window.scrollTo({ top: cy, behavior: 'instant' });
      if (gliding) requestAnimationFrame(glide);
    }
    addEventListener('wheel', function (e) {
      if (e.ctrlKey || e.defaultPrevented || Math.abs(e.deltaX) > Math.abs(e.deltaY)) return;
      if (e.target.closest && e.target.closest('textarea, select, input, .nav-menu')) return;
      var d = e.deltaY * (e.deltaMode === 1 ? 40 : e.deltaMode === 2 ? innerHeight : 1);
      if (!gliding && Math.abs(d) < 50) return;            // touchpad: already smooth
      e.preventDefault();
      if (!gliding) { ty = cy = scrollY; gT = performance.now(); gliding = true; requestAnimationFrame(glide); }
      ty = clamp(ty + d * 1.1, 0, maxY());
    }, { passive: false });
    ['keydown', 'mousedown', 'touchstart'].forEach(function (ev) { addEventListener(ev, function () { gliding = false; }, { passive: true }); });
    document.addEventListener('click', function (e) { if (e.target.closest && e.target.closest('a[href^="#"]')) gliding = false; }, true);
  }
  addEventListener('resize', function () { offCache = {}; placePoster(); measure(); snap = true; update(); });
  // page height changes (fonts, images, sections rendering in) -> measure again
  if ('ResizeObserver' in window) { var lastH = 0, roT = 0; new ResizeObserver(function () { var h = document.body.scrollHeight; if (h === lastH) return; lastH = h;
    cancelAnimationFrame(roT); roT = requestAnimationFrame(function () { offCache = {}; measure(); update(); }); }).observe(document.body); }

  /* ---------- 05 route: dotted path, the PC hops from stop to stop ---------- */
  var R = null, routeReady = false;
  function buildRoute() {
    var box = $('#route'); if (!box || reduce) return;
    var W = box.clientWidth, H = box.clientHeight, desk = vw >= 900;
    var pts = desk ? [[.1, .64], [.37, .26], [.63, .66], [.9, .3]] : [[.25, .02], [.75, .28], [.25, .54], [.75, .78]];
    var P = pts.map(function (p) { return [p[0] * W, p[1] * H]; });
    var d = 'M' + P[0][0] + ',' + P[0][1], segs = [];
    for (var i = 1; i < P.length; i++) {
      var x0 = P[i - 1][0], y0 = P[i - 1][1], x1 = P[i][0], y1 = P[i][1];
      var c = desk ? 'C' + (x0 + (x1 - x0) * .5) + ',' + y0 + ' ' + (x0 + (x1 - x0) * .5) + ',' + y1 + ' ' + x1 + ',' + y1
                   : 'C' + x0 + ',' + (y0 + (y1 - y0) * .6) + ' ' + x1 + ',' + (y1 - (y1 - y0) * .6) + ' ' + x1 + ',' + y1;
      d += c; segs.push('M' + x0 + ',' + y0 + c);
    }
    var svg = $('.route-svg', box); svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
    svg.innerHTML = '<path d="' + d + '" fill="none" stroke="#3A3F3B" stroke-width="3" stroke-dasharray="1 12" stroke-linecap="round"/>' +
      '<path class="done" d="' + d + '" fill="none" stroke="#2FB863" stroke-width="4" stroke-linecap="round"/>' +
      segs.map(function (s) { return '<path class="seg" d="' + s + '" fill="none" stroke="none"/>'; }).join('');
    var done = $('.done', svg), L = done.getTotalLength(); done.style.strokeDasharray = L; done.style.strokeDashoffset = L;
    var segEls = $$('.seg', svg), segL = segEls.map(function (s) { return s.getTotalLength(); });
    $$('.stop', box).forEach(function (s, i) { s.style.left = P[i][0] + 'px'; s.style.top = (P[i][1] + 18) + 'px'; });
    var hop = $('.hopper', box);
    R = { box: box, done: done, L: L, segEls: segEls, segL: segL, desk: desk, hop: hop, hopW: hop.offsetWidth || (desk ? 110 : 78), stops: $$('.stop', box) };
  }
  function drawRoute(p) {
    if (!R) return;
    var s = clamp((p - .08) / .76, 0, 1) * 3, i = Math.min(2, Math.floor(s)), f = s - i;
    var hopF = clamp((f - .35) / .65, 0, 1), e = ease(hopF);
    var pt = R.segEls[i].getPointAtLength(R.segL[i] * e);
    var before = R.segL.slice(0, i).reduce(function (a, b) { return a + b; }, 0) + R.segL[i] * e;
    R.done.style.strokeDashoffset = Math.max(0, R.L - before);
    var w = R.hopW, air = Math.sin(Math.PI * hopF) * (R.desk ? 90 : 56);
    var sq = hopF > 0 && hopF < .08 ? .86 : hopF >= .08 && hopF < .95 ? 1.06 : 1;   // squash on take-off, stretch in the air
    R.hop.style.transform = 'translate(' + (pt.x - w / 2).toFixed(1) + 'px,' + (pt.y - w * .86 - air).toFixed(1) + 'px) scale(' + (2 - sq).toFixed(3) + ',' + sq.toFixed(3) + ')';
    R.stops.forEach(function (st, k) { st.classList.toggle('on', s >= k - .001 && (k > 0 || p > .06)); });
  }

  /* ---------- reveal fallback (where scroll-driven animations are missing) ---------- */
  var hasTimeline = window.CSS && CSS.supports && CSS.supports('animation-timeline: view()');
  if (!hasTimeline || reduce) {
    if ('IntersectionObserver' in window && !reduce) {
      var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { rootMargin: '0px 0px -10% 0px' });
      $$('.rv').forEach(function (el) { io.observe(el); });
    } else $$('.rv').forEach(function (el) { el.classList.add('in'); });
  }
  if (reduce) { // final states for the story sections
    if (newScr) { newScr.classList.add('on'); phoneNew.classList.add('is-new'); nbs.forEach(function (n) { n.classList.add('on'); }); acts.forEach(function (a) { a.classList.add('done'); }); }
    oldBits.forEach(function (o) { o.style.opacity = 0; });
    problem.style.setProperty('--p', 1); loesung.style.setProperty('--p', 1);
    $$('.stop').forEach(function (s) { s.classList.add('on'); });
  }

  /* ---------- magnetic main buttons (desktop, pointer only) ---------- */
  if (fine && !reduce) $$('.mag').forEach(function (b) {
    b.addEventListener('pointermove', function (e) { var r = b.getBoundingClientRect();
      b.style.transform = 'translate(' + ((e.clientX - r.left - r.width / 2) * .18).toFixed(1) + 'px,' + ((e.clientY - r.top - r.height / 2) * .28).toFixed(1) + 'px)'; });
    b.addEventListener('pointerleave', function () { b.style.transform = ''; });
  });
  // the PC looks at the pointer
  if (fine) addEventListener('pointermove', function (e) { if (window.PC3D && PC3D.look) PC3D.look(e.clientX / vw * 2 - 1, -(e.clientY / vh * 2 - 1)); }, { passive: true });

  /* ---------- calculator (Armsin-Preisliste, Nov. 2026) ---------- */
  var calc = $('#preis-check'), sumEl = $('#calc-sum'), shown = [100, 299], anim = 0;
  var fmt = function (n) { return Math.round(n).toLocaleString('de-DE'); };
  function range() {
    var nb = $$('input[name=b]:checked', calc).length, ne = $$('input[name=e]:checked', calc).length, ph = +$('#calc-photos').value || 0;
    var lo = 0, hi = 0;
    if (ne > 0) { lo = 500 + 200 * (ne - 1); hi = 999 + 300 * (ne - 1); }        // basis features included
    else if (nb > 0) { lo = 100 + 100 * (nb - 1); hi = 299 + 100 * (nb - 1); }
    var f = Math.ceil(ph / 10) * 12; return [lo + f, hi + f];                    // 12 € per 10 images
  }
  function paint(r) { sumEl.textContent = r[0] ? fmt(r[0]) + ' – ' + fmt(r[1]) + ' €' : '0 €'; }
  function recalc() {
    var to = range(), from = shown.slice(), t0 = performance.now();
    cancelAnimationFrame(anim);
    if (reduce) { shown = to; return paint(to); }
    (function step(now) { var q = clamp((now - t0) / 450, 0, 1), e = 1 - Math.pow(1 - q, 3);
      shown = [from[0] + (to[0] - from[0]) * e, from[1] + (to[1] - from[1]) * e]; paint(shown); if (q < 1) anim = requestAnimationFrame(step); })(t0);
  }
  calc.addEventListener('change', recalc);
  function calcSummary() {
    var picked = $$('input:checked', calc).map(function (i) { return i.parentNode.querySelector('span:last-child').textContent.trim(); });
    var ph = +$('#calc-photos').value; if (ph) picked.push(ph + ' Fotos mit KI verbessern');
    return 'Bedarfs-Check: ' + (picked.join(', ') || 'noch nichts gewählt') + '. Richtwert: ' + sumEl.textContent + '.';
  }

  /* ---------- contact form: prefill, validate, send via mailto ---------- */
  var form = $('#contact-form'), msg = $('#f-msg');
  function goForm(text, trade) {
    if (trade) { var r = $('input[name=trade][value="' + trade + '"]', form); if (r) r.checked = true; }
    if (text && (!msg.value || msg.dataset.auto === '1')) { msg.value = text; msg.dataset.auto = '1'; }
  }
  $$('[data-demo]').forEach(function (a) { a.addEventListener('click', function () { goForm('Ich interessiere mich für eine kostenlose Demo-Website für meinen Betrieb.'); }); });
  var tradeText = { 'Friseur': 'meinen Friseursalon', 'Café': 'mein Café', 'Handwerk': 'meinen Handwerksbetrieb', 'Praxis': 'meine Praxis', 'Anderes': 'meinen Betrieb' };
  $$('[data-trade]').forEach(function (a) { a.addEventListener('click', function () { var t = a.getAttribute('data-trade');
    goForm('Ich interessiere mich für eine kostenlose Demo-Website für ' + (tradeText[t] || 'meinen Betrieb') + '.', t); }); });
  $('#calc-cta').addEventListener('click', function () { goForm(calcSummary()); });
  msg.addEventListener('input', function () { msg.dataset.auto = '0'; });
  function check(input, ok) { var f = input.closest('.field'); f.classList.toggle('bad', !ok); input.setAttribute('aria-invalid', String(!ok));
    if (!ok) input.setAttribute('aria-describedby', input.id + '-err'); else input.removeAttribute('aria-describedby'); return ok; }
  function validContact(v) { v = v.trim(); return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v) || /^[+()\d\s\/-]{6,}$/.test(v); }
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var n = $('#f-name'), c = $('#f-contact');
    var ok = [check(n, n.value.trim().length > 1), check(c, validContact(c.value)), check(msg, msg.value.trim().length > 3)];
    if (ok.indexOf(false) > -1) { form.querySelector('[aria-invalid="true"]').focus(); return; }
    var trade = ($('input[name=trade]:checked', form) || {}).value || '-';
    var body = msg.value.trim() + '\n\nName: ' + n.value.trim() + '\nKontakt: ' + c.value.trim() + '\nBranche: ' + trade;
    location.href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent('Demo-Anfrage über armsin.de') + '&body=' + encodeURIComponent(body);
    var btn = $('.send', form); btn.classList.add('ok'); btn.querySelector('span').textContent = '✓ ' + t('f.sent', 'Gesendet');
    $('.ok-msg', form).textContent = t('f.thanks', 'Danke, ich melde mich innerhalb von 24 h.');
  });

  /* ---------- boot screen, then power on the PC ---------- */
  function power() { if (window.PC3D && PC3D.power) PC3D.power(); }
  function later(fn) { if ('requestIdleCallback' in window) requestIdleCallback(fn, { timeout: 1500 }); else setTimeout(fn, 300); }
  document.addEventListener('DOMContentLoaded', function () {
    requestAnimationFrame(function () { measure(); update(); later(function () { routeReady = true; buildRoute(); update(); }); });
    var ready = window.PC3D ? PC3D.ready : Promise.resolve(false);
    if (!html.classList.contains('booting')) { ready.then(power); return; }
    var bar = $('#boot-bar'), pct = $('#boot-pct'), bm = $('#boot-msg'), boot = $('#boot'), t0 = performance.now(), target = .35, cur = 0, done = false;
    var fontsP = document.fonts ? document.fonts.ready : Promise.resolve();
    fontsP.then(function () { target = Math.max(target, .6); bm.textContent = t('boot.2', 'Lade Modell'); });
    function finish() {
      if (done) return; done = true; target = 1;
      setTimeout(function () { bm.textContent = t('boot.3', 'Bereit'); }, 120);
      setTimeout(function () { boot.classList.add('out'); power(); }, 420);
      setTimeout(function () { html.classList.remove('booting'); }, 1150);
    }
    Promise.race([ready, new Promise(function (r) { setTimeout(r, 2600); })]).then(function () {
      var wait = Math.max(0, 900 - (performance.now() - t0)); setTimeout(finish, wait); });
    (function tick() { cur += (target - cur) * .12; bar.style.transform = 'scaleX(' + cur.toFixed(3) + ')'; pct.textContent = Math.round(cur * 100) + ' %';
      if (cur < .995) requestAnimationFrame(tick); })();
  });
  addEventListener('load', function () { requestAnimationFrame(function () { offCache = {}; measure(); update(); }); });

  /* ---------- DE / EN (same storage key as the other pages) ---------- */
  var EN = {
    'meta.title': 'Web design Freiberg, Saxony | Armsin Digital Media',
    'meta.description': 'Web design from Freiberg (Saxony): websites, online booking and automation for hair salons, cafés, trades and practices. Free demo until 01.01.2027, then from €100 at a fixed price.',
    'skip': 'Skip to content', 'nav.home': 'Armsin Digital Media: go to homepage', 'nav.main': 'Main navigation', 'nav.menu': 'Open menu', 'nav.close': 'Close menu', 'nav.call': 'Call: +49 176 62625699', 'nav.book': 'Book a call', 'portal.k': 'How your customers search', 'hero.wa': 'or message me on WhatsApp', 'beweis.all': 'All projects',
    'nav.leistungen': 'Services', 'nav.preise': 'Pricing', 'nav.ablauf': 'Process', 'nav.projekte': 'Projects', 'nav.about': 'About me', 'nav.blog': 'Blog',
    'cta.demo': 'Free demo', 'cta.demoShort': 'Request demo', 'cta.wa': 'WhatsApp', 'chip': 'Demo slots open until 01.01.2027', 'rail': 'Chapters',
    'hero.tags': 'Websites · Booking · Automation · Photos', 'hero.h1a': 'Digital', 'hero.h1b': 'solutions', 'hero.h1c': 'from Germany.',
    'hero.sub': 'For hair salons, cafés, trades and practices in Saxony. The free demo first, then from €100 at a fixed price.',
    'trust.aria': 'Facts', 'trust.1': 'Fixed price before we start', 'trust.2': 'Reply within 24 h', 'trust.3': 'You get all logins', 'trust.4': 'From Freiberg, Saxony',
    'problem.label': '01 · The problem', 'problem.h2a': 'Your customers google you.', 'problem.h2b': 'What do they find?',
    'problem.lead': 'An outdated website costs enquiries. Quietly, every day, and usually nobody notices.',
    'problem.m1': 'No opening hours', 'problem.m2': 'No call button', 'problem.m3': 'Not updated since 2014',
    'problem.phone': 'Example: an outdated website on a phone, without opening hours or a call button',
    'loesung.label': '02 · The solution', 'loesung.h2a': 'A site that', 'loesung.h2b': 'calls,', 'loesung.h2c': 'books and orders.',
    'loesung.lead': 'Opening hours at the top, call with one tap, bookings around the clock. Built for phones first.',
    'loesung.cta': 'A demo like this for my business', 'loesung.phone': 'Example: the same site rebuilt, with opening hours, call, booking and directions',
    'fuer.label': '03 · Who it is for', 'fuer.h2a': 'For', 'fuer.h2b': 'you.',
    'fuer.c1.h': 'Hair salon', 'fuer.c1.p': 'Customers book their own appointment, even at 10 pm.', 'fuer.c1.a': 'Demo for salons',
    'fuer.c2.h': 'Café', 'fuer.c2.p': 'Menu, opening hours and table booking at a glance.', 'fuer.c2.a': 'Demo for cafés',
    'fuer.c3.h': 'Trades', 'fuer.c3.p': 'Requests with photos of the damage, straight to your phone.', 'fuer.c3.a': 'Demo for trades',
    'fuer.c4.h': 'Practice', 'fuer.c4.p': 'Services, opening hours and directions, without a phone queue.', 'fuer.c4.a': 'Demo for practices',
    'fuer.more': 'Your business is not listed?', 'fuer.moreA': 'Write to me anyway',
    'preise.label': '04 · Services & pricing', 'preise.h2': 'What does it cost?', 'preise.lead': 'Guide prices up front, so you know where you stand. The first call and the demo are free.',
    'p1.k': 'Website', 'p1.t': 'Starter', 'p1.h': 'Simple website', 'p1.l1': 'Offer, opening hours and contact', 'p1.l2': 'Photos, menu or references', 'p1.l3': 'Contact or enquiry form',
    'p2.k': 'Website+', 'p2.t': 'With booking', 'p2.h': 'Website with booking & extras', 'p2.l1': 'Online appointments or reservations', 'p2.l2': 'Online ordering, animations', 'p2.l3': 'Everything from “Simple website” included',
    'p3.k': 'App', 'p3.h': 'Your own app', 'p3.l1': 'Customer account, bookings, orders', 'p3.l2': 'Push notifications, payments', 'p3.l3': 'Also for your team internally',
    'p4.k': 'System', 'p4.h': 'Systems & automation', 'p4.price': 'by scope', 'p4.l1': 'Appointment reminders, e-mails, workflows', 'p4.l2': 'A short call first, then the fixed price', 'p4.l3': 'Runs in the background, no extra work',
    'once': 'one-off', 'from': 'from', 'fotos.k': 'Photography:', 'fotos.p': 'improve existing photos with AI, €12 per 10 images (cheaper together with a website). New photos on site by arrangement.',
    'preise.note': 'Guide prices; the written fixed-price offer is binding.',
    'calc.k': 'Needs check · 30 seconds', 'calc.h': 'What does your business need?', 'calc.base': 'Basics', 'calc.extra': 'Extras',
    'calc.b1': 'Offer, opening hours & contact', 'calc.b2': 'Photos, menu or references', 'calc.b3': 'Contact or enquiry form',
    'calc.e1': 'Online booking', 'calc.e2': 'Reservations', 'calc.e3': 'Online ordering', 'calc.e4': 'Animations',
    'calc.photos': 'Improve existing photos with AI', 'calc.none': 'none', 'calc.result': 'Guide price', 'calc.cta': 'Request a demo with this result',
    'calc.note': 'App or automation? I name the price after a short call.',
    'ablauf.label': '05 · Process', 'ablauf.h2a': 'From the first call to the', 'ablauf.h2b': 'finished site.',
    's1.h': 'Short call', 's1.p': '15–20 minutes, free', 's2.h': 'Free demo', 's2.p': 'You see your site before you pay', 's3.h': 'Fixed price & build', 's3.p': 'Written offer, then progress updates', 's4.h': 'Handover', 's4.p': 'Domain, hosting, logins: all yours',
    'ablauf.cta': 'Book step 1 now', 'ablauf.more': 'Process in detail',
    'beweis.label': '06 · Real work', 'beweis.h2': 'No invented clients.', 'beweis.yK': 'Client project · beta demo · Dresden', 'beweis.yH': 'Youroma, perfumery',
    'beweis.yP': 'Beta demo for a small perfumery with fragrances from the Gulf states, presented calmly. Shown with the owner’s permission.', 'beweis.yA': 'View project',
    'beweis.yAlt': 'Homepage of the beta demo for the Youroma perfumery in Dresden',
    'beweis.kT': 'Concept project', 'beweis.kP': 'Concept website for a young marketing agency in Dresden', 'beweis.kAlt': 'Concept website for KIVORA, a marketing agency in Dresden',
    'beweis.rT': 'Demo project, fictional brand', 'beweis.rP': 'Sample website for a travel agency with a booking request', 'beweis.rAlt': 'ReiseGlück demo website for a fictional travel agency',
    'beweis.hS': 'Armsin has existed since 2026.', 'beweis.hP': 'You only see what was really built. I will show reviews once real clients have written them. Your business could be the next project.', 'beweis.cta': 'Start my project',
    'ueber.label': '07 · Who is behind it', 'ueber.h2': 'Hello, I’m Yass.', 'ueber.aside': 'one contact person, from the first call until after launch.', 'ueber.alt': 'Yass Almardoud, founder of Armsin Digital Media',
    'ueber.p': 'I founded Armsin Digital Media in Freiberg in 2026. Before that I worked as a backend developer. Today I build websites and automations for businesses, explain everything clearly and work at a fixed price.',
    'ueber.place': 'Freiberg, Saxony · for all of Germany', 'ueber.cta': 'Talk to Yass', 'ueber.more': 'More about me',
    'faq.label': '08 · Questions', 'faq.h2': 'Quick answers.',
    'faq.q1': 'What does the demo website cost?', 'faq.a1': 'Nothing. Until 01.01.2027 I build you a demo website, free and without obligation.',
    'faq.q2': 'Do I have to buy anything afterwards?', 'faq.a2': 'No. If you like the demo, you get a written fixed-price offer. If not, that’s the end of it.',
    'faq.q3': 'How long until my website is online?', 'faq.a3': 'We set the schedule in the offer. It depends mostly on how quickly texts, photos and opening hours are ready. I help you with that.',
    'faq.q4': 'Can I change texts myself later?', 'faq.a4': 'Yes. I show you how. Or you send me a short message and I change it.',
    'faq.q5': 'Who owns the domain and hosting?', 'faq.a5': 'You do. Domain and hosting run in your name, and you get all logins. Nothing stays with me.',
    'faq.q6': 'Do you only work in Freiberg and Saxony?', 'faq.a6': 'No. I am based in Freiberg, Saxony and work for businesses all over Germany. Calls run by phone or video, in Saxony also in person if you like.',
    'faq.q7': 'Will people find my new website on Google?', 'faq.a7': 'Nobody can honestly guarantee Google rankings. I make sure of a clean technical base, fast loading and clear details about your location and area, and I help with your Google Business Profile.',
    'kontakt.label': '09 · Contact', 'kontakt.h2': 'Write to me.', 'kontakt.lead': 'Via WhatsApp, in a call or with the form. You get a reply within 24 hours.',
    't1.h': 'Message on WhatsApp', 't2.h': 'Book a call with Yass', 't2.p': '15–20 minutes, free (Cal.com)', 't3.h': 'E-mail',
    'f.name': 'Your name', 'f.nameP': 'First and last name', 'f.nameE': 'Please enter your name.', 'f.contact': 'E-mail or phone', 'f.contactP': 'How I can reach you', 'f.contactE': 'Please enter an e-mail address or phone number.',
    'f.trade': 'Business type', 'tr.1': 'Hair salon', 'tr.2': 'Café', 'tr.3': 'Trades', 'tr.4': 'Practice', 'tr.5': 'Other',
    'f.msg': 'What is it about?', 'f.msgP': 'For example: new website with online booking', 'f.msgE': 'One or two sentences are enough.',
    'f.send': 'Request free demo', 'f.note': 'Opens your e-mail app with a ready message to me. I only use your details to reply.',
    'f.sent': 'Sent', 'f.thanks': 'Thank you, I will get back to you within 24 h.',
    'foot.p': 'Websites, booking and automation for businesses. Karl-Kegel-Str. 45, 09599 Freiberg, Germany.', 'foot.nav': 'Pages', 'foot.careers': 'Careers', 'foot.impressum': 'Legal notice', 'foot.datenschutz': 'Privacy policy',
    'foot.small': 'Examples are marked as “Example”.', 'wa.aria': 'Message Yass on WhatsApp',
    'boot.2': 'Loading model', 'boot.3': 'Ready'
  };
  var lang = 'de';
  function t(key, de) { return lang === 'en' && EN[key] ? EN[key] : de; }
  var els = $$('[data-i18n]'), ariaEls = $$('[data-i18n-aria]'), altEls = $$('[data-i18n-alt]'), phEls = $$('[data-i18n-ph]');
  els.forEach(function (e) { e._de = e.tagName === 'META' ? e.content : e.textContent; });
  ariaEls.forEach(function (e) { e._de = e.getAttribute('aria-label'); });
  altEls.forEach(function (e) { e._de = e.alt; });
  phEls.forEach(function (e) { e._de = e.placeholder; });
  function applyLang(l) {
    lang = l; html.lang = l;
    els.forEach(function (e) { var v = t(e.getAttribute('data-i18n'), e._de); if (e.tagName === 'META') e.content = v; else e.textContent = v; });
    ariaEls.forEach(function (e) { e.setAttribute('aria-label', t(e.getAttribute('data-i18n-aria'), e._de)); });
    altEls.forEach(function (e) { e.alt = t(e.getAttribute('data-i18n-alt'), e._de); });
    phEls.forEach(function (e) { e.placeholder = t(e.getAttribute('data-i18n-ph'), e._de); });
    $$('.lang-btn').forEach(function (b) { var on = b.dataset.lang === l; b.classList.toggle('is-active', on); b.setAttribute('aria-pressed', String(on)); });
    $$('[data-wa]').forEach(function (a) { a.href = waHref(l === 'en' ? 'Hello Yass, I am interested in a free demo website for my business.' : WA_TEXT); });
  }
  $$('.lang-btn').forEach(function (b) { b.addEventListener('click', function () { try { localStorage.setItem('armsin-lang', b.dataset.lang); } catch (e) {} applyLang(b.dataset.lang); }); });
  var saved = 'de'; try { saved = localStorage.getItem('armsin-lang') || 'de'; } catch (e) {}
  if (saved === 'en') applyLang('en');
})();
