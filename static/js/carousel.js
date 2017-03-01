$(document).ready(
    function() {
    $('#myCarousel').carousel({
    interval: 1000
    })
    
    $('#myCarousel').on('slid.bs.carousel', function() {
        //alert("slid");
    });


    $.('carousel.item').each(function(){
         var next = $(this).next();
         if (!next.length) {
           next = $(this).siblings(':first');
         }
         next.children(':first-child').clone().appendTo($(this));
         
         for (var i=0;i<2;i++) {
           next=next.next();
           if (!next.length) {
               next = $(this).siblings(':first');
           }
           
           next.children(':first-child').clone().appendTo($(this));
         }
    });

});
