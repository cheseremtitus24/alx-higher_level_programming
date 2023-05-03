
$(function () {
  $.ajax(
    {
      type: 'GET',
      dataType: 'json',
      url: 'https://fourtonfish.com/hellosalut/?lang=fr',
      success: function (results) {
        $('DIV#hello').html(results.hello);
      },
      error: function () {
        alert('error loading results');
      }
    });
}
);
