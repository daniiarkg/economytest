from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.





class OthersInline(admin.StackedInline):
    model = Others
    extra = 1

class SubconsInline(admin.StackedInline):
    model = Subcons
    extra = 1

class OwnprAdmin(admin.ModelAdmin):
    inlines = [OthersInline,]
    list_display = ['name']
    readonly_fields = ['total']
    @admin.display(description='Общая себестоимость')
    def total(self,obj):
        return format_html( str( sum( [ obj.material + obj.work + obj.social + obj.amort ] + [ i.money for i in Others.objects.filter(cons=obj.id) ] ) if obj.material else 'Сумма будет указана после введения данных'  ) )

class ConsumptionsAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['total']
    inlines = [SubconsInline,]

    @admin.display(description='Сумма расходов')
    def total(self,obj):
        return format_html(str( sum( [ i.total for i in Subcons.objects.filter(con=obj.id) ] ) ))

admin.site.register(Ownpr, OwnprAdmin)
admin.site.register(Consumptions, ConsumptionsAdmin)