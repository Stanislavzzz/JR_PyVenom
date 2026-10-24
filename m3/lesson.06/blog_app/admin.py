from django.contrib import admin

from .models import Post, Comment, Author, AuthorProfile, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_lower', 'rating', 'author', 'created_at', 'tag_list')
    ordering = ('author', '-created_at',)
    list_filter = ('author', 'rating',)
    search_fields = ('title', 'content')
    search_help_text = "Введите часть заголовка или текста"

    fieldsets = (
        ("Основная информация", {
            'fields': ('title', 'author')
        }),
        ("Дополнительная информация", {
            'fields': ('rating', 'tags', ),
            'classes': ('collapse',)
        }),
    )

    def title_lower(self, post: Post):
        return post.title.lower()

    def tag_list(self, post: Post):
        return ", ".join(tag.name for tag in post.tags.all())

    tag_list.short_description = "Тэги"

    @admin.action(description="Увеличить рейтинг поста")
    def add_rating(self, request, queryset):
        """Массовое увеличение рейтинга."""
        for post in queryset:
            post.rating += 1
            post.save()

        self.message_user(request, f"{queryset.count()} постов обновлено")

    actions = (add_rating, )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at', 'text_size')
    ordering = ('post', 'author',)
    list_filter = ('author', )
    search_fields = ('text',)
    search_help_text = "Введите часть комментария"

    fields = ('author', 'post', 'text')
    # readonly_fields = ('post', )

    def text_size(self, comment: Comment):
        return comment.text[:50]

    text_size.short_description = "Текст"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('name', )
    list_filter = ('name', )
    search_fields = ('name',)
    search_help_text = "Введите часть имени"


@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ('author', 'website', 'bio_size')
    ordering = ('author',)
    list_filter = ('author',)
    search_fields = ('bio',)
    search_help_text = "Введите часть bio"

    def bio_size(self, profile: AuthorProfile):
        return profile.text[:50]

    bio_size.short_description = "Биография>"


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    search_help_text = "Введите часть тэга"


admin.site.register(Tag, TagAdmin)




