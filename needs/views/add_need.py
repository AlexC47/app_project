from django.views import View
from django.shortcuts import render, HttpResponse, Http404, redirect
from needs.models.needs import NeedTemplateModel, UserNeedModel
from django.contrib.auth import get_user_model
from django.urls import reverse

AuthUserModel = get_user_model()


class AddNeedToProfileView(View):
    def get(self, request, id):
        need_template = NeedTemplateModel.objects.get(id=id)
        user = request.user
        print(user.first_name)
        print(need_template.id)

        user_need, created = UserNeedModel.objects.get_or_create(user=user, need=need_template, is_active=True)
        user_need.save()
        #
        # return render(request, 'needs/add_user_need.html', {
        #     'need_template': need_template,
        #
        # })

        return redirect(reverse('needs:my_needs'))

    def post(self, request):
        pass
