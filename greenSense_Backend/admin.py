from django.contrib import admin
from greenSense_Backend.models import User, Chat, Message, Question

admin.site.register(User)
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Question)

# Bundling