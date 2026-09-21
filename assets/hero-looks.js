/**
 * Hero looks — synced slideshows.
 * One ticker per section advances every [data-looks-stage] inside it at the same instant,
 * so left and right change together while each shows its own set of outfits.
 * No controls, no indicators. Pauses on hover/focus (setting) and when the tab is hidden.
 */
(function () {
  'use strict';

  class HeroLooks {
    /** @param {HTMLElement} root */
    constructor(root) {
      this.root = root;
      this.interval = Math.max(2000, parseInt(root.dataset.interval || '5000', 10));
      this.pauseOnHover = root.dataset.pauseHover === 'true';
      this.stages = Array.from(root.querySelectorAll('[data-looks-stage]'))
        .map((el) => ({ el, slides: Array.from(el.querySelectorAll('[data-slide]')), index: 0 }))
        .filter((s) => s.slides.length > 0);
      this.timer = 0;
      this.paused = false;

      this.stages.forEach((s) => {
        s.slides.forEach((slide, i) => slide.classList.toggle('is-active', i === 0));
        s.el.setAttribute('data-ready', '');
      });

      if (this.stages.every((s) => s.slides.length < 2)) return;

      if (this.pauseOnHover) {
        root.addEventListener('mouseenter', () => this.pause());
        root.addEventListener('mouseleave', () => this.resume());
        root.addEventListener('focusin', () => this.pause());
        root.addEventListener('focusout', () => this.resume());
      }
      document.addEventListener('visibilitychange', () => (document.hidden ? this.pause() : this.resume()));
      this.resume();
    }

    advance() {
      this.stages.forEach((s) => {
        if (s.slides.length < 2) return;
        const from = s.slides[s.index];
        s.index = (s.index + 1) % s.slides.length;
        const to = s.slides[s.index];
        const next = s.slides[(s.index + 1) % s.slides.length].querySelector('img');
        if (next && next.loading === 'lazy') next.loading = 'eager';
        from.classList.remove('is-active');
        from.classList.add('is-leaving');
        to.classList.add('is-active');
        to.classList.remove('is-leaving');
        from.removeAttribute('aria-current');
        to.setAttribute('aria-current', 'true');
        window.setTimeout(() => from.classList.remove('is-leaving'), 2000);
      });
    }

    pause() {
      this.paused = true;
      window.clearInterval(this.timer);
      this.timer = 0;
    }

    resume() {
      this.paused = false;
      if (this.timer) return;
      this.timer = window.setInterval(() => this.advance(), this.interval);
    }
  }

  const init = () => document.querySelectorAll('[data-hero-looks]').forEach((el) => {
    if (!el.__heroLooks) el.__heroLooks = new HeroLooks(el);
  });

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();

  // Theme editor: re-init when the section is (re)loaded
  document.addEventListener('shopify:section:load', (e) => {
    const el = e.target && e.target.querySelector('[data-hero-looks]');
    if (el) el.__heroLooks = new HeroLooks(el);
  });
})();
