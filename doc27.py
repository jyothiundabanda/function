'''Q27. Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended”'''

def func(speed):
    if speed<70:
        print("ok")
    if speed>70:
        i=70
        while i<=70:
            point=(speed-70)//5
            if point>12:
                print(point,speed,"licence suspend")
            else:
                print(point,speed,"okay")
            i=i+1
speed=int(input("no"))
func(speed)