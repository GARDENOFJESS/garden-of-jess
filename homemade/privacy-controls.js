'use strict';
document.querySelector('#clear-storage').addEventListener('click', () => {
  try {
    localStorage.removeItem('homemade-by-jess-cart-v2');
    localStorage.removeItem('homemade-by-jess-selection-v1');
    document.querySelector('#storage-status').textContent = 'Je taartdoos is gewist uit deze browser.';
  } catch {
    document.querySelector('#storage-status').textContent = 'De opslag is niet toegankelijk. Wis de websitegegevens via je browserinstellingen.';
  }
});
document.querySelector('#clear-storage').disabled = false;
