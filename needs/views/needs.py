from django.shortcuts import render, HttpResponseRedirect, Http404, redirect
from django.views.generic import ListView
from ..models.needs import NeedModel, NeedTemplateModel, UserNeedModel
from ..models.categories import CategoryModel
from ..models.tags import TagModel
from django.views import View
from ..forms.categories import CategoryForm
from ..forms.tags import TagForm
from ..forms.needs import NeedForm
from ..forms.needtemplate import NeedTemplateForm
from users.models import AuthUser
from django.urls import reverse


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
            'form': NeedTemplateForm
        })

    def post(self, request):
        form = NeedTemplateForm(request.POST)
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

        return redirect(reverse('needs:needs'))


class HelpNeedView(View):
    def get(self, request, id):
        need = UserNeedModel.objects.get(id=id)
        helper = request.user
        need.pending_list.add(helper)

        # return redirect('/')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class StopHelpView(View):
    def get(self, request, id):
        need = UserNeedModel.objects.get(id=id)
        helper = request.user
        need.pending_list.remove(helper)
        need.confirmed_with.remove(helper)

        # return redirect('/')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class ConfirmHelpView(View):
    def get(self, request, id1, id2):
        need = UserNeedModel.objects.get(id=id1)
        helper = AuthUser.objects.get(id=id2)
        need.confirmed_with.add(helper)
        need.pending_list.remove(helper)

        # return redirect('/')
        return redirect(reverse('needs:my_needs'))
