from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    #1 conatact is show in url, 2nd view.contact show in views of the name, 3rd contact is match with thw header page name if not match then nothing show
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'), 
    path('login/',views.login,name='login'),
]