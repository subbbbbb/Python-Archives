import matplotlib.pyplot as plt 
import math

stateList = {"Alabama":0.035, "Alaska":0, "Arizona":0.03565, "Arkansas":0.039, "California": 0.0715, "Colorado":0.0463, "Connecticut":0.04995, "Delaware": 0.044, "Florida":0, "Georgia":0.03375, "Hawaii":0.062, "Idaho":0.04025, "Illinois":0.0495, "Indiana":0.0323, "Iowa":0.0443, "Kansas":0.044, "Kentucky":0.05, "Louisiana":0.04, "Maine":0.06475, "Maryland":0.03875, "Massachusetts":0.0505, "Michigan":0.0425, "Minnesota":0.076, "Mississippi":0.04, "Missouri":0.037, "Montana":0.0395, "Nebraska": 0.0465, "Nevada":0, "New Hampshire":0.05, "New Jersey":0.06075, "New Mexico":0.033, "New York":0.0641, "North Dakota":0.02, "Ohio":0.034885, "Oklahoma":0.0275, "Pennsylvania":0.0307, "Rhode Island":0.0487, "South Carolina":0.0405, "South Dakota":0, "Tennessee":0, "Texas":0, "Utah":0.0495, "Vermont":0.0615, "Virginia":0.03875, "Washington":0, "West Virginia":0.0475, "Wisconsin":0.05825, "Wyoming":0, "District of Columbia":0.06475}


def getState():
    state = input("Enter in the state that you live in")
    taxRate = stateList[state]
    return taxRate

def getSalary():
    taxRate = getState()
    salary = float(input("Enter in your monthly salary"))
    return salary
    
def getTax():
    salary = getSalary()
    taxRate = getState()
    tax = salary*taxRate
    print("Keep in mind, due to a variety of variables, your income tax will vary, depending on state legislature, this provides an average estimate")
    print("$" + str(tax))

def main():
    salary = getSalary()
    print("We will separate your basic budget into 5 categories - Housing, Food, Transportation, Bills/Utilities/Health Care, Leisure")
    housing = float(input("Enter in how much you spend on housing/rent/etc."))
    transportation = float(input("Enter in how much you spend on transportation (traveling to work/ridesharing/etc.)"))
    bills = float(input("Enter in how much you spend on all of your other bills (utilities, subscriptions, healthcare fees/medications, etc.) "))
    lesiure = float(input("Enter in how much you spend on any other \"fun\" things."))
    savings = (salary) - (housing + transportation + bills + lesiure)
    
    labels = "Housing", "Transportation", "Bills", "Leisure", "Savings"
    sizes = [housing, transportation, bills, lesiure, savings]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')

    plt.show()

    if (housing + transportation + bills + lesiure < salary):
        print("You are saving $" + str(savings) + " every month.")
    if(housing + transportation + bills + lesiure > salary):
        print("You are spending more than you are making and going into debt of $" + str(abs(savings)) + " every month.")   

main()

