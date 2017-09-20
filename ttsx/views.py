from django.shortcuts import render,redirect
from django.http import JsonResponse


# Create your views here.


def index(request):
    return render(request, 'search/search.html', {'request': request})


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


# TODO 是否记住密码业务
def login_check(request):
    # res数据 {'username_checked':true,'password_checked':true}
    # 取出用户名密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remembered = request.POST.get('remembered')
    print(username, password, remembered)
    # 验证
    res_data = {'username_checked': False}
    if username == 'jakyy':
        res_data['username_checked'] = True
        if password == 'jakyy':
            res_data['password_checked'] = True
            # 记录session数据login=true
            request.session['logined'] = True
            request.session['username'] = username
            return JsonResponse(res_data)
        return JsonResponse(res_data)
    return JsonResponse(res_data)


def logout(request):
    request.session.flush()
    return redirect('/index/')
