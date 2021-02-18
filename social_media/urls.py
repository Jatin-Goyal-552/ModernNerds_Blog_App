"""social_media URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from social_media_app import views
from django.conf.urls.static import static
from social_media import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.showsignuppage,name='signup'),
    path('', views.home, name='home'),
    path('login/', views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    # path('about/',views.aboutpage,name='about'),
    path('newPost/',views.newPost,name='newPost'),
    path('post/',views.postpage,name='post'),
    path('myPost/',views.myPost,name='myPost'),
    path('delete/<post_id>',views.delete_post,name='delete'),
    path('edit/<post_id>',views.edit_post,name='edit'),
    path('like/<post_id>',views.like_post,name='like'),
 ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)