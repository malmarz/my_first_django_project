from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    print("Request:", dir(request))

    name = "mohammad"

    c = {}
    c["z"] = name
    c["age"] = 29

    return render(request, "test.html", c)