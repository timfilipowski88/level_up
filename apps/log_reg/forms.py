from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Fieldset
from crispy_forms.bootstrap import FormActions

# VALDIATORS


# def lengthGreaterThanTwo(value):
#     if len(value) < 3:
#         raise ValidationError(
#             '{} must be longer than: 2'.format(value)
#         )


# class UserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = (
#             'first_name',
#             'last_name',
#             'username',
#             'email',
#             'password',
#         )

#     widgets = {
#         'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#         'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#         'username': forms.TextInput(attrs={'class': 'form-control'}),
#         'email': forms.EmailInput(attrs={'class': 'form-control'}),
#         'password': forms.PasswordInput(attrs={'class': 'form-control'}),
#     }
class LogForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'log_email'}))
    password = forms.CharField(max_length=45)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.attrs = {
            'novalidate': ''
        }

        self.helper.form_action = 'login'

        self.helper.add_input(Submit('submit', 'Login', css_class='btn-primary'))


# cleaning-and-validating-fields-that-depend-on-each-other
# https: // docs.djangoproject.com/en/3.1/ref/forms/validation/

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=45)
    last_name = forms.CharField(max_length=45)
    username = forms.CharField(max_length=45)
    email = forms.EmailField(
        max_length = 150,
        widget=forms.EmailInput(attrs={'id': 'reg_email'}))
    password = forms.CharField(
        max_length=150, 
        widget=forms.PasswordInput(attrs={'id':'reg_password'})
        )  
    confirm_password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={'id':'reg_conf_password'})
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'reg_form'
        self.helper.form_class = 'log_reg_form'
        self.helper.form_method = 'POST'
        self.helper.attrs = {
            'novalidate': ''
        }
        self.helper.form_action = 'login_register:register'

        self.helper.layout = Layout(
            Row(
                Column('first_name'),
                Column('last_name')
            ),
            'username',
            'email',
            'password',
            'confirm_password',
            FormActions(
                Submit('submit', 'Register', css_id='register_btn', css_class='btn-primary', action="register")
            ),
        )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError(
                '{} passwords must match'.format(self)
            )

