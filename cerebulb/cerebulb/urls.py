"""cerebulb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.conf.urls.static import static
from  django.conf import settings

admin.site.site_header = 'CEREBULB'
admin.site.site_title = "CEREBULB"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/docs/', include_docs_urls(title=admin.site.site_header, permission_classes=[AllowAny])),
    path('', include('accounts.urls')),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)