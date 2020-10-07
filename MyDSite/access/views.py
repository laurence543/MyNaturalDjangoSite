from django.shortcuts import render
from .forms import RegForm, EntryForm
from .models import User, Token
from hashlib import md5
from time import strftime, localtime


# Представление для загрузки страницы входа
def entry(request):
    if request.method == 'POST':
        # Получение данных из формы:
        login = request.POST.get('login')
        pass1 = request.POST.get('pass1')
        hash_code = md5(pass1.encode())
        password = hash_code.hexdigest()

        # Сецнарий авториазции:
        check = User.objects.filter(login=login, password=password)
        n = len(check)
        if n == 0:
            message = 'Пользователь не найден!'
            color = 'red'
        else:
            request.session['user'] = login
            message = 'Автоизация пройдена успешно!'
            color = 'green'

        # Проверка текущего статуса пользователя:
        if 'user' in request.session:
            user = request.session['user']
        else:
            user = 'Гость'

        # Определение контекста и загрузка страницы:
        context = {
            'message': message,
            'color': color,
            'user': user
        }
        return render(request, 'access/entry_res.html', context)
    else:
        # Проверка текущего статуса пользователя:
        if 'user' in request.session:
            user = request.session['user']
        else:
            user = 'Гость'

        # Создание экземпляра формы и контекста:
        entry_form = EntryForm()
        context = {
            'form': entry_form,
            'user': user
        }
        return render(request, 'access/entry.html', context)


# Представление для загрузки страницы регистрации
def reg(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        email = request.POST.get('email')
        token = request.POST.get('token')

        hash_code = md5(pass1.encode())
        password = hash_code.hexdigest()
        reg_date = strftime('%Y-%m-%d %H:%M:%S', localtime())
        status = 'usual'

        # Проверка занятости логина/пароля/наличие токена и регистрация:
        temp_token = Token.objects.filter(token=token)
        select = User.objects.filter(login=login)
        t = len(temp_token)
        n = len(select)
        if n > 0:
            message = 'Логин занят!'
            color = 'red'
        elif pass1 != pass2:
            message = 'Пароли не совпадают!'
            color = 'red'
        elif t == 0:
            message = 'Неправильный токен!'
            color = 'red'
        else:
            user = User(
                login=login, password=password, email=email,
                reg_date=reg_date, status=status
            )
            user.save()
            message = 'Регистрация успешно завершена'
            color = 'green'

        # Проверка текущего статуса пользователя:
        if 'user' in request.session:
            user = request.session['user']
        else:
            user = 'Гость'

        # Определение контекста и загрузка страницы:
        context = {
            'message': message,
            'color': color,
            'user': user
            # 'login': login,
            # 'pass1': pass1,
            # 'pass2': pass2,
            # 'email': email,
            # 'password': password,
            # 'reg_date': reg_date,
            # 'status': status
        }
        return render(request, 'access/reg_res.html', context)
    else:
        # Проверка текущего статуса пользователя:
        if 'user' in request.session:
            user = request.session['user']
        else:
            user = 'Гость'

        # Создание экземпляра формы и контекста:
        reg_form = RegForm()
        context = {
            'form': reg_form,
            'user': user
        }
        return render(request, 'access/reg.html', context)


# Представление для загрузки страницы выхода
def exit_(request):
    # Удаление пользователя из сессии:
    del request.session['user']

    # Загрузка страницы:
    if 'user' in request.session:
        user = request.session['user']
    else:
        user = 'Гость'
    context = {
        'user': user
    }
    return render(request, 'access/exit_.html', context)


# Представление для загрузки страницы профиля
def profile(request):
    if 'user' in request.session:
        user = request.session['user']
    else:
        user = 'Гость'
    context = {
        'user': user
    }
    return render(request, 'access/profile.html', context)
