/* Enhance the existing inline catalogue without adding a framework. */
(() => {
  const catalogue = Object.values(monographs).map(product => ({
    name: product.title.replace(/^\d+\.\s*/, ''),
    price: Number(product.price), image: product.image
  }));
  try {
    const saved = JSON.parse(localStorage.getItem('garden_cart_v1') || '[]');
    if (Array.isArray(saved)) {
      cart = catalogue.flatMap(product => {
        const item = saved.find(item => item && item.name === product.name);
        return item && Number.isInteger(item.qty) && item.qty > 0 && item.qty <= 999
          ? [{ ...product, qty: item.qty }] : [];
      });
    }
  } catch (_) { cart = []; }
  document.getElementById('cart-count').setAttribute('aria-live', 'polite');
  document.getElementById('cart-subtotal').setAttribute('aria-live', 'polite');
  renderCart();
  filterBlends('all');

  const hero = document.querySelector('.hero-section');
  hero.id = 'main-content';
  hero.tabIndex = -1;
  const skip = document.createElement('a');
  skip.className = 'skip-link';
  skip.href = '#main-content';
  skip.textContent = 'Naar de inhoud';
  document.body.prepend(skip);
  document.querySelectorAll('.product-card img, .science-section img').forEach(img => {
    img.loading = 'lazy'; img.decoding = 'async';
  });
  document.querySelectorAll('.faq-question').forEach((question, index) => {
    const answer = question.nextElementSibling;
    answer.id = `faq-answer-${index}`;
    question.setAttribute('role', 'button');
    question.tabIndex = 0;
    question.setAttribute('aria-controls', answer.id);
    const sync = () => question.setAttribute('aria-expanded', String(question.parentElement.classList.contains('open')));
    sync();
    question.addEventListener('click', sync);
    question.addEventListener('keydown', event => {
      if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); question.click(); }
    });
  });

  const panels = ['cart-drawer', 'mobile-nav-drawer', 'product-modal'].map(id => document.getElementById(id));
  const labels = ['Uw kruidentas', 'Navigatiemenu', 'Ontdek uw melange'];
  const triggers = [document.querySelector('.btn-header-cart'), document.querySelector('.mobile-menu-btn')];
  let activePanel = null;
  let returnFocus = null;
  let previousOverflow = '';
  const focusables = panel => [...panel.querySelectorAll('button, a[href], input, select, textarea, [tabindex="0"]')]
    .filter(el => !el.disabled && el.getClientRects().length);
  panels.forEach((panel, index) => {
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', labels[index]);
    panel.setAttribute('aria-modal', 'true');
    panel.tabIndex = -1;
    if (triggers[index]) triggers[index].setAttribute('aria-controls', panel.id);
  });
  function syncPanels() {
    const next = panels.findLast(panel => panel.classList.contains('active')) || null;
    panels.forEach((panel, index) => {
      panel.inert = panel !== next;
      panel.setAttribute('aria-hidden', String(panel !== next));
      if (triggers[index]) triggers[index].setAttribute('aria-expanded', String(panel === next));
    });
    if (next === activePanel) {
      if (next && !next.contains(document.activeElement)) (focusables(next)[0] || next).focus();
      return;
    }
    if (next) {
      if (!activePanel) { returnFocus = document.activeElement; previousOverflow = document.body.style.overflow; }
      document.body.style.overflow = 'hidden';
      (focusables(next)[0] || next).focus();
    } else {
      document.body.style.overflow = previousOverflow;
      if (returnFocus?.isConnected) returnFocus.focus();
    }
    activePanel = next;
  }
  panels.forEach(panel => new MutationObserver(syncPanels).observe(panel, { attributes: true, attributeFilter: ['class'], childList: true, subtree: true }));
  syncPanels();
  // Native scrolling remains in control; motion is an optional enhancement.
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  if ('IntersectionObserver' in window) {
    const reveal = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        if (!motion.matches) entry.target.animate([
          { opacity: 0, transform: 'translateY(22px)' },
          { opacity: 1, transform: 'translateY(0)' }
        ], { duration: 550, easing: 'cubic-bezier(.2,.65,.3,1)' });
        reveal.unobserve(entry.target);
      });
    }, { threshold: .08 });
    document.querySelectorAll('.section-header, .product-card, .origin-visual, .origin-body p, .cred-item').forEach(el => reveal.observe(el));
    motion.addEventListener('change', () => {
      if (motion.matches) document.getAnimations().forEach(animation => animation.finish());
    });
  }
  const progress = document.createElement('div');
  progress.className = 'scroll-progress';
  progress.setAttribute('aria-hidden', 'true');
  const topButton = document.createElement('button');
  topButton.className = 'back-to-top';
  topButton.textContent = '↑';
  topButton.setAttribute('aria-label', 'Terug naar boven');
  topButton.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: motion.matches ? 'instant' : 'smooth' });
    document.querySelector('.mobile-menu-btn').offsetParent
      ? document.querySelector('.mobile-menu-btn').focus({ preventScroll: true })
      : document.querySelector('.brand-logo-wrap').focus({ preventScroll: true });
  });
  document.body.append(progress, topButton);
  const sectionLinks = [...document.querySelectorAll('.nav-left a[href^="#"]')];
  let scrollQueued = false;
  function updateScroll() {
    const max = document.documentElement.scrollHeight - innerHeight;
    progress.style.transform = `scaleX(${max > 0 ? Math.min(1, scrollY / max) : 0})`;
    topButton.hidden = scrollY < 600 || !!activePanel;
    const collection = document.getElementById('signature-six').getBoundingClientRect();
    const sticky = document.getElementById('mobile-sticky-cta');
    const showSticky = collection.top < innerHeight && collection.bottom > 0 && !activePanel;
    sticky.classList.toggle('is-away', !showSticky);
    sticky.inert = !showSticky;
    const current = sectionLinks.findLast(link => document.querySelector(link.hash)?.getBoundingClientRect().top < 160);
    sectionLinks.forEach(link => {
      if (link === current) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    scrollQueued = false;
  }
  addEventListener('scroll', () => {
    if (!scrollQueued) { scrollQueued = true; requestAnimationFrame(updateScroll); }
  }, { passive: true });
  addEventListener('resize', updateScroll);
  updateScroll();
  document.addEventListener('keydown', event => {
    if (!activePanel) return;
    if (event.key === 'Escape') {
      event.preventDefault();
      if (activePanel.id === 'cart-drawer') toggleCart();
      else if (activePanel.id === 'mobile-nav-drawer') toggleMobileMenu();
      else closeProductModal();
    }
    if (event.key === 'Tab') {
      const items = focusables(activePanel);
      const first = items[0] || activePanel;
      const last = items.at(-1) || activePanel;
      if (event.shiftKey && (document.activeElement === first || !activePanel.contains(document.activeElement))) {
        event.preventDefault(); last.focus();
      } else if (!event.shiftKey && (document.activeElement === last || !activePanel.contains(document.activeElement))) {
        event.preventDefault(); first.focus();
      }
    }
  });
})();
