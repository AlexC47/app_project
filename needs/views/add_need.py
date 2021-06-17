from django.views import View
from django.shortcuts import render, HttpResponse, Http404, redirect
from needs.models import NeedTemplateModel, UserNeedModel
from django.contrib.auth import get_user_model
from users.models import Statistics
from django.urls import reverse

AuthUserModel = get_user_model()


class AddNeedToProfileView(View):
    def get(self, request, id):
        need_template = NeedTemplateModel.objects.get(id=id)
        user = request.user

        user_need, created = UserNeedModel.objects.get_or_create(user=user, need=need_template, is_active=True)
        user_need.set_special
        user_need.save()
        stats, created = Statistics.objects.get_or_create(user=user)
        stats.save()

        for category in user_need.need.category.all():
            if category.name == "Acts of Service":
                stats.acts += 1
            elif category.name == "Physical Touch":
                stats.touch += 1
            elif category.name == "Receiving Gifts":
                stats.gifts += 1
            elif category.name == "Quality Time":
                stats.quality_time += 1
            elif category.name == "Words of Affirmation":
                stats.words += 1

        stats.save()

        return redirect(reverse('needs:my_needs'))

    def post(self, request):
        pass
