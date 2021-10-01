from math import ceil

from GeneralGoal import GeneralGoal

# Stress Management class extends General Goal
from InvalidInputException import InvalidInputException


class StressManagementGoal(GeneralGoal):
    def __init__(self, startTime=0, endTime=60, timeFrame=60):
        super().__init__(startTime, endTime, timeFrame)
        self.goalType = "STRESS MANAGEMENT GOAL"
        self.stressManagementActivities = ["Meditation", "Breathing Ex.", "Journaling",
                                           "Gratefulness Ex."]
        self.calendarActivityMatrix = []

    # call method to have user add activity and create calendar
    def personalizeSMGoals(self):
        self.userAddActivityType()
        self.createCalendarActivityMatrix()

    # display activity types
    def displayActivityTypes(self):
        print("\nCurrent Stress Management Activities are the following:\n")
        for x in range(len(self.stressManagementActivities)):
            print(self.stressManagementActivities[x])


    # prompt user and allow to add activity to list of stress management activities
    def userAddActivityType(self):
        choiceDic = {'Y', 'N'}
        while True:
            self.displayActivityTypes()

            try:
                choice = input("\nWould you like to add a stress management activity? "
                               "Enter Y or N: ")
                if choice.upper()[0] == 'Y':
                    while True:
                        try:
                            newSMActivity = input("\nEnter activity name now: ")
                            newSMActivity = newSMActivity.title().strip()
                            if len(newSMActivity) > 17:
                                raise InvalidInputException(newSMActivity)
                            break
                        except InvalidInputException:
                            print("Activity characters exceeds 17.  Please abbreviate.")
                            continue

                    print("You entered: ", newSMActivity)
                    self.stressManagementActivities.append(newSMActivity)
                    continue
                if choice.upper()[0] == 'N':
                    break
                else:
                    raise KeyError
            except KeyError:
                print("\nInvalid Input. Enter only Y or N. ")
                continue

    # create 2D array to hold activities depending on time frame
    def createCalendarActivityMatrix(self):
        numOfRows = ceil(self.timeFrame / 7)
        numOfCol = 7
        count = 0
        i = 0
        for row in range(numOfRows):
            self.calendarActivityMatrix.append([])
            for col in range(numOfCol):
                self.calendarActivityMatrix[row].append(self.stressManagementActivities[i])
                i += 1
                if i == len(self.stressManagementActivities):
                    i = 0
                count += 1
                if count == self.timeFrame:
                    break

    # create and write out to file calendar with activity and time
    def createFileBody(self):
        days = ["SUN", "MON", "TUES", "WED", "THURS", "FRI", "SAT"]

        # calls method to write out into information into file
        self.createFileIntro()

        calendarFile = open("GoalCalendarFile.txt", "a+")
        calendarFile.write(format("\n", "8s"))
        for i in range(len(days)):
            calendarFile.write(format(days[i], "^28s"))
        calendarFile.write("\n")
        print("          ")

        for row in range(len(self.calendarTimeMatrix)):
            calendarFile.write(f'WEEK {row + 1:>2}   ')
            for col in range(len(self.calendarTimeMatrix[row])):
                if round(self.calendarTimeMatrix[row][col]) == 0:
                    self.calendarTimeMatrix[row][col] = 1
                    calendarFile.write(f'{self.calendarActivityMatrix[row][col]:17}: '
                                       f'{round(self.calendarTimeMatrix[row][col]):4}     ')
                else:
                    calendarFile.write(f''
                                       f'{self.calendarActivityMatrix[row][col]:17}: '
                                       f'{round(self.calendarTimeMatrix[row][col]):4}     ')
            calendarFile.write("\n")

        calendarFile.write("\nTotal number of minutes spent in goal activity: {}".format(
            self.sumTime()))
        calendarFile.close()


