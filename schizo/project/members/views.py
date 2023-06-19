from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required



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
    profile_url=reverse('profilepage', kwargs={'username': username})
    context = {
        'user': user,
        'profile_url':profile_url
    }
    return render(request, 'members/profilepage.html', context)
    
    '''form_class = UserChangeForm
    template_name = 'members/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user

    return render (request, template_name, {'lf':form_class})'''



