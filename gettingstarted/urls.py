from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
import login.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("jobs/", hello.views.jobs, name="jobs"),
    path("add/", hello.views.add, name="add"),
    path("db/", hello.views.db, name="db"),
    path("signup/", login.views.registerPage, name="signup"),
    path("login/", login.views.loginPage, name="login"),
    path('logout/', login.views.logoutPage, name="logout"),
    path("bienvenida/", login.views.welcomePage, name="welcome"),
    path("admin/", admin.site.urls),
]
