from django.contrib.auth import views as auth_views


class LoginUserView(auth_views.LoginView):
    redirect_authenticated_user = True
    template_name = "users/login.html"


class LogoutUserView(auth_views.LogoutView):
    template_name = "users/logout.html"
