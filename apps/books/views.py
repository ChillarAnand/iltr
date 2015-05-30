import urllib

from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse

from .models import Book


def home_view(request):
    """
    Home page for iltr.
    """
    return render(request, 'home.html')


def book_or_author(request, query):
    """
    Auto complete function for book, author names.
    """
    if query:
        query = urllib.parse.unquote(query)
        results = Book.objects.filter(
            Q(name__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__middle_name__icontains=query) |
            Q(author__last_name__icontains=query) 
        )
        data = [[i.name, str(i.author)] for i in results[:21]]
        if data:
            return JsonResponse(data, safe=False)


