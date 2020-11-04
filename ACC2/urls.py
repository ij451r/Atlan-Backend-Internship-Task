"""ACC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Filehandler import views as SHViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #urls to each Example
    path('', SHViews.Home, name='Home'),
    path('example1/', SHViews.Example1View, name='Example1'),
    path('example2/', SHViews.Example2View, name='Example2'),
    path('example3/', SHViews.Example3View, name='Example3'),
    path('example2/<str:initiator1>/<str:initiator2>/<date1>/<date2>/', SHViews.Example2Dashboard, name='Example2Dashboard'),
    #urls to views that trigger change in database and forwardsto functions
    path('delete/<str:initiator>/', SHViews.Delete, name='delete'),    
    path('resume/<str:initiator>/', SHViews.Resume, name='resume'),
    #api endpoints to retrieve data from database
    path('example1/<str:initiator>/', SHViews.Example1List, name='Example1List'),
    path('example2/<str:initiator>/', SHViews.Example2List, name='Example2List'),
    path('example3/<str:initiator>/', SHViews.Example3List, name='Example3List'),
    #api endpoint to make changes in database
    path('update/<str:initiator>/', SHViews.Update, name='update'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)