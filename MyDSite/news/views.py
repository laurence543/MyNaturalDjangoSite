from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import CreateForm, EditForm, EditPhotoForm
from .models import Posts
from django.core.files.storage import FileSystemStorage
from time import strftime, localtime


def check_user(request):
    global user
    if 'user' in request.session:
        user = request.session['user']
    else:
        user = 'Гость'


def index(request):
    check_user(request)
    posts_x = Posts.objects.all()
    paginator = Paginator(posts_x, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'news/index.html', context)


def create(request):
    if request.method == 'POST':
        check_user(request)
        title = request.POST.get('title')
        annotation = request.POST.get('annotation')
        content = request.POST.get('content')
        link = request.POST.get('link')

        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        file_url = fs.url(filename)

        publish = strftime('%Y-%m-%d %H:%M:%S', localtime())
        status = 'Опубликована'

        post = Posts(
            title=title, annotation=annotation, content=content,
            link=link, photo=file_url, publish=publish,
            status=status
        )
        post.save()

        color = 'green'
        message = 'Новость успешно добавлена'
        context = {
            'user': user,
            'color': color,
            'message': message
        }
        return render(request, 'news/create_res.html', context)
    else:
        check_user(request)
        form = CreateForm()
        context = {
            'user': user,
            'form': form
        }
        return render(request, 'news/create.html', context)


def delete(request, id):
    if request.method == 'POST':
        check_user(request)
        post = Posts.objects.get(id=id)
        post.delete()
        context = {
            'user': user,
            'message': 'Новость успешно удалена'
        }
        return render(request, 'news/delete_res.html', context)
    else:
        check_user(request)
        post = Posts.objects.get(id=id)
        context = {
            'user': user,
            'post': post
        }
        return render(request, 'news/delete.html', context)


def edit(request, id):
    post = Posts.objects.get(id=id)
    if request.method == 'POST':

        check_user(request)
        title = request.POST.get('title')
        annotation = request.POST.get('annotation')
        content = request.POST.get('content')
        link = request.POST.get('link')
        photo = request.POST.get('photo')

        publish = strftime('%Y-%m-%d %H:%M:%S', localtime())
        status = 'Опубликована'

        post = Posts(
            id=id, title=title, annotation=annotation, content=content,
            link=link, photo=photo, publish=publish,
            status=status
        )
        post.save()

        context = {
            'user': user,
        }
        return render(request, 'news/edit_res.html', context)
    else:  # request.method == 'GET':
        check_user(request)
        form = EditForm(initial={'title': post.title,
                                 'annotation': post.annotation,
                                 'content': post.content,
                                 'link': post.link,
                                 'photo': post.photo,
                                 })
        context = {
            'user': user,
            'post': post,
            'form': form,
        }
        return render(request, 'news/edit.html', context)


def edit_photo(request, id):
    post = Posts.objects.get(id=id)
    if request.method == 'POST':
        check_user(request)

        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        file_url = fs.url(filename)

        publish = strftime('%Y-%m-%d %H:%M:%S', localtime())
        status = 'Опубликована'

        post = Posts(
            id=id, photo=file_url, publish=publish,
            status=status
        )
        post.save(update_fields=["photo"])
        context = {
            'user': user,
            'post': post,
        }
        return render(request, 'news/edit_photo_res.html', context)
    else:  # elif request.method == 'GET':
        check_user(request)
        photo_form = EditPhotoForm(initial={
            'photo': post.photo,
        })
        context = {
            'user': user,
            'photo_form': photo_form,
            'post': post,
        }
        return render(request, 'news/edit_photo.html', context)


def single(request, id):
    check_user(request)
    post = Posts.objects.get(id=id)
    context = {
        'user': user,
        'post': post
    }
    return render(request, 'news/single.html', context)
