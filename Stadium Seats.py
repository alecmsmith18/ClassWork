def main():
    valueA = int(input("Enter Amount of Seating A: "))
    seat_A(valueA)
    valueB = int(input("Enter the Amount of Seating B: "))
    seat_B(valueB)
    valueC = int(input("Enter Amount of Seating C: "))
    seat_C(valueC)

def seat_A(number):
    result = number * 20
    print("$", format(result, ',.2f'))
def seat_B(number):
    result = number * 15
    print("$", format(result, ',.2f'))
def seat_C(number):
    result = number * 10
    print("$", format(result, ',.2f'))

main()