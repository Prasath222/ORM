# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Screenshot 2024-11-14 135945.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
modles.py
from django.db import models
from django.contrib import admin
class BankLoan (models.Model):
    loan_id = models.IntegerField(primary_key=True)
    loan_type = models.CharField(max_length=10)
    loan_amt = models.FloatField()
    cust_acno = models.IntegerField()
    cust_name =  models.CharField(max_length=50)

class BankAdmin(admin.ModelAdmin):
        list_display = ('loan_id','loan_type','loan_amt','cust_acno','cust_name')

        admin.py
        from django.contrib import admin
from .models import BankLoan,BankAdmin
admin.site.register(BankLoan,BankAdmin)

```



## OUTPUT

![alt text](<Screenshot 2024-11-14 133642.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
