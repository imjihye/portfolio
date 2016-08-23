from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        if cleaned_data['email'] == 'dlvzz@naver.com' \
                and cleaned_data['password'] == 'dlvzz':
            return True
        else:
            raise forms.ValidationError('Error!')
