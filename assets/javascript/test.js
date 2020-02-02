function square() {
  var width = $('#imeg1, #imeg2').outerWidth();
  var minus = width * 0.4;
  var final = width - minus;
  console.log(width);
  $('#imeg1, #imeg2, .ss-image, .gameimage').css('height', final);
}

function sideSugest() {
  var width = $('.listlast, .list-tit').outerWidth();
  var minus = width * 0.75;
  var final = width - minus;
  $('.listlast').css('height', final);
}

function image() {
  var width = $('.list, .list-title').outerWidth();
  var minus = width * 0.35;
  var final = width - minus;
  $('.list, .list-title').css('height', final);
}

function iframe() {
  var width = $('#iframe').outerWidth();
  var minus = width * 0.5;
  var final = width - minus
  $('#iframe').css('height', final);
}

$(document).ready(function () {
  square();
  iframe();
  sideSugest();
  image();
});

$(window).resize(function () {
  square();
  iframe();
  sideSugest();
  image();
});
