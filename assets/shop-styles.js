/*
 * Shop Styles — LTK-style grid → pop-up post (sections/shop-styles.liquid).
 * Tiles are real links to /pages/looks/<handle>; a plain click opens the look in a <dialog>
 * instead, with prev/next, filters, and add-to-cart that refreshes Dawn's cart drawer.
 */
if (!customElements.get('shop-styles')) {
  class ShopStyles extends HTMLElement {
    connectedCallback() {
      this.dialog = this.querySelector('[data-ss-dialog]');
      this.slot = this.querySelector('[data-ss-slot]');
      if (!this.dialog || typeof this.dialog.showModal !== 'function') return; // no <dialog>: links just navigate
      this.current = 0;
      this.returnFocus = null;

      this.addEventListener('click', (event) => this.onClick(event));
      this.dialog.addEventListener('click', (event) => {
        if (event.target === this.dialog) this.close(); // backdrop
      });
      this.dialog.addEventListener('close', () => this.onClosed());
      this.dialog.addEventListener('keydown', (event) => {
        if (event.target.closest('select, input')) return;
        if (event.key === 'ArrowLeft') this.step(-1);
        if (event.key === 'ArrowRight') this.step(1);
      });
    }

    get tiles() {
      return Array.from(this.querySelectorAll('.shop-styles__item:not([hidden]) [data-ss-open]'));
    }

    onClick(event) {
      const tile = event.target.closest('[data-ss-open]');
      if (tile && !(event.metaKey || event.ctrlKey || event.shiftKey || event.button === 1)) {
        event.preventDefault();
        this.returnFocus = tile;
        this.open(tile.dataset.ssOpen);
        return;
      }
      const filter = event.target.closest('[data-ss-filter]');
      if (filter) return this.filter(filter);
      if (event.target.closest('[data-ss-close]')) return this.close();
      if (event.target.closest('[data-ss-prev]')) return this.step(-1);
      if (event.target.closest('[data-ss-next]')) return this.step(1);
      const add = event.target.closest('[data-ss-add]');
      if (add) return this.add([add.closest('[data-ss-piece]')], add);
      const all = event.target.closest('[data-ss-add-all]');
      if (all) return this.add(Array.from(this.slot.querySelectorAll('[data-ss-piece]')).filter((row) => row.querySelector('[data-ss-add]')), all);
      const copy = event.target.closest('[data-ss-copy]');
      if (copy) return this.copy(copy);
    }

    open(id) {
      const template = this.querySelector(`template[data-ss-post="${id}"]`);
      if (!template) return;
      this.pauseMedia();
      this.slot.replaceChildren(template.content.cloneNode(true));
      this.current = id;
      if (!this.dialog.open) {
        this.dialog.showModal();
        document.body.classList.add('overflow-hidden');
      }
      const video = this.slot.querySelector('video');
      if (video) video.play().catch(() => {});
      const close = this.slot.querySelector('[data-ss-close]');
      if (close) close.focus();
    }

    step(delta) {
      const tiles = this.tiles;
      if (!tiles.length) return;
      const at = tiles.findIndex((t) => t.dataset.ssOpen === String(this.current));
      const next = tiles[(at + delta + tiles.length) % tiles.length];
      this.returnFocus = next;
      this.open(next.dataset.ssOpen);
    }

    close() {
      if (this.dialog.open) this.dialog.close();
    }

    onClosed() {
      this.pauseMedia();
      this.slot.replaceChildren();
      document.body.classList.remove('overflow-hidden');
      if (this.returnFocus) this.returnFocus.focus();
    }

    pauseMedia() {
      this.slot.querySelectorAll('video').forEach((v) => v.pause());
    }

    filter(button) {
      const kind = button.dataset.ssFilter;
      this.querySelectorAll('[data-ss-filter]').forEach((b) => b.setAttribute('aria-pressed', String(b === button)));
      this.querySelectorAll('.shop-styles__item').forEach((item) => {
        item.hidden = kind !== 'all' && item.dataset.ssKind !== kind;
      });
    }

    async add(rows, button) {
      const items = rows
        .map((row) => row && row.querySelector('[data-ss-variant]'))
        .filter((input) => input && input.value && isAvailable(input))
        .map((input) => ({ id: Number(input.value), quantity: 1 }));
      if (!items.length) return;

      const status = this.slot.querySelector('[data-ss-status]');
      const cart = document.querySelector('cart-drawer');
      const body = { items };
      if (cart && typeof cart.getSectionsToRender === 'function') {
        body.sections = cart.getSectionsToRender().map((s) => s.id);
        body.sections_url = window.location.pathname;
      }

      button.setAttribute('aria-disabled', 'true');
      button.classList.add('loading');
      try {
        const res = await fetch(`${window.Shopify?.routes?.root || '/'}cart/add.js`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify(body),
        });
        const data = await res.json();
        if (!res.ok || data.status) throw new Error(data.description || data.message || 'Could not add to cart');

        if (status) status.textContent = items.length === 1 ? 'Added to cart' : `Added ${items.length} pieces to cart`;
        button.classList.add('is-added');
        if (typeof publish === 'function' && typeof PUB_SUB_EVENTS !== 'undefined') {
          publish(PUB_SUB_EVENTS.cartUpdate, { source: 'shop-styles', cartData: data });
        }
        if (cart && data.sections && typeof cart.renderContents === 'function') {
          this.close();
          cart.classList.remove('is-empty');
          cart.renderContents(data);
        } else {
          window.location.href = window.routes?.cart_url || '/cart';
        }
      } catch (error) {
        if (status) status.textContent = error.message;
        window.alert(error.message);
      } finally {
        button.removeAttribute('aria-disabled');
        button.classList.remove('loading');
      }
    }

    async copy(button) {
      const url = button.dataset.ssCopy;
      const status = this.slot.querySelector('[data-ss-status]');
      try {
        if (navigator.share) await navigator.share({ url });
        else await navigator.clipboard.writeText(url);
        if (status) status.textContent = 'Link copied';
        button.classList.add('is-copied');
      } catch (_) {
        /* share sheet dismissed */
      }
    }
  }

  // A <select> whose chosen option is sold out adds nothing.
  function isAvailable(input) {
    return !(input.tagName === 'SELECT' && input.selectedOptions[0] && input.selectedOptions[0].disabled);
  }

  customElements.define('shop-styles', ShopStyles);
}
