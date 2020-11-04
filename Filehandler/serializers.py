from .models import TaskManager, Employee, Example2, Teams
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'

class TaskManagerSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskManager
		fields = ['Task','status']

class Example2Serializer(serializers.ModelSerializer):
	class Meta:
		model = Example2
		fields = '__all__'

class TeamsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teams
		fields = ['teamid','TeamLeader','TeamMember']