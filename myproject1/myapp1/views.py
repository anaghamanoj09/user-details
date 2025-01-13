from django.shortcuts import render,redirect
from.models import *
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def page(request):
    return render(request,'page.html')

def click(request):
    return render(request,'link.html')

def index(request):
    return render(request,'page.html')

def stud_reg(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        place=request.POST['place']
        address=request.POST['address']
        phone=request.POST['number']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        user=register(name=name,gender=gender,place=place,address=address,phone=phone,email=email,username=username,password=password)
        user.save()
        messages.add_message(request,messages.INFO,"REGISTRATION SUCCESSFUL")
        return redirect(page)

        
    return render(request,'register.html')

def view(request):
    user=register.objects.all()
    return render(request,'viewuser.html',{'us':user})

def edit(request,id):
    if request.method=="POST":
        
        name=request.POST['name']
        gender=request.POST['gender']
        address=request.POST['address']
        place=request.POST['place']
        phone=request.POST['number']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        register.objects.filter(id=id).update(name=name,gender=gender,address=address,place=place,phone=phone,email=email,username=username,password=password)
        return redirect(view)
    data=register.objects.filter(id=id)
    return render(request,'edituser.html',{'da':data})

def delete(request,id):
    register.objects.filter(id=id).delete()
    messages.add_message(request,messages.INFO,"deleted successfull")
    return redirect(view)

def login(request):
    if request.method=='POST':
        user=request.POST['username']
        password=request.POST['password']
        data=register.objects.filter(username=user,password=password)
        if(data.count()>0):
            request.session['userid']=data[0].id
            messages.add_message(request,messages.INFO,"Login successfull")
            return render(request,'userhome.html')
        else:
            messages.add_message(request,messages.INFO,'Login failed')
            return redirect(page)
    return render(request,'login.html')
    

def upload_img(request):
    if request.method=='POST':
        if len(request.FILES)>0:
            images=request.FILES['image']
            data=image(photo=images)
            data.save()
            return render(request,'image.html')
        return render(request,'image.html')
    return render(request,'image.html')


def image_view(request):
    data=image.objects.all()
    return render(request,'image_view.html',{'da':data})

def edit_img(request,id):
    if request.method=='POST':
        photo=request.FILES['image']
        image.objects.filter(id=id).update(photo=photo)
        return redirect(image_view)
    data=image.objects.filter(id=id)
    return render(request,'edit_img.html',{'da':data})

def jquery_link(request):
    return render(request,'my.html')

def dropdown_binding(request):
    data=country_tb.objects.all()
    return render(request,'dropdown.html',{'da':data})

def getstate(request):
    id=request.GET['id']
    data=state.objects.filter(cid=id)
    return render(request,'state.html',{'st':data})

def getuser(request):
    user=request.GET['name']
    data=register.objects.filter(username=user)
    if len(data)>0:
        msg="exist"
    else:
        msg="not exist"
    print(msg)
    return JsonResponse({'valid':msg})

    
def profile(request):
    id= request.session['userid']
    user=register.objects.filter(id=id)
    return render(request,'viewuser.html',{'us':user})

def user_logout(request):
    request.session.clear()
    return redirect(login)