from django.contrib import admin
from .models import FakeData
import decimal, csv
from django.http import HttpResponse

admin.site.site_header = 'Mani Kumar'

def export_books(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    writer = csv.writer(response)
    writer.writerow(['id','first_name','last_name','email','job','salary','city'])
    books = queryset.values_list('id','first_name','last_name','email','job','salary','city')
    for book in books:
        writer.writerow(book)
    return response
export_books.short_description = 'Export to csv'
class Fakeadmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','job','salary','city')
    list_filter = ('first_name',)
    search_fields = ('first_name',)
    actions = ['', export_books]
admin.site.register(FakeData,Fakeadmin)