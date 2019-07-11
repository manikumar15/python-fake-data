
from django.contrib import admin
from django.conf.urls import url
from fakeapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',views.insertingdata),
    url(r'^$',views.fetchingdata)

]
