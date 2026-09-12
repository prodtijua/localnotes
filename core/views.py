from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'index.html', {
            "bookmarks": bookmarks,
        })

def add(request):
    if request.method == 'POST':
        data = request.POST
        category_id = int(data.get('category'))
        category = Category.objects.get(id = category_id)
        Bookmark.objects.create(title = data.get('title'), url = data.get('url'), description = data.get('description'), category = category)
        return redirect ('main')
    return render(request, 'add.html', {
            "categories": Category.objects.all()
        })

def del_note(request, note_id):
    note = Bookmark.objects.get(id = note_id)
    note.delete()
    return redirect('main')

def categories(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name and name.strip():
            name = name.strip()
            if not Category.objects.filter(name = name).exists():
                Category.objects.create(name = name)
        return redirect('categories')
    return render(request, 'categories.html', {
            "categories": Category.objects.all()
        })

def del_category(request, category_id):
    category = Category.objects.get(id = category_id)
    category.delete()
    return redirect('categories')
