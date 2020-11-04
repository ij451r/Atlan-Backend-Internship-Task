from django.shortcuts import render,reverse, get_object_or_404 ,redirect
from django.http import HttpResponse, HttpResponseRedirect
import logging
from django.contrib import messages

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmployeeSerializer,TaskManagerSerializer, Example2Serializer, TeamsSerializer

import pandas as pd
from .models import Employee, TaskManager, Example2, Teams
from .forms import TaskManagerInputForm, DateFilterForm
from .utils import RunTaskex1,RunTaskex2,RunTaskex3


def Home(request):
	return render (request, "Filehandler/home.html")

def Example1View (request):
	
	if request.method == 'POST':
		form = TaskManagerInputForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f'Your File has been uploaded and is being updated in the database')
			initiator = form.cleaned_data.get('TaskInitiator')
			RunTaskex1(initiator)
			return render(request, "Filehandler/example1.html")
	else:
		form = TaskManagerInputForm()
	context={
		'form' : form
	}
	return render(request, "Filehandler/example1.html",context)

def Example2View(request):
	
	if request.method == 'POST':
		form = TaskManagerInputForm(request.POST,request.FILES)
		l_form = DateFilterForm(request.POST)
		if form.is_valid():
			obj=form.save(commit=False)
			obj.Task='Task2'
			obj.save()
			messages.success(request, f'Your File has been uploaded and is being updated in the database')
			initiator = form.cleaned_data.get('TaskInitiator')
			RunTaskex2(initiator)
			return render(request, "Filehandler/example2.html")
		if l_form.is_valid():
			RefInitiator = l_form.cleaned_data.get('RefInitiator')
			NewInitiator = l_form.cleaned_data.get('NewInitiator')
			date1 = l_form.cleaned_data.get('start_date')
			date2 = l_form.cleaned_data.get('end_date')
			return redirect('Example2Dashboard',initiator1=RefInitiator,initiator2=NewInitiator,date1=date1,date2=date2 )
	else:
		form = TaskManagerInputForm()
		l_form = DateFilterForm()
	context={
		'form' : form,
		'l_form' : l_form 
	}
	return render(request, "Filehandler/example2.html",context)

def Example3View (request):
	if request.method == 'POST':
		form = TaskManagerInputForm(request.POST,request.FILES)
		if form.is_valid():
			obj=form.save(commit=False)
			obj.Task='Task3'
			obj.save()
			messages.success(request, f'Your Team is being created in the database')
			initiator = form.cleaned_data.get('TaskInitiator')
			RunTaskex3(initiator)
			return render(request, "Filehandler/example3.html")
	else:
		form = TaskManagerInputForm()
	context={
		'form' : form
	}
	return render(request, "Filehandler/example1.html",context)

def Example2Dashboard (request,initiator1,initiator2,date1,date2):
	CurrentTask=TaskManager.objects.create(
		TaskInitiator=initiator2,
		Task='Task2',
		status='running',
		status_bar=0
	)
		
	ReferenceTask=TaskManager.objects.get(TaskInitiator=initiator1)
	Items = Example2.objects.filter(TaskRefree=ReferenceTask).filter(DoB__range=[date1,date2])
	Running='running'
	Pause='Pause'
	context={
		'CurrentTask' : CurrentTask,
		'Items' : Items,
		'running' : Running,
		'Pause' : Pause
	}
	return render(request, "Filehandler/dashboard.html",context)


def Resume(request,initiator):
	Task=TaskManager.objects.get(TaskInitiator=initiator)
	Task.status="running"
	Task.save()
	if Task.Task == 'Task1':
		RunTaskex1(initiator)
		return redirect( 'Example1List',initiator=initiator)
	if Task.Task == 'Task2':
		RunTaskex2(initiator)
		return redirect( 'Example2List',initiator=initiator)
	if Task.Task == 'Task3':
		RunTaskex3(initiator)
		return redirect( 'Example3List',initiator=initiator)
	

def Delete(request,initiator):
	Task=TaskManager.objects.get(TaskInitiator=initiator)
	task = Task.Task
	Task.delete()
	if task == 'Task1':
		return redirect( 'Example1List',initiator=initiator)
	if task == 'Task2':
		return redirect( 'Example2List',initiator=initiator)
	if task == 'Task3':
		return redirect( 'Example3List',initiator=initiator)
	

	

@api_view(['GET'])
def Example1List(request,initiator):
	Task=TaskManager.objects.get(TaskInitiator=initiator)
	employee = Employee.objects.filter(TaskRefree=Task)
	serializer = EmployeeSerializer(employee, many = True)
	return Response(serializer.data)

@api_view(['GET'])
def Example2List(request,initiator):
	Task=TaskManager.objects.get(TaskInitiator=initiator)
	example2 = Example2.objects.filter(TaskRefree=Task)
	serializer = Example2Serializer(example2, many = True)
	return Response(serializer.data)

@api_view(['GET'])
def Example3List(request,initiator):
	Task=TaskManager.objects.get(TaskInitiator=initiator)
	Team = Teams.objects.filter(TaskRefree=Task)
	serializer = TeamsSerializer(Team, many = True)
	return Response(serializer.data)

@api_view(['GET','PATCH'])
def Update(request,initiator):
	Task=TaskManager.objects.get(TaskInitiator=initiator)
	serializer = TaskManagerSerializer(instance =Task, data=request.data,many=False)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
