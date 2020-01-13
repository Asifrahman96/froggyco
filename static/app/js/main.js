// Js code to fading out message alerts

setTimeout(function(){
    $('#message').fadeOut('slow');
}, 4000);

// Js Code for Video Popup During Page Load

$(function() {

    // CLOSE AND REMOVE ON ESC
    $(document).on('keyup',function(e) {
      if (e.keyCode == 27) {
        $('.video-overlay').remove();
      }
    });
    
    // CLOSE AND REMOVE ON CLICK
    $('body').on('click','.overlay, .close', function() {
      $('.video-overlay').remove();
    });
    
    // SO PLAYING WITH THE VIDEO CONTROLS DOES NOT
    // CLOSE THE POPUP
    $('body').on('click','.videoBox', function(e) {
      e.stopPropagation();
    });
    
});