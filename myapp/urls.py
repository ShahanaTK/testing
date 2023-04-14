"""mydjangosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.main,name='main'),
    # path('',views.index, name='index'),
    path('',views.main,name='main'),
    # path('login1',views.login1,name='login1'),
    path('manageStaff', views.manageStaff, name='manageStaff'),
    path('addStaff', views.addStaff, name='addStaff'),
    path('addStaff1', views.addStaff1, name='addStaff1'),

    path('editStaff/<int:id>', views.editStaff, name='editStaff'),
    path('editStaff1', views.editStaff1, name='editStaff1'),
    path('updateStaff', views.updateStaff, name='updateStaff'),
    path('deleteStaff/<int:id>', views.deleteStaff, name='deleteStaff'),

    path('manageCourse', views.manageCourse, name='manageCourse'),
    path('addcourse', views.addcourse, name='addcourse'),
    path('addcourse1', views.addcourse1, name='addcourse1'),
    path('edit_course/<int:id>', views.edit_course, name='edit_course'),
    path('editCourse_post', views.editCourse_post, name='editCourse_post'),
    path('deleteCourse/<int:id>', views.deleteCourse, name='deleteCourse'),
    path('manageSub',views.manageSub,name='manageSub'),
    path('addSub',views.addSub,name='addSub'),
    path('addSub1', views.addSub1, name='addSub1'),
    path('edit_sub/<int:id>',views.edit_sub,name='edit_sub'),
    path('editSub_post',views.editSub_post,name='editSub_post'),
    path('deleteSubject/<int:id>',views.deleteSubject,name='deleteSubject'),



    path('alloSub',views.alloSub,name='alloSub'),
    path('alloSub1', views.alloSub1, name='alloSub1'),
    path('delAllSub/<int:id>',views.delAllSub, name='delAllSub'),
    path('viewAllSub',views.viewAllSub,name='viewAllSub'),

    path('genNotifi',views.genNotifi,name='genNotifi'),
    path('genNotifi1',views.genNotifi1,name='genNotifi1'),


    path('login',views.login1,name='login'),
    path('adminhome',views.adminhome,name='adminhome'),

    path('staffHome',views.staffHome,name='staffHome'),

    path('manageStud',views.manageStud,name='manageStud'),
    path('addStud',views.addStud,name='addStud'),
    path('addStud1',views.addStud1,name='addStud1'),
    path('editStud/<int:id>',views.editStud,name='editStud'),
    path('editStud1',views.editStud1,name='editStud1'),
    path('deleteStud/<int:id>',views.deleteStud,name='deleteStud'),
    path('manageAtt',views.manageAtt,name='manageAtt'),
    path('manageAtt1',views.manageAtt1,name='manageAtt1'),
    path('addAtt',views.addAtt,name='addAtt'),
    path('addAtt1',views.addAtt1,name='addAtt1'),
    path('viewNotifi',views.viewNotifi,name='viewNotifi'),

    path('logout',views.logout,name='logout'),

]


urlpatterns +=staticfiles_urlpatterns()
