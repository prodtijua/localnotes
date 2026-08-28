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
