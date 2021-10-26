from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class CustomBackend(ModelBackend):
    """
    This is a ModelBacked that allows authentication
    with either a username or an email address.

    """
    def authenticate(self, username=None, password=None):
        if '@' in username:  # TODO: ban character "@" in username
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            return None
