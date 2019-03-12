from django.urls import path

from users.views import LoginUserView, LogoutUserView, RegisterUserView, ProfileView, ChangePasswordView, \
    RegisterSalesTeamView, RegisterValuationTeamView, RegisterCalculationTeamView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('register_sales/', RegisterSalesTeamView.as_view(), name='register-sales'),
    path('register_valuation/', RegisterValuationTeamView.as_view(), name='register-valuation'),
    path('register_calculation/', RegisterCalculationTeamView.as_view(), name='register-calculation'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change-password'),
]
