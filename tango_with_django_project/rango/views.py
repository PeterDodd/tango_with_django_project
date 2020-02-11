from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Dictionary to pass to the template engine as its context.
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Returns rendered response to send to client
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # Dictionary to pass to the template engine as its context.
    context_dict = {'boldmessage': 'This tutorial has been put together by Peter Dodd'}

    # Returns rendered response to send to client
    return render(request, 'rango/about.html', context=context_dict)

