from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import FileUploadView

urlpatterns = [
    path('', FileUploadView.as_view(), name='file-upload')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

