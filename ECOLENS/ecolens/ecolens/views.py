from django.shortcuts import render

# Create your views here.


def home_view(request):
    context = {
        "title": "home",
    }
    return render(request, "home.html", context)


def about_view(request):
    context = {
        "title": "about",
    }
    return render(request, "about.html", context)
