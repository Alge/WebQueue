from django import forms


class AddQueuePlaceForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True
    )
    location = forms.CharField(
        max_length=100,
        required=False
    )

class MakeQueue(forms.Form):
    name = forms.CharField(
        max_length=100
    )

class RemoveFromQueueForm(forms.Form):
    placement_id = forms.IntegerField(
        required=True
    )

class DeleteQueueForm(forms.Form):
    queue_id = forms.IntegerField()

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputUsername', 'placeholder': 'användarnamn'})
    )
    password = forms.CharField(
        label="Password",
        max_length=50,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputPassword', 'placeholder': 'lösenord'})
    )