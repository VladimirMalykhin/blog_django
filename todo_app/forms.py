from django import forms

from todo_app.models import Blog, Comments


class TodoForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body')


class TodoFullForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body')


class ToCommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)
