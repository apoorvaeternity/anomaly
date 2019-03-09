from django import forms
from django.forms import Form


class FileUploadForm(Form):
    available_datasets = ['Rainfall in India']
    dataset_choices = ((dataset, dataset) for dataset in available_datasets)
    supported_datasets = forms.ChoiceField(choices=dataset_choices, label='Supported Datasets',
                                           widget=forms.Select(attrs = {'class': 'form-control',
                                                                               'data-toggle': 'select'}))
    file = forms.FileField(label='Select a CSV file', widget=forms.FileInput(attrs={'accept': '.csv'}))


class MovingAverageForm(Form):
    regions = ['LAKSHADWEEP', 'SAURASHTRA & KUTCH', 'WEST MADHYA PRADESH', 'EAST RAJASTHAN', 'TELANGANA',
               'WEST RAJASTHAN', 'ARUNACHAL PRADESH', 'JAMMU & KASHMIR', 'TAMIL NADU', 'GANGETIC WEST BENGAL',
               'SOUTH INTERIOR KARNATAKA', 'VIDARBHA', 'NAGA MANI MIZO TRIPURA', 'PUNJAB', 'KONKAN & GOA',
               'WEST UTTAR PRADESH', 'UTTARAKHAND', 'CHHATTISGARH', 'HIMACHAL PRADESH',
               'SUB HIMALAYAN WEST BENGAL & SIKKIM', 'EAST MADHYA PRADESH', 'EAST UTTAR PRADESH',
               'HARYANA DELHI & CHANDIGARH', 'COASTAL KARNATAKA', 'ORISSA', 'NORTH INTERIOR KARNATAKA', 'BIHAR',
               'KERALA', 'MADHYA MAHARASHTRA', 'GUJARAT REGION', 'COASTAL ANDHRA PRADESH', 'ASSAM & MEGHALAYA',
               'RAYALSEEMA', 'MATATHWADA', 'JHARKHAND', 'ANDAMAN & NICOBAR ISLANDS']
    region_choices = ((region, region) for region in regions)
    threshold = forms.IntegerField(min_value=0, label='Set a threshold value')
    region = forms.ChoiceField(choices=region_choices, label='Region',
                               widget=forms.Select(attrs={'class': 'form-control',
                                                          'data-toggle': 'select'}))
