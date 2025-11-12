// Initializes Swiper and Google Maps for the post detail page (no inline JS)
(function() {
  // Swiper carousel init
  function initSwiper() {
    if (typeof Swiper !== 'undefined') {
      new Swiper('.swiper-container', {
        loop: true,
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        },
        pagination: {
          el: '.swiper-pagination',
          clickable: true,
        },
      });
    }
  }

  // Google Maps callback required by script tag (&callback=initMap)
  window.initMap = function() {
    var el = document.getElementById('map');
    if (!el || !window.google || !google.maps) return;
    var lat = parseFloat(el.getAttribute('data-lat')) || 0;
    var lng = parseFloat(el.getAttribute('data-lng')) || 0;
    var map = new google.maps.Map(el, {
      center: { lat: lat, lng: lng },
      zoom: 12
    });
    new google.maps.Marker({ position: { lat: lat, lng: lng }, map: map, draggable: false });
  };

  // Initialize swiper on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSwiper);
  } else {
    initSwiper();
  }
})();
