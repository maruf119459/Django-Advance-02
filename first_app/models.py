from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()
    
    def __str__(self):
        return f"Name : {self.name}"

# Module inheritance
# 1. abstract base class
# 2. multitable inheritance : 
# 3. proxy model

# 1. abstract base class: sob gulo object class abstract class niye toiri hobe kintu abstract class er kono object toiri hobe na


# 1. abstract base class

class CommonInfoClass(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    class Meta:
        abstract = True

class StudentInfoModel(CommonInfoClass):
    roll = models.IntegerField()
    payment = models.IntegerField()
    section = models.CharField(max_length=20)
    
class TeacherInfoModel(CommonInfoClass):
    salary = models.IntegerField()


# 2. multitable inheritance 
# 2. multitable inheritance : multitable inheritance ek dhoroner abstract class tobe multitable inheritance classke object hisabe use kora jay.jekhane abstract class ke object hisabe use kora jay na

class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    designation = models.CharField(max_length=20)

class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()

# 3. proxy model : x model er proxy model jodi y hoy tahole x model er ja ja boisisto ache sei sob boisisto y model pabe.

class Friend(models.Model): # amar friend class e present ache
    school = models.CharField(max_length=40)
    section = models.CharField(max_length=10)
    attendence = models.BooleanField()
    hw = models.CharField(max_length=50)
    
class Me(Friend): # ami ajke class e jai nai
    class Meta:
        proxy = True
        ordering = ['id']

# 1. one to one relationship
class Person(models.Model):
    name = models.CharField(max_length = 30)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    def __str__(self):  ## ei ta likhar madhome admin site object likhake over write kore person er name dekhay
        return self.name

class Passport(models.Model):
    user = models.OneToOneField(to=Person, on_delete = models.CASCADE)  # on_delete = models.CASCADE dile person delete korle passport o delet hpye jabe
    pass_number = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()    
    

# 2. one to many relationships
class Post(models.Model):
    user = models.ForeignKey(Person, on_delete=models.SET_NULL, null = True)
    post_cap = models.CharField(max_length=30)
    post_details = models.CharField(max_length=100)
    
# 3. Many to many relationships
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    student = models.ManyToManyField(Student, related_name='teachers')
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    def student_list(self):
        return ",".join([str(i) for i in self.student.all()])
