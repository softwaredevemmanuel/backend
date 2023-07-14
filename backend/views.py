from django.shortcuts import redirect, render


def index(request):
    return render(request, "index.html", context={
        "title": "From The backend"
    })