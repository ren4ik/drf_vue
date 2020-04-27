from django.contrib import admin
from chat.models import Room, Chat


class RoomAdmin(admin.ModelAdmin):
	list_display = ("creater", "invited_user", "date")

	def invited_user(self, obj):
		return "\n".join(user.username for user in obj.invited.all())


class ChatAdmin(admin.ModelAdmin):
	"""Dialog chat"""
	list_display = ("room", "user", "text", "date")


admin.site.register(Chat, ChatAdmin)
admin.site.register(Room, RoomAdmin)
