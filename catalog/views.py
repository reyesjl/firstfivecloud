from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Category, WRSInqueries
from django.core.mail import send_mail

def handleFetchHome(request):
    return render(request, "catalog.html")

def handleFetchWrs(request):
    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # create the wrs catalog inquery
        wrs_inquery = WRSInqueries(name=name, email=email, phone=phone, message=message)
        wrs_inquery.save()

        # Send email to this user and to admins
        # .... coming soon .... 5v.0.1
        
        # Redirect to success page
        return redirect("home")
    context = {"activelink": "catalog"}
    return render(request, "products/wrs_products.html")

def handleFetchProducts(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)
    return render(
        request,
        "products/product_list.html",
        {"products": products, "categories": categories},
    )

def handleAddProduct(request):
    if request.method == "POST":
        product_name = request.POST.get("productName")
        product_price = request.POST.get("productPrice")

        # Validate the data here. For example, make sure all fields are filled and the price is a number
        # If the data is not valid, you can send a message and render the form again
        if not product_name or not product_price:
            messages.error(request, "Invalid input. Please try again.")
            return render(request, "products/add_product.html")

        # Save the new product to database
        Product.objects.create(name=product_name, price=product_price)
        messages.success(request, "Product added successfully!")

        # After successfully saving the new product redirect to the same page or any other page
        return redirect("add_product")

    # GET request
    return render(request, "products/add_product.html")
