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

// Types out a small Java class line by line into the retro monitor's screen,
// like someone actually writing code — each finished line gets its
// highlighting (keyword/string) applied, then a new line starts below it;
// once the visible window fills up, the oldest line is dropped so the code
// keeps "moving down" instead of growing the page. Loops the same short
// class forever. Reduced-motion / no element: leave the server-rendered
// static lines in style.css/index.html exactly as they are — no JS needed
// for those to look correct.
function initCodeTypewriter() {
  var screen = document.getElementById('pc-code-lines');
  if (!screen) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var lines = [
    { indent: 0, plain: 'public class Armsin {', html: '<span class="tok-kw">public class</span> Armsin {' },
    { indent: 1, plain: 'public static void main(String[] args) {', html: '<span class="tok-kw">public static void</span> main(<span class="tok-kw">String</span>[] args) {' },
    { indent: 2, plain: 'System.out.println("Hallo Welt!");', html: 'System.out.println(<span class="tok-str">&quot;Hallo Welt!&quot;</span>);' },
    { indent: 2, plain: 'int status = deploy();', html: '<span class="tok-kw">int</span> status = deploy();' },
    { indent: 2, plain: 'while (status == 0) {', html: '<span class="tok-kw">while</span> (status == 0) {' },
    { indent: 3, plain: 'build();', html: 'build();' },
    { indent: 3, plain: 'test();', html: 'test();' },
    { indent: 2, plain: '}', html: '}' },
    { indent: 1, plain: '}', html: '}' },
    { indent: 0, plain: '}', html: '}' }
  ];

  var MAX_VISIBLE = 7;
  var CHAR_DELAY = 32;
  var LINE_PAUSE = 260;
  var lineIndex = 0;

  screen.innerHTML = '';

  var typeNextLine = function () {
    var def = lines[lineIndex % lines.length];
    lineIndex++;

    var li = document.createElement('li');
    li.className = 'pc-code-line';
    li.style.setProperty('--indent', def.indent);
    var textNode = document.createTextNode('');
    li.appendChild(textNode);
    var cursor = document.createElement('span');
    cursor.className = 'retro-pc-cursor';
    li.appendChild(cursor);
    screen.appendChild(li);

    if (screen.children.length > MAX_VISIBLE) {
      screen.removeChild(screen.firstElementChild);
    }

    var charIndex = 0;
    var typeChar = function () {
      charIndex++;
      textNode.textContent = def.plain.slice(0, charIndex);
      if (charIndex < def.plain.length) {
        setTimeout(typeChar, CHAR_DELAY);
      } else {
        li.innerHTML = def.html;
        setTimeout(typeNextLine, LINE_PAUSE);
      }
    };
    typeChar();
  };

  typeNextLine();
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

initNavToggle();
initNavIndicator();
initScrollReveal();
initBookingFade();
initHeroParallax();
initCodeTypewriter();
initContactForm();
