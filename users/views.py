from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .models import Profile
from  fb.models import Post,Friend
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from rest_framework import generics
from .serializers import ProfileSerializer


# Create your views here.



# View to sign up
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            messages.success(request,'Your acccount has been created')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            Profile.objects.create(user=request.user)
    
            Friend.objects.create(current_user=request.user)
            logout(request)


            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})




# View for Profile page
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    posts = Post.objects.filter(author=user).order_by('-created_date')
    args = {'user': user,'posts':posts}
    return render(request, 'users/profile.html', args)


# View for  Edit Profile

@login_required
def edit_profile(request):
    if request.method == 'POST':
        # u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid():
            # u_form.save()
            p_form.save()
            #messages.success(request, 'Your account has been updated!')
            return redirect('edit_profile')

    else:
        # u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    posts = Post.objects.filter(author=request.user).order_by('-created_date')

    context = {
        # 'u_form': u_form,
        'p_form': p_form,
        'posts':posts

    }

    return render(request, 'users/edit_profile.html', context)



# View for change password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('post_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form })



class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer