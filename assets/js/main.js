/* Clavis IT Service – Interaktionen (ohne Abhängigkeiten, ohne Cookies) */
(function () {
  'use strict';

  var root = document.documentElement;
  root.classList.add('js');
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.addEventListener('DOMContentLoaded', function () {
    initTheme();
    initHeader();
    initNav();
    initReveal();
    initTabs();
    initCalc();
    initDownload();
    document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
  });

  /* ---------- Hell/Dunkel ----------
     Gespeichert wird nur nach Klick auf den Schalter (localStorage "clavis-theme"). */
  function initTheme() {
    var btn = document.querySelector('[data-theme-toggle]');
    if (!btn) return;
    var mq = window.matchMedia('(prefers-color-scheme: dark)');
    function current() {
      var t = root.getAttribute('data-theme');
      return t || (mq.matches ? 'dark' : 'light');
    }
    function label() {
      btn.setAttribute('aria-label', current() === 'dark' ? 'Helle Darstellung aktivieren' : 'Dunkle Darstellung aktivieren');
    }
    btn.addEventListener('click', function () {
      var next = current() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('clavis-theme', next); } catch (e) { /* privat/gesperrt: nur für diese Sitzung */ }
      label();
    });
    if (mq.addEventListener) mq.addEventListener('change', label);
    label();
  }

  /* ---------- Header: Hintergrund beim Scrollen ---------- */
  function initHeader() {
    var header = document.querySelector('[data-header]');
    if (!header) return;
    var ticking = false;
    function update() { header.classList.toggle('is-scrolled', window.scrollY > 16); ticking = false; }
    window.addEventListener('scroll', function () {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  /* ---------- Mobile Navigation ---------- */
  function initNav() {
    var toggle = document.querySelector('[data-nav-toggle]');
    var nav = document.querySelector('[data-nav]');
    if (!toggle || !nav) return;
    function setOpen(open) {
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
      nav.classList.toggle('is-open', open);
    }
    toggle.addEventListener('click', function () { setOpen(toggle.getAttribute('aria-expanded') !== 'true'); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) { setOpen(false); toggle.focus(); }
    });
    var desktop = window.matchMedia('(min-width: 961px)');
    var onChange = function (m) { if (m.matches) setOpen(false); };
    if (desktop.addEventListener) desktop.addEventListener('change', onChange);
  }

  /* ---------- Scroll-Reveal mit Stagger ---------- */
  function initReveal() {
    var items = document.querySelectorAll('.reveal, [data-reveal-line]');
    if (reduceMotion || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-visible'); });
      return;
    }
    var counts = new Map();
    document.querySelectorAll('.reveal').forEach(function (el) {
      var p = el.parentElement;
      var i = counts.get(p) || 0;
      el.style.setProperty('--stagger', Math.min(i, 6) * 60 + 'ms');
      counts.set(p, i + 1);
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add('is-visible'); io.unobserve(entry.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.1 });
    items.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Tabs (Preise) ---------- */
  function initTabs() {
    var list = document.querySelector('[data-tabs]');
    if (!list) return;
    var tabs = Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));

    function select(tab, focus, updateHash) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(t.getAttribute('aria-controls'));
        if (!panel) return;
        panel.hidden = !on;
        if (on && !reduceMotion) {
          panel.classList.remove('is-entering');
          void panel.offsetWidth;
          panel.classList.add('is-entering');
        }
      });
      if (focus) tab.focus();
      if (updateHash && history.replaceState) history.replaceState(null, '', '#' + tab.getAttribute('aria-controls'));
    }
    function byId(id) { return tabs.filter(function (t) { return t.getAttribute('aria-controls') === id; })[0]; }

    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { select(tab, false, true); });
      tab.addEventListener('keydown', function (e) {
        var n = null;
        if (e.key === 'ArrowRight') n = tabs[(i + 1) % tabs.length];
        if (e.key === 'ArrowLeft') n = tabs[(i - 1 + tabs.length) % tabs.length];
        if (e.key === 'Home') n = tabs[0];
        if (e.key === 'End') n = tabs[tabs.length - 1];
        if (n) { e.preventDefault(); select(n, true, true); }
      });
    });

    document.querySelectorAll('[data-tab-link]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        var t = byId(a.getAttribute('data-tab-link'));
        if (!t) return;
        e.preventDefault();
        select(t, true, true);
        list.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'center' });
      });
    });

    function fromHash() {
      var t = byId(location.hash.slice(1));
      if (t) select(t, false, false);
    }
    window.addEventListener('hashchange', fromHash);
    fromHash();
  }

  /* ---------- Vertragsrechner (Unternehmen) ---------- */
  function initCalc() {
    var form = document.querySelector('[data-calc]');
    if (!form) return;
    var MIN = 199;
    var rows = Array.prototype.slice.call(form.querySelectorAll('[data-calc-row]'));
    var totalEl = form.querySelector('[data-calc-total]');
    var minEl = form.querySelector('[data-calc-min]');
    var mailEl = form.querySelector('[data-calc-mail]');
    var fmt = new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' });
    var shown = MIN;

    function clamp(input) {
      var min = parseInt(input.min, 10) || 0;
      var max = parseInt(input.max, 10) || 99;
      var v = parseInt(input.value, 10);
      if (isNaN(v)) v = min;
      v = Math.max(min, Math.min(max, v));
      input.value = v;
      return v;
    }

    function update(changedRow) {
      var sum = 0;
      var lines = [];
      rows.forEach(function (row) {
        var input = row.querySelector('[data-calc-input]');
        var price = parseFloat(row.getAttribute('data-price'));
        var v = clamp(input);
        var line = v * price;
        sum += line;
        row.querySelector('[data-calc-line]').textContent = fmt.format(line);
        var btns = row.querySelectorAll('[data-step]');
        btns[0].disabled = v <= (parseInt(input.min, 10) || 0);
        btns[1].disabled = v >= (parseInt(input.max, 10) || 99);
        if (v > 0) lines.push('- ' + row.querySelector('label').textContent + ': ' + v + ' × ' + fmt.format(price) + ' = ' + fmt.format(line));
      });
      var total = Math.max(MIN, sum);
      minEl.hidden = sum >= MIN;
      animateTotal(total);
      var body = 'Guten Tag Herr Kumaru,\n\nich interessiere mich für einen Wartungsvertrag. Meine Kalkulation:\n\n' +
        lines.join('\n') + '\n\nMonatsbeitrag: ' + fmt.format(total) + ' netto zzgl. 19 % USt.\n\nBitte melden Sie sich für eine Bestandsaufnahme.\n\nFirma:\nAnsprechpartner:\nTelefon:\n';
      mailEl.href = 'mailto:kontakt@clavis-itservice.de?subject=' + encodeURIComponent('Anfrage Wartungsvertrag') + '&body=' + encodeURIComponent(body);
      if (changedRow && !reduceMotion) {
        var out = changedRow.querySelector('[data-calc-line]');
        out.classList.remove('bump'); void out.offsetWidth; out.classList.add('bump');
      }
    }

    var raf = null, settle = null;
    function animateTotal(target) {
      if (raf) cancelAnimationFrame(raf);
      clearTimeout(settle);
      // Endwert sicher setzen, auch wenn rAF gedrosselt ist (Hintergrund-Tab)
      settle = setTimeout(function () { if (raf) cancelAnimationFrame(raf); shown = target; totalEl.textContent = fmt.format(target); }, 450);
      if (reduceMotion || document.hidden || shown === target) { shown = target; totalEl.textContent = fmt.format(target); return; }
      var from = shown, start = null, dur = 380;
      function step(ts) {
        if (start === null) start = ts;
        var p = Math.min((ts - start) / dur, 1);
        var e = 1 - Math.pow(1 - p, 3);
        shown = from + (target - from) * e;
        totalEl.textContent = fmt.format(Math.round(shown * 100) / 100);
        if (p < 1) raf = requestAnimationFrame(step); else { shown = target; totalEl.textContent = fmt.format(target); }
      }
      raf = requestAnimationFrame(step);
    }

    rows.forEach(function (row) {
      var input = row.querySelector('[data-calc-input]');
      row.querySelectorAll('[data-step]').forEach(function (b) {
        b.addEventListener('click', function () {
          input.value = (parseInt(input.value, 10) || 0) + parseInt(b.getAttribute('data-step'), 10);
          update(row);
        });
      });
      input.addEventListener('input', function () { if (input.value !== '') update(row); });
      input.addEventListener('change', function () { update(row); });
    });

    form.querySelector('[data-calc-reset]').addEventListener('click', function () {
      rows.forEach(function (row) {
        var input = row.querySelector('[data-calc-input]');
        input.value = input.defaultValue;
      });
      update(null);
    });

    update(null);
  }

  /* ---------- Fernwartung: passenden Download wählen ---------- */
  function initDownload() {
    var box = document.querySelector('[data-download]');
    if (!box) return;
    var ua = navigator.userAgent || '';
    var isMobile = /Android|iPhone|iPad|iPod/i.test(ua) || (/Macintosh/.test(ua) && navigator.maxTouchPoints > 1);
    var isMac = /Macintosh|Mac OS X/.test(ua) && !isMobile;
    var main = box.querySelector('[data-dl-main]');
    var label = box.querySelector('[data-dl-label]');
    if (isMac) {
      main.href = main.getAttribute('data-mac');
      label.textContent = 'Fernwartung herunterladen (macOS)';
    } else if (!isMobile) {
      label.textContent = 'Fernwartung herunterladen (Windows)';
    }
    var hint = document.querySelector('[data-mobile-hint]');
    if (isMobile && hint) hint.hidden = false;
  }
})();
