from django.contrib.auth.models import User
from noticias.models import Notification
from random import choice

def user_info(request):
    if request.user.is_authenticated:
        return {'user_info': {
            'name': request.user.first_name,  # Obtén el nombre completo del usuario
        }}
    return {}


def notifications(request):
    notifications = Notification.objects.all()
    selected_notification = choice(notifications) if notifications else None
    return {
        'notification': selected_notification
    }