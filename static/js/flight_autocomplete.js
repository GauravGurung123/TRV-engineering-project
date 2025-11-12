// jQuery UI Autocomplete for flight search form
(function() {
  function setupAutocomplete(inputId, url) {
    const $input = $('#'+inputId);
    if (!$input.length || !$.ui || !$.ui.autocomplete) return;
    $input.autocomplete({
      source: function(request, response) {
        $.ajax({
          url: url,
          dataType: 'json',
          data: { term: request.term },
          success: function(data){ response(data); },
          error: function(){ response([]); }
        });
      },
      minLength: 2,
      select: function(event, ui){ $(this).val(ui.item.value); }
    })
    .autocomplete('instance')._resizeMenu = function() {
      this.menu.element.outerWidth($input.outerWidth());
    };
  }

  $(function(){
    var endpoint = document.body.getAttribute('data-airport-autocomplete');
    if (!endpoint) { endpoint = '/airport-autocomplete/'; }
    setupAutocomplete('from', endpoint);
    setupAutocomplete('to', endpoint);
  });
})();
