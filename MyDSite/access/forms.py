from django import forms


class RegForm(forms.Form):
    login = forms.CharField(label='Логин:')
    pass1 = forms.CharField(widget=forms.PasswordInput(),
                            label='Пароль:')
    pass2 = forms.CharField(widget=forms.PasswordInput(),
                            label='Повтор:')
    email = forms.EmailField(label='E-Mail:')
    token = forms.CharField(label='Токен:')


class EntryForm(forms.Form):
    login = forms.CharField(label='Логин:')
    pass1 = forms.CharField(widget=forms.PasswordInput(),
                            label='Пароль:')
