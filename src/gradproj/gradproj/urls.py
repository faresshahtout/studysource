"""gradproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from numpy.distutils.from_template import template_name_re
from students import views
from questions import views as sview
from django.conf import settings
from django.conf.urls.static import static
from gradproj.views import faq_view
from courses import views as cview





urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('sign-up/', views.register_request, name=''),
    path('sign-in/', views.login_request, name='',),
    path('tree/', sview.tree_view, name=''),
    path('faq/', faq_view, name=''),
    path('questions/', sview.questions_view, name=''),
    path("logout", views.logout_request, name= "logout"),
    path('c++/', cview.c_view, name=''),
    path('java1/', cview.java_view, name=''),
    path('ds/', cview.ds_view, name=''),
    path('vs/', cview.vs_view, name=''),
    path('swe/', cview.swe_view, name=''),
    path('java2/', cview.java2_view, name=''),
    path('web/', cview.web_view, name=''),
    path('db/', cview.database_view, name=''),
    path('multi/', cview.multi_view, name=''),
    path('algo/', cview.algo_view, name=''),
    path('datamining/', cview.DMining_view, name=''),
    path('ai/', cview.ai_view, name=''),
    path('secure/', cview.secure_view, name=''),
    path('analysis/', cview.analysis_view, name=''),
    path('disc/', cview.disc_view, name=''),
    path('theory/', cview.theory_view, name=''),
    path('logic/', cview.logic_view, name=''),
    path('os/', cview.os_view, name=''),
    path('org/', cview.org_view, name=''),
    path('arch/', cview.arch_view, name=''),
    path('network/', cview.network_view, name=''),
    path('para/', cview.para_view, name=''),
    path('wire/', cview.wire_view, name=''),
    path('cal1/', cview.calc1_view, name=''),
    path('cal2/', cview.calc2_view, name=''),
    path('phy1/', cview.phys1_view, name=''),
    path('phy2/', cview.phys2_view, name=''),
    path('nume/', cview.nume_view, name=''),
    path('statistics/', cview.statistics_view, name=''),

    ]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
