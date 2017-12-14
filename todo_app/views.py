
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from todo_app.models import Blog, Comments
from django.core.paginator import Paginator
from todo_app.forms import TodoForm, TodoFullForm, ToCommentsForm
# Create your views here.


def list_view(request, page_number=1):
    items = Blog.objects.all()
    current_page = Paginator(items, 10)

    return render(request, 'todo_app/list_view.html', {
        'items': current_page.page(page_number),
       
        'author': request.user.get_username()
    })


def view(request, todo_id):
    blog = Blog.objects.get(id=todo_id)
    comments = Comments.objects.filter(post_id=todo_id)
    counter = comments.count()
    form = ToCommentsForm()
    if request.method == 'POST':

        forms = ToCommentsForm(data=request.POST)
        if forms.is_valid():

            forms.save()
            
            if request.user.get_username():
               
                Comments.objects.filter(author='').update(author=request.user.get_username()) 
            else:
                Comments.objects.filter(author='').update(author='No_name')
            Comments.objects.filter(post_id='').update(post_id=todo_id)
            return HttpResponseRedirect('/view/' + todo_id)
        else:
            print(form.errors)
            return HttpResponse('Failed to create')
    else:
        return render(request, 'todo_app/view.html', {

            'items': blog,
            'comments': comments,
            'form': form,
            'author': request.user.get_username(),
            'counter': counter
        
        })   


def create_view(request):
    if request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():

            form.save()
            Blog.objects.filter(author='').update(author=request.user.get_username())

            return HttpResponse('Success')
        else:
            print(form.errors)
            return HttpResponse('Failed to create')
    else:
        if request.user.is_authenticated():
            form = TodoForm()

            return render(request, 'todo_app/create_view.html', {
                'form': form,
            
            })
        else:
            return HttpResponse('No authorize')


def delete_view(request, todo_id):
    blog = Blog.objects.get(id=todo_id)
    author = blog.author
    user = request.user.get_username()
    if request.method == 'POST' and user == author:
        Blog.objects.filter(id=todo_id).delete()
        return HttpResponseRedirect('/')
    elif author != user:
        return HttpResponse('Не ваша запись. Удаление невозможно')
    else:   
        return HttpResponse('Bad request')


def update_view(request, todo_id):
    todo = get_object_or_404(Blog, id=todo_id)

    if request.method == 'POST':
        form = TodoFullForm(data=request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
            return HttpResponse('Error')
    else:
        author = Blog.objects.get(id=todo_id)
        form = TodoFullForm(instance=todo)
        return render(request, 'todo_app/update_view.html', {
            'form': form,
            'author': author.author,
            'user': request.user.get_username()
        })		
