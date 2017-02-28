from django import forms


class SignupForm(forms.Form):
    field_order = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']

    first_name = forms.CharField(max_length=30,
                                 label='First name (optional)',
                                 required=False,
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'First name'
                                 }))

    last_name = forms.CharField(max_length=30,
                                label='Last name (optional)',
                                required=False,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Last name'
                                }))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
