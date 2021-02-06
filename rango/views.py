from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

#created one view called index, each view takes in at least one argument(a HttpRequest object)
#index() function is responsible for the main page view
def about(request):
    return render(request, 'rango/about.html')
    
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

# added new view (chap 6.3)
def show_category(request, category_name_slug):
    # create a context dictionary which we can pass to template rendering machine
    context_dict = {}

    try :
        # tries to see if we can find a category name slug with the given name, if cant, the .get() method raises an exception
        #The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)

        # retrieve all the associated pages, filter() will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)

        #adds our results list to template context under name pages
        context_dict['pages'] = pages
        #add category object from database to context dict. gonna use this in template to verify that the category exists
        context_dict['category'] = category

    except Category.DoesNotExist:
        #this runs if we cudnt find specified category
        # template will display 'no category message' for us
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)

    def about(request):
        return render(request, 'rango/about.html')


