from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import CreateForm
from .models import Events
from time import strftime, localtime


def check_user(request):
    global user
    if 'user' in request.session:
        user = request.session['user']
    else:
        user = 'Гость'


def index(request):
    check_user(request)
    events_x = Events.objects.all()
    paginator = Paginator(events_x, 5)
    page = request.GET.get('page')
    events = paginator.get_page(page)
    context = {
        'user': user,
        'events': events,
    }
    return render(request, 'events/index.html', context)


def create(request):
    if request.method == 'POST':
        check_user(request)
        title = request.POST.get('title')
        annotation = request.POST.get('annotation')
        content = request.POST.get('content')

        publish = strftime('%Y-%m-%d %H:%M:%S', localtime())
        status = 'Опубликована'

        event = Events(
            title=title, annotation=annotation, content=content, publish=publish,
            status=status
        )
        event.save()

        color = 'green'
        message = 'Событие успешно добавлена'
        context = {
            'user': user,
            'color': color,
            'message': message
        }
        return render(request, 'events/create_res.html', context)
    else:
        check_user(request)
        form = CreateForm()
        context = {
            'user': user,
            'form': form
        }
        return render(request, 'events/create.html', context)


def delete(request, id):
    if request.method == 'POST':
        check_user(request)
        event = Events.objects.get(id=id)
        event.delete()
        context = {
            'user': user,
            'message': 'Новость успешно удалена'
        }
        return render(request, 'events/delete_res.html', context)
    else:
        check_user(request)
        event = Events.objects.get(id=id)
        context = {
            'user': user,
            'event': event
        }
        return render(request, 'events/delete.html', context)


def single(request, id):
    check_user(request)
    event = Events.objects.get(id=id)
    context = {
        'user': user,
        'event': event
    }
    return render(request, 'events/single.html', context)
