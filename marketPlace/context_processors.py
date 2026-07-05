from .models import Cart


def cart_context(request):

    if request.user.is_authenticated:

        cart = Cart.objects.filter(
            user=request.user,
            status=Cart.Status.ACTIVE
        ).first()

        if cart:

            return {

                "cartItemCount": cart.itemCount,

                "activeCart": cart

            }

    return {

        "cartItemCount": 0,

        "activeCart": None

    }