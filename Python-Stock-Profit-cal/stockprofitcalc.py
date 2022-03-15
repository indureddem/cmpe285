

def calculations(stockSymbol, stockAllotment, stockFinalSharePrice, stockSellCommision, stockInitialSharePrice, stockBuyCommision, stockCapitalGainTaxRate):
    proceeds = int(stockAllotment) * float(stockFinalSharePrice)
    totalTax = (((float(stockFinalSharePrice) - float(stockInitialSharePrice)) * int(stockAllotment) - float(stockBuyCommision) - float(stockSellCommision)))
    tax = totalTax * float(stockCapitalGainTaxRate) / 100
    initialTotal = int(stockAllotment) * float(stockInitialSharePrice)
    cost = initialTotal + float(stockBuyCommision) + float(stockSellCommision) + tax
    netProfit = proceeds - cost
    returnOnInvestment = netProfit / cost * 100
    breakEven = (initialTotal + float(stockBuyCommision) + float(stockSellCommision)) / int(stockAllotment)

    print("Proceeds = $", proceeds)
    print("Cost = $", cost)
    print("NetProfit  = $", netProfit)
    print("Return on investment = ", returnOnInvestment, "%")
    print("Break Even Price  = $", breakEven)
    

def main():
    print("Enter stock symbol :")
    stockSymbol = input()
    print("Enter stock allotment :")
    stockAllotment = input()
    print("Enter stock final share price :")
    stockFinalSharePrice = input()
    print("Enter stock sell commision :")
    stockSellCommision = input()
    print("Enter stock initial share price :")
    stockInitialSharePrice = input()
    print("Enter stock buy commision:")
    stockBuyCommision = input()
    print("Enter stock capital gain tax rate :")
    stockCapitalGainTaxRate = input()

    calculations(stockSymbol, stockAllotment, stockFinalSharePrice, stockSellCommision, stockInitialSharePrice, stockBuyCommision, stockCapitalGainTaxRate)

if __name__ == '__main__':
    main()

    