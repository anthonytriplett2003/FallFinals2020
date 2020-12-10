total=0
tax=7
sandwhich = input("Please pick a type of sandwhich, krabby patty(kp) for $1.25, double krabby patty(d) for $2.00, triple krabby patty(t) for $3.00")
cheese = input("Would you like cheese on that? ")
if(cheese=="y"):
    cheese=input("cheese(c) for $.25")
print(sandwhich)

meals = input("Pick a meal of your choice, krabby meal(km) for $3.50, double kraby meal(dm) for $3.75, triple krabby meal(tm) for $4.00, salty dog (sd) for $1.25, footlong(f) for $2.00, sailors surprise(ss) for $3.00, golden loaf(gl) for $2.00")
print(meals)

sides = input("Would you like a side of coral bits or kelp rings? ")
if(sides=="y"):
    sides=input("coral bits s for $1.00, m for $1.25, l for $1.50, kr for $1.50")
print(sides)

beverage = input("Would you like a drink, y or no? ")
if(beverage=="y"):
    beverage=input("s for $1.00, m for $1.25, l for $1.50, ks for $2.00")
    print("you said",beverage, "drink")  #print(string,string,string,string)

sauces = input("Any sauces with your order? ")
if(sauces=="y"):
    sauces=input("s for $.50")
    print(sauces)

if sandwhich=="kp":
    total += 1.25
elif sandwhich=="d":
    total += 2.00
elif sandwhich=="t":
    total += 3.00

if cheese=="c":
    total+=.25

if meals=="km":
    total+= 3.50
elif meals=="dm":
    total+= 3.75
elif meals=="tm":
    total+= 4.00
elif meals=="sd":
    total+= 1.25
elif meals=="f":
    total+= 2.00
elif meals=="ss":
    total+= 3.00                    
elif meals=="gl":
    total+= 2.00

if sides=="s":
    total+= 1.00
elif sides=="m":
    total+= 1.25
elif sides=="l":
    total+= 1.50
elif sides=="kr":
    total+=1.50

if beverage=="s":
    total += 1.00
elif beverage=="m":
    total += 1.25
elif beverage=="l":
    total += 1.50
elif beverage=="ks":
    total+= 2.00

if sauces=="s":
    total+= .50

print(total+tax)

#print("You're total is",total)
print('${:,.2f}'.format(total)

('''
Your order is: 
    {} sandwich,
    {} cheese,
    {} meals,
    {} sides,
    {} sauces,
For a total of ${:,.2f}
'''.format(sandwhich,cheese, meals,sides, beverage,sauces,total))