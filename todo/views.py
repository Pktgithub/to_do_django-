from django.shortcuts import render,redirect
from django.contrib import messages 
from todo.models import signupdata




from .forms import TodoForm
from .models import Todolist





def index(request):

    item_list = Todolist.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)



def remove(request, item_id):
    item = Todolist.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')
def registration(request):
    return render(request,'registration.html')
def signup(request):
    a=signupdata()
    a.Name=request.GET['name']
    a.Email=request.GET['email']
    a.Password=request.GET['password']
    a.save()
    return render(request,'registration.html')
def login(request):
    return render(request,'login.html')
# def log(request):    
#     a=signupdata.objects.filter(Email=request.GET['email'],Password=request.GET['password'])
#     if a:
        
#         return render(request,'todo/index.html')
#     else:
#         return render(request,'login.html')
def log(request):
    # Check if user exists with the given email and password
    a = signupdata.objects.filter(Email=request.GET['email'], Password=request.GET['password'])
    
    if a:  # User exists
        user = a.first()  # Get the first user matching the query
        
        # Now use the same context that was in the 'index' function
        item_list = Todolist.objects.order_by("-date")  # Fetch the todo items
        form = TodoForm()  # Create the empty form for adding todos
        
        # Page context, which was used in the 'index' function
        page = {
            "forms": form,
            "list": item_list,
            "title": "TODO LIST",
            "user": user,  # You can pass the user to be displayed in the page
        }
        
        # Render the page with this context
        return render(request, 'todo/index.html', page)
    
    else:  # User not found
        # Return to login page with an error message
        messages.error(request, "Invalid email or password")
        return render(request, 'login.html')


# Create your views here.
