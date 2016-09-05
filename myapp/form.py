from django import forms
from django.core.validators import RegexValidator


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        data = self.data

        if data["email"] != 'dlvzz@naver.com' or data["password"] != '1234':
            raise forms.ValidationError("Error!")
        return data


class CreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        class_name = 'form-control'
        for field in self.fields:
            if (field == 'check'):
                class_name = '';
            self.fields[field].widget.attrs['class'] = class_name


    email = forms.EmailField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(widget=forms.TextInput())
    phone = forms.CharField(max_length=20, validators=[RegexValidator(r'^\d{1,10}$')])
    check = forms.CharField(widget=forms.CheckboxInput())


    def clean(self):
        data = self.data

        if data["password"] != data["password_confirm"]:
            raise forms.ValidationError("password dont match")
        return data
