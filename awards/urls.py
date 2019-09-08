from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    url('^$',views.home,name='home'),
    url('^home$',views.project_all,name='project_all'),
    url(r'^accounts/profile/', views.profile, name='myProfile'),
    url(r'^project/(\d+)', views.project, name ='project'),
    url(r'^new/project$', views.new_project, name='new_project')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
