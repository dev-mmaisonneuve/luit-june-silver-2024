purchase_days_ago = int(input('How many days ago have you purchased the item? '))
is_used = input('Have you used the item at all [y/n]? ')
is_broken = input('Has the item broken down on its own [y/n]? ')
 
if(is_broken == 'y' or (purchase_days_ago <= 10 and is_used == 'n')):
  print('You can get a refund.')
else:
  print('You cannot get a refund.')


# second way

# Ask the user the three questions
days_ago = int(input("How many days ago have you purchased the item? "))
used_item = input("Have you used the item at all [y/n]? ")
broken_down = input("Has the item broken down on its own [y/n]? ")

# Determine if the user can get a refund
if (days_ago <= 10 and used_item == "n") or broken_down == "y":
    print("You can get a refund.")
else:
    print("You cannot get a refund.")
