// Document ready
$(function () {
    var $searchFormInput = $('#search-form input');
    $searchFormInput.bind('focus', function () {
        $(this).parents('form').addClass('focus');
    });
    $searchFormInput.bind('blur', function () {
        $(this).parents('form').removeClass('focus');
    });
});