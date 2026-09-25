'use strict';
(() => {
  const form = document.getElementById('contact-form');
  const message = document.getElementById('ContactFormMessage');
  const name = document.getElementById('ContactFormName');
  const email = document.getElementById('ContactFormEmail');
  const topic = document.getElementById('ContactFormTopic');
  const status = document.getElementById('contact-status');
  const selection = new URLSearchParams(location.search).get('selection');
  if (selection) message.value = 'Ik heb interesse in de volgende melanges:\n\n' + selection.slice(0,2000) + '\n\nKunt u mij informeren over beschikbaarheid en bestellen?';
  form.addEventListener('submit', event => {
    event.preventDefault();
    const whatsapp = event.submitter?.value === 'whatsapp';
    if (!name.reportValidity() || !message.reportValidity()) return;
    if (!whatsapp && !email.reportValidity()) return;
    const body = message.value + '\n\nNaam: ' + name.value + (email.value ? '\nE-mail: ' + email.value : '');
    if (whatsapp) {
      window.open('https://wa.me/31641615544?text=' + encodeURIComponent('Garden by Jess — ' + topic.selectedOptions[0].textContent + '\n\n' + body), '_blank', 'noopener,noreferrer');
      status.textContent = 'Verstuur uw bericht zelf in WhatsApp. Er is nog niets verstuurd. Opent er geen venster? Gebruik dan de WhatsApp-link hierboven.';
    } else {
      location.href = 'mailto:care@gardenbyjess.store?subject=' + encodeURIComponent(topic.selectedOptions[0].textContent) + '&body=' + encodeURIComponent(body);
      status.textContent = 'Verstuur het bericht in uw e-mailprogramma. Opent er niets? Mail rechtstreeks naar care@gardenbyjess.store; uw tekst blijft hier staan.';
    }
  });
})();
