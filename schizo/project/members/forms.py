from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date', 'website']

class CSVUploadForm(forms.Form):
    csv_file1 = forms.FileField()
    csv_file2 = forms.FileField()
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=255)
    model = forms.CharField(max_length=50)

    def clean_csv_file1(self):
        csv_file1 = self.cleaned_data['csv_file1']
        if not csv_file1.name.endswith('.csv'):
            raise ValidationError('File must be a CSV file.')
        return csv_file1
    def clean_csv_file2(self):
        csv_file2 = self.cleaned_data['csv_file2']
        if not csv_file2.name.endswith('.csv'):
            raise ValidationError('File must be a CSV file.')
        return csv_file2