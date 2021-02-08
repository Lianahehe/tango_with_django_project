from rango.models import Page
from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from django.shortcuts import redirect

#created one view called index, each view takes in at least one argument(a HttpRequest object)
#index() function is responsible for the main page view
def about(request):
    return render(request, 'rango/about.html')
    
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}

    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list

     # Returns a rendered response to the client
     # We make use of the shortcut function to make our lives easier
     # Note : first param is template we wish to use
    return render(request, 'rango/index.html', context = context_dict  )

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

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            # it saves the new category to database
            form.save(commit=True)
            return redirect('/rango/')

        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form' : form})
            



