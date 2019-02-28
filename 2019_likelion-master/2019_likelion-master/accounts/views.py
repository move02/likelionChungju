from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        email = request.POST['user_email']
        user = User.objects.get(email=email)
        password = request.POST['user_password']
        user = auth.authenticate(request, username=user.username, password=password)
           
        if user is not None: #있는 회원
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('/account/signup') # 없는 회원 - 회원가입창으로 
    else:
        return render(request,'login.html') # 제출 아닐땐 - 기본 폼 띄워줌

def signup(request):
    if request.method == 'POST':
        if request.POST['user_password'] == request.POST['user_confirm']:
            user = User.objects.create_user(
                username=request.POST['user_name'], email=request.POST['user_email'], password=request.POST['user_password'])
            return redirect('/')
    return render(request,'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    return redirect('/')