from dashboard.models import Book
from django.forms import ModelForm, forms
from django.utils.text import slugify


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'description',
        ]

    # def clean_title(self):
    #     title = self.cleaned_data["title"]
    #     slug = slugify(title)
    #     try:
    #         book = Book.objects.get(slug=slug)
    #         raise forms.ValidationError("Title Already Exists. Please try a different one.")
    #     except Book.DoesNotExist:
    #         return title
    #     except:
    #         raise forms.ValidationError("Title Already Exists. Please try a different one.")
