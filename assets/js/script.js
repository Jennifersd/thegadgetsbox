// Menu 
window.onload = function(){ 

	(function() {
	    var burger = document.querySelector(".burger-container"),
	    	header_content = document.querySelector(".header-wrap"),
	        header = document.querySelector(".header-container");
	    
	
	    burger.onclick = function() {
	        header.classList.toggle("menu-opened");
	        header_content.classList.toggle("header-opened");
	    };
	})();
	

};


// -----------------------------------------------
// -----------------------------------------------

$(document).ready(function(){
	
	// Nav categories
	
	(function() {
		$('.blocks-container > h3').click(function() {
			    $( ".blocks-container > ul" ).slideToggle( "slow" );
		});

	})();
	
	// Social fixed scroll

	(function() {
	  function fixDiv() {
	    var $cache = $('#social-fixed');
	    if ($(window).scrollTop() > 750){
	    	$cache.addClass("fixed-nav");
		} else {
			$cache.removeClass("fixed-nav");
		} 
	  }
	  $(window).scroll(fixDiv);
	  fixDiv();
	})();
	
	// Scroll bottom to content post
	
	jQuery('#button-header-post').click(function(){
	    if(jQuery('#view-post').is(":visible")){
	        jQuery("html, body").animate({scrollTop: jQuery('#view-post').offset().top});
	    }
	});

	
});



