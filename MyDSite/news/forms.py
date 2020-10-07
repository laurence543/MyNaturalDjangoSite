from django import forms


class CreateForm(forms.Form):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'input'}))
    annotation = forms.CharField(label='Аннотация', widget=forms.Textarea(attrs={'class': 'input'}))
    content = forms.CharField(label='Содержимое', widget=forms.Textarea(attrs={'class': 'input'}))
    link = forms.CharField(label='Источник', widget=forms.TextInput(attrs={'class': 'input'}))
    photo = forms.FileField(label='Изображение', widget=forms.FileInput(attrs={'class': 'file'}))


class EditForm(forms.Form):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'input'}))
    annotation = forms.CharField(label='Аннотация', widget=forms.Textarea(attrs={'class': 'input'}))
    content = forms.CharField(label='Содержимое', widget=forms.Textarea(attrs={'class': 'input'}))
    link = forms.CharField(label='Источник', widget=forms.TextInput(attrs={'class': 'input'}))
    photo = forms.CharField(label='Изображение', widget=forms.TextInput(attrs={'class': 'input'}))


class EditPhotoForm(forms.Form):
    photo = forms.FileField(label='Изображение', widget=forms.FileInput(attrs={'class': 'file'}))
