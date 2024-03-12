from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from homeworks.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]


class LoginForm(AuthenticationForm):
    pass
