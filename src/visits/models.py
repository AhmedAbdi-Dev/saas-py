from django.db import models

# Create your models here.
class PageVisit(models.Model):
    #this maps to a database table
    #id column is auto generated and hidden, dont need to declare
    path = models.TextField(blank=True, null=True) # is a column in the db
    timestamp = models.DateTimeField(auto_now_add=True)
    