from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'challenge/home.html')

def about(request):
    return render(request,'challenge/about.html')

def challenge(request):

    characters=list('abcdefghijklmnopqrstuvwxyz')

    if(request.GET.get('special')):
        characters.extend(list('!@#$%^&*()_-+=\/{[}],.`~'))

    if(request.GET.get('uppercase')):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if(request.GET.get('numbers')):
        characters.extend(list('1234567890'))

    thepassword=''

    length = int(request.GET.get('length',10))
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request,'challenge/challenge.html', {'password':thepassword})
