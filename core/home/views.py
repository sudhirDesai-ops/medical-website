from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
# Create your views here.

def rasik(request):
    return render(request,'index.html')

def sudhir(request):
    return HttpResponse("Hello Sudhir")

# def login(request):
#     if request.method=="POST":
#         email=request.POST.get('email')
#         password=request.POST.get('password')

#         print(email)
#         print(password)

#         Login.objects.create(
#             email=email,
#             password=password
#         )
#     sudhir=Login.objects.all()
#     context={'rasik':sudhir}
#     return render(request,"login.html", context)



   
def Login(request):
    if request.method=="POST": 
        email=request.POST.get('email')
        password=request.POST.get('password')


        print(email)
        print(password)

        login.objects.create(
            email=email,
            password=password
        )

    akshay=login.objects.all()       
    context={'sudhir':akshay}  
    return render(request,"login.html", context)

def delete(request, id):
    demo=login.objects.get(id=id)
    demo.delete()
    return redirect('/loginpage/')




def account(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        print(email)
        print(password)
    return render(request,'loginpage.html')




def Login2(request):
    if request.method=="POST": 
        email=request.POST.get('email')
        password=request.POST.get('password')


        print(email)
        print(password)

        login2.objects.create(
            email=email,
            password=password
        )

    akshay2=login2.objects.all()       
    context={'rasik':akshay2}  
    return render(request,"login2.html", context)


def sdesai(request, id):
    demo2=login2.objects.get(id=id)
    demo2.delete()
    return redirect('/loginpage2/')

#Update Karva Mate
def update(request,id):
    hello=login2.objects.get(id=id)
    if request.method=="POST": 
        email=request.POST.get('email')
        password=request.POST.get('password')


        hello.email=email
        hello.password=password

        hello.save()
        return redirect('/loginpage2/')
    hello=login2.objects.all()
    context={'rasik':hello}
    return render(request,"login2.html", context)










# def register(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         confirmpassword = request.POST.get("confirmpassword")

#         if email and password and confirmpassword:
#             email = User.objects.create(
#                 email=email,
#                 password=password,
#                 confirmpassword=confirmpassword
#             )
#             email.set_password(password)
#             email.save()

#             return redirect("/logintemplete2/")
#         else:
#             context = {"error": "All Fields Are Required."}
#             return render(request, 'logintemplete2.html', context)

#     return render(request, 'logintemplete2.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            email = User.objects.create(
                username=username,
                password=password
               
            )
            email.set_password(password)
            email.save()

            return redirect("/logintemplete2/")
        else:
            context = {"error": "All Fields Are Required."}
            return render(request, 'logintemplete2.html', context)

    return render(request, 'logintemplete2.html')


def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')


        email = User.objects.filter(username=username).first()
        if email:
            pwd = check_password(password,email.password)
            if pwd:
                return redirect('/loginpage2/')
            else:
                return render(request,'logintemplete1.html',{'errorMsg:Invalid Password'})
        else:
            return render(request,'logintemplete1.html',{'errorMsg':'Invalid Login'})
    return render(request, 'logintemplete1.html')
# def signup(request):
#     if request.method=='POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')


#         email = User.objects.filter(email=email).first()
#         if email:
#             pwd = check_password(password,email.password)
#             if pwd:
#                 return redirect('/loginpage2/')
#             else:
#                 return render(request,'logintemplete1.html',{'errorMsg:Invalid Password'})
#         else:
#             return render(request,'logintemplete1.html',{'errorMsg':'Invalid Login'})
#     return render(request, 'logintemplete1.html')

def master(request):
    return render(request,'master.html')

def website(request):
    return render(request,'website.html')