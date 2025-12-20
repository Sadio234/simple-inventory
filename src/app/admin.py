from django.contrib import admin

from app.models import BlogPost
from app.models import BlogPost2

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('caisse', 'date', 'description_pannes', 'intervention', 'design_refer', 'quantity', 'agent_dsi', 'fonction', 'agent', 'Fonct', )

class BlogPostAdmin2(admin.ModelAdmin):
    list_display = ('caisse', 'date', 'description_pannes', 'intervention', 'design_refer', 'quantity', 'agent_dsi', 'fonction', 'agent', 'Fonct',)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogPost2, BlogPostAdmin2)

