from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, Thank you for joining us!')
            return redirect("login")
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(request, "service/register.htm", context)
