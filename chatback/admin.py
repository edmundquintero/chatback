from django.contrib import admin
from chatback.models import *

admin.site.register(Room)
admin.site.register(User)
admin.site.register(ChatLog)
admin.site.register(Entry)

