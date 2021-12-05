from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    print("Request:", dir(request))

    name = request.GET.get("username")    #["username"]
    y = "Accounting"

    c = {}
    c["name"] = name
    c["age"] = 29
    c["major"] = "Finance"
    c["majors"] = [
        "MIS",
        "Finance",
        "ORM",
        "Marketing",
        "MAnagement",
        "Economics",
        "Public Admin",
        "Accounting",
    ]

    return render(request, "test.html", c)

def greet_view(request, u=None, a=None):

    # Same as below 
    # p = {}
    # p["username"] = u

    p = {
         "username":u,
         "age":a,
    }

    return render(request, "greet2.html", p)
