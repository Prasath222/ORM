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