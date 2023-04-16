from django.http import HttpResponse 

def index(request):
    s = ('''Navigation bar <br> <a href = "https://www.codewithharry.com/tutorial/python/"> Python code with Harry </a> <br>
     <a href = "https://www.codewithharry.com/videos/python-django-tutorials-hindi-11/> Django Code With Harry  </a> ''' )
    return HttpResponse(s)
def about(request):
    return HttpResponse('Hello Mumbai')