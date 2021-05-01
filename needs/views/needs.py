from django.shortcuts import render, HttpResponse, Http404
from django.views.generic import ListView
from needs.models.needs import Need


def needs_list(request):
    search_by_name = request.GET.get('name')

    if search_by_name:
        needs = Need.objects.filter(name__icontains=search_by_name).all()
    else:
        needs = Need.objects.all()

    return render(request, 'needs/list.html', {
        'needs_list': needs
    })