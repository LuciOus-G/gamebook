function square() {
  var width = $('#imeg1, #imeg2, #iframe').outerWidth();
  var minus = width * 100 / 20;
  var final = width - minus;

  $('#imeg1, #imeg2, #iframe, .ss-image, .gameimage').css('height', final);
}

$(document).ready(function () {
  square();
});

$(window).resize(function () {
  square();
  console.log("test");
});
