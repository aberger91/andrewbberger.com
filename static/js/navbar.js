(function ($) {
    var menuPosition = function () {
        var nav = $("#navbar-floating"),

        height = nav.height(),
        windowHeight = $("#navbar-fixed").outerHeight();

        if ($(window).scrollTop() > windowHeight) {
            nav.addClass('fixed');
            $("body").css({ 'margin-top': height + 'px'})
        } else {
            nav.removeClass('fixed');
            $("body").css({ 'margin-top': 0 })
        }
    };

    menuPosition();
    $(document).scroll(menuPosition);
}(jQuery));
