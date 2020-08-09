from django.shortcuts import render, request
from accounts.forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your account has been created successfully")
            return redirect ('login')
    else:
        form = UserRegisterForm()

    dict = {'form':form}
    return render(request, 'accounts/register.html')
