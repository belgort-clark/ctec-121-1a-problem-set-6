# CTEC 121
# Author: Bruce Elgort
# problem-set-6-problem-1.py

"""
INSTRUCTIONS:
READ ALL OF THE INSTRUCTIONS BEFORE YOU START WORKING ON THE CODE
0) The code below will not run.
1) The code below contains 5 errors.
2) Your job is to fix the errors and to place a comment above the line or to the right of the line that
   contains the error and tell me what you fixed.
3) Make sure the code runs.
4) Re-read Steps 1 - 3 above :-).
"""


def main():
    # get the day month and year as numbers
    day = integer(input("Enter the day number: "))
    month = int(input("Enter the month number: '))
    year == int(input("Enter the year: "))

    # concatenate the numbers together by converting each variable to a string
    date1 = str(month) "/" + str(day) + "/"+str(year)

    # define a list of the months of the year
    months = ["January"  "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]

    # Take the number entered by the user and subtract 1 since Python lists start index 0
    monthStr = months[month-1]

    # concatenat the data together again converting numbers to strings
    date2 = monthStr+" " + str(day) + ", "  str(year)

    # display the date
    print("The date is", date1, "or", date2+".")


main()
