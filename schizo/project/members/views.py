from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CSVUploadForm
from .models import Experiment, Profile
import csv


#from django.urls import reverse_lazy
@login_required
def profile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'members/profile.html', {
        'user': user,
        'user_form': user_form,
        'profile_form': profile_form,
    })

def profilepage(request,username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=request.user)
    experiments = Experiment.objects.filter(user=request.user)
    profile_url=reverse('profilepage', kwargs={'username': username})
    context = {
        'user': user,
        'profile_url':profile_url,
        'profile':profile,
        'experiments':experiments
    }
    return render(request, 'members/profilepage.html', context)  


'''class CSVUpload(LoginRequiredMixin, FormView):
    template_name = 'upload_csv.html'
    form_class = CSVUploadForm
    success_url = reverse_lazy('process_csv')

    def form_valid(self, form):
        csv_file = form.cleaned_data['csv_file']
        experiment = Experiment(user=self.request.user, csv_file=csv_file)
        experiment.save()
        return FormView.form_valid(self,form)'''

def worked(request):
    return render(request, 'members/worked.html')
def sad(request):
    return render(request, 'members/sad.html')

@login_required
def CSVUpload(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
                csv_file1 = form.cleaned_data['csv_file1']
                csv_file2 = form.cleaned_data['csv_file2']
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                model = form.cleaned_data['model']
                experiment = Experiment(user=request.user, csv_file1=csv_file1,
                csv_file2=csv_file2,                             
                name=name,
                description=description,
                model=model)
                experiment.save()
        # Check if the file has any data
                if not csv_file1.read(1) and not csv_file2.read(1):
                    error_message = 'Error: The CSV file is empty.'
                    return render(request, 'upload_csv.html', {'error_message': error_message})

                # Reset file pointer to the start
                csv_file1.seek(0)
                csv_file2.seek(0)

                # Read the CSV file using the csv module
                with csv_file1.open(mode='rb') as csv_file1:
                    # Create a CSV reader object
                    csv_reader1 = csv.reader(csv_file1.read().decode('utf-8').splitlines())
                with csv_file2.open(mode='rb') as csv_file2:
                    # Create a CSV reader object
                    csv_reader2 = csv.reader(csv_file2.read().decode('utf-8').splitlines())
                    
                    # Iterate over the rows in the CSV file
                    '''for row in csv_reader:
                        # Do something with the row data
                        print(row)'''
                    try:
                        header1 = next(csv_reader1)
                        header2 = next(csv_reader2)
                    except StopIteration:
                        error_message = 'Error: The CSV file has no rows.'
                        return render(request, 'upload_csv.html', {'error_message': error_message})

                # Check if the file has any columns
                if len(header1) == 0 and len(header2):
                    error_message = 'Error: The CSV file has no columns.'
                    return render(request, 'upload_csv.html', {'error_message': error_message})

                return render(request, 'members/worked.html')
    else:
        form = CSVUploadForm()
    return render(request, 'members/upload_csv.html', {'form': form})

def history(request):
    experiments = Experiment.objects.filter(user=request.user)
    return render(request, 'members/history.html', {'experiments':experiments})