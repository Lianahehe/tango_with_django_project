from django.shortcuts import render

from django.http import HttpResponse
#created one view called index, each view takes in at least one argument(a HttpRequest object)
def index(request):
    return HttpResponse("Rango says hey there partner!")

def index(request):
     # Constructs a dict to pass to the template engine as its context
     # The key boldmessage matches to {{boldmessage}} in the template
    context_dict = {'boldmessage' : 'Crunchy, creamy, cookie, candy, cupcake!'}

     # Returns a rendered response to the client
     # We make use of the shortcut function to make our lives easier
     # Note : first param is template we wish to use
    return render(request, 'rango/index.html', context = context_dict)

