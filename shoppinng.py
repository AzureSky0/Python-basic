"""
name: [{Shopping Note}]
_version_0.01
Target Users: anyone
Target System: GNU/Linux
Interface: Command-line

Objective:
    project: item Note
    condition: create an application to help listing  items and there price also help with calculating the total sum etc.
Data required : 
    name of the items
    price of the items
    total amount on the hand
Desired_output :
    list of items user need
    amount left
    total price of the item

Maintainer Email ID: akshatsahu007@gmail.com
"""
from datetime import datetime

'version_0.01'
input('PRESS ENTER TO BEGAIN.')
starting_message= 'welcome to shopping Note.'
about_the_app='This is an application to help you list item needed for listing as you would in your Note.'
statement_data_for_items='First write down the name of the item you need'
warning_for_data_for_item='{currently we can store up to 5 items and if the item to be listed is below 5 then just Enter (0) for the rest}. '
statement_data_for_price='Now Enter there price: '
statement_for_Total_cash='Enter the amount you have: '
statement_for_Total_amount='Your total price for the given items is: '
statement_for_Amount_left='So the amount left is: '
fancy_line1='#######@@@@@@|||||||||\\\\\\\\^^|||||||\\\\\\\||||||||^^|\\\\\\\\\\|||||||||^^\\\\\\\\\\|||||||||@@@@@@@######'
fancy_start_line='**********************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%$$$$$$$$$$$$$$$$$$$$$$$$$$***************'
fancy_end_line='========================================================================================================================'

# Here the the main thing starts:::
print(f'\n\n{fancy_line1}\n')
print(starting_message)
print(about_the_app)
print('\n')
print(fancy_end_line)
print(fancy_start_line)
print('\n')
Total_cash_on_Hand=input(statement_for_Total_cash)
Total_cash_on_Hand=float(Total_cash_on_Hand)
Total_cash_on_Hand=round(Total_cash_on_Hand)
Total_cash_on_Hand=int(Total_cash_on_Hand)

print('\n')
print(statement_data_for_items),print(f'[{warning_for_data_for_item}]')
print('\n')

#Item:
Item_1=input('Item 1: ')
Item_2=input('Item 2: ')
Item_3=input('Item 3: ')
Item_4=input('Item 4: ')
Item_5=input('Item 5: ')

print('\n')
print(fancy_end_line)
print(fancy_start_line)
print('\n')
print(statement_data_for_price)


if Item_1 == '0' :
    Item_1_price='0'
    Item_1_price=int(Item_1_price)
    print('\t')
else:
    Item_1_price=input('Item_1 price =RS.')
    Item_1_price=float(Item_1_price)
    Item_1_price=round(Item_1_price)
    Item_1_price=int(Item_1_price)
if Item_2 == '0' :
    Item_2_price='0'
    Item_2_price=int(Item_2_price)
    print('\t')
else:
    Item_2_price=input('Item_2 price =RS.')
    Item_2_price=float(Item_2_price)
    Item_2_price=round(Item_2_price)
    Item_2_price=int(Item_2_price)
if Item_3 == '0' :
    Item_3_price= '0'
    Item_3_price=int(Item_3_price)
    print('\t')
else:
    Item_3_price=input('Item_3 price =RS.')
    Item_3_price=float(Item_3_price)
    Item_3_price=round(Item_3_price)
    Item_3_price=int(Item_3_price)
if Item_4 == '0' :
    Item_4_price='0'
    Item_4_price=int(Item_4_price)
    print('\t')
else:
    Item_4_price=input('Item_4 price =RS.')
    Item_4_price=float(Item_4_price)
    Item_4_price=round(Item_4_price)
    Item_4_price=int(Item_4_price)
if Item_5 == '0' :
    Item_5_price='0'
    Item_5_price=int(Item_5_price)
    print('\t')
else:
    Item_5_price=input('Item_5 price =RS.')
    Item_5_price=float(Item_5_price)
    Item_5_price=round(Item_5_price)
    Item_5_price=int(Item_5_price)
    print('\t')


print(fancy_end_line)
print(fancy_start_line)
print('Now your final list is: ')
cash=(f'Initial Amount=Rs.{Total_cash_on_Hand}')
total_cost=(Item_1_price+Item_2_price+Item_3_price+Item_4_price+Item_5_price)
amount_left=(float(Total_cash_on_Hand)-float(total_cost))
final_list=f'\t\t{cash}\n\t\t\t1.{Item_1}=Rs.{Item_1_price}\n\t\t\t2.{Item_2}=Rs.{Item_2_price}\n\t\t\t3.{Item_3}=RS.{Item_3_price}\n\t\t\t4.{Item_4}=Rs.{Item_4_price}\n\t\t\t5.{Item_5}=RS.{Item_5_price}\n\t\t\tTotal price of the Item you have=Rs.{total_cost}\n\t\t\tTotal Amount Left=Rs.{amount_left}\n\n'
print(f'\n{fancy_start_line}\n')
print(f'{final_list}\n')
print(fancy_end_line)
input('Press Any Key to end')

note=open("shoppinglist.txt","w+")

note.write(f"\t\t\tYour list for shopping on {datetime.now()}\n")
note.write(f"""
{fancy_start_line}

\t{cash}\n\n\t\t\t1.{Item_1}=Rs.{Item_1_price}\n\t\t\t2.{Item_2}=Rs.{Item_2_price}\n\t\t\t3.{Item_3}=RS.{Item_3_price}\n\t\t\t4.{Item_4}=Rs.{Item_4_price}\n\t\t\t5.{Item_5}=RS.{Item_5_price}\n\t\t\tTotal price of the Item you have=Rs.{total_cost}\n\t\t\tTotal Amount Left=Rs.{amount_left}\n\n
\t{fancy_start_line}\n
{fancy_end_line}
""")

note.close()