from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from.models import Resorts
from.models import Contactus
from.models import Signup
from.models import Addrooms
from.models import Bookroom
from.models import Adminregistration


# Create your views here.
def index(request):
 template = loader.get_template("index.html")
 return HttpResponse(template.render({},request))

def about(request):
 template = loader.get_template("about.html")
 return HttpResponse(template.render({},request))

def bookresorts(request):
  
 bookresort1=Resorts.objects.filter(cat_name = 'premium class')
 bookresort2=Resorts.objects.filter(cat_name = 'budget class')
 context={
   'bookresort1': bookresort1,
   'bookresort2': bookresort2,
 }
 template = loader.get_template("bookresorts.html")
 return HttpResponse(template.render(context,request))

def contactus(request):
    if request.method == 'POST':
            cname=request.POST['contact_name']
            cemail=request.POST['contact_email']
            cmessage=request.POST['contact_msg']
            con= Contactus(con_name=cname, con_email=cemail, con_message=cmessage)
            con.save()
    template=loader.get_template("contactus.html")
    return HttpResponse(template.render({},request))

def services(request):
    template = loader.get_template("service.html")
    return HttpResponse(template.render({},request))

def signup(request):
    if "user" in request.session:
        return HttpResponseRedirect("/account")
    if request.method == 'POST':
        rname=request.POST['reg_name']
        remail=request.POST['reg_email']
        rusername=request.POST['reg_username']
        rpassword=request.POST['reg_password']
        

        x= Signup(reg_name=rname,reg_email=remail,reg_username=rusername,reg_password=rpassword)
        x.save()

    template=loader.get_template("signup.html")
    return HttpResponse(template.render({},request))

def login(request):
    if "user" in request.session:
        return HttpResponseRedirect("/login")
    if request.method == 'POST':
        log_user= request.POST['log_username']
        log_pswd=request.POST['log_password']


        log = Signup.objects.filter(reg_username=log_user,reg_password=log_pswd)
        if log:
            request.session["user"]=log_user
            return HttpResponseRedirect("/bookresorts")
    template = loader.get_template("login.html")
    return HttpResponse(template.render({},request))

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return HttpResponseRedirect("/login")

def account(request):
    if "user" not in request.session:
        return HttpResponseRedirect("/login")
    
    template = loader.get_template("account.html")
    return HttpResponse(template.render({},request))

def viewbooking(request,id):
    if "user" not in request.session:
        return HttpResponseRedirect("/login")
    rooms = Addrooms.objects.filter(resort_name=id)
    context = {
        'rooms':rooms,   
        }
    template = loader.get_template("viewbooking.html")
    return HttpResponse(template.render(context,request))

def checkout(request,id):
    # if "user" not in request.session:
    #     return HttpResponseRedirect('/login')
    co=0
    adrs = dtype = ""

    if 'dlv_adrs' in request.POST:
        adrs = request.POST["dlv_adrs"]
        dtype = request.POST["dlv_type"]
        co = 1

    user= request.session["user"]

    olddel = Bookroom.objects.filter(book_user=user,order_status=0)
    olddel.delete()
    cart=Addrooms.objects.filter(id=id)
    for x in cart:
     odr = Bookroom(resort_name = x.resort_name,
                    room_name = x.room_name,
                    book_image = x.room_image,
                    book_price = x.room_price,
                    book_number=x.room_number,
                    book_status=x.room_status,
                    book_type=x.room_type,
                    book_description=x.room_description,
                    book_capacity=x.room_capacity,
                    book_user=request.session['user'],
                    # order_qty = x.cart_qty,
                    # order_amount = x.cart_amount,
                    book_adress = adrs,
                    payment_type = dtype,
                    order_status = 0
                    )
     odr.save()

    book=Bookroom.objects.filter(book_user=user,order_status=0).values()
    tot = 0
    for x in cart:
        tot += int(x.room_price)
    
    shp = tot*8/100
    gst = tot*18/100
    gtot = tot + shp + gst
    request.session['tot']=tot
    request.session['gst']=gst
    request.session['gtot']=gtot

    context={
        'book':book,
        'tot':tot,
        'gst':gst,
        'gtot':gtot,
        'co':co,
        'odr':odr,
        'cart':cart
    }

    
    

    template = loader.get_template("checkout.html")
    return HttpResponse(template.render(context,request))




# DASHBOARD


def dashboard(request):
 
 if 'admin' not in request.session:
       return HttpResponseRedirect("/adminlogin")
 template = loader.get_template("dashboard/dashboard.html")
 return HttpResponse(template.render({},request))

def addresort(request):
    

    if request.method == 'POST':
        brandname=request.POST['brand_name']
        resortname=request.POST['resort_name']
        place=request.POST['place_name']
        resortimage=request.FILES['resort_image']
        catname=request.POST['cat_name']
        

        resorts = Resorts(
            brand_name=brandname,resort_name=resortname,resort_image=resortimage,resort_place=place,cat_name=catname)
        resorts.save()
    resort = Resorts.objects.all().values()
    context= {
        'resort' : resort,
        }

    template = loader.get_template("dashboard/addresort.html")
    return HttpResponse(template.render(context,request))
 

def viewcontact(request):
    cons=Contactus.objects.all().values()
    context= {
        'viewcontact' : cons

    }
    # return HttpResponseRedirect("/viewcontact")
    template=loader.get_template("dashboard/viewcontact.html")
    return HttpResponse(template.render(context,request))

def viewsignup(request):
    viewreg=Signup.objects.all().values()
    context={
        'viewsignup' : viewreg
    }

    template=loader.get_template("dashboard/registrationadmin.html")
    return HttpResponse(template.render(context,request))

def viewregistration(request):
    regadmin=Signup.objects.all().values()
    context={
        'registrationadmin' : regadmin
    }

    template=loader.get_template("dashboard/viewregistration.html")
    return HttpResponse(template.render(context,request))

def adminlogin(request):

    if request.method == 'POST':
        username = request.POST['admin_user']
        password = request.POST['admin_password'] 
        adminlogin = Adminregistration.objects.filter( admin_user=username, admin_password=password)
        if adminlogin:  
            request.session['admin'] = username
            return HttpResponseRedirect("/dashboard")
    template = loader.get_template("dashboard/adminlogin.html")    
    return HttpResponse(template.render({},request))

def adminlogout(request):
    if "admin" in request.session:
        del request.session["admin"]
        return HttpResponseRedirect("/adminlogin")


def addrooms(request):
    if 'user' not in request.session:
        return HttpResponseRedirect("/login")
      
    room=Addrooms.objects.all().values()

    if request.method == 'POST':
        resortname=request.POST['resort_name']
        roomname=request.POST['roomname']
        roomimage=request.FILES['room_image']
        roomprice=request.POST['room_price']
        roomnumber=request.POST['room_number']
        roomstatus=request.POST['room_status']
        roomcapacity=request.POST['room_capacity']
        roomtype=request.POST['room']
        roomdescription=request.POST['room_description']
        
        
        room = Addrooms(
            resort_name=resortname,
            room_name=roomname,room_image=roomimage,room_price=roomprice,room_capacity=roomcapacity,room_type=roomtype,room_description=roomdescription)
        room.save()
    resortname = Resorts.objects.all()
    context= {
        'room' : room,
        "resort":resortname,
        "resort_room": room
        }

    template = loader.get_template("dashboard/addrooms.html")
    return HttpResponse(template.render(context,request))

def bookconfirmation(request):
    user = request.session ['user']
    if 'cancel' in request.GET:
        user= request.session["user"]
        olddel = Bookroom.objects.filter(book_user=user,order_status=1)
        olddel.delete()
        request.session['cancelmsg'] = 'cancel'
        # return HttpResponseRedirect('/bookconfirmation')
    else:
        if 'cancelmsg' in request.session:
            del request.session['cancelmsg']
        bookroom = Bookroom.objects.filter(book_user=user,order_status=0)
        for x in bookroom: 
            x.order_status=1
            x.save()

    template = loader.get_template("bookconfirmation.html")
    return HttpResponse(template.render({},request))

def cancelbooking(request):
    if 'user' in request.session:
        user= request.session["user"]
        olddel = Bookroom.objects.filter(book_user=user,order_status=1)
        olddel.delete()
        return HttpResponseRedirect('/bookresorts')



 
    