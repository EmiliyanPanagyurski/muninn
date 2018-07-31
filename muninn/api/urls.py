from rest_framework import routers
from django.conf.urls import url, include
from .views.developer_view import DeveloperView
from .views.publisher_view import PublisherView
from .views.engine_view import EngineView
from .views.game_view import GameView

router = routers.DefaultRouter()
router.register('developers', DeveloperView, base_name='developer')
router.register('publishers', PublisherView, base_name='publisher')
router.register('engines', EngineView, base_name='engine')
router.register('games', GameView, base_name='game')

urlpatterns = [
  url(r'', include(router.urls)),
]
