function square() {
  var width = $('#imeg1, #imeg2').outerWidth();
  var minus = width * 0.4;
  var final = width - minus;
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

function carousel() {
  var width = $('slider-own, #slides-own, #slide-own').outerWidth();
  var minus = width * 0.6;
  var final = width - minus;
  $('#slider-own, #slides-own, #slide-own').css('height', final);
}

function footer() {
  var width = $('#footer').outerWidth();
  var minus = width * 0.91;
  var final = width - minus;
  $('#footer').css('height', final);
}

$(document).ready(function () {
  square();
  iframe();
  sideSugest();
  image();
  carousel();
  footer();
});

$(window).resize(function () {
  square();
  iframe();
  sideSugest();
  image();
  carousel();
  footer();
});
