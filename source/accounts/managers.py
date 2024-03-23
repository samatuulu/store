from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email=None, password=None, username=None, phone=None, is_superuser=False):
        if not password:
            raise ValueError('User name must have a password.')
        if not email:
            raise ValueError('User name must have an email.')
        model_data = {'is_superuser': is_superuser}

        if email:
            model_data['email'] = self.normalize_email(email)
        if phone:
            model_data['phone'] = phone
        if username:
            model_data['username'] = username

        user = self.model(**model_data)
        user.set_password(password)
        user.save(using=self._db)
        return user
