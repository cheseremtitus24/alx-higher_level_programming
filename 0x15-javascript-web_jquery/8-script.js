
$(function () {
  $.ajax(
    {
      type: 'GET',
      dataType: 'json',
      url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
      success: function (results) {
        $.each(results.results, function (index, result) {
          $('UL#list_movies').append('<li>' + result.title + '</li>');
        });
      },
      error: function () {
        alert('error loading results');
      }
    });
}
);
