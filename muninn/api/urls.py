from django.conf.urls import url

from .views.developer_view import DeveloperListView
from .views.publisher_view import PublisherView
from .views.engine_view import EngineView
from .views.game_view import GameView


urlpatterns = [
  url(r'^developers/$', DeveloperListView.as_view(), name='developers'),
  url(r'^publishers/$', PublisherView.as_view(), name='publishers'),
  url(r'^engines/$', EngineView.as_view(), name='engines'),
  url(r'^games/$', GameView.as_view(), name='games'),
]
