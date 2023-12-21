from django.shortcuts import render, redirect
from django.http import HttpResponse
from Home_App.models import Book_Table, Employees, Items, CardItems, ItemsOrder
from django.contrib.auth.models import User, auth
import random
import datetime

# Create your views here.

Active_User = False
query_data = Items.objects.all()
ItemsOfDay_1 = random.choice(query_data)
ItemsOfDay_2 = random.choice(query_data)

if ItemsOfDay_1 == ItemsOfDay_2:
    ItemsOfDay_2 = random.choice(query_data)

# Get the current date
current_date = datetime.datetime.now()

# Get the day of the week as an integer (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
day_of_week = current_date.weekday()

# Define a list of day names
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
name_of_day = day_names[day_of_week]

def home(request):
    data = {
        'title' : 'Canteen Store',
        'active_user' : Active_User
    }

    return render(request, 'home.html', {'data': data, 'query_data': query_data, 'ItemsOfDay_1': ItemsOfDay_1, 'ItemsOfDay_2': ItemsOfDay_2, 'name_of_day': name_of_day })

def about(request):
    data = {
        'title' : 'About Us',
        'active_user' : Active_User
    }
    return render(request, 'about.html', {'data': data})

def order(request):
    data = {
        'title' : 'Order',
        'active_user' : Active_User
    }
    return render(request, 'order.html', {'data': data})

def book_table(request):
    data = {
        'title' : 'Book table',
        'active_user' : Active_User
    }
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        date = request.POST.get('date')
        person = request.POST.get('person')
    
        if name != '' and email != '' and number != '' and date != '' and person != '':
            date = Book_Table(Name=name, Email=email, Number=number, Date=date, Person=person)
            date.save()
            return render(request, 'thanks.html')
        
    return render(request, 'book.html', {'data': data})

order_item = False

def add_data(order_item):
    if order_item:
        user_id = order_item
        item_image  = Items.objects.get(id=order_item).Image
        item_name = Items.objects.get(id=order_item).Title
        item_type = Items.objects.get(id=order_item).Type
        item_price = Items.objects.get(id=order_item).Price

        if CardItems.objects.filter(UserId = user_id, Username = UserName).values().exists():
            my_object = CardItems.objects.get(UserId = user_id, Username = UserName)
            my_object.Price = my_object.Price + item_price
            my_object.Quantity += 1
            my_object.save()
        else:
            card_data = CardItems(Image=item_image, Name=item_name, Type=item_type, Price=item_price, UserId=user_id, Username = UserName)
            card_data.save()

def menu(request):
    global order_item
    data = {
        'title' : 'Canteen Menu',
        'active_user' : Active_User
    }

    query_data = Items.objects.all()

    if request.method == "POST":
        active = request.POST.get('show_svg')

        if active == "not_active":
            return redirect('login')
        elif active:
            order_item = active
        
        if order_item:
            add_data(order_item)
            return redirect('card')

    return render(request, 'menu.html', {'data': data, 'query_data': query_data})


def login(request):
    global Active_User, UserName
    data = {
        'title' : 'User LogIn',
        'is_exist' : False,
        'active_user' : Active_User,
    }

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Employees.objects.filter(Username = username, Password = password).values()
        
        if user.exists():
            UserName = username
            Active_User = True
            return redirect('user')
        else:
            data['is_not'] = True
            return render(request, 'login.html', {'data': data})

    return render(request, 'login.html', {'data': data})


def registration(request):
    data = {
        'title' : 'Registration Page',
        'is_correct' : False,
        'active_user' : Active_User
    }
    
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('rpassword')
        sing_up = request.POST.get('sing_up')

        if Employees.objects.filter(Password = password).values().exists():
            data['is_correct'] = "This password is already used."
        elif Employees.objects.filter(Email=email).values().exists():
            data['is_correct'] = "The Email_Id has already been used."
        elif Employees.objects.filter(Username=username).values().exists():
            data['is_correct'] = "The username has already been taken."
        elif password == repeat_password:
            if first_name != '' and last_name != '' and email != '' and username != 'username' and password != '' and repeat_password != '' and sing_up == '1':
                data = Employees(First_Name=first_name, Last_Name=last_name, Email=email, Username=username, Password=password)
                data.save()
                return redirect('login')
            else:
                data['is_correct'] = "please fill out this fields"
        else:
            data['is_correct'] = "Password is not matched !"
            return render(request, 'registration.html', {'data': data})

    return render(request, 'registration.html', {'data': data})

def user(request):
    global Active_User
    data = {
        'title' : 'User Dashboard',
        'active_user' : Active_User
    }

    if request.method == "POST":
        sing_out = request.POST.get('sing_out')

        if sing_out == '1':
            Active_User = False
            return redirect('login')
    
    employees = Employees.objects.get(Username = UserName)
    DataOfCard = ItemsOrder.objects.filter(Username=UserName)

    return render(request, 'user_dashboard.html', {'data': data, 'employees':employees, 'DataOfCard': DataOfCard})


def card(request):
    data = {
        'title' : 'Shopping Card',
        'active_user' : Active_User,
    }

    if request.method == "POST":
        pay_button = request.POST.get('pay_button')
        delete_item = request.POST.get('delete_item')
        add_item = request.POST.get('add_item')
        less_item = request.POST.get('less_item')

        if delete_item:
            data_to_delete = CardItems.objects.filter(id = delete_item, Username = UserName)
            data_to_delete.delete()
            return redirect('card')
        
        if add_item:
            data_to_add = CardItems.objects.get(id = add_item, Username = UserName)
            data_to_add.Price = data_to_add.Price + Items.objects.get(id = data_to_add.UserId).Price
            data_to_add.Quantity += 1
            data_to_add.save()
        
        if less_item:
            data_to_less = CardItems.objects.get(id = less_item, Username = UserName)
            data_to_less.Price = data_to_less.Price - Items.objects.get(id = data_to_less.UserId).Price
            data_to_less.Quantity -= 1
            if data_to_less.Quantity > 0:
                data_to_less.save()

        if pay_button == "1":
            cart_items = CardItems.objects.filter(Username=UserName)
            total_price = sum(item.Price for item in cart_items)
            data['total_price'] = total_price

            # Get the user's available coins
            user_coins = Employees.objects.get(Username=UserName).Coins

            if total_price <= user_coins:
                # The total price is within the user's available coins
                for cart_item in cart_items:
                    # Create an order item for each item in the cart
                    item_order = ItemsOrder(
                        Image=cart_item.Image,
                        Name=cart_item.Name,
                        Type=cart_item.Type,
                        Price=cart_item.Price,
                        Username=UserName,
                        Quantity=cart_item.Quantity
                    )
                    item_order.save()  # Save the order item to the database

                # Deduct the total price from the user's available coins
                Employees.objects.filter(Username=UserName).update(Coins=user_coins - total_price)

                item_order = ItemsOrder.objects.filter(Username=UserName)
                buyer_name = Employees.objects.get(Username=UserName)
                data['formatted_date'] = current_date.strftime("%B %d, %Y")
                
                # Render the invoice.html template and pass data, cart items, and buyer name
                invoice_data = {'data': data, 'cart_items': cart_items, 'buyer_name': buyer_name}
                invoice_template = 'invoice.html'
                
                # Optionally, you can redirect to an order confirmation page instead of rendering the template
                # return render(request, 'order_confirmation.html', {'invoice_data': invoice_data})
                
                # Render the invoice.html template
                response = render(request, invoice_template, invoice_data)
                
                # Clear the user's cart by deleting the cart items
                cart_items.delete()
                
                return response
            else:
                # Handle the case where the user doesn't have enough coins
                # You can show an error message or take appropriate action
                # For now, we'll print a message
                data['Insufficient_coins'] = "Insufficient coins to complete the purchase"


    DataOfCard = CardItems.objects.filter(Username = UserName)

    return render(request, 'shopping_cart.html', {'data': data, 'DataOfCard': DataOfCard})