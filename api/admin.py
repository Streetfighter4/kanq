from django.contrib import admin

from api.models import Post, Tag, User, Comment, Image, Medal, Topic


class CommonModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


@admin.register(Post)
class PostModelAdmin(CommonModelAdmin):
    date_hierarchy = 'created_at'
    fields = ('title', 'description', 'tags')


@admin.register(Tag)
class TagModelAdmin(CommonModelAdmin):
    pass


@admin.register(User)
class UserModelAdmin(CommonModelAdmin):
    date_hierarchy = 'date_joined'
    fields = ('first_name', 'last_name', 'email')


@admin.register(Comment)
class CommentModelAdmin(CommonModelAdmin):
    date_hierarchy = 'created_at'
    fields = ('content',)


@admin.register(Image)
class ImageModelAdmin(CommonModelAdmin):
    date_hierarchy = 'created_at'
    fields = ('uri',)


@admin.register(Medal)
class MedalModelAdmin(CommonModelAdmin):
    date_hierarchy = 'post__topic__end'
    fields = ('rank',)


@admin.register(Topic)
class TopicModelAdmin(CommonModelAdmin):
    date_hierarchy = 'end'
    fields = ('name', 'description', 'start', 'end', 'tags')


# admin.site.register(User)
# admin.site.register(Post)
# admin.site.register(Comment)
