from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm, UserForm, UserProfileForm, PageForm, Page
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


#created one view called index, each view takes in at least one argument(a HttpRequest object)
#index() function is responsible for the main page view
def about(request):
    return render(request, 'rango/about.html', {})
    
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

@login_required
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

@login_required
def add_page(request, category_name_slug):
    try :
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect('/rango/')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('rango:show_category', kwargs={'category_name_slug':category_name_slug}))
            
        else:
            print(form.errors)

    context_dict = {'form' : form, 'category' : category}
    return render(request, 'rango/add_page.html', context=context_dict)

def register(request):
    # code changes calue when registration suceeds, initially its set to false
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # if user provided profile pic, we need to get it from input form and put it in UserProfile model
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()
            #update variable that the registration was successful
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        #if its not a HTTP post
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'rango/register.html', context={'user_form': user_form,'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        #returns None if value DNE
        username = request.POST.get('username')
        password = request.POST.get('password')

        # if valid a user object is returned
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'rango/login.html')


@login_required
def restricted(request):
    return render(request, 'rango/restricted.html', {})

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:index'))







