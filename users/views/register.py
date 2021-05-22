from django.views import View
from users.forms.register import RegisterForm
from django.shortcuts import render, redirect, reverse


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {
            'form': form
        })

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect(reverse('users:account:login'))

        else:
            return render(request, 'users/register.html', {
                'form': form
            })
