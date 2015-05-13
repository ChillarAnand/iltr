import urllib

from django.shortcuts import render
from django.http import JsonResponse

from .models import Book


def home_view(request):
    """
    Home page for iltr.
    """
    return render(request, 'home.html')


def autocomplete(request, query):
    """
    Auto complete function for mesh tissues, diseases.
    """
    if query:
        print(query)
        query = urllib.parse.unquote(query)
        results = Book.objects.filter(name__icontains=query)[:10]
        data = [i.name for i in results]
        return JsonResponse(data, safe=False)
