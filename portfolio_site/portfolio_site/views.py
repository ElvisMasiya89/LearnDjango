from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home_view(request):
    return HttpResponse('HOME PAGE')

#Setting up Custom error page
def my_custom_page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
