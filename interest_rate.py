money = float(input('How much money is in the account initially?'))
percent = float(input("What is the interest rate?"))
years = int(input("How many years?"))
interest = money * (1 + (percent/100))**years
print interest, "This is your total amount after", years, "years."
