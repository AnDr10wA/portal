from django.contrib import admin
from django import  forms
from .models import CategoryForum, MessageForum, TopicForum
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

admin.site.register(MessageForum)


class TopicForumAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorUploadingWidget())
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = TopicForum
        fields = '__all__'
# Register your models here.



@admin.register(TopicForum)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'body', 'category']
    prepopulated_fields = {'slug': ('title', )}
    form = TopicForumAdminForm


class CategoryForumAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorUploadingWidget())
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = CategoryForum
        fields = '__all__'
# Register your models here.



@admin.register(CategoryForum)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'body']
    prepopulated_fields = {'slug': ('title', )}
    form = CategoryForumAdminForm




