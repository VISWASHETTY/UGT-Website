"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from contact import views

# urlpatterns = [
#     path('', views.contact_view, name='contact'),
#     path('thank-you/', views.thank_you_view, name='thank_you'),
# ]

# Step 7: Include the app's URLs in the main project's urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin

from django.urls import path
from contact import views

from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls.static import static



from django.conf import settings
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('quote/', views.quote_request_view, name='quote'),
    path('ourteam/', views.ourteam, name='ourteam'),
    path('career/', views.career, name='career'),
    
    path('admin/', admin.site.urls),
    path('contact/',views.contact_view, name='contact_view'),  # Include the contact app URLs
    path('contact-list/', views.contact_list, name='contact_list'),  # Add this line
    path('thank-you/', views.thank_you_view, name='thank_you'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
