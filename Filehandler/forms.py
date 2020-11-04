from django import forms
from .models import TaskManager

class TaskManagerInputForm (forms.ModelForm):
	class Meta:
		model = TaskManager
		fields = ['TaskInitiator','TaskFile']

class DateFilterForm(forms.Form): 
	RefInitiator = forms.CharField(max_length=50)
	NewInitiator = forms.CharField(max_length=50)
	start_date = forms.DateTimeField()
	end_date = forms.DateTimeField()
    