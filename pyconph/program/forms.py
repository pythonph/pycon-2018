from django import forms
from registration.forms import RegistrationForm
from registration.users import UserModel, UsernameField

from pyconph.program.models import Proposal

User = UserModel()


class NamedRegistrationForm(RegistrationForm):
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)

    class Meta:
        model = User
        fields = [UsernameField(), 'email', 'first_name', 'last_name']


class ProposalForm(forms.ModelForm):
    duration = forms.ChoiceField(choices=[
        ('00:30:00', '30 minutes'),
        ('00:45:00', '45 minutes'),
        ('01:00:00', '1 hour'),
        ('02:00:00', '2 hours'),
        ('03:00:00', '3 hours'),
    ])

    class Meta:
        model = Proposal
        fields = ['title', 'description', 'abstract', 'presentation_type',
                  'audience_level', 'duration']

