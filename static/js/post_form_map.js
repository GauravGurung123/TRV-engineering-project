// Google Maps initialization for the post form page
window.initMap = function() {
  var el = document.getElementById('map');
  if (!el || !window.google || !google.maps) return;
  var map = new google.maps.Map(el, {
    center: { lat: 52.2297, lng: 21.0122 },
    zoom: 6
  });

  var marker;
  map.addListener('click', function(event) {
    var lat = event.latLng.lat();
    var lng = event.latLng.lng();
    var latInput = document.getElementById('id_latitude');
    var lngInput = document.getElementById('id_longitude');
    if (latInput) latInput.value = lat;
    if (lngInput) lngInput.value = lng;
    if (marker) {
      marker.setPosition(event.latLng);
    } else {
      marker = new google.maps.Marker({ position: event.latLng, map: map });
    }
  });
};
