from django.shortcuts import render, HttpResponse, Http404, redirect
from django.views.generic import ListView
from needs.models.needs import NeedModel, NeedTemplateModel
from needs.models.categories import CategoryModel
from needs.models.tags import TagModel
from django.views import View
from needs.forms.categories import CategoryForm
from needs.forms.tags import TagForm
from needs.forms.needs import NeedForm


def needs_list(request):
    search_by_name = request.GET.get('name')

    if search_by_name:
        needs = NeedModel.objects.filter(name__icontains=search_by_name).all()
    else:
        needs = NeedModel.objects.all()

    return render(request, 'needs/needs_list.html', {
        'needs_list': needs
    })


class NeedTemplateView(View):
    def get(self, request):
        need_templates = NeedTemplateModel.objects.all

        return render(request, 'needs/needs_list.html', {
            'need_templates': need_templates,
            # 'form': NeedTemplateForm
        })

    def post(self, request):
        form = CategoryForm(request.POST)
        form.save()

        return redirect('/needs/list/')


class CategoryView(View):
    def get(self, request):
        categories = CategoryModel.objects.all

        return render(request, 'needs/categories.html', {
            'categories': categories,
            'form': CategoryForm
        })

    def post(self, request):
        form = CategoryForm(request.POST)
        form.save()

        return redirect('/needs/categories/')


class TagView(View):
    def get(self, request):
        tags = TagModel.objects.all

        return render(request, 'needs/tags.html', {
            'tags': tags,
            'form': TagForm
        })

    def post(self, request):
        form = TagForm(request.POST)
        form.save()

        return redirect('/needs/tags/')


class NeedView(View):
    def get(self, request):
        needs = NeedModel.objects.all

        return render(request, 'needs/needs.html', {
            'needs': needs,
            'form': NeedForm
        })

    def post(self, request):
        form = NeedForm(request.POST)
        form.save()

        return redirect('/needs/needs/')
