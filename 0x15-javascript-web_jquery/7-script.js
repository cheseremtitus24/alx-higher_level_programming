$(function () {
  $.ajax(
    {
      type: 'GET',
      url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
      success: function (results) {
        $('DIV#character').html(results.name);
      },
      error: function () {
        alert('error loading results');
      }
    });
}
);
