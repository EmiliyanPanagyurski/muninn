from django.conf.urls import url

from .views.developer_view import (
  DeveloperListAllView,
  DeveloperListAllFilteredView,
  DeveloperRetrieveView
)
from .views.publisher_view import (
  PublisherListView,
  PublisherListAllFilteredView,
  PublisherRetrieveView
)
from .views.engine_view import (
  EngineListAllView,
  EngineListAllFilteredView,
  EngineRetrieveView
)
from .views.game_view import (
  GameListAllView,
  GameListAllFilteredView,
  GameRetrieveView
)

urlpatterns = [
  url(r'^developers/all/$', DeveloperListAllView.as_view(), name='developers-all'),
  url(r'^developers/$', DeveloperListAllFilteredView.as_view(), name='developers-filtered'),
  url(r'^developers/(?P<name>.+)/$', DeveloperRetrieveView.as_view(), name='developer-name'),
  url(r'^publishers/all/$', PublisherListView.as_view(), name='publishers-all'),
  url(r'^publishers/$', PublisherListAllFilteredView.as_view(), name='publishers-filtered'),
  url(r'^publishers/(?P<name>.+)/$', PublisherRetrieveView.as_view(), name='publisher-name'),
  url(r'^engines/all/$', EngineListAllView.as_view(), name='engines-all'),
  url(r'^engines/$', EngineListAllFilteredView.as_view(), name='engines-filtered'),
  url(r'^engines/(?P<name>.+)/$', EngineRetrieveView.as_view(), name='engine-name'),
  url(r'^games/all/$', GameListAllView.as_view(), name='games-all'),
  url(r'^games/$', GameListAllFilteredView.as_view(), name='games-filtered'),
  url(r'^games/(?P<name>.+)/$', GameRetrieveView.as_view(), name='game-name'),
]
