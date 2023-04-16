from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

    # return HttpResponse('''home <br> <button> <a href = 'http://127.0.0.1:8000/about'> About </a> </button>  <br> <br> <br>
    #                     <button> <a href = 'http://127.0.0.1:8000/contact'> Contact </a> </button> <br> <br> <br>
    #                     <button> <a href = 'http://127.0.0.1:8000/services'> Servies </a> </button> ''')

def about(request):
    # get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    #Analyze the text
    return HttpResponse("about <br> <button> <a href = 'http://127.0.0.1:8000'> Home </a> </button>")

def contact(request):
    return HttpResponse("contact <br> <button> <a href = 'http://127.0.0.1:8000'> Home </a> </button>")

def services(request):
    return HttpResponse("services <br> <button> <a href = 'http://127.0.0.1:8000'> Home </a> </button>")