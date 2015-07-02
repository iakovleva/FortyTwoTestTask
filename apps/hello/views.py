from django.views.generic import DetailView
from apps. hello.models import Person

class PersonDetail(DetailView):
	model = Person 
