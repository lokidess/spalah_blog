"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from api.views import PostViewSet
from core.views import HomeView, AddNewPostView, Profile, FilterView
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^profile/', Profile.as_view(), name='profile'),
    url(r'^edit_post/(?P<pk>\d+)/', AddNewPostView.as_view(), name='edit_post'),
    url(r'^add_post/', AddNewPostView.as_view(), name='add_post'),
    url(r'^filter_form/', FilterView.as_view()),
    url(r'', include('django.contrib.auth.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/v1/', include(router.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
