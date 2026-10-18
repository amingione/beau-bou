/*
 * <announcement-spotlight> — rotates the Announcements section (sections/announcement-spotlight.liquid).
 * Each slide holds its own text and picture, so they always change together. Hidden slides are
 * inert. Rotation pauses on hover/focus, has a pause button, and never starts for visitors who
 * prefer reduced motion. In the theme editor, selecting a block shows that announcement.
 */
if (!customElements.get('announcement-spotlight')) {
  class AnnouncementSpotlight extends HTMLElement {
    connectedCallback() {
      this.slides = Array.from(this.querySelectorAll('.spot__slide'));
      if (this.slides.length < 2) return;
      this.index = 0;
      this.interval = (parseInt(this.dataset.interval, 10) || 0) * 1000;
      const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      this.paused = reduce || this.interval === 0;
      this.hold = false;

      // After a sign-up posts, the page reloads on slide 1; open the slide holding the
      // thank-you / error message instead, and stop rotating so it stays readable.
      const posted = this.slides.findIndex((slide) => slide.querySelector('.spot__form-msg'));
      if (posted > -1) {
        this.index = posted;
        this.paused = true;
      }

      this.addEventListener('click', (event) => {
        const dot = event.target.closest('[data-spot-go]');
        if (dot) {
          this.go(Number(dot.dataset.spotGo));
          this.slides[this.index].querySelector(`[data-spot-go="${this.index}"]`)?.focus();
          return;
        }
        if (event.target.closest('[data-spot-toggle]')) {
          this.paused = !this.paused;
          this.sync();
          this.slides[this.index].querySelector('[data-spot-toggle]')?.focus();
          this.restart();
        }
      });
      this.addEventListener('mouseenter', () => this.setHold(true));
      this.addEventListener('mouseleave', () => this.setHold(this.contains(document.activeElement)));
      this.addEventListener('focusin', () => this.setHold(true));
      this.addEventListener('focusout', (event) => {
        if (!this.contains(event.relatedTarget)) this.setHold(this.matches(':hover'));
      });

      this.onBlockSelect = (event) => {
        const at = this.slides.indexOf(event.target);
        if (at > -1) {
          this.go(at);
          this.setHold(true);
        }
      };
      document.addEventListener('shopify:block:select', this.onBlockSelect);

      this.sync();
      this.restart();
    }

    disconnectedCallback() {
      this.stop();
      if (this.onBlockSelect) document.removeEventListener('shopify:block:select', this.onBlockSelect);
    }

    go(at) {
      this.index = (at + this.slides.length) % this.slides.length;
      this.sync();
    }

    sync() {
      this.slides.forEach((slide, n) => {
        const active = n === this.index;
        slide.classList.toggle('is-active', active);
        slide.toggleAttribute('inert', !active);
        if (active) slide.removeAttribute('aria-hidden');
        else slide.setAttribute('aria-hidden', 'true');
      });
      this.querySelectorAll('[data-spot-go]').forEach((dot) => {
        dot.setAttribute('aria-current', String(Number(dot.dataset.spotGo) === this.index));
      });
      this.querySelectorAll('[data-spot-toggle]').forEach((button) => {
        button.classList.toggle('is-paused', this.paused);
        button.setAttribute('aria-label', this.paused ? 'Play announcements' : 'Pause announcements');
      });
    }

    setHold(hold) {
      this.hold = hold;
      this.restart();
    }

    stop() {
      clearInterval(this.timer);
      this.timer = null;
    }

    restart() {
      this.stop();
      if (this.paused || this.hold || !this.interval) return;
      this.timer = setInterval(() => this.go(this.index + 1), this.interval);
    }
  }
  customElements.define('announcement-spotlight', AnnouncementSpotlight);
}
