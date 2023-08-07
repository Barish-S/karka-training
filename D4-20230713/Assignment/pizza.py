print("Price Of The Pizza")
product_price=500
print(product_price)
print("Price Of Extra Toppings")
extra_toppings=45
print(extra_toppings)
print("Price Of Soft Drinks")
soft_drink=50
print(soft_drink)
print("Your Total Order Price")
total_order=((product_price)*2+extra_toppings+(soft_drink)*3)
print(total_order)
print("Delivery Charge")
delivery_charge=50
print(delivery_charge)
total_delivery=(total_order+delivery_charge)
print("GST - 18%")
gst=total_delivery*.18
print(gst)
print("Final Price")
final_price=(total_delivery+gst)
print(final_price)