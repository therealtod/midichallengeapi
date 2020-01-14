from django.urls import include, path
from rest_framework import routers
from apps.games import views

router = routers.SimpleRouter()
router.register(r'question', views.QuestionViewSet)
router.register(r'game', views.GameViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
