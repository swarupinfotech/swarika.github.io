from django.contrib import admin
from Home_App.models import Book_Table, Employees, Items, CardItems, ItemsOrder

# Register your models here.

class Book_TableAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Number', 'Date', 'Person')

    def Name(self, obj):
        return obj.Name  # Replace 'Name' with the actual field name in your Items model
    
    def Email(self, obj):
        return obj.Email  # Replace 'Email' with the actual field name in your Items model

    def Number(self, obj):
        return obj.Number  # Replace 'Number' with the actual field name in your Items model

    def Date(self, obj):
        return obj.Date  # Replace 'Date' with the actual field name in your Items model

    def Person(self, obj):
        return obj.Person  # Replace 'Person' with the actual field name in your Items model

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Username', 'user_email', 'Coins')

    def Name(self, obj):
        return obj.First_Name + ' ' +  obj.Last_Name # Replace 'First_Name' and 'Last_Name with the actual field name in your Items model
    
    def Username(self, obj):
        return obj.Username  # Replace 'Username' with the actual field name in your Items model

    def user_email(self, obj):
        return obj.Email  # Replace 'Email' with the actual field name in your Items model

    def Coins(self, obj):
        return obj.Coins  # Replace 'Coins' with the actual field name in your Items model

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('Type', 'item_title', 'item_description', 'item_price', 'item_quantity')

    def item_title(self, obj):
        return obj.Title  # Replace 'title' with the actual field name in your Items model
    
    def Type(self, obj):
        return obj.Type  # Replace 'type' with the actual field name in your Items model

    def item_description(self, obj):
        return obj.Decription  # Replace 'description' with the actual field name in your Items model

    def item_price(self, obj):
        return obj.Price  # Replace 'price' with the actual field name in your Items model

    def item_quantity(self, obj):
        return obj.Quantity  # Replace 'quantity' with the actual field name in your Items model

class CardItemsAdmin(admin.ModelAdmin):
    list_display = ('Username', 'item_title', 'item_price', 'total_Items')

    def Username(self, obj):
        return obj.Username  # Replace 'Username' with the actual field name in your Items model
    
    def item_title(self, obj):
        return obj.Name  # Replace 'Name' with the actual field name in your Items model

    def item_price(self, obj):
        return obj.Price  # Replace 'price' with the actual field name in your Items model
    
    def total_Items(self, obj):
        return obj.Quantity  # Replace 'Quantity' with the actual field name in your Items model

class ItemsOrderAdmin(admin.ModelAdmin):
    list_display = ('Username', 'item_title', 'item_price', 'total_Items')

    def Username(self, obj):
        return obj.Username  # Replace 'Username' with the actual field name in your Items model
    
    def item_title(self, obj):
        return obj.Name  # Replace 'Name' with the actual field name in your Items model

    def item_price(self, obj):
        return obj.Price  # Replace 'price' with the actual field name in your Items model
    
    def total_Items(self, obj):
        return obj.Quantity  # Replace 'Quantity' with the actual field name in your Items model

admin.site.register(Book_Table, Book_TableAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(CardItems, CardItemsAdmin)
admin.site.register(ItemsOrder, ItemsOrderAdmin)