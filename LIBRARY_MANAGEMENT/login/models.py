##https://docs.djangoproject.com/en/3.0/topics/db/models/


# ./manage.py makemigrations login //run this after writing in models.py
# python manage.py makemigrations //not working, use above line instead
# python manage.py migrate
# python manage.py runserver  //to run the server

from django.db import models

class university(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 20)
    

class student(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 20)
    univ_id = models.ForeignKey(university, on_delete=models.CASCADE)
    email_id = models.CharField(max_length = 20)
    

class library(models.Model):
     id = models.IntegerField(primary_key = True)
     name = models.CharField(max_length = 20)
     univ_id = models.ForeignKey(university, on_delete=models.CASCADE)

class librarian(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=100)
    librarian_id = models.ForeignKey(library, on_delete=models.CASCADE)
    
class book(models.Model):
    
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=100)

class library_contains(models.Model):
    
    lib_id = models.ForeignKey(library, on_delete=models.CASCADE)
    book_id = models.ForeignKey(book, on_delete=models.CASCADE)
    no_of_copies = models.IntegerField()


class student_borrowed(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    library_id = models.ForeignKey(library, on_delete=models.CASCADE)
    book_id = models.ForeignKey(book, on_delete=models.CASCADE)
    due_date = models.DateField()
    returned = models.BooleanField()



class librarian_login(models.Model):
    
    library_id = models.ForeignKey(library, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)


class student_login(models.Model):
    
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)

