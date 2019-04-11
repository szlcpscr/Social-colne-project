from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email address'


class UserCreateForm2(UserCreateForm):

    class Meta2:
        field2 = ('username', 'email', 'password1', 'password2')
        model2 = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field2['username'].label = 'Display Name'
        self.field2['email'].label = 'Email Address'


class EditProfileForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
        )