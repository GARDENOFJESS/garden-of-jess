'use strict';
(() => {
  const $ = selector => document.querySelector(selector);
  const bag = $('#bag');
  const key = 'homemade-by-jess-cart-v2';
  const catalog = {
    puur: { name: 'Pure chocoladetaart', image: 'assets/brownietaart-detail.webp' },
    zacht: { name: 'Zachte chocoladetaart', image: 'assets/chocoladetaarten-hero.webp' }
  };
  let cart = { puur: 0, zacht: 0 };
  try {
    const saved = JSON.parse(localStorage.getItem(key));
    for (const id of Object.keys(catalog)) if (Number.isInteger(saved?.[id]) && saved[id] >= 0 && saved[id] <= 99) cart[id] = saved[id];
    localStorage.removeItem('homemade-by-jess-selection-v1');
  } catch {}
  function render() {
    const total = cart.puur + cart.zacht;
    $('#bag-count').textContent = total;
    $('#empty').hidden = total > 0;
    $('#bag-filled').hidden = total === 0;
    const list = $('#bag-items');
    list.replaceChildren();
    for (const [id, product] of Object.entries(catalog)) {
      if (!cart[id]) continue;
      const item = document.createElement('section');
      item.className = 'bag-item';
      item.dataset.product = id;
      item.innerHTML = `<div class="bag-product"><img src="${product.image}" alt="" width="70" height="80"><div><strong>${product.name}</strong><p>Prijs op aanvraag</p></div></div><div class="bag-controls"><span>Aantal taarten</span><div><button data-change="-1" aria-label="Minder ${product.name}" ${cart[id] === 1 ? 'disabled' : ''}>−</button><output>${cart[id]}</output><button data-change="1" aria-label="Meer ${product.name}" ${cart[id] === 99 ? 'disabled' : ''}>+</button></div></div><button class="remove" data-remove aria-label="Verwijder ${product.name}">Verwijderen</button>`;
      list.append(item);
    }
    $('#request').hidden = true;
    $('#status').textContent = '';
    try { localStorage.setItem(key, JSON.stringify(cart)); } catch {}
  }
  document.querySelectorAll('[data-open-bag]').forEach(button => button.addEventListener('click', () => bag.showModal()));
  $('.close').addEventListener('click', () => bag.close());
  bag.addEventListener('click', event => {
    if (event.target === bag) {
      const box = bag.getBoundingClientRect();
      if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) bag.close();
    }
  });
  document.querySelectorAll('[data-add]').forEach(button => button.addEventListener('click', () => {
    const id = button.dataset.add;
    const quantity = Number($(`#quantity-${id}`).value);
    cart[id] = Math.min(99, cart[id] + quantity);
    render(); bag.showModal();
  }));
  $('#bag-items').addEventListener('click', event => {
    const button = event.target.closest('button');
    const id = button?.closest('[data-product]')?.dataset.product;
    if (!id) return;
    if (button.hasAttribute('data-remove')) cart[id] = 0;
    else cart[id] = Math.min(99, Math.max(1, cart[id] + Number(button.dataset.change)));
    const action = button.getAttribute('data-change');
    render();
    const replacement = action && $(`[data-product="${id}"] [data-change="${action}"]`);
    if (replacement && !replacement.disabled) replacement.focus();
    else if ($(`[data-product="${id}"] [data-remove]`)) $(`[data-product="${id}"] [data-remove]`).focus();
    else $('.close').focus();
  });
  $('#wish').addEventListener('input', () => { $('#request').hidden = true; $('#status').textContent = ''; });
  $('#prepare').addEventListener('click', () => {
    const wish = $('#wish').value.trim();
    const selection = Object.entries(catalog).filter(([id]) => cart[id] > 0).map(([id, product]) => `${cart[id]} × ${product.name}`).join('\n');
    const message = `Hoi Jessica! Ik heb interesse in de volgende taarten van Homemade by Jess:\n\n${selection}\n\n${wish ? `Mijn wens of gewenste datum: ${wish}\n\n` : ''}Graag verneem ik de beschikbaarheid en afspraak (bezorgen regio Beets/Hoorn/Purmerend ~20 km, of afhalen in Beets / Bio Rosa Purmerend).\n\nDank je wel!`;
    $('#request-text').value = message;
    $('#request').hidden = false;
    $('#send-whatsapp').href = 'https://wa.me/31641615544?text=' + encodeURIComponent(message);
    $('#send-email').href = 'mailto:j.d.vandenhout@gmail.com?subject=' + encodeURIComponent('Taartaanvraag — Homemade by Jess') + '&body=' + encodeURIComponent(message);
    $('#request-text').focus();
    $('#status').textContent = 'Je aanvraagtekst is klaar. Er is nog niets verstuurd.';
  });
  $('#copy').addEventListener('click', async () => {
    try { await navigator.clipboard.writeText($('#request-text').value); $('#status').textContent = 'Gekopieerd. Je kunt de tekst nu zelf met Jessica delen.'; }
    catch { $('#request-text').focus(); $('#request-text').select(); $('#status').textContent = 'Selecteer en kopieer de tekst handmatig.'; }
  });
  render();
})();
