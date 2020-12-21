from django.urls import path
from . import views

app_name = 'polls'


### Generic view (class-based view)
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results.
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]



#urlpatterns=[ //6주차
# ex: /polls/
#path('', views.index, name='index'), //6주차
# ex: /polls/5/
#path('<int:question_id>/', views.detail, name='detail'), //6주찿
#ex: /polls/5/results.
#path('<int:question_id>/results/', views.results, name='results'), //6주차
#ex: /polls/5/vote/
#path('<int:question_id>/vote/', views.vote, name='vote') //6주차
#]
