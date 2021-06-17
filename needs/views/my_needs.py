from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()

# Create your views here.


def my_needs_view(request):
    user_needs = request.user.needs.all
    return render(request, 'needs/my_needs.html', {
           'user_needs': user_needs,
    })


class RemoveNeedView(View):
    def get(self, request, id):
        need = request.user.needs.filter(id=id)
        need.delete()

        return redirect(reverse('needs:my_needs'))