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

// The Google Calendar iframe otherwise pops in unstyled the instant it
// finishes loading; fading it in avoids that jarring flash.
function initBookingFade() {
  var iframe = document.querySelector('.booking-frame iframe');
  if (!iframe) return;
  iframe.addEventListener('load', function () {
    iframe.classList.add('is-loaded');
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
