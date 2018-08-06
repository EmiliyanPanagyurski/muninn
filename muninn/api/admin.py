from django.contrib import admin
from .models.game import Game
from .models.publisher import Publisher
from .models.developer import Developer
from .models.engine import Engine
# Register your models here.

admin.site.register(Game)
admin.site.register(Publisher)
admin.site.register(Developer)
admin.site.register(Engine)
