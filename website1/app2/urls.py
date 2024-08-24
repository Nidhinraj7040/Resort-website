from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('bookresorts',views.bookresorts,name='bookresorts'),
    path('contactus',views.contactus,name='contactus'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('account',views.account,name='account'),
    path('logout',views.logout,name='logout'),
    path('viewbooking/<int:id>',views.viewbooking,name='viewbooking'),
    path('checkout/<int:id>',views.checkout,name='checkout'),
    path('bookconfirmation',views.bookconfirmation,name='bookconfirmation'),
    path('cancelbooking',views.cancelbooking,name='cancelbooking'),



     # for admin page
    path('dashboard',views.dashboard,name='dashboard'),
    path('addresort',views.addresort,name='addresort'),
    path('viewcontact',views.viewcontact,name='viewcontact'),
    path('viewregistration',views.viewregistration,name='viewregistration'),
    path('addrooms',views.addrooms,name='addrooms'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)