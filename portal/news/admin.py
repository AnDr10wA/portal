from django.contrib import admin
from django import  forms
from .models import Tag, News
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

admin.site.register(Tag)


class NewsAdminForm(forms.ModelForm):
    head = forms.CharField(widget=CKEditorUploadingWidget())
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'
# Register your models here.



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'head', 'body']
    prepopulated_fields = {'slug': ('title', )}
    form = NewsAdminForm

