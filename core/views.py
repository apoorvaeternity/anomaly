from django.shortcuts import render, redirect, reverse
from django.views import View
from matplotlib import pyplot as plt
from mpld3 import fig_to_html
from django.core.files.storage import FileSystemStorage
from .forms import FileUploadForm, MovingAverageForm
from .anomaly_detection_tools import moving_average, arima
from math import fabs

import pandas as pd


# Create your views here.

class FileUploadView(View):
    form_class = FileUploadForm
    template_name = 'core/file_upload.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request, *args, **kwargs):
        if request.POST['supported_datasets'] == 'Rainfall in India' and request.POST['algorithm'] == 'Moving Average':
            fs = FileSystemStorage()
            file_name = fs.save(str(request.FILES['file'].name), request.FILES['file'])
            request.session['file'] = file_name
            return redirect(reverse('core:moving-avg'))
        elif request.POST['supported_datasets'] == 'Rainfall in India' and request.POST[
            'algorithm'] == 'ARIMA':
            fs = FileSystemStorage()
            file_name = fs.save(str(request.FILES['file'].name), request.FILES['file'])
            request.session['file'] = file_name
            return redirect(reverse('core:arima'))


class MovingAveragePlotView(View):
    def get(self, request, *args, **kwargs):
        threshold = 200 if 'threshold' not in request.GET else float(request.GET['threshold'])
        state = 'HARYANA DELHI & CHANDIGARH' if 'region' not in request.GET else request.GET['region']
        fs = FileSystemStorage()
        dataframe = pd.read_csv(fs.open(request.session.get('file')))
        dataframe_region = dataframe.loc[dataframe['subdivision'] == state]
        fig = plt.figure()
        plt.xlabel('year')
        plt.ylabel('mm')
        mv_avg = moving_average(dataframe_region['annual'].tolist(), dataframe_region['year'].tolist())
        for x, y in zip(dataframe_region['year'].tolist(), dataframe_region['annual'].tolist()):
            if x in mv_avg and fabs(y - mv_avg[x]) > threshold:
                plt.plot(x, y, 'r+')
            else:
                plt.plot(x, y, 'bx')
        return render(request, 'core/plot.html',
                      context={'plot': fig_to_html(fig), 'state': state, 'threshold': threshold,
                               'algorithm': 'Moving Average',
                               'mv_avg_form': MovingAverageForm})


class ARIMAPlotView(View):
    def get(self, request, *args, **kwargs):
        threshold = 200 if 'threshold' not in request.GET else float(request.GET['threshold'])
        state = 'HARYANA DELHI & CHANDIGARH' if 'region' not in request.GET else request.GET['region']
        fs = FileSystemStorage()
        dataframe = pd.read_csv(fs.open(request.session.get('file')))
        dataframe_region = dataframe.loc[dataframe['subdivision'] == state]
        series = pd.Series(dataframe_region['annual'].tolist(), index=dataframe_region['year'])
        arima_calc = arima(series)
        fig = plt.figure()
        plt.xlabel('year')
        plt.ylabel('mm')
        for x, y in zip(dataframe_region['year'].tolist(), dataframe_region['annual'].tolist()):
            if x in arima_calc and fabs(y - arima_calc[x]) > threshold:
                plt.plot(x, y, 'r+')
            else:
                plt.plot(x, y, 'bx')
        return render(request, 'core/plot.html',
                      context={'plot': fig_to_html(fig), 'state': state, 'threshold': threshold, 'algorithm': 'ARIMA',
                               'mv_avg_form': MovingAverageForm})
