$(function () {
    var $username = $('#username'),
        $password = $('#password'),
        $checkbox = $('#checkbox'),
        $hidden = $('input[type="hidden"]'),
        $user_error = $('#user_error'),
        $pwd_error = $('#pwd_error');
    $submit = $('#btn').click(function () {
        var post_data = {
            'username': $username.val(),
            'password': $password.val(),
            'remembered': $checkbox.prop('checked'),
            [$hidden.prop('name')]: $hidden.val()
        };
        console.log(post_data);
        $.ajax({
            'url': '{% url "main:login_check" %}',
            'type': 'POST',
            'ContextType': 'json',
            'data': post_data
        }).done(function (res) {
            // res = {
            //     'username_checked': true, 'password_checked': true
            // };
            console.log(res);
            var username_checked = res.username_checked,
                password_checked = res.password_checked;
            $user_error.hide();
            $pwd_error.hide();
            if (username_checked && password_checked) {
                location.href = '{% url "main:index" %}';
            }
            else {
                if (!username_checked) {
                    $user_error.show();
                }
                if (!password_checked) {
                    $pwd_error.show();
                }
            }
        });
    });
});
