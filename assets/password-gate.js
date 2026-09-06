/**
 * Garden by Jess — Storefront Password Gate
 * Protection for private atelier & testing preview.
 * Target Password: 1974 (SHA-256 verified)
 */
(function() {
  const TARGET_HASH = 'ec54e99514663edb97adef400fbf34a77daae108303d3da8008a7dfb4cdf0f52';
  const AUTH_KEY = 'garden_by_jess_auth';

  // Check existing authorization
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
    const isSubpage = window.location.pathname.includes('/pages/');
    const logoSrc = isSubpage ? '../assets/garden_by_jess_logo.jpg' : 'assets/garden_by_jess_logo.jpg';

    const overlay = document.createElement('div');
    overlay.id = 'password-gate-overlay';
    overlay.innerHTML = `
      <div id="password-gate-card">
        <div class="gate-logo-frame">
          <img src="${logoSrc}" alt="Garden by Jess" class="gate-logo-img">
        </div>
        <p class="gate-eyebrow">Besloten Atelier & Proeflokaal</p>
        <h1 class="gate-title">Garden by Jess</h1>
        <p class="gate-description">
          Onze theecollectie en het botanisch compendium zijn momenteel uitsluitend toegankelijk voor genodigden. Voer de toegangscode in om het atelier te betreden.
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
            Atelier Betreden →
          </button>
          <div class="gate-error" id="gate-error">
            Onjuiste toegangscode. Controleer uw code en probeer opnieuw.
          </div>
        </form>

        <div class="gate-footer">
          © 2026 Garden by Jess B.V. • Padjedijk 30, Purmerend
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

  // Global helper to re-lock the store anytime for testing
  window.lockGardenAtelier = function() {
    localStorage.removeItem(AUTH_KEY);
    sessionStorage.removeItem(AUTH_KEY);
    localStorage.removeItem('garden_by_jess_key');
    sessionStorage.removeItem('garden_by_jess_key');
    window.location.reload();
  };
})();
