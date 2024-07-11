from django.views.generic import CreateView

from users.forms import UserRegistrationForm
from users.models import User


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = '...'
    success_message = 'Поздравляем! Вы успешно зарегестрировались!'