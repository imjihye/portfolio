from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        data = self.data

        if data["email"] != 'dlvzz@naver.com' or data["password"] != '1234':
            raise ValidationError(_("Error!"))
        return data

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

class CreateForm(forms.Form):
    email = forms.EmailField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(widget=forms.TextInput())
    # phone = forms.CharField(max_length=20, validators=[RegexValidator(r'^\d{1, 10}$', 'zz')])
    phone = forms.CharField(max_length=20)
    check = forms.CharField(widget=forms.CheckboxInput())

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        class_name = 'form-control'
        for field in self.fields:
            if (field == 'check'):
                class_name = '';
            self.fields[field].widget.attrs['class'] = class_name


    def clean(self):
        data = self.data
        if data["password"] != data["password_confirm"]:
            # raise ValidationError("Password dont match")
            raise ValidationError(_("%(value)s dont match"), params={'value': 'Password'})

        elif data["email"] != 'dlvzz@naver.com' or data["password"] != '1234':
            raise ValidationError(_("Error!"))

        return data
