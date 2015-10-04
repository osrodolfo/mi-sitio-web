from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.sitio.urls)),
    url(r'', include('blog.urls')),
]
