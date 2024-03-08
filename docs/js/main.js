/*
Template Name: Mediclinis - Medical & Health HTML Template
Author       : Theme_crazy
Version      : 1.0
*/

(function ($) {
    "use strict";

    /*=============================================
        =     Menu sticky & Scroll to top      =
    =============================================*/
    $(window).on('scroll', function () {
        var scroll = $(window).scrollTop();
        if (scroll < 245) {
            $("#sticky-header").removeClass("sticky-menu");
            $('.scroll-to-target').removeClass('open');

        } else {
            $("#sticky-header").addClass("sticky-menu");
            $('.scroll-to-target').addClass('open');
        }
    });


    var counterUp = window.counterUp["default"]; // import counterUp from "counterup2"

    var $counters = $(".counter");

    /* Start counting, do this on DOM ready or with Waypoints. */
    $counters.each(function (ignore, counter) {
        var waypoint = new Waypoint({
            element: $(this),
            handler: function () {
                counterUp(counter, {
                    duration: 1000,
                    delay: 16
                });
                this.destroy();
            },
            offset: 'bottom-in-view',
        });
    });

    $('select').niceSelect();

})(jQuery);

// For Live Projects
window.addEventListener('load', function () {
    document.querySelector('body').classList.add("loaded")
});

// Testimonial Slider 
var swiper = new Swiper(".testimonial-slider-active", {
    slidesPerView: 1,
    spaceBetween: 10,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        768: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        992: {
            slidesPerView: 3,
            spaceBetween: 30,
        },
    }
});

// Client Slider 
var swiper2 = new Swiper(".client-slider-active", {
    slidesPerView: 2,
    spaceBetween: 20,
    loop: true,
    breakpoints: {
        768: {
            slidesPerView: 3,
        },
        992: {
            slidesPerView: 4,
            spaceBetween: 30,
        },
    }
});

// Responsive Menu
document.addEventListener(
    "DOMContentLoaded", () => {
        if (document.querySelector("#menu")) {
            const menu = new MmenuLight(
                document.querySelector("#menu"),
                "(max-width: 991px)"
            );

            const navigator = menu.navigation();
            const drawer = menu.offcanvas();

            document.querySelector("a[href='#menu']").addEventListener("click", (evnt) => {
                evnt.preventDefault();
                drawer.open();
            });
        }
    }
);

// Scroll Animation
scrollCue.init();
