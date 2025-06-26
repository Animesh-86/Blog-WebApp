from django.shortcuts import render, redirect
from .forms import UserProfileForm

def user_form_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # create this view/template later
    else:
        form = UserProfileForm()
    return render(request, 'blog/user_form.html', {'form': form})
