import math  
#title
print("Dokkan Battle Zeni calculator By Reds#9999 on Discord and RedsLovesGames on Github")
print("-------------------------------------------------")
print("Enter values in corresponding area")
print("----------------------------------")
#entering values
Bronze_Statues = int(input("Enter Amount of Bronze Hercule Statues): "))  

Silver_Statue = int(input("Enter Amount of Silver Hercule Statues): "))

Gold_Statues = int(input("Enter Amount of Gold Hercule Statues): "))

Platinum_Statues = int(input("Enter Amount of Platinum Hercule Statues): "))

Diamond_Statues = int(input("Enter Amount of Diamond Hercule Statues: "))

Purse_Zeni = int(input("Enter Your Banks Zeni: "))
#Math time
print("-----------------------------------------")
Total_Zeni = (
((Bronze_Statues*250000) + (Silver_Statue*500000) + (Gold_Statues*1000000) + (Platinum_Statues*1500000) + (Diamond_Statues*5000000) + (Purse_Zeni))
)

print(Total_Zeni)
#final judgements
if Total_Zeni > 1999999999:
  print("Rich Boi")
elif Total_Zeni < 1999999999:
  print("Broke Boi")

k=input("press any key to close")