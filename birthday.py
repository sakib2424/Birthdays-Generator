# birthday.py
import mydate

number_of_sims = input("How many times should I run the simulation?\n")
number_of_birthdays = input("How many birthdays should I generate per trial?\n")

def generate_sims(number_of_sims, number_of_birthdays):
    number_of_trials_with_dups = 0
    for i in range(int(number_of_sims)):
        birthdays = []
        for j in range(int(number_of_birthdays)):
            birthdays.append(mydate.generate_date(1900,2019))
        final = mydate.remove_years(birthdays)
        # print (final)
        duplicates = []
        dup_counter = 0
        while (len(final) > 0):
            current = final.pop()
            if current in final:
                duplicates.append(current)
                dup_counter += 1
                while current in final:
                    final.remove(current)
        duplicates_formatted = mydate.dates_to_strings(duplicates)

        if (dup_counter == 0):
            print("Trial #" + str(i + 1) + ": " + "No dates are the same.")
        elif (dup_counter == 1):
            number_of_trials_with_dups += 1
            print("Trial #" + str(i + 1) + ": " + str(dup_counter) + 
            " date occurs more than once! (" + 
            str(duplicates_formatted).strip("[]").replace("'", "") + ")")
        else:
            number_of_trials_with_dups += 1
            print("Trial #" + str(i + 1) + ": " + str(dup_counter) + 
            " dates occur more than once! (" + 
            str(duplicates_formatted).strip("''[]").replace("'", "") + ")")

    print("\nResults:\n=====")
    print("Out of " + str(number_of_sims) + " trials, " + 
    str(number_of_trials_with_dups) + " had dates that were repeated")

    # percentage = str (100 * 
    # float(number_of_trials_with_dups)/float(number_of_sims)) + "%"

    percentage = "{0:.2f}".format(100 * 
    float(number_of_trials_with_dups)/float(number_of_sims))

    # print ("Numerator: " + str(number_of_trials_with_dups))
    # print("Denomentaor: " + number_of_sims)
    # print ("Percentage: " + str(percentage))

    print("We can conclude that you have a " + 
    percentage + 
    " chance of sharing a birthday with someone if you are in a group of " +
    number_of_birthdays + " people")


generate_sims(number_of_sims, number_of_birthdays)
