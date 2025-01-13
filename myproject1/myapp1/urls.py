from django.urls import path
from myapp1 import views
urlpatterns = [
    path('link/',views.click,name="link"),
    path('register/',views.stud_reg,name="register"),
    path('view',views.view,name="view"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('login',views.login,name='login'),
    path('upload_img',views.upload_img,name='upload_img'),
    path('image_view',views.image_view,name='image_view'),
    path('edit_img/<int:id>',views.edit_img,name='edit_img'),
    path('jquery_link',views.jquery_link,name='jquery_link'),
    path('dropdown_binding',views.dropdown_binding,name='dropdown_binding'),
    path('getstate',views.getstate,name="getstate"),
    path('getuser',views.getuser,name='getuser'),
    path('profile',views.profile,name="profile"),
    path('user_logout',views.user_logout,name="user_logout")

]

