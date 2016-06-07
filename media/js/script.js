$(document).ready(function () {
    $('.slider1').bxSlider({
        slideWidth: 235,
        minSlides: 2,
        maxSlides: 3,
        slideMargin: 10,
        pager: false,
        auto: true,
    });
});

$(document).ready(function () {
    $('.slider2').bxSlider({
        slideWidth: 357,
        minSlides: 2,
        maxSlides: 2,
        slideMargin: 10,
        pager: false,
        auto: true,
    });
});

$(document).ready(function () {
    $('.slider3').bxSlider({
        slideWidth: 235,
        minSlides: 2,
        maxSlides: 3,
        slideMargin: 10,
        pager: false,
        auto: true,
    });
});

$(document).ready(function () {
    $('.minus').click(function () {
        var $input = $(this).parent().find('input');
        var count = parseInt($input.val()) - 1;
        count = count < 1 ? 1 : count;
        $input.val(count);
        $input.change();
        return false;
    });
    $('.plus').click(function () {
        var $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) + 1);
        $input.change();
        return false;
    });
});

$(function() {

  $('ul.tabs__caption').on('click', 'li:not(.active)', function() {
    $(this)
      .addClass('active').siblings().removeClass('active')
      .closest('div.tabs').find('div.tabs__content').removeClass('active').eq($(this).index()).addClass('active');
  });

});

function addToCart(id) {
            var item = $('#' + id + '_input');
            count = "" + item.val();
            url = "/eshop_item/" + id + "/addtocart/" + count + "/";
            $.ajax({
                url: url,
                type: 'GET',
                datatype: 'json',
                error: function (xhr, status, errorThrown) {
                    alert(errorThrown + '\n' + status + '\n' + xhr.statusText + '\n' + url);
                },
                success: function (data) {
                    $('#item-add-box').removeClass('item_add_hidden');
                    $('#item-add-box').addClass('item_add_visible');
                    setTimeout(function () {
                        $('#item-add-box').addClass('item_add_hidden');
                        $('#item-add-box').removeClass('item_add_visible');
                    }, 2000);
                    $('#cart-quantity').html(data['total_count']);
                    $('#cart-price').html(data['total_price']);
                }
            });
        }

$(function(){
        $.ajax({
            url: "/eshop_item/0/addtocart/0/",
            type: 'GET',
            datatype: 'json',
            error: function(xhr, status, errorThrown) {
            alert(errorThrown+'\n'+status+'\n'+xhr.statusText+'\n'+url);
            },
            success: function(data) {
                $('#cart-quantity').html(data['total_count']);
                $('#cart-price').html(data['total_price']);
            }
        });
});

function show() {
    document.getElementById('cargo-inform').style.display='block';
    }
    function hide() {
        document.getElementById('cargo-inform').style.display='none';
    }

$(document).ready(function(){
    $("#id_username").attr('placeholder', 'Ваш E-mail');
    $("#id_email").attr('placeholder', 'Ваш E-mail');
    $("#id_password").attr('placeholder', 'Пароль');
    $("#id_password1").attr('placeholder', 'Пароль');
    $("#id_password2").attr('placeholder', 'Повторите пароль');
    $("#id_fio").attr('placeholder', 'Фамилия, Имя');
    $("#id_city").attr('placeholder', 'Ваш город');
    $("#id_phone").attr('placeholder', 'Телефон');
    $("#id_street").attr('placeholder', 'Улица');
    $("#id_house").attr('placeholder', 'Дом');
    $("#id_flat").attr('placeholder', 'Квартира');
    $("#id_index").attr('placeholder', 'Почтовый индекс');
    $("#id_name").attr('placeholder', 'Ваше имя');
    $("#id_message").attr('placeholder', 'Ваше сообщение');
});