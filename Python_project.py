def age_duration(age, time_unit):

    # Defferent  units in a year
    
    months_in_year = 12
    weeks_in_year = 52.17    #incluiding leap year
    days_in_year = 365.25    #incluiding  leap year
    hours_in_year = 365 * 24
    minutes_in_year = 365 * 24 * 60
    seconds_in_year = 365 * 24 * 60 * 60

    # Calculate duration based on the selected time unit
    if time_unit.lower() in ['months', 'm']:
        return age * months_in_year
    elif time_unit.lower() in ['weeks', 'w']:
        return age *  weeks_in_year
    elif time_unit.lower() in ['days', 'd']:
        return age * days_in_year
    elif time_unit.lower() in ['hours', 'h']:
        return age * hours_in_year
    elif time_unit.lower() in ['minutes', 'min']:
        return age * minutes_in_year
    elif time_unit.lower() in ['seconds', 's']:
        return age * seconds_in_year
    else:
        return None

def main():
    age = int(input("Please Enter your age........= "))
    time_unit = input("\n Please choose time unit: Months, Weeks, Days, Hours, Minutes, Seconds.\n\n"
                      "Note: You can write the first letter or the full name of the time unit. ")
    
    duration = age_duration(age, time_unit)
    
    if duration is not None:
        print(f"\n Wow!!!! You lived for {duration} {time_unit}.  Great.....")
    else:
        print("Invalid time unit selected.")

if __name__ == "__main__":
    main()
