def Main():
    half = 0.5
    g =9.8
    t = int(input("Enter Total Amount of time: "))
    falling_distance(half, g, t)


def falling_distance(point_five, gravity, time):
    for year in range(1, 11):
        print('Year {} ')(year)
        print("Total Distnace is:")
        result = point_five * gravity * time ** 2
        print (format(result, ",.2f"))
Main()