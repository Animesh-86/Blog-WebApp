from django.urls import path
from .views import user_form_view

urlpatterns = [
    path('user-form/', user_form_view, name='user_form'),
    path('success/', lambda request: render(request, 'blog/success.html'), name='success'),
]
