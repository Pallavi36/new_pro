from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=20)
    year=models.CharField(max_length=30)
    book=models.CharField(max_length=30)
    dttime=models.DateTimeField(auto_now=False)
    
    def __str__(self) -> str:
        return self.name
class Book(models.Model):
    name=models.CharField(max_length=20)
    author=models.CharField(max_length=30)
    language=models.CharField(max_length=20)
    issuedby=models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.name 


