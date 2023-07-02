(function($){"use strict";$(document).ready(function(){init_typed();load_modal();});$(window).on("load",function(){$("#preloader-active").delay(450).fadeOut("slow");$("body").delay(450).css({overflow:"visible",});});function init_typed(){var $typed=$("#typed");if($typed.length){var typed=new Typed("#typed",{strings:["Plan. &#128203;","Supply. &#128668;","Craft. &#128736;","Execute. &#127959;","Build. &#128119;","Deliver. &#127969;",],loop:true,typeSpeed:80,backSpeed:30,});}}
$(document).ready(function(){$("#btn-description").click(function(){$("#description-container").toggle();});});var menu=$("ul#navigation");if(menu.length<1025){menu.slicknav({label:"Main Menu",prependTo:".mobile_menu",closedSymbol:"+",openedSymbol:"-",duration:1000,easingOpen:"easeOutBounce",closeOnClick:true,});}
function mainSlider(){var BasicSlider=$(".slider-active");BasicSlider.on("init",function(e,slick){var $firstAnimatingElements=$(".single-slider:first-child").find("[data-animation]");doAnimations($firstAnimatingElements);});BasicSlider.on("beforeChange",function(e,slick,currentSlide,nextSlide){var $animatingElements=$('.single-slider[data-slick-index="'+nextSlide+'"]').find("[data-animation]");doAnimations($animatingElements);});BasicSlider.slick({autoplay:false,autoplaySpeed:4000,dots:false,fade:true,arrows:false,prevArrow:'<button type="button" class="slick-prev"><img src="img/hero_thumb/arrow-left.png" alt=""><img class="secondary-img" src="img/hero_thumb/left-white.png" alt=""></button>',nextArrow:'<button type="button" class="slick-next"><img src="img/hero_thumb/arrow-right.png" alt=""><img class="secondary-img" src="img/hero_thumb/right-white.png" alt=""></button>',responsive:[{breakpoint:1024,settings:{slidesToShow:1,slidesToScroll:1,infinite:true,},},{breakpoint:991,settings:{slidesToShow:1,slidesToScroll:1,arrows:false,},},{breakpoint:767,settings:{slidesToShow:1,slidesToScroll:1,arrows:false,},},],});function doAnimations(elements){var animationEndEvents="webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend";elements.each(function(){var $this=$(this);var $animationDelay=$this.data("delay");var $animationType="animated "+$this.data("animation");$this.css({"animation-delay":$animationDelay,"-webkit-animation-delay":$animationDelay,});$this.addClass($animationType).one(animationEndEvents,function(){$this.removeClass($animationType);});});}}
mainSlider();var testimonial=$(".h1-testimonial-active");if(testimonial.length){testimonial.slick({dots:false,infinite:true,speed:1200,autoplay:true,arrows:true,prevArrow:'<button type="button" class="slick-prev"><i class="ti-angle-left"></i></button>',nextArrow:'<button type="button" class="slick-next"><i class="ti-angle-right"></i></button>',slidesToShow:1,slidesToScroll:1,responsive:[{breakpoint:1024,settings:{slidesToShow:1,slidesToScroll:1,infinite:true,dots:false,arrow:false,},},{breakpoint:600,settings:{slidesToShow:1,slidesToScroll:1,arrows:true,},},{breakpoint:480,settings:{slidesToShow:1,slidesToScroll:1,arrows:true,prevArrow:'<button type="button" class="slick-prev" style="right: 40px;"><i class="ti-angle-left"></i></button>',nextArrow:'<button type="button" class="slick-next" style="right: 0px;"><i class="ti-angle-right"></i></button>',},},],});}
var client_list=$(".gallery-active");if(client_list.length){client_list.owlCarousel({slidesToShow:3,slidesToScroll:1,loop:true,autoplay:true,speed:3000,smartSpeed:2000,nav:false,dots:false,margin:0,autoplayHoverPause:true,responsive:{0:{nav:false,items:2,},768:{nav:false,items:3,},},});}
var nice_Select=$("select");if(nice_Select.length){nice_Select.niceSelect();}
$(window).on("scroll",function(){var scroll=$(window).scrollTop();if(scroll<245){$(".header-sticky").removeClass("sticky-bar");}else{$(".header-sticky").addClass("sticky-bar");}});$(window).on("scroll",function(){var scroll=$(window).scrollTop();if(scroll<245){$(".header-sticky").removeClass("sticky");}else{$(".header-sticky").addClass("sticky");}});$.scrollUp({scrollName:"scrollUp",topDistance:"300",topSpeed:300,animation:"fade",animationInSpeed:200,animationOutSpeed:200,scrollText:'<i class="ti-arrow-up"></i>',activeOverlay:false,});$("[data-background]").each(function(){$(this).css("background-image","url("+$(this).attr("data-background")+")");});new WOW().init();$(".counter").counterUp({delay:13,time:4000,});function mailChimp(){$("#mc_embed_signup").find("form").ajaxChimp();}
mailChimp();var popUp=$(".single_gallery_part, .img-pop-up");if(popUp.length){popUp.magnificPopup({type:"image",gallery:{enabled:true,},});}
$(".timeline").timeline({forceVerticalMode:800,mode:"vertical",visibleItems:4,});})(jQuery);;