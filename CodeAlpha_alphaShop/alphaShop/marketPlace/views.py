from django.shortcuts import render, redirect, get_object_or_404

from .models import (
    Product,
    Cart,
    CartItem,
    Order,
    OrderItem
)

from django.contrib import messages

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from .forms import RegisterForm

from django.contrib.auth.decorators import login_required
from django.db import transaction


def productList(request):

    products = Product.objects.all()

    context = {

        "products": products

    }

    return render(

        request,

        "marketPlace/product_list.html",

        context

    )



def productDetail(request, slug):

    product = get_object_or_404(

        Product,

        slug=slug

    )

    context = {

        "product": product

    }

    return render(

        request,

        "marketPlace/product_detail.html",

        context

    )


def register(request):

    if request.user.is_authenticated:

        return redirect("product_list")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(

                request,

                "Account created successfully."

            )

            return redirect("product_list")

    else:

        form = RegisterForm()

    return render(

        request,

        "marketPlace/register.html",

        {

            "form": form

        }

    )




def loginUser(request):

    if request.user.is_authenticated:

        return redirect("product_list")

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user:

            login(request, user)

            messages.success(

                request,

                "Welcome back."

            )

            return redirect("product_list")

        messages.error(

            request,

            "Invalid username or password."

        )

    return render(

        request,

        "marketPlace/login.html"

    )



@login_required
def logoutUser(request):

    logout(request)

    messages.success(

        request,

        "Logged out successfully."

    )

    return redirect("login")


@login_required
def showCart(request):

    cart = Cart.objects.filter(

        user=request.user,

        status=Cart.Status.ACTIVE

    ).first()

    return render(

        request,

        "marketPlace/cart.html",

        {

            "cart": cart

        }

    )



@login_required
def addToCart(request, productId):

    product = get_object_or_404(

        Product,

        id=productId

    )

    if product.stock <= 0:

        messages.error(

            request,

            "This product is out of stock."

        )

        return redirect(

            "product_detail",

            slug=product.slug

        )

    cart, _ = Cart.objects.get_or_create(

        user=request.user,

        status=Cart.Status.ACTIVE

    )

    item = CartItem.objects.filter(

        cart=cart,

        product=product

    ).first()
    
    if item:

        if item.quantity < product.stock:

            item.quantity += 1

            item.save()

            messages.success(
                request,
                "Product quantity updated."
            )

        else:

            messages.warning(
                request,
                "You have reached the maximum available stock."
            )

    else:

        CartItem.objects.create(

            cart=cart,

            product=product,

            quantity=1

        )

        messages.success(
            request,
            "Product added to cart."
        )

    return redirect("show_cart")



@login_required
def removeFromCart(request, itemId):

    item = get_object_or_404(

        CartItem,

        id=itemId,

        cart__user=request.user

    )

    item.delete()

    messages.success(

        request,

        "Product removed from cart."

    )

    return redirect(

        "show_cart"

    )



@login_required
def increaseQuantity(request, itemId):

    item = get_object_or_404(

        CartItem,

        id=itemId,

        cart__user=request.user

    )

    if item.quantity < item.product.stock:

        item.quantity += 1

        item.save()

    else:

        messages.warning(

            request,

            "No more stock available."

        )

    return redirect(

        "show_cart"

    )



@login_required
def decreaseQuantity(request, itemId):

    item = get_object_or_404(

        CartItem,

        id=itemId,

        cart__user=request.user

    )

    if item.quantity > 1:

        item.quantity -= 1

        item.save()

    else:

        item.delete()

    return redirect(

        "show_cart"

    )


@login_required
def checkout(request):

    cart = Cart.objects.filter(
        user=request.user,
        status=Cart.Status.ACTIVE
    ).first()

    if not cart or not cart.items.exists():

        messages.warning(
            request,
            "Your cart is empty."
        )

        return redirect("show_cart")

    if request.method == "POST":

        for item in cart.items.all():

            if item.quantity > item.product.stock:

                messages.error(
                    request,
                    f"Not enough stock for {item.product.name}."
                )

                return redirect("show_cart")

        with transaction.atomic():

            order = Order.objects.create(
                user=request.user,
                total=cart.total
            )

            for item in cart.items.all():

                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

                item.product.stock -= item.quantity
                item.product.save()

            cart.status = Cart.Status.CHECKED_OUT
            cart.save()

        messages.success(
            request,
            "Order placed successfully."
        )

        return redirect("orders")

    return render(
        request,
        "marketPlace/checkout.html",
        {
            "cart": cart
        }
    )


@login_required
def orderList(request):

    orders = (
        Order.objects
        .filter(user=request.user)
        .prefetch_related("items__product")
    )

    return render(

        request,

        "marketPlace/orders.html",

        {

            "orders": orders

        }

    )