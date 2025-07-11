# polls/urls.py
from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet
from .views import HelloApiView


app_name = "polls"

router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='question')

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('api/', include(router.urls)),
     # path('api/hello/', views.hello_api, name='hello_api'),
     path("api/hello-class/", HelloApiView.as_view(), name="hello_class_api"),
]

# Avant :
path("<int:question_id>/", views.detail, name="detail"),

# Après :
path("<int:pk>/", views.DetailView.as_view(), name="detail"),

