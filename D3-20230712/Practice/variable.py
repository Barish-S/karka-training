print("Laptop Price")
product_price=40000
delivery_charge=100+(product_price*0.01)
product_gst=(product_price+delivery_charge)*0.18
final_price=product_price+delivery_charge+product_gst
print(final_price)