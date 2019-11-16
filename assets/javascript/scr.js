if (navigator.userAgent.indexOf('UBrowser') >= 0 ) {
	$('#css').prop("href", "/static/css/uc-css.css")
}
// detect

//search animation
var text = document.getElementById('id_q');
var btn = document.getElementById('searchbtn');
var search = $('#search');

$('#search').hover(function () {
	if (text.value == 0) {
		$('#search').removeClass('box-nonhover').addClass('search-box');
		$('#id_q').removeClass('txt-nonhover').addClass('search-txt');
		$('#searchbtn').removeClass('btn-nonhover').addClass('search-btn');
	} else if (text.value !=0 ){
		$('#search').removeClass('search-box').addClass('box-nonhover');
		$('#id_q').removeClass('search-txt').addClass('txt-nonhover');
		$('#searchbtn').removeClass('search-btn').addClass('btn-nonhover');
	}
})
//end search animation


//enter to go
$( "#searchbtn, #id_q" ).keyup(function( event ) {

}).keydown(function( event ) {
  if ( event.which == 13 ) {
    event.preventDefault();
    document.getElementById('searchbtn').click()
  }
});
//end enter to go

// carousel script
$(function() {
var moveSpeed = 1000;
var delay = 3000;
var currentSlide = 0;
var interval;
var stopSlide;

function startSlide() {
 interval = setInterval(function() {
		$('#slides-own').animate({
			'margin-left' : "-=99.5%"
		}, moveSpeed, function() {
			currentSlide++;
			if (currentSlide === 19) {
				currentSlide = 1;

				$('#slides-own').animate({
					'margin-left' : "0"
				});
			}
		});
	}, delay)
}

function stopSlide() {
	clearInterval(interval)
}
startSlide();

$('#slider-own').on('mouseleave',startSlide).on('mouseenter', stopSlide	)

})
// end carousel script

// header animation
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    document.getElementById("header").style.fontSize = "15px";
    $('#h1-hd').css({"font-size": "30", "margin-top": "0px"})
    $('#list-hd').css({"margin-top": "-19px"})
    $('#search').css({"margin-top": "1	0px"})
    $('#header').css({"height": "60"})

  } else {
    document.getElementById("header").style.fontSize = "17px";
    $('#h1-hd').css({"font-size": "40px", "margin-top": "0px"})
    $('#list-hd').css({"margin-top": "0"})
    $('#search').css({"top": "23%"})
    $('#header').css({"height": "90"})

  }
}
// end header animation

// scrool left
var countLeft = 0;
var countRight = 0;

function left() {
	if (countLeft <= 3) {
		if (countLeft == 1 || countLeft == 0) {
				$('#ss-ul').animate({
					'margin-left': "-=101%"
				});
		} else if (countLeft == 2 || countLeft == 3) {
			$('#ss-ul').animate({
				'margin-left': "-=100%"
			});
		}
		countLeft += 1
		countRight -= 1
	} else {
		$('#ss-ul').animate({
			'margin-left': "+=402.001%"
		})
		countLeft = 0;
	}
}
// end scroll left

// mini slide
var miniSlide = 0;
var miniInterval;

function miniSlideSR() {
	miniInterval = setInterval(function () {
		$('#mini-slides').animate({
			'margin-left' : '-=100.3%'
		},1500, function () {
			miniSlide++;
			if (miniSlide == 10) {
				miniSlide = 0;
				$('#mini-slides').animate({
					'margin-left': "2%"
				})
			}
		})
	}, 3000)
}

function miniSlideST() {
	clearInterval(miniInterval);
}

miniSlideSR();

$('#mini-slider').on('mouseleave',miniSlideSR).on('mouseenter', miniSlideST);
//end mini slide
