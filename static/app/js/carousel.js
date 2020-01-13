$('#cover', '.carousel').owlCarousel({
    items:2,
    margin: 5,
    nav: true,  
    center:true,
    loop: true,
    autoplay:true,
    autoplayTimeout:10000,
    autoplayHoverPause:true,
    navText: [
        '<i class="fa fa-chevron-left" aria-hidden="true"></i>',
        '<i class="fa fa-chevron-right" aria-hidden="true"></i>'
    ],
    navContainer: '.carousel .custom-nav',
    responsive: {
      0: {
        items: 1
      },
      600: {
        items: 1
      },
      1000: {
        items: 2
      }
    }
})


$('#carousel-small', '.carousel-card').owlCarousel({
    items:6,
    margin: 30,
    responsive: {
      0: {
        items: 2
      },
      600: {
        items: 4
      },
      1000: {
        items: 5
      }
    }
})


$('#carousel-category','.carousel-icon').owlCarousel({
  items:3,
  margin: 30,
  responsive: {
    0: {
      items: 1
    },
    300: {
      items: 2
    },
    600: {
      items: 3
    },
    1000: {
      items: 3
    }
  }
})