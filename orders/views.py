from django.shortcuts import render

from .models import *
from shop.models import *
from users.models import *

def basket(request):
    user, _ = UserBasket.objects.get_or_create(user_kay=request.session.session_key)   # *
    lst_product = ProductInBasket.objects.filter(user_basket=user)
    # lst_product.delete()
    return render(request, "basket.html", {"products":lst_product})




def order_create(request):
  name = data.get("name")
  email = data.get("email")
  telephone = data.get("telephone")
  print(telephone) 
  print(data)

  new_order = Orders.objects.create(customer_name=name,customer_email=email,customer_telephone=telephone)
  #new_product_in_order = ProductInOrder.objects.create(order=new_order,name=Product(basket_name_id),number=number)
  summary_price = 0
  for item in data.get('basket'):
    total_price = int(item["number"])*float(item["price"])
    summary_price += total_price
    product = Product.objects.get(id=item["id"])
    product.quantity = item["quantity"]-item["number"]
    product.save()

    new_product_in_order = ProductInOrder.objects.create(order=new_order,name=Product(item["id"]),number=item["number"],total_price=total_price)
  new_order.total_pice = summary_price
  new_order.save()
  return render(request,'Product/info_about_name.html',locals())