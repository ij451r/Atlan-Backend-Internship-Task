An Application(TaskManager) is build to interact with the processes of other application, Which keeps track of the processes.


**Installation and Running** <br>
*clone the repository to your local machine<br>
*navigate to the project folder<br>
*Build docker image<br>
```
docker-compose up --build 
```
*If first time: Please run migrations<br>
```
docker-compose exec web python ./manage.py makemigrations
docker-compose exec web python ./manage.py migrate
```
