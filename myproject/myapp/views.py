from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    print("Request:", dir(request))

    name = "mohammad"

    return HttpResponse(f"""
    <HTML>
        <head></head>
        <body>
            <h1>Hello { name } </h1>
            <h2>This is our</h2> first HTML page
        </body>
    </HTML>
    """)