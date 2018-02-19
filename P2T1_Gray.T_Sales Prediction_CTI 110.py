# CTI-110 
# P2T1 - Sales Prediction 
# Ta'Mera Gray
# 18 February 2018

def main () :
    
    #Get the totalSales
    totalSales = float(input("Enter the projected amount of total sales: "))

    #calculate the annualProfit
    annualProfit = 0.23 * totalSales

    #display the annualProfit
    print( "Profit will be: ", format(annualProfit, ",.2f"))

main () 
