jQuery(document).ready(function($){
    //xử lý đóng mở menu
    $(document).on('click', ".icon_close_menu, .over", function() {
        $('.over, .nav').fadeOut(300 , function() {
            $('.over').remove();
        });
        $('.nav').hide();
        $('.icon_show_menu').show(100)
    return false;
    });
    $('.icon_show_menu').click(function(){
        $('.nav').show();
        $('body').append('<div class="over">');
        $('.over').fadeIn();
    })
})