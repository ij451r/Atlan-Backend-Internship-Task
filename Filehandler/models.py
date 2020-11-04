from django.db import models

class TaskManager (models.Model):
	TaskInitiator = models.CharField(max_length=50,primary_key=True)
	Task = models.CharField(max_length=50, default='Task1')
	status = models.CharField(max_length=50, default='running')
	status_bar = models.IntegerField(default=0)
	TaskFile = models.FileField(upload_to='exfiles/',null=True)
	
	def __str__ (self):
		return self.TaskInitiator
	
class Employee (models.Model):
	TaskRefree = models.ForeignKey(TaskManager,on_delete=models.CASCADE)
	EmpID = models.CharField(max_length=50)
	NamePrefix = models.CharField(max_length=50)
	FirstName = models.CharField(max_length=50)
	MiddleInitial = models.CharField(max_length=50)
	LastName= models.CharField(max_length=50)
	Gender = models.CharField(max_length=50)
	EMail= models.CharField(max_length=50)
	FatherName= models.CharField(max_length=50)
	MotherName = models.CharField(max_length=50)
	MotherMaidenName = models.CharField(max_length=50)
	DateofBirth= models.CharField(max_length=50)
	TimeofBirth= models.CharField(max_length=50)
	AgeinYrs= models.CharField(max_length=50)
	WeightinKgs= models.CharField(max_length=50)
	DateofJoining= models.CharField(max_length=50)
	QuarterofJoining= models.CharField(max_length=50)
	HalfofJoining= models.CharField(max_length=50)
	YearofJoining= models.CharField(max_length=50)
	MonthofJoining= models.CharField(max_length=50)
	MonthNameofJoining= models.CharField(max_length=50)
	ShortMonth= models.CharField(max_length=50)
	DayofJoining= models.CharField(max_length=50)
	DOWofJoining= models.CharField(max_length=50)
	ShortDOW= models.CharField(max_length=50)
	AgeinCompany= models.CharField(max_length=50)
	Salary= models.CharField(max_length=50)
	Last= models.CharField(max_length=50)
	SSN= models.CharField(max_length=50)
	PhoneNo= models.CharField(max_length=50)
	PlaceName= models.CharField(max_length=50)
	County= models.CharField(max_length=50)
	City= models.CharField(max_length=50)
	State= models.CharField(max_length=50)
	Zip= models.CharField(max_length=50)
	Region= models.CharField(max_length=50)
	UserName= models.CharField(max_length=50)
	Password= models.CharField(max_length=50)

	def __str__ (self):
		return self.FirstName

class Example2(models.Model):
	TaskRefree = models.ForeignKey(TaskManager,on_delete=models.CASCADE)
	EmpId=models.CharField(max_length=50)
	Name =models.CharField(max_length=50)
	DoB = models.DateTimeField()
	State = models.CharField(max_length=10)
	def __str__ (self):
		return self.Name

class Teams (models.Model):

	teamid = models.AutoField(primary_key=True) #Not using the values in the sheet as it will raise redundancy as this field is ecpected to be a primary Key
	TaskRefree = models.ForeignKey(TaskManager,on_delete=models.CASCADE)
	TeamLeader = models.ForeignKey(Employee, max_length=50,on_delete=models.CASCADE,related_name = 'TeamLeader') 
	TeamMember = models.ManyToManyField(Employee,related_name = 'TeamMember')
