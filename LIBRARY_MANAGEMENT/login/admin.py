from django.contrib import admin
from .models import *

#winpty python manage.py createsuperuser
# Register your models here.

# python manage.py createsuperuser //run this after writing the below code

admin.site.register(university)
admin.site.register(student)
admin.site.register(library)
admin.site.register(librarian)
admin.site.register(book)
admin.site.register(library_contains)
admin.site.register(student_borrowed)
admin.site.register(librarian_login)
admin.site.register(student_login)

