from django.contrib import admin
from django.urls import path, include
from accounts.views import MeView
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({"message": "Bem-vindo à API do Journal!", "status": "online"})

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/me/', MeView.as_view(), name='me'),
    path('api/', include('journal.urls')),
]
