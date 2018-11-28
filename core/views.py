from django.shortcuts import render
from django.views import View
from matplotlib import pyplot as plt
import pandas as pd
from .forms import FileUploadForm
import mpld3


# Create your views here.

class FileUploadView(View):
    form_class = FileUploadForm
    template_name = 'core/file_upload.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request, *args, **kwargs):
        dataframe = pd.read_csv(request.FILES['file'])
        x = [2012,2015,2019]
        y = x
        fig = plt.figure()
        plt.plot(x, y)
        plt.axis([None, None, 2005, 2020])
        return render(request, 'core/plot.html', context={'plot': mpld3.fig_to_html(fig)})
