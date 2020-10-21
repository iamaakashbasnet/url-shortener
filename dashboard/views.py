from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.forms import UrlForm
from core.models import Link


@login_required
def dashboard(request):
    if request.method == "GET":
        form = UrlForm()
    else:
        form = None

    return render(request, 'dashboard/dashboard.html', context={
        "form": form,
        "all_url": Link.objects.filter(author=request.user).order_by('-pk'),
        "total_url": Link.objects.filter(author=request.user).count()
    })
