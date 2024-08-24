from django.db import models

# Create your models here.

class Contactus(models.Model):
    con_name=models.CharField(max_length=255)
    con_email=models.CharField(max_length=255)
    con_message=models.TextField()

    def __str__(self):
        return self.con_name
    
class Resorts(models.Model):
 brand_name=models.CharField(max_length=255)
 resort_name=models.CharField(max_length=255)
 resort_image=models.FileField(null=True,upload_to="products")
 resort_place=models.CharField(max_length=255)
 resort_rooms=models.CharField(max_length=255,default="0")
 resort_type=models.CharField(max_length=255,null=True)
 cat_name=models.CharField(max_length=255,null=True)
    
 def __str__(self):
    return self.resort_name
 
class Signup(models.Model):
   reg_name=models.CharField(max_length=255)
   reg_email=models.CharField(max_length=255)
   reg_username=models.CharField(null=True,max_length=255)
   reg_password=models.CharField(null=True,max_length=255)

class Addrooms(models.Model):
   resort_name=models.CharField(max_length=255,default="resort name")
   room_name=models.CharField(max_length=255,default='premium')
   room_image=models.FileField(null=True,upload_to="media")
   room_price=models.CharField(max_length=255,default="1") 
   room_number=models.CharField(max_length=255,default="1")
   room_status=models.CharField(max_length=255,default="available")
   room_capacity=models.CharField(max_length=255,default="1")
   room_type=models.CharField(max_length=255,default="non ac")
   room_description=models.CharField(max_length=255,default="no disc")

class Bookroom(models.Model):

   resort_name=models.CharField(max_length=255)
   room_name=models.CharField(max_length=255)
   book_image=models.FileField(null=True)
   book_price=models.CharField(max_length=255) 
   book_number=models.CharField(max_length=255)
   book_status=models.CharField(max_length=255)
   book_capacity=models.CharField(max_length=255)
   book_type=models.CharField(max_length=255)
   book_description=models.CharField(max_length=255)
   book_user=models.CharField(max_length=255)
   book_adress=models.CharField(max_length=255)
   payment_type=models.CharField(null=True,max_length=255)
   order_status=models.IntegerField(default=0,null=True)
   
class Adminregistration(models.Model):
   admin_user=models.CharField(max_length=255)
   admin_password=models.CharField(max_length=255)

   def __str__(self):
      return self.admin_user
