/*
 * <bb-scroller> — a swipeable row with optional prev/next buttons.
 * Used by Shop Styles (Highlights layout) and the Collections carousel.
 *
 * Markup:
 *   <bb-scroller>
 *     <ul data-scroller-track>…</ul>
 *     <button data-scroller-prev>…</button> <button data-scroller-next>…</button>
 *   </bb-scroller>
 *
 * The track scrolls natively (touch, trackpad, keyboard); the buttons page by ~one view and
 * disable themselves at either end. Without JavaScript the row still scrolls.
 */
if (!customElements.get('bb-scroller')) {
  class BbScroller extends HTMLElement {
    connectedCallback() {
      this.track = this.querySelector('[data-scroller-track]');
      if (!this.track) return;
      this.prev = this.querySelector('[data-scroller-prev]');
      this.next = this.querySelector('[data-scroller-next]');
      this.onScroll = () => this.update();
      this.track.addEventListener('scroll', this.onScroll, { passive: true });
      this.prev?.addEventListener('click', () => this.page(-1));
      this.next?.addEventListener('click', () => this.page(1));
      if ('ResizeObserver' in window) {
        this.observer = new ResizeObserver(this.onScroll);
        this.observer.observe(this.track);
      }
      this.update();
    }

    disconnectedCallback() {
      this.track?.removeEventListener('scroll', this.onScroll);
      this.observer?.disconnect();
    }

    page(direction) {
      const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      this.track.scrollBy({ left: direction * this.track.clientWidth * 0.85, behavior: reduce ? 'auto' : 'smooth' });
    }

    update() {
      const { scrollLeft, scrollWidth, clientWidth } = this.track;
      const max = scrollWidth - clientWidth - 2;
      const scrollable = max > 0;
      this.toggleAttribute('data-scrollable', scrollable);
      if (this.prev) this.prev.disabled = !scrollable || scrollLeft <= 2;
      if (this.next) this.next.disabled = !scrollable || scrollLeft >= max;
    }
  }
  customElements.define('bb-scroller', BbScroller);
}
