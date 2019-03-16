from django import forms

from .models import Dog
from .models import Owner

class DogForm(forms.ModelForm):
	class Meta:
		model = Dog
		fields = ['dogownerid', 'dogid', 'dogname', 'dogbreed', 'dogage']
		labels = {'dogownerid': 'Owner ID', 'dogid': 'Dog ID', 'dogname': 'Name of the dog', 'dogbreed': 'Breed', 'dogage': 'Age' }
