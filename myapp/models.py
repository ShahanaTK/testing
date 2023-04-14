from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=60)
    password=models.CharField(max_length=60)
    type=models.CharField(max_length=60)

class course(models.Model):
    course_name=models.CharField(max_length=60)
    description=models.CharField(max_length=60)

class subject(models.Model):
    course_id=models.ForeignKey(course,on_delete=models.CASCADE)
    sem=models.CharField(max_length=60)
    subject=models.CharField(max_length=60)
    th=models.IntegerField(default=0)
    ph=models.IntegerField(default=0)


class staff(models.Model):
    login_id=models.ForeignKey(login,on_delete=models.CASCADE)
    name=models.CharField(max_length=60)
    date_of_birth=models.DateField()
    qualification=models.CharField(max_length=60)
    experience=models.CharField(max_length=15)
    gender=models.CharField(max_length=60)
    place=models.CharField(max_length=60)
    post=models.CharField(max_length=60)
    pin=models.CharField(max_length=60)
    phone=models.CharField(max_length=60)
    email_id=models.CharField(max_length=90)

class allocate_subject(models.Model):
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(subject,on_delete=models.CASCADE)

class notification(models.Model):
    notifications=models.CharField(max_length=1200)
    date=models.DateField()

class complaint(models.Model):
    student_id=models.ForeignKey(login,on_delete=models.CASCADE)
    complaints=models.CharField(max_length=60)
    date=models.DateField()
    reply=models.CharField(max_length=60)

class student(models.Model):
    login_id=models.ForeignKey(login,on_delete=models.CASCADE)
    std_name=models.CharField(max_length=60)
    roll_no=models.CharField(max_length=60)
    DOB=models.DateField()
    gender=models.CharField(max_length=60)
    course_id=models.ForeignKey(course,on_delete=models.CASCADE)
    semester=models.CharField(max_length=60)
    stu_place=models.CharField(max_length=100)
    stu_post=models.CharField(max_length=100)
    stu_pin=models.CharField(max_length=60)
    stu_phone=models.CharField(max_length=60)
    stu_email=models.CharField(max_length=60)

class attendance(models.Model):
    student_id=models.ForeignKey(student,on_delete=models.CASCADE)
    std_attendance=models.CharField(max_length=60)
    att_date=models.DateField()
    att_time=models.TimeField()
    subj_id=models.ForeignKey(subject,on_delete=models.CASCADE)
