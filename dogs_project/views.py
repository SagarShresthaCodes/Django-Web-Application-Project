from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Dog
from .models import Owner
from .forms import DogForm

# Create your views here.
def index(request):
    ownerObject = Owner.objects.all()
    dogObjects = Dog.objects.all()
    context = {'dogs': dogObjects, 'owner': ownerObject}
    return render(request, 'dogs_project/index.html', context)

def new_dog(request):
	"""Add a new topic."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = DogForm()
	else:
		#POST data submitted; process data.
		form = DogForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('dogs_project:index'))

	context = {'form': form}
	return render(request, 'dogs_project/new_dog.html', context)
