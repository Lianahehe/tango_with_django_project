from django.shortcuts import render
from django.http import HttpResponse
#6.2, importing required models, in this case we want Category
from rango.models import Category

#created one view called index, each view takes in at least one argument(a HttpRequest object)
#index() function is responsible for the main page view
def index(request):
    return HttpResponse("Rango says hey there partner!")

def index(request):
    # 6.2 : asked the database for a list of all categories currently stored then order it by number of likes in descending order, but we asked for top 5 only, or all if its less than 5. Then we place the list in our context_dict(w our bold message) n that'll be passed to the template engine 
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
     # Constructs a dict to pass to the template engine as its context
     # The key boldmessage matches to {{boldmessage}} in the template
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

     # Returns a rendered response to the client
     # We make use of the shortcut function to make our lives easier
     # Note : first param is template we wish to use
    return render(request, 'rango/index.html', context = context_dict)

