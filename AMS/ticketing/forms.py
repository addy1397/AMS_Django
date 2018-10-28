from django import forms


class PassengerLogin(forms.Form):
    id = forms.IntegerField(label='ID')
    name = forms.CharField(label='First Name')
    password = forms.CharField(widget=forms.PasswordInput)

class BookTicket(forms.Form):
    source=forms.CharField(label='Source')
    destination=forms.CharField(label='Destination')
    CHOICES=(
        ('1','BUSSINESS'),
        ('2','ECONOMY'),
    )
    _class=forms.ChoiceField(choices=CHOICES)

class EmployeeLogin(forms.Form):
    name = forms.CharField(label='First Name')
    password = forms.CharField(widget=forms.PasswordInput)
