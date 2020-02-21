# Birthdays-Generator
Apparently, in a set of 23 randomly chosen people, there's a pretty good chance that two of those people will have the same birthday! Yes, it's actually true, and it's called the Birthday Problem or the Birthday Paradox. betterexplained.com has a good write-up on why, but we'll use a computer simulation to approximate this probability. We'll create tools to randomly generate dates, and then we'll see if any month and day combinations match.
Assignment #1 - Modules, Strings, Lists, Dictionaries, File I/O - Due Thursday, Feb 6th at 11pm
This assignment consists of two parts:

## Part 1 - Happy Birthday!
Apparently, in a set of 23 randomly chosen people, there's a pretty good chance that two of those people will have the same birthday! Yes, it's actually true, and it's called the Birthday Problem or the Birthday Paradox. betterexplained.com has a good write-up on why, but we'll use a computer simulation to approximate this probability. We'll create tools to randomly generate dates, and then we'll see if any month and day combinations match.

You'll be doing this in two parts:
1. write a bunch of functions to help with creating dates
2. create an interactive program that allows you to run the simulation multiple times
3. Open mydate.py in a text editor of your choice
4. Write the following functions in mydate.py to help implement your program:
* is_valid_month_num(n)
* month_num_to_string(month_num)
* date_to_string(date_list)
* dates_to_strings(date_list)
* remove_years(date_list)
* is_leap_year(year)
* get_num_days_in_month
* generate_date(start_year, end_year)
5. Using your previously implemented mydate.py as a module, import it and use it to help write birthday.py
* In birthday.py, you'll write a simulation by generating random birthdays
* The simulation will be an interactive program that asks the user how many trials to run… as well as other parameters for generating birthdays for a group of people
* The percentage of times that at least one duplicate occurs should be printed out at the end

### is_valid_month_num(n)
#### Parameters:
n - an integer representing a month, with 1 being January and 12 being December
Return Value:

a boolean - True if number passed in is between 1 and 12 inclusive, False otherwise
Description:

is_valid_month_num will take a month in numeric format and return a boolean value based on whether that number is a valid month (1 through 12, inclusive)

#### Example Usage:
result1 = is_valid_month_num(3) 
print(result1) # True
result2 = is_valid_month_num(37) 
print(result2) # False

### month_num_to_string(month_num)
#### Parameters:

month_num - an integer representing a month, with 1 being January and 12 being December
Return Value:

a string - the month name corresponding to the number passed in, None if the number passed in is invalid
Description:

month_num_to_string will take a month in numeric format and return a string representing the month's name (given a valid month number). If the month number passed in is not valid, None is returned (either implicitly by not returning anything or by explicitly returning None).

#### Example Usage:
result1 = month_num_to_string(1) 
print(result1) # 'January'
result2 = month_num_to_string(10) 
print(result2) # 'October'
result3 = month_num_to_string(234) 
print(result3) # None
date_to_string(date_list)
#### Parameters:
date_list - a three-element list containing integers representing a year, month and day; for example, [2012, 3, 14] represents March 14th, 2012
Return Value:

a string - the string version of the date passed in as the original list; the format of the string returned is month_name day_number, year: March 14th, 2012
Description:

date_to_string assumes that it will be passed a list containing valid numbers for year, month and day (you will not have to check the numbers passed in). Given [YEAR_NUMBER, MONTH_NUMBER, DAY_NUMBER], this function will construct a string in the format of MONTH_NAME DAY_NUMBER, YEAR_NUMBER where MONTH_NAME is determined by using one of the previous function with MONTH_NUMBER.

For example, [1979, 10, 7] should give back 'October 7, 1979'.

#### Example Usage:

date_to_string([1979, 10, 7]) 
returns the string: October 7, 1979
dates_to_strings(list_of_date_lists)
Parameters:

list_of_date_lists - a list containing dates, with each date being a sub list of composed of three elements (as described in date_to_string)
Return Value:

a list - a list of string versions of each sub list (date) from the original list passed in
Description:

dates_to_strings converts a list of lists to a list of strings. Each inner list in the list of lists is a date in the format of a three-element list (as explained in the previous function). The result is a list of strings, with each string representing one of the original dates in the list passed in. For example, [[1979, 10, 7], [2000, 2, 20]] should give back ['October 7, 1979', 'February 20, 2000'].

Example Usage:

res = dates_to_strings([[1979, 10, 7], [2000, 2, 20]]) 
print(res) # ['October 7, 1979', 'February 20, 2000']
remove_years(list_of_date_lists)
Parameters:

list_of_date_lists - a list containing dates, with each date being a sub list composed of three elements (as described in date_to_string)
Return Value:

a list - a new list with 2-element sub lists representing a month and a day (year is removed)
Description:

remove_years creates a new list with the year element removed for every sub list in a list of date lists. This essentially converts a list of three-element lists to a list of two-element lists.

Example Usage:

res = remove_years([[1979, 10, 7], [2000, 2, 20]]) 
print(res) # [[10, 7], [2, 20]]
is_leap_year(year)
Parameters:

year - an int specifying the year to check
Return Value:

a boolean - True if the year, year, is a leap year, False otherwise
Description:

Determines whether a year is a leap year or not using this algorithm from microsoft. Returns True or False accordingly.

Show Hint


Example Usage:

for year in [1988, 1992, 1996, 1600, 2000, 2400]:
    print(is_leap_year(year)) # True for each one!

for year in [1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600]:
    print(is_leap_year(year)) # False for each one!
get_num_days_in_month(month_num, year)
Parameters:

month_num - an int specifying the month number
year - an int specifying the year to check
Return Value:

an int - the number of days for the month represented by month_num at year, year or None if the month_num passed in is not valid
Description:

Determines the number of days in a month given a month (in the format of a number from 1 through 12), as month_num and a year as year. Leap years should be taken into account (February may have 28 or 29 days). You can map months with their days by storing number of days in a list. The position of the number of days in the list will help determine what month it's in. If the month number passed in is not between 1 and 12, inclusive, then give back None (this could be done implicitly by no having a return or by explicitly returning None).

Show Hint


Example Usage:

get_num_days_in_month(2, 1988) # 29
get_num_days_in_month(2, 1900) # 28
get_num_days_in_month(11, 1900) # 30
get_num_days_in_month(12, 1900) # 31
get_num_days_in_month(1, 1900) # 31
get_num_days_in_month(30, 1999) # None
generate_date(start_year, end_year)
Parameters:

start_year - an int specifying the minimum year that the randomly generated date may have
end_year - an int specifying the maximum year that the randomly generated date may have
Return Value:

a list - a new list consisting of 3 ints: a year, month number, and a day
Description:

generate_date creates a date with random, month, day and year using other functions from this module. The date generated must have a year that falls within start_year and end_year. It must also generate a valid month number (1 through 12)… and lastly a valid number of days (including a valid number of days for February during leap years).

Show Hint


Example Usage:

date = generate_date(2015, 2017) 
print(date) # a random 3 element list, like: [2017, 9, 5]
Interactive Program (birthday.py)
Once you've finished your functions, write an interactive program that simulates creating a group of people, each with a random birthday. To do this:

Open birthday.py if you haven't done so already
Using your mydate module
First, ask how many times the simulation should be run
How many times should I run the simulation?
Then, ask wow many birthdays should be generated
How many birthdays should I generate per trial?
Once you have the user input…
repeat the following based on the number of trials specified by the user:
generate the number of birthdays specified (you can use and start and end year to create these dates)
remove the years from the dates
find the dates that occur more than once
print out the following:
the trial number
the number of dates that occur more than once
and a comma separated list of the duplicate dates, in parentheses
here's some example output:
Trial #1: 2 dates occur more than once! (August 2, April 24)
Trial #2: 1 date occurs more than once! (September 16)
How many times should I run the simulation?
Trial #3: No dates are the same.
.
.
.
After running all of the trials specified…
calculate the probability that there will be duplicates by…
taking the count of trials where at least one date occurred more than once
…and dividing that by the number of trials specified
output the resulting number as a percentage with the following information:
the total number of trials
the total number of trials that had a birthday that occurred more than once
the probability of a duplicate
the number of birthdays generated for every trial
for example:
Results:
=====
Out of 7 trials, 4 had dates that were repeated
We can conclude that you have a 57.14% chance of sharing a birthday with someone if you are in a group of 23 people
An example of a full run of the program is below:
How many times should I run the simulation?
>7
How many birthdays should I generate per trial?
>23
Trial #1: 2 dates occur more than once! (August 2, April 24)
Trial #2: 1 date occurs more than once! (September 16)
Trial #3: No dates are the same.
Trial #4: 2 dates occur more than once! (February 4, July 21)
Trial #5: No dates are the same.
Trial #6: 1 date occurs more than once! (September 14)
Trial #7: No dates are the same.

Results:
=====
Out of 7 trials, 4 had dates that were repeated
We can conclude that you have a 57.14% chance of sharing a birthday with someone if you are in a group of 23 people
Part 2 - Oh Darcy
Using a book from project Gutenberg:

download a txt version of any book you like
in jupyter lab, edit the notebook book.ipynb
in a markdown cell, write a question you'd like answered about the book that might require some programming… for example:
who was the most frequently mentioned character in Pride and Prejudice?
are the pronouns in Frankenstein predominantly male or female?
etc. …. (feel free to use either of the above questions, or come up with your own!)
open the txt version of the book that you downloaded through code
use jupyter notebook code cells to analyze the text in your file…and come up with an answer
a dictionary must be part of your analysis
document your steps in markdown cells
your answer does not have to be correct (or even exact!)… as long as you have some description of your analysis
include the txt file in your repository
