import urllib

from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Book
# from .forms import SearchForm


@require_http_methods(['GET', 'POST'])
def home(request):
    """
    Home page for iltr.
    """
    return render(request, 'home.html')


@require_http_methods(['GET', 'POST'])
def search(request):
    query = request.GET.get('query', '')
    return render(request, 'home.html')
    

# def search(request, query):
#     """
#     Auto complete function for book, author names.
#     """
#     if query:
#         query = urllib.parse.unquote(query)
#         results = Book.objects.filter(
#             Q(name__icontains=query) |
#             Q(author__first_name__icontains=query) |
#             Q(author__middle_name__icontains=query) |
#             Q(author__last_name__icontains=query) 
#         )
#         data = [[i.name, str(i.author)] for i in results[:21]]
#         if not data:
#             data = ['Couldn\'t find "{}".'.format(query)]
#         return JsonResponse(data, safe=False)
        
#     else:
#         return JsonResponse([], safe=False)

