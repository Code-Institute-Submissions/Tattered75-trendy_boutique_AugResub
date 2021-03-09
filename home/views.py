from django.shortcuts import render

# Lesson code used

def index(request):


    return render(request, 'home/index.html')