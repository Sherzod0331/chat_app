from django.db import models

# Create your models here.
    
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/teacher/')
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    
    def __str__(self) -> str:
        return self.full_name
    
class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    student = models.ManyToManyField(Student)
    
    def __str__(self) -> str:
        return self.name

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/teacher/')
    group = models.ManyToManyField(Group)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    
    def __str__(self) -> str:
        return self.full_name
    
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self) -> str:
        return self.sender
    
class role(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
    
    
class login_required(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    role = models.ManyToManyField(role, blank=True)
    
    def __str__(self) -> str:
        return self.username