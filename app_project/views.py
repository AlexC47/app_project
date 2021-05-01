from django.http import HttpResponse
from django.shortcuts import render


def homepage_view(request):
    return render(request, 'homepage.html', {
        'brand': 'friend',
        'motto': 'wanna help out ?',
        'need_list': [{
            'name': 'pizza',
            'tag': 'hunger'
        },{
            'name': 'hugs',
            'tag': 'touch'
        }]
    })


def contact_view(request):
    return render(request, 'contact.html')
