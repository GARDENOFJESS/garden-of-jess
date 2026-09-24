(() => {
  const cards = [...document.querySelectorAll('.herb-card')];
  const search = document.getElementById('search-input');
  const counter = document.getElementById('counter-info');
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const slug = value => normalize(value).replace(/[^a-z0-9]+/g, '-');
  const herbs = cards.map(card => ({ card, id: slug(card.dataset.name), name: card.querySelector('.herb-name').textContent,
    blends: [...card.querySelectorAll('.blend-tag')].map(link => link.textContent.replace('✦', '').trim()) }));
  let favourites = new Set();
  try { const stored = JSON.parse(localStorage.getItem('jess-herbs-v1') || '[]'); if (Array.isArray(stored)) favourites = new Set(stored.filter(id => herbs.some(herb => herb.id === id))); } catch (_) {}
  let onlyFavourites = false;
  let visible = herbs;
  let opened = null;
  let returnFocus = null;
  const label = document.createElement('label');
  label.htmlFor = search.id; label.className = 'search-label'; label.textContent = 'Welk kruid wilt u ontdekken?';
  search.closest('.search-box').before(label);
  search.type = 'search'; search.placeholder = 'Bijvoorbeeld munt, citrus of menthol…';
  search.setAttribute('aria-controls', 'herbs-grid');
  const tools = document.createElement('div'); tools.className = 'explorer-tools';
  tools.innerHTML = '<label>Ontdek per melange<select id="blend-select"><option value="all">Alle melanges</option></select></label><button type="button" id="favourite-filter" aria-pressed="false">Mijn favorieten</button><button type="button" id="surprise-herb">Verras me ↗</button><button type="button" id="reset-herbs">Wis filters</button>';
  search.closest('.search-box').after(tools);
  const blend = tools.querySelector('select');
  [...new Set(herbs.flatMap(herb => herb.blends))].sort().forEach(name => blend.add(new Option(name, name)));
  const empty = document.createElement('div'); empty.className = 'explorer-empty'; empty.hidden = true;
  empty.innerHTML = '<h2>Hier groeit nog niets.</h2><p>Geen kruiden gevonden. Probeer een andere zoekterm of wis uw filters.</p><button type="button">Toon alle kruiden</button>';
  document.getElementById('herbs-grid').after(empty);
  counter.setAttribute('role', 'status'); counter.setAttribute('aria-live', 'polite');
  const dialog = document.createElement('dialog'); dialog.className = 'herb-dialog'; dialog.setAttribute('aria-labelledby', 'herb-detail-title');
  dialog.innerHTML = '<button class="dialog-close" autofocus>Sluiten ×</button><div class="herb-detail"></div><nav class="dialog-navigation" aria-label="Bladeren door kruiden"><button class="previous-herb">← Vorige</button><button class="next-herb">Volgende →</button></nav>';
  document.body.append(dialog);
  function updateURL() {
    const params = new URLSearchParams();
    if (search.value.trim()) params.set('q', search.value.trim());
    if (currentTaste !== 'all') params.set('taste', currentTaste);
    if (currentLetter !== 'all') params.set('letter', currentLetter);
    if (blend.value !== 'all') params.set('blend', blend.value);
    if (onlyFavourites) params.set('saved', '1');
    if (opened) params.set('herb', opened.id);
    history.replaceState(null, '', location.pathname + (params.size ? '?' + params : ''));
  }
  function openHerb(herb) {
    if (!dialog.open) returnFocus = document.activeElement;
    opened = herb;
    const detail = dialog.querySelector('.herb-detail'); detail.replaceChildren();
    const top = herb.card.querySelector('.herb-card-top').cloneNode(true);
    top.querySelector('.herb-name').id = 'herb-detail-title';
    detail.append(top, herb.card.querySelector('.herb-blends-footer').cloneNode(true));
    const index = visible.indexOf(herb);
    dialog.querySelector('.previous-herb').disabled = index <= 0;
    dialog.querySelector('.next-herb').disabled = index < 0 || index >= visible.length - 1;
    if (!dialog.open) { dialog.showModal(); document.body.style.overflow = 'hidden'; }
    dialog.scrollTop = 0;
    updateURL();
  }
  dialog.querySelector('.dialog-close').onclick = () => dialog.close();
  dialog.addEventListener('click', event => {
    const bounds = dialog.getBoundingClientRect();
    if (event.target === dialog && (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom)) dialog.close();
  });
  dialog.addEventListener('close', () => { opened = null; document.body.style.overflow = ''; updateURL(); if (returnFocus?.isConnected) returnFocus.focus(); });
  dialog.querySelector('.previous-herb').onclick = () => { const next = visible[visible.indexOf(opened) - 1]; if (next) openHerb(next); };
  dialog.querySelector('.next-herb').onclick = () => { const next = visible[visible.indexOf(opened) + 1]; if (next) openHerb(next); };
  herbs.forEach(herb => {
    const actions = document.createElement('div'); actions.className = 'herb-actions';
    const detail = document.createElement('button'); detail.className = 'detail-button'; detail.textContent = 'Ontdek dit kruid ↗'; detail.setAttribute('aria-label', 'Ontdek ' + herb.name); detail.onclick = () => openHerb(herb);
    const save = document.createElement('button'); save.textContent = '♡ Bewaren'; save.setAttribute('aria-label', herb.name + ' bewaren');
    const sync = () => { const saved = favourites.has(herb.id); save.setAttribute('aria-pressed', String(saved)); save.textContent = saved ? '♥ Bewaard' : '♡ Bewaren'; };
    save.onclick = () => { favourites.has(herb.id) ? favourites.delete(herb.id) : favourites.add(herb.id); try { localStorage.setItem('jess-herbs-v1', JSON.stringify([...favourites])); } catch (_) {} sync(); filterHerbs(); };
    sync(); actions.append(detail, save); herb.card.querySelector('.herb-blends-footer').before(actions);
  });
  window.filterHerbs = () => {
    const words = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
    visible = herbs.filter(herb => {
      const data = herb.card.dataset;
      const text = normalize(Object.values(data).join(' ') + ' ' + herb.blends.join(' '));
      const show = words.every(word => text.includes(word)) && (currentTaste === 'all' || normalize(data.taste).includes(currentTaste)) && (currentLetter === 'all' || data.letter === currentLetter) && (blend.value === 'all' || herb.blends.includes(blend.value)) && (!onlyFavourites || favourites.has(herb.id));
      herb.card.hidden = !show; herb.card.style.display = show ? 'flex' : 'none'; return show;
    });
    counter.textContent = `${visible.length} van ${herbs.length} kruiden · ${favourites.size} bewaard`;
    empty.hidden = visible.length > 0;
    tools.querySelector('#surprise-herb').disabled = !visible.length;
    document.querySelectorAll('.btn-filter, .letter-btn').forEach(button => button.setAttribute('aria-pressed', String(button.classList.contains('active'))));
    updateURL();
  };
  const reset = () => {
    search.value = ''; currentTaste = currentLetter = 'all'; blend.value = 'all'; onlyFavourites = false;
    document.querySelectorAll('.btn-filter, .letter-btn').forEach(button => button.classList.toggle('active', button.getAttribute('onclick').includes("'all'")));
    tools.querySelector('#favourite-filter').setAttribute('aria-pressed', 'false'); filterHerbs(); search.focus();
  };
  tools.querySelector('#reset-herbs').onclick = reset; empty.querySelector('button').onclick = reset;
  blend.onchange = filterHerbs;
  tools.querySelector('#favourite-filter').onclick = event => { onlyFavourites = !onlyFavourites; event.currentTarget.setAttribute('aria-pressed', String(onlyFavourites)); filterHerbs(); };
  tools.querySelector('#surprise-herb').onclick = () => { if (visible.length) openHerb(visible[Math.floor(Math.random() * visible.length)]); };
  const params = new URLSearchParams(location.search);
  search.value = params.get('q') || '';
  if ([...blend.options].some(option => option.value === params.get('blend'))) blend.value = params.get('blend');
  for (const [key, selector] of [['taste', '.btn-filter'], ['letter', '.letter-btn']]) {
    const choice = [...document.querySelectorAll(selector)].find(button => button.getAttribute('onclick').includes("'" + params.get(key) + "'"));
    if (choice) { document.querySelectorAll(selector).forEach(button => button.classList.toggle('active', button === choice)); if (key === 'taste') currentTaste = params.get(key); else currentLetter = params.get(key); }
  }
  onlyFavourites = params.get('saved') === '1';
  tools.querySelector('#favourite-filter').setAttribute('aria-pressed', String(onlyFavourites));
  document.body.classList.add('explorer-ready'); filterHerbs();
  const initialHerb = herbs.find(herb => herb.id === params.get('herb')); if (initialHerb) openHerb(initialHerb);
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      if (!motion.matches) entry.target.animate([{ opacity: 0, transform: 'translateY(16px)' }, { opacity: 1, transform: 'translateY(0)' }], { duration: 350, easing: 'ease-out' });
      observer.unobserve(entry.target);
    }), { threshold: .05 });
    cards.forEach(card => observer.observe(card));
  }
})();
