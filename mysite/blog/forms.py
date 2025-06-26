from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Full Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    contact = forms.CharField(label="Contact Number", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(label="Basic Info", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))


from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'password', 'contact', 'bio']
