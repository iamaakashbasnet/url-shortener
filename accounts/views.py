from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AccountCreationForm, AccountUpdateForm


def signup(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! Now you can login.')
            return redirect('login')
    else:
        form = AccountCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def update_profile(request):
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Updated!')
            return redirect('dashboard')
    else:
        form = AccountUpdateForm(instance=request.user)

    return render(request, 'accounts/account_update.html', {'form': form})
