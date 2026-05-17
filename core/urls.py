from django.contrib import admin
from django.urls import path, include
from accounts.views import MeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/me/', MeView.as_view(), name='me'),
    path('api/', include('journal.urls')),
]
