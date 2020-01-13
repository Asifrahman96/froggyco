from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, user_passes_test


def login_forbidden(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name="register"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
    path('logout', views.logout, name="logout"),

    # Password Reset and Change URL's
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
         template_name='accounts/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
         template_name='accounts/password_change.html'),
         name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(
         template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),

    path('password_reset/', login_forbidden(auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset_confirm.html')),
        name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
]
