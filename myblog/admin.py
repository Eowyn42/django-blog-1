from django.contrib import admin
from myblog.models import Post, Category, Categorization


#  Model admin classes
class CategorizationInline(admin.TabularInline):
    model = Categorization
    extra = 1
    readonly_fields = ['category',]


class PostAdmin(admin.ModelAdmin):
    inlines = (CategorizationInline,)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


# admin registrations
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
