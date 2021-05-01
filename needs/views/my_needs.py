from django.shortcuts import render

# Create your views here.


def my_needs_view(request):
    return render(request, 'needs/my_needs.html')
