/**
 * Created by noel on 15.02.16.
 */
var $ = django.jQuery;

var picker_widget = "<div id='colorpicker'></div>";

$(document).ready(function() {
    var id_palette = $('#id_palette');
    $(picker_widget).appendTo('body');
    $('#id_color_picker').bind('click', function() {
        var offset = id_palette.offset();
        var helper_style = {
            'top': offset.top + id_palette.height() + 3,
            'left': offset.left,
        };
        $('#colorpicker').css(helper_style).toggle(400);
   });
    $('#colorpicker').hide().farbtastic(id_palette);
});