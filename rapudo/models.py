from django.db import models

from django .db import models

class Product(models.Model):
    product_name = models.CharField(max_length=50,null=False,blank=False)
    product_price =models.DecimalField(max_digits=10,decimal_places=2)
    product_description = models.TextField(null=False,blank=False)
    product_image = models.ImageField(upload_to='products/',null=True,blank=True)
    
    def __str__(self):
        return self.product_name



class Teacher(models.Model):
    product_name = models.CharField(max_length=50,null=False,blank=False)
    product_price =models.DecimalField(max_digits=10,decimal_places=2)
    product_description = models.TextField(null=False,blank=False)

    def __str__(self):
        return self.product_name
    

    

    
 

