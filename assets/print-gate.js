/**
 * Garden by Jess — Drukwerk & Huisstijl Password Gate
 * Beveiliging voor officiële drukwerk-, sticker- en kaartjesspecificaties.
 * Toegangscode: 1974 (SHA-256 geverifieerd)
 */
(function() {
  const TARGET_HASH = 'ec54e99514663edb97adef400fbf34a77daae108303d3da8008a7dfb4cdf0f52';
  const AUTH_KEY = 'garden_print_auth_1974';

  const isAuth = localStorage.getItem(AUTH_KEY) === 'granted' || sessionStorage.getItem(AUTH_KEY) === 'granted';

  if (isAuth) {
    document.documentElement.classList.remove('gate-locked');
  } else {
    document.documentElement.classList.add('gate-locked');
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', mountGate);
    } else {
      mountGate();
    }
  }

  function mountGate() {
    if (document.getElementById('password-gate-overlay')) return;

    // Detect path depth for logo
    const isSubdir = window.location.pathname.includes('/stickers_print_package/');
    const logoSrc = isSubdir ? '../assets/garden_by_jess_logo.jpg' : 'assets/garden_by_jess_logo.jpg';
    const homeUrl = isSubdir ? '../index.html' : 'index.html';

    const overlay = document.createElement('div');
    overlay.id = 'password-gate-overlay';
    overlay.innerHTML = `
      <div id="password-gate-card">
        <div class="gate-logo-frame">
          <img src="${logoSrc}" alt="Garden by Jess Logo" class="gate-logo-img">
        </div>
        <p class="gate-eyebrow">Besloten Drukwerk & Huisstijl</p>
        <h1 class="gate-title">Garden by Jess</h1>
        <p class="gate-description">
          De technische drukwerkspecificaties, 300 DPI bestanden en het officiële bedrijfskaartje zijn beveiligd. Voer de toegangscode (1974) in om toegang te krijgen.
        </p>
        
        <form class="gate-form" id="gate-form" onsubmit="return false;">
          <input 
            type="password" 
            id="gate-password-input" 
            class="gate-input" 
            placeholder="Toegangscode..." 
            autocomplete="current-password"
            autofocus
            required
          >
          <button type="submit" class="gate-btn" id="gate-submit-btn">
            Ontgrendel Drukwerksheet →
          </button>
          <div class="gate-error" id="gate-error">
            Onjuiste toegangscode. Controleer uw code en probeer opnieuw.
          </div>
        </form>

        <div style="margin-top: 18px;">
          <a href="${homeUrl}" style="font-size: 12px; color: var(--gate-sage, #6B7A55); text-decoration: none; font-weight: 600;">
            ← Terug naar de Webwinkel
          </a>
        </div>

        <div class="gate-footer">
          © 2026 Garden by Jess • Voorkamp 14, Beets
        </div>
      </div>
    `;

    document.body.appendChild(overlay);

    const form = document.getElementById('gate-form');
    const input = document.getElementById('gate-password-input');
    const errorBox = document.getElementById('gate-error');
    const card = document.getElementById('password-gate-card');

    form.addEventListener('submit', async function(e) {
      e.preventDefault();
      const val = input.value.trim();
      if (!val) return;

      let verified = false;

      // Primary verification: Web Crypto SHA-256
      if (window.crypto && crypto.subtle) {
        try {
          const encoder = new TextEncoder();
          const data = encoder.encode(val);
          const hashBuffer = await crypto.subtle.digest('SHA-256', data);
          const hashArray = Array.from(new Uint8Array(hashBuffer));
          const hex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
          if (hex === TARGET_HASH) {
            verified = true;
          }
        } catch (err) {
          console.error('Crypto error:', err);
        }
      }

      // Fallback verification
      if (!verified && val === '1974') {
        verified = true;
      }

      if (verified) {
        localStorage.setItem(AUTH_KEY, 'granted');
        sessionStorage.setItem(AUTH_KEY, 'granted');
        errorBox.style.display = 'none';
        
        // Smooth unlock transition
        overlay.style.opacity = '0';
        overlay.style.transform = 'scale(1.02)';
        
        setTimeout(() => {
          document.documentElement.classList.remove('gate-locked');
          overlay.remove();
        }, 450);
      } else {
        errorBox.style.display = 'block';
        card.classList.add('gate-shake');
        input.value = '';
        input.focus();
        setTimeout(() => {
          card.classList.remove('gate-shake');
        }, 450);
      }
    });

    // Auto-focus input
    setTimeout(() => {
      if (input) input.focus();
    }, 100);
  }

  // Global helper om de drukwerkpagina opnieuw te vergrendelen
  window.lockPrintSheet = function() {
    localStorage.removeItem(AUTH_KEY);
    sessionStorage.removeItem(AUTH_KEY);
    window.location.reload();
  };
})();
