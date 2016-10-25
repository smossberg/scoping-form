from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def index(request):
    return HttpResponse('<iframe width="560" height="315" src="https://www.youtube.com/embed/IAooXLAPoBQ?list=RDIAooXLAPoBQ" frameborder="0" allowfullscreen></iframe>')
