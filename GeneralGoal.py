# General Goal Class
from math import ceil


class GeneralGoal:
    # construct goal object
    def __init__(self, startTime=0, endTime=60, timeFrame=60):
        self.startTime = startTime
        self.endTime = endTime
        self.timeFrame = timeFrame
        self.timeIncrement = 0
        self.calendarTimeMatrix = []
        self.goalType = "GENERAL GOAL"

    # calculate time increment using beginning and ending time over timeframe
    def calculateTimeIncrement(self):
        self.timeIncrement = (self.endTime - self.startTime) / self.timeFrame
        return self.timeIncrement

    # display time increment 2 decimal places
    def displayTimeIncrement(self):
        print("\nThe time frame increment is ", format(self.timeIncrement, "5.2f"))

    # populate a 2D matrix of time increments
    def createCalendar(self):
        newTime = self.startTime + self.timeIncrement
        numOfRows = ceil(self.timeFrame / 7)
        numOfCol = 7
        count = 0

        # fill 2D time matrix with incremented time
        for row in range(numOfRows):
            self.calendarTimeMatrix.append([])
            for col in range(numOfCol):
                self.calendarTimeMatrix[row].append(newTime)
                newTime = newTime + self.timeIncrement
                count += 1
                # stop filling matrix once the time frame has been reached
                if count == self.timeFrame:
                    break

    # write out the intro info to the file
    def createFileIntro(self):
        calendarFile = open("GoalCalendarFile.txt", "w+")
        calendarFile.write("\tPERSONALIZED CALENDAR\n")
        calendarFile.write("GOAL TYPE: {}".format(self.goalType))
        calendarFile.write("\nTIMEFRAME: {}".format(self.timeFrame))
        calendarFile.write("\nSTARTING MINUTES: {}".format(self.startTime))
        calendarFile.write("\nEND MINUTES: {}\n".format(self.endTime, "5.2f"))
        calendarFile.close()

    # write out/append the created calendar to the file
    def createFileBody(self):
        self.createFileIntro()
        calendarFile = open("GoalCalendarFile.txt", "a+")

        # write out days of week format
        days = ["SUN", "MON", "TUES", "WED", "THURS", "FRI", "SAT"]
        calendarFile.write(format("\n", "8s"))
        for i in range(len(days)):
            calendarFile.write(format(days[i], ">8s"))
        calendarFile.write("\n")

        # write out contents of Time Matrix
        for row in range(len(self.calendarTimeMatrix)):
            calendarFile.write(f'WEEK {row + 1:>2}')
            for col in range(len(self.calendarTimeMatrix[row])):
                # if time less than 1 minute, convert and display second
                if round(self.calendarTimeMatrix[row][col]) < 1:
                    seconds = str(round(self.convertMinToSec(round(self.calendarTimeMatrix[row][
                                                                       col],
                                                             2)))) + " sec"
                    calendarFile.write(f'{seconds:>8}')
                else:
                    calendarFile.write(f'{round(self.calendarTimeMatrix[row][col]):>8}')
            calendarFile.write("\n")

        # write out number of minutes spent in activity
        calendarFile.write("\nTotal number of minutes spent in goal activity: {}".format(
            self.sumTime()))
        calendarFile.close()

    # sum the amount of time spent over the time frame
    def sumTime(self):
        return round(sum(map(sum, self.calendarTimeMatrix)), 2)

    def convertMinToSec(self, minutes):
        return 60 * minutes
