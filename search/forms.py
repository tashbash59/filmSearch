from django import forms
from .models import SearchNumbers

class NumbersForm(forms.ModelForm):

	class Meta:
		model = SearchNumbers
		fields = ['first','second']

		widgets = {
			"first": forms.NumberInput(),
			"second": forms.NumberInput(),
		}

