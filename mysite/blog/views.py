from django import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required

from .models import Dataset
from .forms import DatasetForm


# ------------------------
# Custom Signup Form
# ------------------------
class CustomSignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password1") != cleaned_data.get("password2"):
            self.add_error("password2", "Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = User(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email']
        )
        full_name = self.cleaned_data['name']
        if " " in full_name:
            user.first_name, user.last_name = full_name.split(" ", 1)
        else:
            user.first_name = full_name
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


# ------------------------
# Auth Views
# ------------------------
def signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomSignupForm()
    return render(request, 'blog/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # or redirect('home')


# ------------------------
# Pages
# ------------------------
@login_required
def home_view(request):
    datasets = Dataset.objects.filter(owner=request.user)
    return render(request, 'blog/home.html', {'datasets': datasets})


def about_view(request):
    return render(request, 'blog/about.html')


@login_required
def profile_view(request):
    user = request.user
    datasets = Dataset.objects.filter(owner=user)
    return render(request, 'blog/profile.html', {'user': user, 'datasets': datasets})


# ------------------------
# Dataset / Blog
# ------------------------
@login_required
def add_dataset_view(request):
    if request.method == 'POST':
        form = DatasetForm(request.POST)
        if form.is_valid():
            dataset = form.save(commit=False)
            dataset.owner = request.user
            dataset.save()
            return redirect('home')
    else:
        form = DatasetForm()
    return render(request, 'blog/add_dataset.html', {'form': form})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Dataset

@login_required
def profile_view(request):
    user = request.user
    datasets = Dataset.objects.filter(owner=user)
    return render(request, 'blog/profile.html', {'user': user, 'datasets': datasets})

@staff_member_required  # only superuser/staff can access
def dashboard_view(request):
    users = User.objects.all()
    total_users = users.count()
    total_blogs = Dataset.objects.count()

    # Optional: user-wise blog counts
    user_blog_data = []
    for user in users:
        blog_count = Dataset.objects.filter(owner=user).count()
        user_blog_data.append({
            'name': user.get_full_name() or user.username,
            'email': user.email,
            'username': user.username,
            'blogs': blog_count,
            'date_joined': user.date_joined
        })

    return render(request, 'blog/dashboard.html', {
        'total_users': total_users,
        'total_blogs': total_blogs,
        'user_blog_data': user_blog_data
    })

from django.shortcuts import get_object_or_404

@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(Dataset, pk=blog_id)
    return render(request, 'blog/view_blog.html', {'blog': blog})
