from .models import TaskManager, Employee, Example2, Teams
import pandas as pd
import os
import time
from django.http import StreamingHttpResponse


def RunTaskex1(initiator):
	Task=TaskManager.objects.filter(TaskInitiator=initiator).first()
	file_data = pd.read_csv(Task.TaskFile)
	j=0 #Counter to check how many rows to skip
	n=1	#Counter to check if first iteration
	for i in file_data.itertuples(index=False,name=Task.TaskInitiator):
		time.sleep(0.1) #Django has sqlite database, it doesnt allow multiple entries at a time (API)
		Task=TaskManager.objects.filter(TaskInitiator=initiator).first()
		print(Task.status)
		if Task.status == "Pause":
			print("Upload has been discontinued")
			return
		elif Task.status == "Terminate":
			Task.delete()
			return
		elif Task.status == 'running':
			if Task.status_bar != 0 and Task.status_bar>j and n==1:
				j+=1
				print(j,"   ",Task.status_bar)
				continue
			
			employee = Employee.objects.create(
					TaskRefree = Task,
					EmpID = i[0],
					NamePrefix= i[1],
					FirstName= i[2],
					MiddleInitial= i[3],
					LastName= i[4],
					Gender= i[5],
					EMail= i[6],
					FatherName= i[7],
					MotherName= i[8],
					MotherMaidenName= i[9],
					DateofBirth= i[10],
					TimeofBirth= i[11],
					AgeinYrs= i[12],
					WeightinKgs= i[13],
					DateofJoining= i[14],
					QuarterofJoining= i[15],
					HalfofJoining= i[16],
					YearofJoining= i[17],
					MonthofJoining= i[18],
					MonthNameofJoining= i[19],
					ShortMonth= i[20],
					DayofJoining= i[21],
					DOWofJoining= i[22],
					ShortDOW= i[23],
					AgeinCompany= i[24],
					Salary= i[25],
					Last= i[26],
					SSN= i[27],
					PhoneNo= i[28],
					PlaceName= i[29],
					County= i[30],
					City= i[31],
					State= i[32],
					Zip= i[33],
					Region= i[34],
					UserName= i[35],
					Password= i[36],
				)
			print(Task.status_bar)
			Task.status_bar+=1
			Task.save()
			n=0
		else:
			Task.status="running"
			Task.save()

def RunTaskex2(initiator):
	Task=TaskManager.objects.filter(TaskInitiator=initiator).first()
	file_data = pd.read_csv(Task.TaskFile)
	j=0 #Counter to check how many rows to skip
	n=1	#Counter to check if first iteration
	for i in file_data.itertuples(index=False,name=Task.TaskInitiator):
		time.sleep(0.1) #Django has sqlite database, it doesnt allow multiple entries at a time (API)
		Task=TaskManager.objects.filter(TaskInitiator=initiator).first()
		print(Task.status)
		if Task.status == "Pause":
			print("Upload has been discontinued")
			return
		elif Task.status == "Terminate":
			Task.delete()
			return
		elif Task.status == 'running':
			if Task.status_bar != 0 and Task.status_bar>j and n==1:
				j+=1
				print(j,"   ",Task.status_bar)
				continue
			example2 = Example2.objects.create(
					TaskRefree = Task,
					EmpId = i[0],
					Name= i[1],
					DoB= i[2],
					State= i[3],
				)
			print(Task.status_bar)
			Task.status_bar+=1
			Task.save()
			n=0
		else:
			Task.status="running"
			Task.save()

def RunTaskex3(initiator):
	Task=TaskManager.objects.filter(TaskInitiator=initiator).first()
	file_data = pd.read_csv(Task.TaskFile)
	j=0 #Counter to check how many rows to skip
	n=1	#Counter to check if first iteration
	for i in file_data.itertuples(index=False,name=Task.TaskInitiator):
		time.sleep(0.1) #Django has sqlite database, it doesnt allow multiple entries at a time (API)
		Task=TaskManager.objects.filter(TaskInitiator=initiator).first()
		Members=[]
		print(Members)
		print(Task.status)
		if Task.status == "Pause":
			print("Upload has been discontinued")
			return
		elif Task.status == "Terminate":
			Task.delete()
			return
		elif Task.status == 'running':
			if Task.status_bar != 0 and Task.status_bar>j and n==1:
				j+=1
				print(j,"   ",Task.status_bar)
				continue
			example3 = Teams.objects.create(
					TaskRefree = Task,
					TeamLeader = Employee.objects.filter(EmpID=i[1]).last()								
				)
			for mem in i[2].split(','):
				if Task.status == 'running':
					member = Employee.objects.filter(EmpID=mem).last()
					example3.TeamMember.add(member)
			example3.save()
			print(Task.status_bar)
			Task.status_bar+=1
			Task.save()
			n=0
		else:
			Task.status="running"
			Task.save()
