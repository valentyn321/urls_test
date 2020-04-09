from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.models import Profile
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View 
from django.views.decorators.csrf import csrf_exempt

class RegisterView(View):  #class-based register view
    form = UserRegisterForm()
    template_name = 'users/register.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request, *args, **kwargs):
        profile = Profile()
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save(commit=False)
            user.save()
            profile.user = user
            profile.save()
            messages.success(request, f'Account created successfully!')
            return redirect('home')