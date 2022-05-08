def timeConv(a, b, c, d):
    # YOUR CODE GOES HERE
    # The code for taking input and printing output is already taken care of.
    # Make sure to complete the functions and return the asked requirements.
    class Spanoftime:
        def __init__(self, h, m):
            self.hours = h
            self.mins = m

        def displayTime(self):
            return ("{} hours and {} min".format(self.hours, self.mins))

        def addTime(t1, t2):
            t3 = Spanoftime(0, 0)
            # Complete the function
            t3.hours = t1.hours + t2.hours
            t3.mins = t1.mins + t2.mins
            if t3.mins >= 60:
                hours = t3.mins // 60
                mins = t3.mins % 60
                t3.hours = t3.hours + hours
                t3.mins = mins
            return t3

        def returnMinutes(t1, t2):

            return (t1.hours + t2.hours) * 60 + t1.mins + t2.mins
            # Return the total number of minutes

    t1 = Spanoftime(a, b)
    t2 = Spanoftime(c, d)
    t3 = Spanoftime.addTime(t1, t2)
    t3.displayTime()
    totalmin = str(Spanoftime.returnMinutes(t1, t2))
    return t3.displayTime(), ("The total minutes in time t1 and t2 are: " + totalmin)

print(timeConv(1,45,1,30))