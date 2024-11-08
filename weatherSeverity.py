# Initializing rain and wind values and lists
rain = 0
wind = 0
rainList = []
windList = []

# Initial input for rain and wind
rainAndWind = input("Please enter the expected rainfall (in inches) and wind (in mph) separated by a space. Enter -1.0 to end and calculate weather severity.:\n")

# While loop with sentinel value as -1.0 or -1
while rainAndWind != "-1.0" and rainAndWind != "-1":
    # Transforming input separated by space into one list
    weatherList = rainAndWind.split(' ')

    # Ensuring input is in correct format
    if len(weatherList) != 2:
        print("Your input is invalid. Please enter rain and wind separated by a space.\n")

    else:

        # Separating list indexes into new lists for respective rain and wind
        rain = float(weatherList[0])
        wind = float(weatherList[1])

        # Adding individual values for rain and wind from input into lists
        rainList.append(rain)
        windList.append(wind)

    # Creating a new line after each request for input
    print()

    # Requesting input again to continue loop
    rainAndWind = input("Please enter the expected rainfall (in inches) and wind (in mph) separated by a space. Enter -1.0 to end and calculate weather severity.:\n")

# Calculating number of reading for print statement, only rain list is needed since numbers are forced to be entered in proper format
numberOfReadings = int(len(rainList))

# Ensuring there are readings
if numberOfReadings > 0:

    # Determining averages for rain and wind
    averageRain = sum(rainList)/len(rainList)
    averageWind = sum(windList)/len(windList)

    # Implementing weather severity formula
    weatherSeverity = (averageRain * 10) + averageWind

    # Printing average rain and wind with weather severity
    print("The average rain is", "%0.1f" % averageRain, "inches.")
    print("The average wind is", "%0.1f" % averageWind, "mph.")
    print("The weather severity for these", numberOfReadings, "readings is:", "%0.1f" % (weatherSeverity) +".")

else:
    print("You have not entered any data. Program stopped.")