from django.shortcuts import render
from myapp.models import User
from myapp.forms import UserForm

# Create your views here.
def index(request):
    return render (request, 'myapp/index.html')

# def user(request):
#     my_user = User.objects.order_by('first_name')
#     names = {'user_names': my_user}
#     return render(request, 'myapp/users.html', context=names)

def userform (request):
    form = UserForm()
    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            # return index(request)
        else:
            print("error")
    return render(request,'myapp/forms.html',{'form': form})
