from dashboard.forms import BookForm
from dashboard.models import Book
from django.contrib import admin

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    readonly_fields = ['slug', 'updated', 'timestamp', 'added_by', 'last_edited_by']
    form = BookForm


admin.site.register(Book, BookAdmin)
