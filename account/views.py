from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from image.models import Image
from django.db.models import Q


class Homepage(View):
    users = User.objects.filter(is_active=True)

    def get(self, request):
        search_query = request.GET.get('search', '')

        if search_query:
            images = Image.objects.filter(Q(title__icontains=search_query))
        else:
            images = Image.objects.all()
        return render(request, 'account/homepage.html', {'users': self.users, 'images': images})


class RegisterView(View):
    user = User

    @login_required
    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, 'account/edit.html', {'user_form': user_form})

    @login_required
    def post(self, request):
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)

            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password2')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'account/register.html', {'user_form': user_form})


class EditView(View):
    user = User

    @login_required
    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

    @login_required
    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(f'/{request.user.username}')
        return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/profile.html', {'section': 'people', 'user': user})
