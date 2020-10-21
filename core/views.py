from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from . import models
from .forms import UrlForm
# Create your views here.


def create_url(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.author = request.user
            link.save()

    return redirect("dashboard")


def url_redirect(request, url):
    return redirect(get_object_or_404(models.Link, short_url=url).url)


def delete_url(request, pk):
    models.Link.objects.get(pk=pk).delete()

    return redirect('dashboard')
