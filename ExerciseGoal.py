# Exercise class extends General Goal
from math import ceil

from GeneralGoal import GeneralGoal


class ExerciseGoal(GeneralGoal):
    # construct Exercise goal object with 2D matrix to hold Exercise types
    def __init__(self, startTime=0, endTime=60, timeFrame=60):
        super().__init__(startTime, endTime, timeFrame)
        self.goalType = "EXERCISE GOAL"
        self.calendarExerciseTypeMatrix = []
        self.exerciseType = ("Weightlifting", "Cardio", "Plyometrics", "Stretching",
                             "Calisthenics", "HIIT", "Active Recovery")

    # populate both 2D matrix and add rest days every Wednesday
    def createCalendar(self):
        newTime = (self.startTime + self.timeIncrement)
        numOfRows = ceil(self.timeFrame / 7)
        numOfCol = 7
        count = 0

        # fill 2D time matrix with increments, placing none/null value in on expected rest days
        for row in range(numOfRows):
            self.calendarTimeMatrix.append([])
            for col in range(numOfCol):
                # populate time matrix with 'None' on rest days
                if col == 3:
                    self.calendarTimeMatrix[row].append(None)
                else:
                    self.calendarTimeMatrix[row].append(newTime)
                newTime += self.timeIncrement
                count += 1
                # stop filling matrix once the time frame has been reached
                if count == self.timeFrame:
                    # If last day in calendar is a 'Rest', add incremented time to last position
                    # so as not to end the calendar on a rest day
                    if self.timeFrame == 60:
                        self.calendarTimeMatrix[row][col] = self.endTime
                    break

        exerciseTypeCount = 0
        count = 0
        # fill 2D exercise type matrix with activities, adding "REST" days on Wednesdays
        for row in range(numOfRows):
            self.calendarExerciseTypeMatrix.append([])
            for col in range(numOfCol):
                # populate exercise matrix with 'Rest' on rest days
                if col == 3:
                    self.calendarExerciseTypeMatrix[row].append("REST")
                else:
                    self.calendarExerciseTypeMatrix[row].append(
                        self.exerciseType[exerciseTypeCount])
                    exerciseTypeCount += 1
                if exerciseTypeCount == len(self.exerciseType):
                    exerciseTypeCount = 0
                count += 1
                if count == self.timeFrame:
                    # If last day in calendar is a 'Rest', add a last exercise type to last position
                    # so as not to end the calendar on a rest day
                    if self.timeFrame == 60:
                        self.calendarExerciseTypeMatrix[row][col] = self.exerciseType[
                            exerciseTypeCount]
                    break

    # write out/append the created calendar to the file
    def createFileBody(self):
        self.createFileIntro()
        calendarFile = open("GoalCalendarFile.txt", "a+")

        days = ["SUN", "MON", "TUES", "WED", "THURS", "FRI", "SAT"]
        calendarFile.write(format("\n", "9s"))

        # write out contents of Exercise Matrix and Time Matrix
        for row in range(len(self.calendarTimeMatrix)):
            calendarFile.write(f'\nWEEK {row + 1:>2}  \n')
            i = 0
            for col in range(len(self.calendarTimeMatrix[row])):
                calendarFile.write(f' {days[i]: <5}  ')
                i += 1
                # write out exercise activity and time, unless "REST", then write out only REST
                try:
                    # if time less than 1 minute, convert and display second
                    if self.calendarTimeMatrix[row][col] < 1:
                        seconds = round(self.convertMinToSec(self.calendarTimeMatrix[row][col]))
                        seconds = str(seconds) + " sec"
                        calendarFile.write(f'{self.calendarExerciseTypeMatrix[row][col]:17}:'
                                           f' {seconds:>6}')
                    else:
                        calendarFile.write(f'{self.calendarExerciseTypeMatrix[row][col]:17}:'
                                           f'  {(round(self.calendarTimeMatrix[row][col])):>5}    ')
                except TypeError:
                    calendarFile.write(f'{self.calendarExerciseTypeMatrix[row][col]:23}')
                calendarFile.write("\n")

        # write out number of minutes spent in activity
        calendarFile.write("\nTotal number of minutes spent in goal activity: {}".format(
            self.sumTime()))
        calendarFile.close()

    # sum the amount of time spent over the time frame
    def sumTime(self):
        count = self.timeFrame
        sum1 = 0
        while count > 0:
            for row in range(len(self.calendarTimeMatrix)):
                for col in range(len(self.calendarTimeMatrix[row])):
                    # check to see if value is integer, add to sum (skips "None" values)
                    if isinstance(self.calendarTimeMatrix[row][col], float):
                        sum1 = sum1 + self.calendarTimeMatrix[row][col]
                    count -= 1
        return round(sum1, 2)
