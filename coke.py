def main():
    print("Amount Due : 50 ")
    amount = 50 
    insert_coin(amount)


def insert_coin(amount):
   
       
       while amount >0:
          coin = int(input ("Enter Coin :") )
          if coin ==50 or coin ==25 or coin == 10 :
               amount -= coin
               print (f"Changed owed {amount}")
            
          else:
                ("enter valid coin such as 50, 15 ,10")

main()
