import json
from datetime import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.messages.storage import session
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
# def index(request):
#     return render(request, "myapp/index.html",{})


def main(request):

    return render(request,'login.html')

def login1(request):
    uname=request.POST['textfield']
    passwd=request.POST['textfield2']
    try:
        ob=login.objects.get(username=uname,password=passwd)
        if ob.type=="admin":
            request.session['lid']=ob.id
            ob1=auth.authenticate(username='admin',password='admin')
            if ob1 is not None:
                auth.login(request,ob1)
            return HttpResponse("<script>alert('ok');window.location='/adminhome'</script>")
        elif ob.type=="staff":
            request.session['lid'] = ob.id
            ob1 = auth.authenticate(username='admin',password='admin')
            if ob1 is not None:
                auth.login(request, ob1)
            return HttpResponse("<script>alert('ok');window.location='/staffHome'</script>")
        else:
            return HttpResponse("<script>alert('Invalid username or password');window.location='/'</script>")
    except:
        return HttpResponse("<script>alert('Invalid username or password');window.location='/'</script>")


# ADMIN

@login_required(login_url='/')
def adminhome(request):
    return render(request,'ADMIN/indexAdmin1.html')

@login_required(login_url='/')
def manageStaff(request):
    ob=staff.objects.all()
    return render(request,'ADMIN/MANAGE STAFF.html',{'val':ob})

@login_required(login_url='/')
def addStaff(request):
    return render(request,'ADMIN/ADD STAFF.html')

@login_required(login_url='/')
def addStaff1(request):
    name=request.POST['textfield']
    place=request.POST['textfield2']
    post=request.POST['textfield9']
    pin=request.POST['textfield11']
    dob=request.POST['textfield3']
    qualification=request.POST['textfield4']
    experience=request.POST['textfield5']
    phone_no=request.POST['textfield6']
    email=request.POST['textfield7']
    user_name=request.POST['textfield8']
    password=request.POST['textfield10']
    gender=request.POST['radiobutton']
    ob=login()
    ob.username=user_name
    ob.password=password
    ob.type='staff'
    ob.save()
    sob=staff()
    sob.login_id=ob
    sob.name=name
    sob.date_of_birth=dob
    sob.gender=gender
    sob.place=place
    sob.post=post
    sob.pin=pin
    sob.phone=phone_no
    sob.email_id=email
    sob.qualification=qualification
    sob.experience=experience
    sob.save()
    return HttpResponse("<script>alert('Registered');window.location='/manageStaff'</script>")

@login_required(login_url='/')
def editStaff(request,id):
    ob=staff.objects.get(login_id__id=id)
    request.session['sid']=id
    return render(request,'ADMIN/EDIT STAFF.html',{'val':ob})

@login_required(login_url='/')
def editStaff1(request):
    name=request.POST['textfield']
    place=request.POST['textfield2']
    post=request.POST['textfield9']
    pin=request.POST['textfield11']
    dob=request.POST['textfield3']
    qualification=request.POST['textfield4']
    experience=request.POST['textfield5']
    phone_no=request.POST['textfield6']
    email=request.POST['textfield7']
    user_name=request.POST['textfield8']
    password=request.POST['textfield10']
    gender=request.POST['radiobutton']
    ob=login()
    ob.username=user_name
    ob.password=password
    ob.type='staff'
    ob.save()
    sob=staff()
    sob.login_id=ob
    sob.name=name
    sob.date_of_birth=dob
    sob.gender=gender
    sob.place=place
    sob.post=post
    sob.pin=pin
    sob.phone=phone_no
    sob.email_id=email
    sob.qualification=qualification
    sob.experience=experience
    sob.save()
    return HttpResponse("<script>alert('Registered');window.location='/manageStaff'</script>")

@login_required(login_url='/')
def updateStaff(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield9']
    pin = request.POST['textfield11']
    dob = request.POST['textfield3']
    qualification = request.POST['textfield4']
    experience = request.POST['textfield5']
    phone_no = request.POST['textfield6']
    email = request.POST['textfield7']
    gender = request.POST['radiobutton']
    ob=staff.objects.get(login_id__id=request.session['sid'])
    ob.name=name
    ob.place=place
    ob.post=post
    ob.pin=pin
    ob.date_of_birth=dob
    ob.qualification = qualification
    ob.experience = experience
    ob.phone = phone_no
    ob.email_id = email
    ob.gender = gender
    ob.save()
    return HttpResponse("<script>alert('updated');window.location='/manageStaff'</script>")

@login_required(login_url='/')
def deleteStaff(request,id):
    ob=staff.objects.get(login_id__id=id)
    ob.delete()
    ob1=login.objects.get(id=id)
    ob1.delete()
    return HttpResponse("<script>alert('deleted');window.location='/manageStaff#about'</script>")

@login_required(login_url='/')
def manageCourse(request):
    ob=course.objects.all()
    return render(request,'ADMIN/MANAGE COURSE.html',{"val":ob})

@login_required(login_url='/')
def addcourse(request):
    return render(request,'ADMIN/ADD COURSE.html')

@login_required(login_url='/')
def addcourse1(request):
    crs=request.POST['textfield']
    description=request.POST['textfield2']
    cob=course()
    cob.course_name=crs
    cob.description=description
    cob.save()
    return HttpResponse('''<script>alert("your course added");window.location="/manageCourse"</script>''')

@login_required(login_url='/')
def edit_course(request,id):
    ob = course.objects.get(id=id)
    request.session['cid'] = id
    return render(request, 'ADMIN/EDIT COURSE.html', {'val': ob})

@login_required(login_url='/')
def editCourse_post(request):
    course1 = request.POST['textfield']
    des = request.POST['textfield2']
    ob = course.objects.get(id=request.session['cid'])
    ob.course_name = course1
    ob.description = des
    ob.save()
    return HttpResponse('''<script>alert("your course updated");window.location="/manageCourse"</script>''')


@login_required(login_url='/')
def deleteCourse(request,id):
    ob = course.objects.get(id=id)
    ob.delete()
    return HttpResponse("<script>alert('deleted');window.location='/manageCourse'</script>")

@login_required(login_url='/')
def edit_sub(request,id):
    ob = subject.objects.get(id=id)
    ob1 = course.objects.all()
    request.session['sid'] = id
    return render(request, 'ADMIN/EDIT SUB.html', {'val': ob,'val2':ob1})

@login_required(login_url='/')
def editSub_post(request):
    sem = request.POST['select2']
    sub = request.POST['textfield2']
    c = request.POST['select']
    p=request.POST['ph']
    t=request.POST['th']
    sbjob = subject(id=request.session['sid'])
    sbjob.course_id = course.objects.get(id=c)
    sbjob.sem = sem
    sbjob.subject = sub
    sbjob.ph=p
    sbjob.th=t
    sbjob.save()
    return HttpResponse('''<script>alert("your subject edited");window.location="/manageSub"</script>''')

@login_required(login_url='/')
def deleteSubject(request,id):
    ob = subject.objects.get(id=id)
    ob.delete()
    return HttpResponse("<script>alert('deleted');window.location='/manageSub'</script>")


@login_required(login_url='/')
def manageSub(request):
    ob=subject.objects.all()
    return render(request,'ADMIN/MANAGE SUB.html',{"val":ob})

@login_required(login_url='/')
def addSub(request):
    ob=course.objects.all()
    return render(request,'ADMIN/ADD SUB.html',{"val":ob})

@login_required(login_url='/')
def addSub1(request):
    sem=request.POST['select2']
    sub=request.POST['textfield2']
    c=request.POST['select']
    th=request.POST['th']
    ph=request.POST['ph']
    sbjob=subject()
    sbjob.course_id=course.objects.get(id=c)
    sbjob.th=th
    sbjob.sem=sem
    sbjob.ph=ph
    sbjob.subject=sub
    sbjob.save()
    return HttpResponse('''<script>alert("your subject added");window.location="/manageSub"</script>''')

@login_required(login_url='/')
def alloSub(request):
    ob=subject.objects.all()
    sob=staff.objects.all()
    aob=allocate_subject.objects.all()
    return render(request,'admin/alloc.html',{"val":ob,"val2":sob,"asub":aob})

@login_required(login_url='/')
def alloSub1(request):
    sub=request.POST['select']
    staf=request.POST['select2']
    ob=allocate_subject.objects.filter(subject_id__id=sub)
    if len(ob)==0:
        print(sub,staf,"=========================")
        aob=allocate_subject()
        aob.staff_id=staff.objects.get(login_id__id=staf)
        aob.subject_id=subject.objects.get(id=sub)
        aob.save()
        return HttpResponse('''<script>alert("your subject is allocated to staff");window.location="/alloSub"</script>''')
    else:
        return HttpResponse(
            '''<script>alert("already allocated to staff");window.location="/alloSub"</script>''')


def viewAllSub(request):
    ob=allocate_subject.objects.all()
    return render(request,'ADMIN/alloc.html',{"vl":ob})


@login_required(login_url='/')
def delAllSub(request,id):
    ob=allocate_subject.objects.get(id=id)
    ob.delete()

    return HttpResponse("<script>alert('deleted');window.location='/alloSub#about'</script>")


@login_required(login_url='/')
def genNotifi(request):
    return render(request,'ADMIN/SEND GEN NOTIF.html')

@login_required(login_url='/')
def genNotifi1(request):
    noti=request.POST['textfield']
    ob=notification()
    ob.notifications=noti
    ob.date=datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("your notification is send");window.location="/genNotifi"</script>''')

# STAFF

@login_required(login_url='/')
def staffHome(request):
    return render(request,'STAFF/indexStaff.html')

@login_required(login_url='/')
def manageStud(request):
    ob=student.objects.all()
    return render(request, 'STAFF/ManageStudent.html', {"val": ob})

@login_required(login_url='/')
def addStud(request):
    ob=course.objects.all()
    return render(request, 'STAFF/AddStudent.html',{"val": ob})


@login_required(login_url='/')
def addStud1(request):
    name=request.POST['textfield']
    r_No=request.POST['textfield5']
    DOB=request.POST['textfield12']
    gender=request.POST['radiobutton']
    semester=request.POST['select2']
    c=request.POST['select']
    place=request.POST['textfield2']
    post=request.POST['textfield3']
    pin=request.POST['textfield4']
    phone=request.POST['textfield7']
    email=request.POST['textfield8']
    username=request.POST['textfield9']
    password=request.POST['textfield10']
    ob = login()
    ob.username = username
    ob.password = password
    ob.type = 'student'
    ob.save()
    sob=student()
    sob.login_id = ob
    sob.std_name=name
    sob.roll_no=r_No
    sob.DOB=DOB
    sob.gender=gender
    sob.course_id=course.objects.get(id=c)
    sob.semester=semester
    sob.stu_place=place
    sob.stu_post=post
    sob.stu_pin=pin
    sob.stu_phone=phone
    sob.stu_email=email
    sob.save()
    return HttpResponse('''<script>alert("Student added");window.location="/manageStud"</script>''')

@login_required(login_url='/')
def editStud(request,id):
    ob=student.objects.get(login_id__id=id)
    request.session['sid']=id
    print(request.session['sid'])
    return render(request,'STAFF/Edit Student.html',{'val':ob})

@login_required(login_url='/')
def editStud1(request):
    name = request.POST['textfield']
    r_no=request.POST['textfield5']
    DOB = request.POST['textfield12']

    gender = request.POST['radiobutton']

    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    phone = request.POST['textfield7']
    email = request.POST['textfield8']


    sob = student.objects.get(login_id__id=request.session['sid'])
    sob.std_name = name
    sob.roll_no=r_no
    sob.DOB = DOB
    sob.gender = gender

    sob.stu_place = place
    sob.stu_post = post
    sob.stu_pin = pin
    sob.stu_phone = phone
    sob.stu_email = email
    sob.save()
    return HttpResponse('''<script>alert("Edited successfully");window.location="/manageStud"</script>''')

@login_required(login_url='/')
def deleteStud(request,id):
    ob=student.objects.get(login_id__id=id)
    ob.delete()
    ob1=login.objects.get(id=id)
    ob1.delete()
    return HttpResponse("<script>alert('deleted');window.location='/manageStud#about'</script>")


@login_required(login_url='/')
def manageAtt(request):
    ob=allocate_subject.objects.filter(staff_id__login_id__id=request.session['lid'])
    return render(request,'STAFF/MANAGE ATTE.html',{"val":ob})

@login_required(login_url='/')
def manageAtt1(request):
    sub = request.POST['select']
    crs = subject.objects.get(id=sub)
    date=request.POST['textfield']
    btn = request.POST['Submit']
    cid = crs.sem
    print(crs,sub,cid,"++++++++++++++++++++++++++")
    ob = student.objects.filter(semester=cid)
    print(ob,"==================================================")
    if btn == "SEARCH":
        ob = allocate_subject.objects.filter(staff_id__login_id__id=request.session['lid'])
        a = subject.objects.get(id=sub)
        b = student.objects.filter(semester=a.sem)

        print(b, "====")
        bb=attendance.objects.filter(subj_id__sem=a.sem,att_date=date,subj_id__id=sub)


        print(bb,"=========================",date)
        return render(request, 'STAFF/MANAGE ATTE.html', {"val": ob,"v": b,"vv":bb,"dt":date,'sid':int(sub)})
    else:
        stud = request.POST.getlist('checkbox')
        for i in stud:
            ob = attendance()

            ob.student_id = student.objects.get(id=i)
            ob.std_attendance = '1'
            ob.att_time=datetime.today()
            ob.att_date = datetime.today()
            ob.subj_id = subject.objects.get(id=sub)
            ob.save()
    return render(request,'STAFF/MANAGE ATTE.html',{'data':ob})

@login_required(login_url='/')
def addAtt(request):
    ob=allocate_subject.objects.filter(staff_id__login_id__id=request.session['lid'])
    return render(request,'STAFF/ADD ATTEND.html',{"val":ob})

@login_required(login_url='/')
def addAtt1(request):
    btn=request.POST['Submit']
    sub = request.POST['select2']
    if btn == "SEARCH":
        ob = allocate_subject.objects.filter(staff_id__login_id__id=request.session['lid'])
        a=subject.objects.get(id=sub)
        b=student.objects.filter(semester=a.sem)

        print(b,"====")
        return render(request, 'STAFF/ADD ATTEND.html', {"val": ob,"v":b,'sid':int(sub)})
    else:

        stud=request.POST.getlist('checkbox')
        print(stud,"+++++++++++++++++++")
        print(stud,"+++++++++++++++++++")
        print(stud,"+++++++++++++++++++")
        print(stud,"+++++++++++++++++++")
        print(stud,"+++++++++++++++++++")
        ob = allocate_subject.objects.filter(staff_id__login_id__id=request.session['lid'])
        a = subject.objects.get(id=sub)
        b = student.objects.filter(semester=a.sem)
        for i in b:
            ob=attendance()
            ob.student_id=student.objects.get(id=i.id)
            att=0
            if str(i.id) in stud:
                att=1


            ob.std_attendance=str(att)
            ob.att_date=datetime.today()
            ob.att_time=datetime.today()
            ob.subj_id=subject.objects.get(id=sub)
            ob.save()
        return HttpResponse('''<script>alert("added successfully");window.location="/manageAtt"</script>''')

@login_required(login_url='/')
def viewNotifi(request):
    ob=notification.objects.all()
    return render(request,'STAFF/VIEW NOTIFICATION.html',{"val":ob})




def logout(request):
    auth.logout(request)
    return HttpResponse('''<script>alert("logout");window.location="/"</script>''')


