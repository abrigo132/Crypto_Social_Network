from django.contrib import admin

from posts.models import Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    search_fields = [
        "title",
        "body",
        "created_at",
        "like_count",
        "dislike_count",
        "reposts_count",
    ]
