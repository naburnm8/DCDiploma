from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView

from users.forms import UserRegistrationForm
from users.models import User


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_message = 'Поздравляем! Вы успешно зарегестрировались!'
