from django import forms


class CreateForm(forms.Form):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'input'}))
    annotation = forms.CharField(label='Аннотация', widget=forms.Textarea(attrs={'class': 'input'}))
    content = forms.CharField(label='Содержимое', widget=forms.Textarea(attrs={'class': 'input'}))

