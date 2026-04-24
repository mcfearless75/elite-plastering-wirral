/* Elite Plastering Wirral — main.js */

(function () {
  'use strict';

  const nav       = document.querySelector('.nav');
  const backToTop = document.getElementById('back-to-top');
  const navToggle = document.getElementById('nav-toggle');
  const navLinks  = document.getElementById('nav-links');
  const yearEl    = document.getElementById('year');

  // Current year in footer
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // ── Navbar scroll state ──────────────────
  function onScroll() {
    const y = window.scrollY;
    nav.classList.toggle('scrolled', y > 60);
    backToTop.classList.toggle('visible', y > 500);
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // ── Back to top ──────────────────────────
  backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // ── Mobile nav toggle ────────────────────
  navToggle.addEventListener('click', () => {
    const isOpen = navLinks.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', isOpen);

    const spans = navToggle.querySelectorAll('span');
    if (isOpen) {
      spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
      spans[1].style.opacity   = '0';
      spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
    } else {
      spans[0].style.transform = '';
      spans[1].style.opacity   = '';
      spans[2].style.transform = '';
    }
  });

  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
      const spans = navToggle.querySelectorAll('span');
      spans[0].style.transform = '';
      spans[1].style.opacity   = '';
      spans[2].style.transform = '';
    });
  });

  // ── Smooth anchor scrolling ──────────────
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', e => {
      const href = link.getAttribute('href');
      if (href === '#') {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return;
      }
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        const navH = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--nav-height')) || 72;
        const top  = target.getBoundingClientRect().top + window.scrollY - navH;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  // ── Scroll reveal (IntersectionObserver) ─
  const revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');

  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  revealEls.forEach(el => revealObserver.observe(el));

  // ── Stat counter animation ───────────────
  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }

  function animateCount(el, target, suffix) {
    const duration = 1800;
    const start    = performance.now();

    function step(now) {
      const elapsed  = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const value    = Math.round(easeOut(progress) * target);
      el.textContent = value + suffix;
      if (progress < 1) requestAnimationFrame(step);
    }

    requestAnimationFrame(step);
  }

  const statsGrid    = document.getElementById('stats-grid');
  let   statsCounted = false;

  const statsObserver = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting && !statsCounted) {
      statsCounted = true;
      document.querySelectorAll('[data-count]').forEach(el => {
        const target = parseInt(el.dataset.count, 10);
        const suffix = el.dataset.suffix || '';
        animateCount(el, target, suffix);
      });
      statsObserver.disconnect();
    }
  }, { threshold: 0.4 });

  if (statsGrid) statsObserver.observe(statsGrid);

  // ── Service card: keyboard accessibility ─
  document.querySelectorAll('.service-card').forEach(card => {
    card.setAttribute('tabindex', '0');
  });

  // ── Area chip hover stagger reset ────────
  // chips use CSS transition-delay via .d1-.d6 classes — no extra JS needed

})();
