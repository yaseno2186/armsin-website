// Shared page behavior — nav toggle, nav hover indicator, scroll reveal,
// and the contact form's mailto handoff. Loaded on every page; each
// function checks for its own elements first, so it's a no-op on pages
// that don't have them (e.g. the contact form only exists on index.html).

function initNavToggle() {
  var nav = document.querySelector('.floating-nav');
  var toggle = document.querySelector('.nav-toggle');
  var panel = document.querySelector('.nav-menu');
  if (!nav || !toggle || !panel) return;

  var close = function () {
    nav.classList.remove('nav-open');
    toggle.setAttribute('aria-expanded', 'false');
  };

  toggle.addEventListener('click', function (e) {
    e.stopPropagation();
    var isOpen = nav.classList.toggle('nav-open');
    toggle.setAttribute('aria-expanded', String(isOpen));
  });

  panel.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', close);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') close();
  });

  // Dropdown has no full-screen scrim (it's a small floating card, not a
  // drawer) — a tap/click anywhere outside the pill closes it instead.
  document.addEventListener('click', function (e) {
    if (nav.classList.contains('nav-open') && !nav.contains(e.target)) close();
  });

  window.addEventListener('resize', function () {
    if (window.innerWidth > 700) close();
  });
}

// Sliding pill highlight that glides to whichever nav link is hovered or
// focused, snapping back to the active link when the pointer leaves.
function initNavIndicator() {
  var links = document.querySelector('.nav-links');
  var indicator = document.querySelector('.nav-indicator');
  if (!links || !indicator) return;

  var moveTo = function (el) {
    indicator.style.setProperty('--indicator-x', el.offsetLeft + 'px');
    indicator.style.setProperty('--indicator-width', el.offsetWidth + 'px');
  };

  var track = function (el) {
    links.classList.add('is-tracking');
    moveTo(el);
  };

  var reset = function () {
    var active = links.querySelector('a.is-active');
    if (active) {
      moveTo(active);
    } else {
      links.classList.remove('is-tracking');
    }
  };

  links.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('mouseenter', function () { track(link); });
    link.addEventListener('focus', function () { track(link); });
  });

  links.addEventListener('mouseleave', reset);
  links.addEventListener('focusout', function (e) {
    if (!links.contains(e.relatedTarget)) reset();
  });

  reset();
}

function initScrollReveal() {
  var revealEls = document.querySelectorAll('[data-reveal]');

  if (!('IntersectionObserver' in window)) {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  revealEls.forEach(function (el) { observer.observe(el); });
}

// Cal.com booking embed: click-to-load. The iframe has no src until the
// visitor clicks "Kalender laden", so no data goes to Cal.com before that
// (see datenschutz.html section 6). The site's current theme (dark/light)
// is passed on so the calendar matches. Fades in once loaded.
function initBookingFade() {
  document.querySelectorAll('.booking-frame').forEach(function (frame) {
    var iframe = frame.querySelector('iframe[data-src]');
    var btn = frame.querySelector('.booking-consent-btn');
    if (!iframe || !btn) return;
    iframe.addEventListener('load', function () {
      if (!iframe.getAttribute('src')) return;
      iframe.classList.add('is-loaded');
      frame.classList.add('is-loaded');
    });
    btn.addEventListener('click', function () {
      frame.classList.add('is-loading');
      var src = iframe.getAttribute('data-src');
      var light = document.documentElement.getAttribute('data-theme') === 'light';
      src += (src.indexOf('?') === -1 ? '?' : '&') + 'theme=' + (light ? 'light' : 'dark');
      iframe.setAttribute('src', src);
      iframe.focus();
    });
  });
}

// Pointer-parallax tilt for the hero's retro-PC scene: eases --tilt-x/--tilt-y
// (both -1..1, read by .pc-scene-inner's transform in style.css) toward the
// cursor position, so the monitor+floaters composition reads as reacting to
// the visitor rather than sitting on a flat sprite. Desktop hover only —
// coarse-pointer devices keep the CSS idle-float animation and skip this.
function initHeroParallax() {
  var scene = document.getElementById('pc-scene-inner');
  if (!scene) return;

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var canHover = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  if (reduceMotion || !canHover) return;

  window.addEventListener('pointermove', function (e) {
    var x = (e.clientX / window.innerWidth - 0.5) * 2;
    var y = (e.clientY / window.innerHeight - 0.5) * 2;
    scene.style.setProperty('--tilt-x', x.toFixed(3));
    scene.style.setProperty('--tilt-y', y.toFixed(3));
  });
}

function initContactForm() {
  var contactForm = document.getElementById('contact-form');
  if (!contactForm) return;

  // No backend yet — hand off to the visitor's own email client with a
  // prefilled message instead of pretending to submit anywhere.
  contactForm.addEventListener('submit', function (e) {
    e.preventDefault();
    var name = document.getElementById('cf-name').value.trim();
    var email = document.getElementById('cf-email').value.trim();
    var message = document.getElementById('cf-message').value.trim();

    var subject = 'Anfrage über die Website von ' + name;
    var body = message + '\n\nVon: ' + name + ' (' + email + ')';

    window.location.href = 'mailto:yaseno2186ss@gmail.com'
      + '?subject=' + encodeURIComponent(subject)
      + '&body=' + encodeURIComponent(body);
  });
}

// Category filter for the portfolio grid (projects.html): shows/hides
// project cards by their data-category, no page reload or routing needed.
function initPortfolioFilter() {
  var buttons = document.querySelectorAll('.portfolio-filter-btn');
  var cards = document.querySelectorAll('.portfolio-card');
  var emptyMsg = document.querySelector('[data-portfolio-empty]');
  if (!buttons.length || !cards.length) return;

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      buttons.forEach(function (b) { b.classList.remove('is-active'); });
      btn.classList.add('is-active');

      var filter = btn.dataset.filter;
      var visibleCount = 0;
      cards.forEach(function (card) {
        var match = filter === 'all' || card.dataset.category === filter;
        card.classList.toggle('is-hidden', !match);
        if (match) visibleCount++;
      });
      if (emptyMsg) emptyMsg.hidden = visibleCount !== 0;
    });
  });
}

// Dark/light switch in the footer. Dark is the default; a saved "light"
// choice is applied before first paint by the inline script in each
// page's <head>. Switching uses the View Transitions API where available:
// the browser cross-fades one snapshot of the page on the GPU instead of
// animating every element, which is what made the old switch laggy.
var THEME_KEY = 'armsin-theme-v2';

// Icons and step illustrations have a "-light.svg" twin drawn in the light
// palette; swap them so the graphics always match the page.
function swapThemeAssets(theme) {
  document.querySelectorAll('img[src*="assets/icons/"], img[src*="assets/images/"]').forEach(function (img) {
    var src = img.getAttribute('src');
    if (!/\.svg$/.test(src)) return;
    var isLight = /-light\.svg$/.test(src);
    if (theme === 'light' && !isLight) img.setAttribute('src', src.replace(/\.svg$/, '-light.svg'));
    if (theme !== 'light' && isLight) img.setAttribute('src', src.replace(/-light\.svg$/, '.svg'));
  });
}

function initThemeSwitch() {
  var root = document.documentElement;
  var buttons = document.querySelectorAll('.theme-btn');
  var current = function () { return root.getAttribute('data-theme') === 'light' ? 'light' : 'dark'; };

  var sync = function () {
    var theme = current();
    buttons.forEach(function (btn) {
      var on = btn.dataset.themeSet === theme;
      btn.classList.toggle('is-active', on);
      btn.setAttribute('aria-pressed', String(on));
    });
    swapThemeAssets(theme);
  };

  var apply = function (theme) {
    if (theme === 'light') root.setAttribute('data-theme', 'light');
    else root.removeAttribute('data-theme');
    try { localStorage.setItem(THEME_KEY, theme); } catch (e) {}
    sync();
  };

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var next = btn.dataset.themeSet;
      if (next === current()) return;
      if (document.startViewTransition && !reduceMotion) {
        document.startViewTransition(function () { apply(next); });
      } else {
        apply(next);
      }
    });
  });

  sync();
}

// ---------- Motion pass ----------

// Thin progress line at the top showing how far down the page you are.
function initScrollProgress() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var bar = document.createElement('div');
  bar.className = 'scroll-progress';
  bar.setAttribute('aria-hidden', 'true');
  document.body.appendChild(bar);
  var ticking = false;
  var update = function () {
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var p = max > 0 ? Math.min(1, window.scrollY / max) : 0;
    bar.style.transform = 'scaleX(' + p.toFixed(4) + ')';
    ticking = false;
  };
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; window.requestAnimationFrame(update); }
  }, { passive: true });
  update();
}

// Terminal "decode" effect: headings briefly show random characters that
// resolve left to right into the real text when they scroll into view.
// The heading font is monospaced, so the line never changes width.
function initHeadingDecode() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (!('IntersectionObserver' in window)) return;
  var GLYPHS = '01<>/{}[]=+*#$%&_';
  var targets = document.querySelectorAll(
    '.section-head h2, .page-hero h1, .about-cta-inner h2, .booking-head h2, .contact-info h2, .blog-section h2, .studio-hero-inner h1'
  );

  var decode = function (el) {
    if (el.children.length) return;          // only plain-text headings
    var finalText = el.textContent;
    var len = finalText.length;
    var start = null;
    var duration = Math.min(900, 300 + len * 14);
    var last = '';
    el.setAttribute('aria-label', finalText);   // screen readers get the real text
    var step = function (now) {
      if (last && el.textContent !== last) return;   // text changed (language switch): stop
      if (start === null) start = now;
      var t = Math.min(1, (now - start) / duration);
      var settled = Math.floor(t * len);
      var out = '';
      for (var i = 0; i < len; i++) {
        var c = finalText[i];
        out += (i < settled || c === ' ') ? c : GLYPHS[(Math.random() * GLYPHS.length) | 0];
      }
      el.textContent = out;
      last = out;
      if (t < 1) window.requestAnimationFrame(step);
      else { el.textContent = finalText; el.removeAttribute('aria-label'); }
    };
    window.requestAnimationFrame(step);
  };

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      io.unobserve(entry.target);
      decode(entry.target);
    });
  }, { threshold: 0.6 });
  targets.forEach(function (el) { io.observe(el); });
}

// Cursor spotlight on cards: feeds the pointer position to CSS.
function initCardSpotlight() {
  if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  document.querySelectorAll('.service-card, .blog-card').forEach(function (card) {
    card.addEventListener('pointermove', function (e) {
      var r = card.getBoundingClientRect();
      card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      card.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });
}

// Homepage process thread draws itself once it scrolls into view.
function initProcessLine() {
  var steps = document.querySelector('.process-steps');
  if (!steps) return;
  if (!('IntersectionObserver' in window)) { steps.classList.add('is-drawn'); return; }
  var io = new IntersectionObserver(function (entries) {
    if (entries[0].isIntersecting) { steps.classList.add('is-drawn'); io.disconnect(); }
  }, { threshold: 0.3 });
  io.observe(steps);
}

// Footer joins the scroll reveal (must run before initScrollReveal).
function markFooterReveal() {
  var f = document.querySelector('.footer-inner');
  if (f) f.setAttribute('data-reveal', '');
}

// Services carousel: endless row of image cards. Auto-scrolls slowly to
// the right; any touch, drag, wheel, hover, focus or arrow click pauses it
// and it resumes after a few quiet seconds. The card nearest the middle
// grows a little, the others return to normal size.
// Services coverflow (index.html .svc-flow): the middle card sits in front
// with its monitor switched on; neighbours sit smaller behind, turned toward
// the middle, screens off. When a card reaches the middle its screen powers
// on (slim-monitor's built-in fade) and the monitor turns to face you.
// Arrows, swipe, arrow keys, click on a side card; slow auto-advance that
// pauses on hover/focus and is off for reduced motion.
function initServiceFlow() {
  var track = document.querySelector('.svc-flow-track');
  if (!track) return;
  var cards = Array.prototype.slice.call(track.querySelectorAll('.svc-card3'));
  var n = cards.length;
  var current = 0;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function layout() {
    cards.forEach(function (card, i) {
      var off = ((i - current) % n + n) % n;      // 0..n-1
      if (off > n / 2) off -= n;                  // -> -n/2..n/2
      var abs = Math.abs(off);
      card.style.setProperty('--off', off);
      card.style.setProperty('--abs', abs);
      card.style.zIndex = String(10 - abs);
      card.classList.toggle('is-active', off === 0);
      card.classList.toggle('is-far', abs >= 2);
      card.setAttribute('aria-hidden', off === 0 ? 'false' : 'true');
      var mon = card.querySelector('slim-monitor');
      if (mon && mon.setView) {
        mon.on = off === 0;
        mon.setView(-6, off === 0 ? 0 : (off < 0 ? 28 : -28), !reduceMotion);
      }
    });
  }
  function go(dir) { current = (current + dir + n) % n; layout(); }

  document.querySelectorAll('.svc-flow [data-svc-dir]').forEach(function (btn) {
    btn.addEventListener('click', function () { go(parseInt(btn.getAttribute('data-svc-dir'), 10)); restart(); });
  });
  // Click a side card to bring it to the middle (ignored right after a swipe).
  var swiped = false;
  track.addEventListener('click', function (e) {
    if (swiped) { swiped = false; return; }
    var card = e.target.closest('.svc-card3');
    if (!card || card.classList.contains('is-active')) return;
    var off = parseInt(card.style.getPropertyValue('--off'), 10);
    if (off) { go(off); restart(); }
  });
  track.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') { go(-1); restart(); e.preventDefault(); }
    if (e.key === 'ArrowRight') { go(1); restart(); e.preventDefault(); }
  });
  var startX = null;
  track.addEventListener('pointerdown', function (e) { startX = e.clientX; });
  track.addEventListener('pointerup', function (e) {
    if (startX === null) return;
    var dx = e.clientX - startX; startX = null;
    if (Math.abs(dx) > 40) { swiped = true; go(dx < 0 ? 1 : -1); restart(); }
  });

  var timer = null, paused = false;
  function restart() {
    if (reduceMotion) return;
    clearInterval(timer);
    timer = setInterval(function () { if (!paused && !document.hidden) go(1); }, 5000);
  }
  ['mouseenter', 'focusin'].forEach(function (ev) { track.parentNode.addEventListener(ev, function () { paused = true; }); });
  ['mouseleave', 'focusout'].forEach(function (ev) { track.parentNode.addEventListener(ev, function () { paused = false; }); });

  // slim-monitor upgrades when its (deferred) script runs; lay out after.
  if (window.customElements && customElements.whenDefined) {
    customElements.whenDefined('slim-monitor').then(layout);
  }
  layout();
  restart();
}

function initServiceCarousel() {
  var track = document.querySelector('.svc-track');
  if (!track) return;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var originals = Array.prototype.slice.call(track.children);
  var SPEED = 28;            // px per second
  var RESUME_MS = 3500;      // quiet time before auto-scroll restarts
  var GROW = 0.07;           // centre card is 7% bigger

  // Endless loop: a copy of the set before and two after the real cards.
  // Copies are hidden from screen readers and keyboard.
  var setWidth = 0;
  function buildClones() {
    track.querySelectorAll('.svc-clone').forEach(function (c) { c.remove(); });
    var make = function () {
      return originals.map(function (card) {
        var c = card.cloneNode(true);
        c.classList.add('svc-clone');
        c.setAttribute('aria-hidden', 'true');
        c.setAttribute('inert', '');
        c.querySelectorAll('[data-i18n]').forEach(function (el) { el.removeAttribute('data-i18n'); });
        return c;
      });
    };
    make().forEach(function (c) { track.insertBefore(c, originals[0]); });
    make().concat(make()).forEach(function (c) { track.appendChild(c); });
  }
  function measure() {
    var gap = parseFloat(getComputedStyle(track).columnGap) || 0;
    setWidth = originals.reduce(function (w, c) { return w + c.offsetWidth + gap; }, 0);
  }
  buildClones();
  measure();

  var cards = function () { return track.children; };
  var pos = 0;
  // start with the first real card in the middle
  function centerOn(card) {
    return card.offsetLeft + card.offsetWidth / 2 - track.clientWidth / 2;
  }
  pos = centerOn(originals[0]);
  track.scrollLeft = pos;

  // Jump by exactly one set when the view drifts too far: the copies make
  // the jump invisible. `pos` keeps sub-pixel precision for the slow
  // auto-scroll (browsers round scrollLeft to whole pixels).
  function wrap() {
    var base = centerOn(originals[0]);
    if (track.scrollLeft < base - setWidth * 0.5) { track.scrollLeft += setWidth; pos += setWidth; }
    else if (track.scrollLeft > base + setWidth * 1.5) { track.scrollLeft -= setWidth; pos -= setWidth; }
  }

  function scaleCards() {
    if (reduceMotion) return;
    var mid = track.scrollLeft + track.clientWidth / 2;
    var list = cards();
    for (var i = 0; i < list.length; i++) {
      var c = list[i];
      var d = Math.abs(c.offsetLeft + c.offsetWidth / 2 - mid);
      var t = Math.max(0, 1 - d / (c.offsetWidth * 0.9));
      var e = t * t * (3 - 2 * t); // smoothstep: eases in and out of the centre
      c.style.setProperty('--s', (1 + GROW * e).toFixed(4));
    }
  }

  // ---- who is in control: auto or person ----
  var userUntil = 0;
  var visible = true;
  var hovering = false;
  function userActive() {
    userUntil = performance.now() + RESUME_MS;
    track.classList.add('is-user');
  }

  ['pointerdown', 'wheel', 'touchstart', 'keydown', 'focusin'].forEach(function (ev) {
    track.addEventListener(ev, userActive, { passive: true });
  });
  track.addEventListener('mouseenter', function () { hovering = true; });
  track.addEventListener('mouseleave', function () { hovering = false; userUntil = performance.now() + 1200; });

  // Mouse drag (touch scrolls natively)
  var drag = null;
  track.addEventListener('pointerdown', function (e) {
    if (e.pointerType !== 'mouse' || e.button !== 0) return;
    drag = { x: e.clientX, left: track.scrollLeft, moved: false };
    track.classList.add('is-user');
  });
  window.addEventListener('pointermove', function (e) {
    if (!drag) return;
    var dx = e.clientX - drag.x;
    if (Math.abs(dx) > 4) { drag.moved = true; track.classList.add('is-dragging'); track.style.scrollSnapType = 'none'; }
    track.scrollLeft = drag.left - dx;
  });
  window.addEventListener('pointerup', function () {
    if (!drag) return;
    drag = null;
    track.classList.remove('is-dragging');
    track.style.scrollSnapType = '';
    userActive();
  });

  // Arrow buttons: one card left/right
  document.querySelectorAll('.svc-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      userActive();
      var step = originals[0].offsetWidth + (parseFloat(getComputedStyle(track).columnGap) || 0);
      track.scrollBy({ left: step * Number(btn.dataset.svcDir), behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  });

  track.addEventListener('scroll', function () {
    if (!drag) wrap();
    scaleCards();
  }, { passive: true });

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) { visible = entries[0].isIntersecting; }).observe(track);
  }

  // Language switch: refresh the copies so they show the new language
  document.querySelectorAll('.lang-btn').forEach(function (b) {
    b.addEventListener('click', function () { setTimeout(function () { var l = track.scrollLeft; buildClones(); measure(); track.scrollLeft = l; scaleCards(); }, 0); });
  });
  window.addEventListener('resize', function () { measure(); scaleCards(); });

  var last = performance.now();
  function tick(now) {
    var dt = Math.min(0.05, (now - last) / 1000);
    last = now;
    var auto = !reduceMotion && visible && !hovering && !drag && now > userUntil && !document.hidden;
    if (auto) {
      if (track.classList.contains('is-user')) { track.classList.remove('is-user'); pos = track.scrollLeft; }
      pos += SPEED * dt;
      track.scrollLeft = pos;   // scroll event wraps + scales
    }
    requestAnimationFrame(tick);
  }
  scaleCards();
  if (!reduceMotion) requestAnimationFrame(tick);
  else track.classList.add('is-user');
}

// Homepage needs check: a short survey that shows a recommendation and
// a price range only at the end. Texts and prices live in index.html;
// which questions appear depends on the first answer (data-path on each
// step). This only decides which result fits and fills it in.
function initNeedsCheck() {
  var app = document.getElementById('check-app');
  if (!app) return;
  var form = app.querySelector('.check-form');
  var allSteps = Array.prototype.slice.call(app.querySelectorAll('.check-step'));
  var progressBar = app.querySelector('.check-progress-track span');
  var nav = app.querySelector('.check-nav');
  var backBtn = app.querySelector('[data-check-action="back"]');
  var nextBtn = app.querySelector('[data-check-action="next"]');
  var result = app.querySelector('.check-result');
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var path = [allSteps[0]];
  var current = 0;
  var showingResult = false;
  var lastPointer = 0;

  var part = function (name) { return app.querySelector('[data-check="' + name + '"]'); };
  var label = function (name) {
    var el = app.querySelector('[data-label="' + name + '"]');
    return el ? el.textContent.trim() : '';
  };
  var fmt = function (n) {
    return new Intl.NumberFormat(document.documentElement.lang === 'en' ? 'en-US' : 'de-DE').format(n);
  };
  var titleOf = function (input) {
    var t = input.closest('label').querySelector('.check-option-title, .check-card-title');
    return t ? t.textContent.trim() : '';
  };

  var need = function () {
    var r = form.querySelector('input[name="need"]:checked');
    return r ? r.value : null;
  };

  var photoType = function () {
    var r = form.querySelector('input[name="phototype"]:checked');
    return r ? r.value : null;
  };

  var buildPath = function () {
    var n = need();
    var pt = photoType();
    path = allSteps.filter(function (step, i) {
      if (i === 0) return true;
      if (!n || step.dataset.path.split(' ').indexOf(n) === -1) return false;
      // "Wie viele Bilder?" is skipped when no photos are wanted. Counted
      // until then, so the step total only ever shrinks, never jumps up.
      if (step.dataset.if === 'photos') return pt !== 'none';
      return true;
    });
  };

  // Everything answered on the active path, in order
  var readState = function () {
    var s = { need: need(), situation: null, picks: [], photoType: null, photos: 0, photosInput: null };
    path.slice(1).forEach(function (step) {
      step.querySelectorAll('input:checked').forEach(function (input) {
        if (input.name === 'situation') s.situation = input;
        else if (input.name === 'phototype') s.photoType = input;
        else if (input.name === 'photos') { s.photos = parseInt(input.value, 10); s.photosInput = input; }
        else s.picks.push(input);
      });
    });
    return s;
  };

  var pickResult = function (s) {
    if (s.need === 'photo') return 'photo-' + (s.photoType ? s.photoType.value : 'new');
    if (s.need !== 'website') return s.need;
    var advanced = s.picks.some(function (i) { return i.dataset.tier === 'advanced'; });
    if (advanced) return 'advanced';
    // A working website that only needs the basics doesn't need replacing.
    if (s.situation && s.situation.value === 'good') return 'none';
    return 'basic';
  };

  // ---- Price calculation ----
  // The base price (data-min/-max) covers the first feature of the
  // recommended kind; every further feature adds data-add-min/-max, and
  // photos add data-per10 per 10 images. All numbers live in index.html.
  var per10 = +(app.querySelector('.check-results').dataset.per10 || 12);

  var calculate = function (s, key) {
    var block = app.querySelector('[data-result="' + key + '"]');
    var mode = block.dataset.mode;
    var lines = [];
    if (key === 'basic' || key === 'advanced' || key === 'app') {
      var counted = key === 'app' ? s.picks
        : s.picks.filter(function (i) { return i.dataset.tier === key; });
      var isFrom = mode === 'from';
      var addMin = +(block.dataset.addMin || 0);
      var addMax = isFrom ? addMin : +(block.dataset.addMax || addMin);
      lines.push({
        text: label('bdBase').replace('{feature}', counted.length ? titleOf(counted[0]) : ''),
        min: +block.dataset.min, max: isFrom ? +block.dataset.min : +block.dataset.max, from: isFrom
      });
      counted.slice(1).forEach(function (i) {
        lines.push({ text: '+ ' + titleOf(i), min: addMin, max: addMax, from: isFrom });
      });
      // The basics come with a website that books, reserves or sells.
      if (key === 'advanced' && s.picks.some(function (i) { return i.dataset.tier === 'basic'; })) {
        lines.push({ text: label('bdIncluded'), included: true });
      }
    }
    if (s.photos > 0 && s.photoType) {
      var photoText = (s.need === 'photo' ? '' : '+ ') + titleOf(s.photoType) + ', ' + titleOf(s.photosInput);
      if (s.photoType.value === 'new') {
        // New photos on site: travel and time on top, so no fixed number
        lines.push({ text: photoText, agree: true });
      } else {
        var cost = s.photos / 10 * per10;
        // "30 or more": the line says "ab", the total keeps its range
        lines.push({ text: photoText, min: cost, max: cost, from: s.photos >= 30, openEnd: true });
      }
    }

    var total;
    if (mode === 'custom') total = [label('custom')];
    else if (mode === 'agree') total = [label('agree')];
    else if (mode === 'talk') total = [label('talk')];
    else {
      var priced = lines.filter(function (l) { return !l.included && !l.agree; });
      var min = 0, max = 0, from = false;
      priced.forEach(function (l) { min += l.min; max += l.max; from = from || (l.from && !l.openEnd); });
      // Photos only, 30 or more: nothing else to give the total a range
      if (!from && priced.length && priced.every(function (l) { return l.openEnd && l.from; })) from = true;
      total = rangeParts(min, max, from);
    }
    return { lines: lines, total: total };
  };

  // Price as pieces; numbers stay numbers so they can count up.
  var rangeParts = function (min, max, from) {
    if (from) return [label('from') + ' ', min, ' €'];
    if (min === max) return [min, ' €'];
    return [min, ' – ', max, ' €'];
  };
  var partsToText = function (parts) {
    return parts.map(function (p) { return typeof p === 'number' ? fmt(p) : p; }).join('');
  };
  var totalLabel = function (calc) {
    return label(calc.lines.some(function (l) { return l.agree; }) ? 'bdTotalPlus' : 'bdTotal');
  };
  var lineValue = function (l) {
    if (l.included) return label('bdIncludedValue');
    if (l.agree) return label('bdAgree');
    return partsToText(rangeParts(l.min, l.max, l.from));
  };

  var renderPrice = function (el, parts, animate) {
    el.textContent = '';
    parts.forEach(function (p) {
      if (typeof p !== 'number') { el.appendChild(document.createTextNode(p)); return; }
      var span = document.createElement('span');
      span.className = 'check-num';
      var run = animate && !reduceMotion && p > 0;
      span.textContent = fmt(run ? 0 : p);
      el.appendChild(span);
      if (!run) return;
      var start = null;
      var tick = function (now) {
        if (start === null) start = now;
        var t = Math.min(1, (now - start) / 800);
        span.textContent = fmt(Math.round(p * (1 - Math.pow(1 - t, 3))));
        if (t < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    });
  };

  var stepValid = function (step) { return !!step.querySelector('input:checked'); };

  var syncChrome = function () {
    var total = need() ? path.length + 1 : 0;      // +1 for the result
    var pos = showingResult ? path.length : current;
    var text = total ? label('stepOf').replace('{n}', total) : label('step');
    part('progress').textContent = text.replace('{x}', pos + 1);
    var share = total ? (pos + 1) / total : 0.2;
    progressBar.style.transform = 'scaleX(' + share + ')';
    backBtn.hidden = current === 0;
    nextBtn.disabled = !stepValid(path[current]);
    var last = current === path.length - 1 && !!need();
    part('nextLabel').hidden = last;
    part('showLabel').hidden = !last;
  };

  var goTo = function (i, focus) {
    path[current].classList.remove('is-active');
    path[i].dataset.dir = i >= current ? 'fwd' : 'back';
    current = i;
    path[i].classList.add('is-active');
    syncChrome();
    if (focus) {
      var legend = path[i].querySelector('legend');
      if (legend) legend.focus({ preventScroll: true });
      if (app.getBoundingClientRect().top < 0) {
        app.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
      }
    }
  };

  var fillResult = function (animate) {
    var s = readState();
    var key = pickResult(s);
    var block = app.querySelector('[data-result="' + key + '"]');
    if (!block) return;
    part('title').textContent = block.querySelector('[data-part="title"]').textContent.trim();
    part('desc').textContent = block.querySelector('[data-part="desc"]').textContent.trim();
    var calc = calculate(s, key);
    renderPrice(part('price'), calc.total, animate);

    // Breakdown, only when there is something to add up
    var dl = part('breakdownList');
    dl.textContent = '';
    var showBreakdown = calc.lines.length > 1;
    part('breakdown').hidden = !showBreakdown;
    if (showBreakdown) {
      var row = function (text, value, cls) {
        var wrap = document.createElement('div');
        wrap.className = 'check-breakdown-row' + (cls ? ' ' + cls : '');
        var dt = document.createElement('dt');
        dt.textContent = text;
        var dd = document.createElement('dd');
        dd.textContent = value;
        wrap.appendChild(dt);
        wrap.appendChild(dd);
        dl.appendChild(wrap);
      };
      calc.lines.forEach(function (l) { row(l.text, lineValue(l), l.included ? 'is-included' : ''); });
      row(totalLabel(calc), partsToText(calc.total), 'is-total');
    }

    var items = [titleOf(form.querySelector('input[name="need"]:checked'))];
    if (s.situation) items.push(titleOf(s.situation));
    s.picks.forEach(function (i) { items.push(titleOf(i)); });
    if (s.photoType && s.photoType.value !== 'none') items.push(titleOf(s.photoType));
    if (s.photosInput && s.photos > 0) items.push(titleOf(s.photosInput));
    var list = part('list');
    list.textContent = '';
    items.forEach(function (text, idx) {
      var li = document.createElement('li');
      li.textContent = text;
      li.style.setProperty('--i', idx);
      list.appendChild(li);
    });

    var photoNote = '';
    if (s.photos > 0 && s.photoType && s.need !== 'photo') {
      if (s.photoType.value === 'new') photoNote = label('photoAgreeNote');
      else if (key === 'basic' || key === 'advanced') photoNote = label('photoBundle');
    }
    part('photo').textContent = photoNote;
    part('photo').hidden = !photoNote;
    part('note').hidden = key === 'unsure';   // nothing to estimate yet
  };

  var showResult = function () {
    showingResult = true;
    app.classList.add('is-result');
    fillResult(true);
    form.hidden = true;
    nav.hidden = true;
    result.hidden = false;
    syncChrome();
    if (app.getBoundingClientRect().top < 0) {
      app.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
    }
    result.focus({ preventScroll: true });
  };

  var markChecked = function () {
    form.querySelectorAll('input').forEach(function (i) {
      i.closest('label').classList.toggle('is-checked', i.checked);
    });
  };

  var restart = function () {
    form.reset();
    markChecked();
    allSteps.forEach(function (step) { step.classList.remove('is-active'); });
    current = 0;
    buildPath();
    showingResult = false;
    app.classList.remove('is-result');
    result.hidden = true;
    form.hidden = false;
    nav.hidden = false;
    goTo(0, true);
  };

  var next = function () {
    if (!stepValid(path[current])) return;
    if (current < path.length - 1) goTo(current + 1, true);
    else showResult();
  };

  var sendAsMessage = function () {
    var s = readState();
    var key = pickResult(s);
    var block = app.querySelector('[data-result="' + key + '"]');
    var field = document.getElementById('cf-message');
    if (!block || !field) return;
    var lines = [label('msgIntro'), '',
      '- ' + label('msgNeed') + ': ' + titleOf(form.querySelector('input[name="need"]:checked'))];
    if (s.situation) lines.push('- ' + label('msgSituation') + ': ' + titleOf(s.situation));
    if (s.picks.length) lines.push('- ' + label('msgFeatures') + ': ' + s.picks.map(titleOf).join(', '));
    if (s.photoType) {
      var photoText = s.photoType.value === 'none' ? label('photosNone')
        : titleOf(s.photoType) + (s.photosInput ? ', ' + titleOf(s.photosInput) : '');
      lines.push('- ' + label('msgPhotos') + ': ' + photoText);
    }
    var calc = calculate(s, key);
    lines.push('- ' + label('msgResult') + ': ' + block.querySelector('[data-part="title"]').textContent.trim() +
      ' (' + partsToText(calc.total) + ')');
    if (calc.lines.length > 1) {
      lines.push('');
      calc.lines.forEach(function (l) { lines.push('  ' + l.text + ': ' + lineValue(l)); });
      lines.push('  ' + totalLabel(calc) + ': ' + partsToText(calc.total));
    }
    field.value = lines.join('\n');
    var contact = document.getElementById('contact');
    if (contact) contact.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
    var name = document.getElementById('cf-name');
    if (name) name.focus({ preventScroll: true });
  };

  form.addEventListener('pointerdown', function () { lastPointer = Date.now(); });

  form.addEventListener('change', function (e) {
    var input = e.target;
    if (input.name === 'need') {
      // New direction: answers from another path no longer apply.
      allSteps.slice(1).forEach(function (step) {
        step.querySelectorAll('input').forEach(function (i) { i.checked = false; });
      });
      buildPath();
    }
    if (input.name === 'phototype') {
      if (input.value === 'none') {
        form.querySelectorAll('input[name="photos"]').forEach(function (i) { i.checked = false; });
      }
      buildPath();
    }
    markChecked();
    syncChrome();
    // Single-choice questions move on by themselves after a click or tap.
    // Keyboard users (arrow keys) keep control and use "Weiter".
    if (input.type === 'radio' && Date.now() - lastPointer < 800) {
      var stepAtClick = current;
      setTimeout(function () { if (current === stepAtClick && !showingResult) next(); }, 320);
    }
  });

  form.addEventListener('submit', function (e) { e.preventDefault(); next(); });
  nextBtn.addEventListener('click', next);
  backBtn.addEventListener('click', function () { if (current > 0) goTo(current - 1, true); });
  app.querySelector('[data-check-action="restart"]').addEventListener('click', restart);
  app.querySelector('[data-check-action="message"]').addEventListener('click', sendAsMessage);

  // Language switch: i18n.js swaps the static texts first, then the
  // generated ones (progress, result) are rebuilt in the new language.
  document.querySelectorAll('.lang-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      setTimeout(function () {
        syncChrome();
        if (showingResult) fillResult(false);
      }, 0);
    });
  });

  syncChrome();
}

markFooterReveal();
initNavToggle();
initNavIndicator();
initScrollReveal();
initBookingFade();
initHeroParallax();
initContactForm();
initPortfolioFilter();
initThemeSwitch();
initScrollProgress();
initHeadingDecode();
initCardSpotlight();
initProcessLine();
initServiceCarousel();
initServiceFlow();
initNeedsCheck();
