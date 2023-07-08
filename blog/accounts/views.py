from django.shortcuts import render,redirect
from django.contrib.auth import login,logout  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
               return redirect('blog:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })


def register(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             #  log the user in
             login(request, user)
             return redirect('blog:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', { 'form': form })


def logout_page(request):
    logout(request)
    return redirect("blog:index")