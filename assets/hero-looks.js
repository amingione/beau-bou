/** Synchronized runway stages with persistent user pause and reduced-motion support. */
(function () {
  'use strict';
  class HeroLooks {
    constructor(root) {
      this.root = root;
      this.events = new AbortController();
      this.timer = 0;
      this.interval = Math.max(2000, parseInt(root.dataset.interval || '5000', 10));
      this.motion = window.matchMedia('(prefers-reduced-motion: reduce)');
      this.userPaused = this.motion.matches;
      this.hovered = false;
      this.focused = false;
      this.toggle = root.querySelector('[data-looks-toggle]');
      this.controls = root.querySelector('[data-looks-controls]');
      this.counter = root.querySelector('[data-looks-counter]');
      this.stages = Array.from(root.querySelectorAll('[data-looks-stage]'))
        .map((el) => ({ el, slides: Array.from(el.querySelectorAll('[data-slide]')), index: 0 }))
        .filter((stage) => stage.slides.length > 0);
      this.stages.forEach((stage) => {
        stage.slides.forEach((slide, i) => this.setSlide(slide, i === 0));
        stage.el.setAttribute('data-ready', '');
      });
      if (this.stages.every((stage) => stage.slides.length < 2)) return;
      const on = (target, event, handler) => target.addEventListener(event, handler, { signal: this.events.signal });
      if (this.controls) this.controls.hidden = false;
      if (this.counter) this.counter.hidden = false;
      [[root.querySelector('[data-looks-prev]'), -1], [root.querySelector('[data-looks-next]'), 1]].forEach(([button, direction]) => {
        if (button) on(button, 'click', () => {
          this.userPaused = true;
          this.advance(direction);
          this.sync();
        });
      });
      if (this.toggle) {
        this.toggle.hidden = false;
        on(this.toggle, 'click', () => {
          this.userPaused = !this.userPaused;
          this.sync();
        });
      }
      if (root.dataset.pauseHover === 'true') {
        on(root, 'pointerenter', (event) => {
          if (event.pointerType === 'mouse') { this.hovered = true; this.sync(); }
        });
        on(root, 'pointerleave', () => { this.hovered = false; this.sync(); });
      }
      // Focused outfit links must remain stable; the playback button can start the show.
      on(root, 'focusin', (event) => {
        this.focused = !!event.target.closest('[data-slide]');
        this.sync();
      });
      on(root, 'focusout', (event) => {
        this.focused = !!(event.relatedTarget && root.contains(event.relatedTarget) && event.relatedTarget.closest('[data-slide]'));
        this.sync();
      });
      on(document, 'visibilitychange', () => this.sync());
      on(this.motion, 'change', () => {
        if (this.motion.matches) this.userPaused = true;
        this.sync();
      });
      this.sync();
    }
    setSlide(slide, active) {
      slide.classList.toggle('is-active', active);
      slide.setAttribute('aria-hidden', String(!active));
      slide.inert = !active;
      if (active) slide.setAttribute('aria-current', 'true');
      else slide.removeAttribute('aria-current');
    }
    advance(direction = 1) {
      this.stages.forEach((stage) => {
        if (stage.slides.length < 2) return;
        this.setSlide(stage.slides[stage.index], false);
        stage.index = (stage.index + direction + stage.slides.length) % stage.slides.length;
        this.setSlide(stage.slides[stage.index], true);
        const next = stage.slides[(stage.index + 1) % stage.slides.length].querySelector('img');
        if (next) next.loading = 'eager';
      });
      this.updateCounter();
    }
    updateCounter() {
      if (!this.counter || !this.stages.length) return;
      const stage = this.stages.reduce((longest, item) => item.slides.length > longest.slides.length ? item : longest);
      this.counter.textContent = `${String(stage.index + 1).padStart(2, '0')} / ${String(stage.slides.length).padStart(2, '0')}`;
    }
    sync() {
      window.clearInterval(this.timer);
      this.timer = 0;
      if (this.toggle) {
        this.toggle.setAttribute('aria-label', this.userPaused ? 'Play slideshow' : 'Pause slideshow');
        this.toggle.dataset.paused = String(this.userPaused);
      }
      this.updateCounter();
      if (!this.userPaused && !this.hovered && !this.focused && !document.hidden) {
        this.timer = window.setInterval(() => this.advance(), this.interval);
      }
    }
    destroy() {
      window.clearInterval(this.timer);
      this.events.abort();
      delete this.root.__heroLooks;
    }
  }
  // A section can appear multiple times; loading its script twice must not add listeners twice.
  if (window.beauBouRunwayInitialized) return;
  window.beauBouRunwayInitialized = true;
  const init = (scope) => scope.querySelectorAll('[data-hero-looks]').forEach((root) => {
    if (!root.__heroLooks) root.__heroLooks = new HeroLooks(root);
  });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => init(document), { once: true });
  else init(document);
  document.addEventListener('shopify:section:load', (event) => init(event.target));
  document.addEventListener('shopify:section:unload', (event) => {
    event.target.querySelectorAll('[data-hero-looks]').forEach((root) => root.__heroLooks?.destroy());
  });
})();
