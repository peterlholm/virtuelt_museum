from django.shortcuts import render

# Create your views here.


def index(request):               # pylint: disable=unused-variable
    "Start museeumside"
    return render(request, 'mus/index.html')
