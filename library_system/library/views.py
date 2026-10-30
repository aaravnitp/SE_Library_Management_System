from django.shortcuts import render
from django.db.models import Q
from .models import Book

def home(request):
    query = request.GET.get('search', '').strip()
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(isbn__icontains=query)
        )
    else:
        books = Book.objects.all()

    return render(request, 'library/home.html', {'books': books, 'query': query})