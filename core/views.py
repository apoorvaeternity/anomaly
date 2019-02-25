from django.shortcuts import render
from django.views import View
from matplotlib import pyplot as plt
from mpld3 import fig_to_html
import pandas as pd
from .forms import FileUploadForm
from .anomaly_detection_tools import moving_average
from math import fabs

# Create your views here.

class FileUploadView(View):
    form_class = FileUploadForm
    template_name = 'core/file_upload.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request, *args, **kwargs):
        threshold = 200
        state = 'HARYANA DELHI & CHANDIGARH'
        dataframe = pd.read_csv(request.FILES['file'])
        dataframe = dataframe.loc[dataframe['subdivision'] == state]
        fig = plt.figure()
        plt.xlabel('year')
        plt.ylabel('mm')
        mv_avg = moving_average(dataframe['annual'].tolist(), dataframe['year'].tolist())
        for x,y in zip(dataframe['year'].tolist(), dataframe['annual'].tolist()):
            if x in mv_avg and fabs(y-mv_avg[x])>threshold:
                plt.plot(x, y, 'r+')
            else:
                plt.plot(x, y, 'bx')


        return render(request, 'core/plot.html',
                      context={'plot': fig_to_html(fig), 'state': state})
