apples=int(input("How many apples do you want?"))
per_unit = 5
cart_value = 5 * apples
print(f"Your total cart value is:{cart_value}")
discount = 0.1 * cart_value
discounted_value = cart_value - discount
print(f"After applying discount the cart value is: {discounted_value}")
tax_value = 0.08 * discounted_value
taxed_value = discounted_value + tax_value
print(f"After adding tax, the total cart value is: {taxed_value}")
name=(input("Please enter your name: "))
print(f"{name} THANK YOU, for shopping here!")
