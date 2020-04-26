from django.views.generic import CreateView
from .models import User

# Create your views here.
class UserCreateView(CreateView):
    model = User
    template_name = 'accounts/login.html'
    fields = ('name','email', 'password')
