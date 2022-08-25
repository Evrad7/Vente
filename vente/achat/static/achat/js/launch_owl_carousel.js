$(document).ready(function(){
    $(".owl-carousel").owlCarousel({

      autoWidth:true,
      nav:true,
      dots:false,
      responsive:{
        500:{
          margin:40,
          items:5,
        },
        0:{
          margin:10,
          items:2,
        }
      }
    });
});
