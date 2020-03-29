# LIBRARY MANAGEMENT
## users - admin, Librarian, Students.
## each student is assigned to university.
## each university has multiple libraries.
## each student can access the books in the libraries of the university he is assigned to.
## he can borrow and return books.
## each librarian is assigned to a particular library.
## librarian can create new books, edit the number of copies of each book and delete books.
## librarian can see the outstanding fines of a student and total fines as a whole.
## student can see the books he has borrowed and its due dates and the total outstanding fine.

## psql -d database -u user -w @111

## https://www.postgresqltutorial.com/postgresql-cheat-sheet/
 
# https://docs.djangoproject.com/en/3.0/topics/forms/

# important postgresql syntax:
1. 	CREATE DATABASE [IF NOT EXISTS] library_management;
## creating required table 
1. CREATE TABLE university(
   id SERIAL PRIMARY KEY,
   name varchar(20) NOT NULL
);

# https://www.postgresqltutorial.com/postgresql-foreign-key/
2. CREATE TABLE student(
   id SERIAL PRIMARY KEY,
   name varchar(20) NOT NULL,
   univ_id integer NOT NULL references university(id),
   email_id varchar NULL
); 


3. CREATE TABLE library(
   id SERIAL PRIMARY KEY,
   name varchar(20) NOT NULL,
   university_id integer NULL references university(id)
); 

4. CREATE TABLE librarian(
   id SERIAL PRIMARY KEY ,
   name varchar(20) NOT NULL,
   library_id integer NULL references library(id)
); 


5. CREATE TABLE book(
   id SERIAL PRIMARY KEY,
   name varchar(20) NOT NULL
); 


6. CREATE  TABLE  library_contains(
   lib_id integer references library(id),
   book_id  integer NOT NULL references book(id),
   no_of_copies integer NULL
); 

7. CREATE  TABLE student_borrowed(
   student_id  integer references student(id),
   library_id integer references library(id),
   book_id integer references book(id),
   due_date date,
   returned boolean NULL
);

# https://x-team.com/blog/storing-secure-passwords-with-postgresql/
8. CREATE  TABLE librarian_login(
   library_id  integer references library(id),
   password TEXT NOT NULL
); 

9. CREATE TABLE student_login(
student_ud integer references student(id),
password TEXT NOT NULL
);

##university(id, name)
##students(id, name, univerisity_id, email_id)
##librarian(id, name, library_id)
##library(id, name, university_id)
##book(id, name)
##library_contains(library_id, book_id, no_of_copies)
##student_borrowed(student_id,library_id,book_id,due_date, returned)
##student_login(student_id, password)
##librarian_login(library_id,password)

## django tutorial
https://pythonprogramming.net/django-web-development-with-python-intro/
https://datacamp.com/community/tutorials/web-development-django

## creating an app
python manage.py startapp login

