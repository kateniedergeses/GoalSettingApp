"""Kate Pohlman
Advanced Python
Spring 2021
Dr. Belinda Copus
Goal setting app:
app to produce personalized calendar
that increases time increments to achieve goals.

"""
from ExerciseGoal import ExerciseGoal
from GeneralGoal import GeneralGoal
from StressManagementGoal import StressManagementGoal


def main():

    #Dictionaries to reference time frame and goals
    timeFrameDict = {
        1: 30,
        2: 60,
        3: 90
    }

    goalDict = {
        1: "a GENERAL GOAL",
        2: "EXERCISING",
        3: "STRESS MANAGEMENT"
    }

    #Welcome message
    print("Welcome to your personalized goal setting application!")
    print("Let's get started!")
    print("Please select which goal you would like to work on.")

    goalType = 0
    #GOALTYPE
    #validate input is only an integer between 1 & 3
    while True:
        try:
            while goalType < 1 or goalType > 3:
                goalType = int(input("Enter 1 for general goals, 2 for exercise goals, and 3 for "
                                     "stress management goals: "))
                if goalType < 1 or goalType > 3:
                    print("You entered a number other than 1, 2, or 3. "
                          "Please re-enter your choice.\n")
            break
        except ValueError:
            print("Please input integer only.")
            continue

    print("\nGreat. Now we are going to build a plan depending on "
          "where you are and where you want to be. ")

    startTime = -1

    #STARTTIME: Prompt user to chose number of minutes they currently spend
    while True:
        try:
            while startTime < 0 or startTime > 89:
                startTime = int(input("\nHow many minutes per day do you spend on "
                                      "this goal currently? "))
                if startTime < 0:
                    print("You entered a negative time. Please enter zero or a positive time. ")
                while startTime > 89:
                    correctInput = input(
                        "You entered that you spend 90 minutes or more a day. "
                        "Is this correct? Enter Y for "
                        "yes, N for no. ")
                    if correctInput.upper()[0] == 'Y':
                        print("It looks like you a bit advanced for this program.   Good for you!")
                        print("Here is a link to a program that might serve you better. "
                              "https://gmb.io/setting-goals/.")
                        quit()
                    if correctInput.upper()[0] == 'N':
                        print("Please re-enter How many minutes a day you spend on this goal: ")
                        startTime = int(input("\nHow many minutes per day do you spend "
                                              "on this goal currently? "))
            break
        except ValueError:
            print("Please input integer only.")
            continue

    #ENDTIME: Prompt user to see how many minutes they want to spend working
    # on this goal at the end of the timeframe
    while True:
        try:
            endTime = int(input("\nAt the end of the the program how many minutes "
                                "a day do you want to be working on your goal? "))
            if startTime >= endTime:
                raise ValueError
            if endTime > 90:
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please enter an integer higher than your start time "
                  "and not more than 90 minutes.")
            continue
    # TIME FRAME: Prompt user to chose the timeframe of their goalsetting
    while True:
        try:
            print("\nHow long do you want to work toward your goal?")
            timeFrameChoice = int(input("Choose 1 for 30 days, 2 for 60 days, and 3 for 90 days. "))
            if 1 > timeFrameChoice or timeFrameChoice > 3:
                raise ValueError
            break
        except ValueError:
            print("Invalid choice.  Please enter either 1, 2, or 3.")
            continue

    #Instatiate Goal Object depending on goal type
    if goalType == 1:
        goal = GeneralGoal(startTime, endTime, timeFrameDict[timeFrameChoice])
    elif goalType == 2:
        goal = ExerciseGoal(startTime, endTime, timeFrameDict[timeFrameChoice])
    elif goalType == 3:
        goal = StressManagementGoal(startTime, endTime, timeFrameDict[timeFrameChoice])
        goal.personalizeSMGoals()

    #Calculated and show time Increment
    goal.calculateTimeIncrement()
    goal.displayTimeIncrement()
    goal.createCalendar()
    goal.createFileBody()

    # DISPLAY CHOICES
    print("\nGreat! Let's review your choices.")
    print("\nYou want to work on:", goal.goalType)
    print("Minutes a day you currently work on goal:", goal.startTime)
    print("Minutes a day you want to work up to: ", goal.endTime)
    print("Days you would like to take to get there: ", goal.timeFrame)
    print("Total number of minutes spent in goal activity: {}".format(
        goal.sumTime()))
    print("A file has been created with this information: \n\t\tGoalCalendarFile.txt")


main()

