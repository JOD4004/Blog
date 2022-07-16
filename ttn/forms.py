
from django.forms import ImageField, ModelForm,TextInput, Textarea
from .models import Post,Comment

#Forms
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','description',  'content', 'place','img']

        widgets = {
            'title': TextInput(attrs={
                'class': "title",
                'placeholder': '',
                'style': 'width: 40%;',
                }),
            'description': TextInput(attrs={
                'class': "description", 
                'placeholder': 'Short Description'
                }),
            'content':Textarea(attrs={
                'class':"content",
                'placeholder':'Write the full article here'
            }),
            'place':TextInput(attrs={
                'class':'place',
                'placeholder':'Exact Location '
            }),

        }
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': Textarea(attrs={
                'placeholder': 'Comment',
                'tag':'Comment',
                })
                }