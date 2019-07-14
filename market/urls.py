from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)