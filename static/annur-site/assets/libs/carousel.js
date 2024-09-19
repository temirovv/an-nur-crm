$(document).ready(function () {
    $('.students .owl-carousel').owlCarousel({
        loop: true,
        margin: 30,
        dots: false,
        autoWidth: false,
        autoplay: true,
        items: 3,
        autoplayTimeout: 5000,
        autoplaySpeed: 3000,
        responsive: {
            0: {
                items: 1
            },
            980: {
                items: 2,
            },
            1810: {
                items: 3
            }
        }
    });

    $('.we .owl-carousel').owlCarousel({
        loop: true,
        margin: 24,
        dots: false,
        autoplay: true,
        autoWidth: true,
        items: 3,
        autoplayTimeout: 5000,
        autoplaySpeed: 3000,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    });

    $('.shop .owl-carousel, .news .owl-carousel').owlCarousel({
        loop: true,
        margin: 30,
        dots: false,
        autoplay: true,
        items: 3,
        autoplayTimeout: 5000,
        autoplaySpeed: 3000,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    });
});
