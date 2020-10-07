from django.shortcuts import render


# Представление для загрузки главной страницы сайта
def index(request):
    if 'user' in request.session:
        user = request.session['user']
    else:
        user = 'Гость'
    context = {'user': user}
    return render(request, 'home/index.html', context)


# Представление для загрузки информационной страницы
def about(request):
    if 'user' in request.session:
        user = request.session['user']
    else:
        user = 'Гость'
    context = {'user': user}
    return render(request, 'home/about.html', context)


# Представление для загрузки страницы контактов
def contacts(request):
    if 'user' in request.session:
        user = request.session['user']
    else:
        user = 'Гость'
    context = {'user': user}
    return render(request, 'home/contacts.html', context)
