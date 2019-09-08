from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    url('^$',views.home,name='home'),
    url('^home$',views.project_all,name='project_all'),
    url(r'^accounts/profile/', views.profile, name='myProfile'),
    url(r'^project/(\d+)', views.project, name ='project'),
    url(r'^new/project$', views.new_project, name='new_project'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/project/$',views.Projectlist.as_view()),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$', views.ProfileDes.as_view()),
    url(r'api/project/project-id/(?P<pk>[0-9]+)/$', views.ProjectDes.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
