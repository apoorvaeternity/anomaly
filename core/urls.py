from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import FileUploadView, MovingAveragePlotView, ARIMAPlotView

app_name = 'core'
urlpatterns = [
                  path('', FileUploadView.as_view(), name='file-upload'),
                  path('moving-average', MovingAveragePlotView.as_view(), name='moving-avg'),
                  path('arima', ARIMAPlotView.as_view(), name='arima')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
