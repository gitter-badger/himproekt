$(document).ready(function () {
    $('#id_username').hide();

    $('#registration_form').submit(function () {
        $('#id_username').val($('#id_email').val());
    });
});