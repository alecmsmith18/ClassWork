ticket_A = int(input("Enter total amount of A Tickets sold: "))
ticket_B = int(input("Enter total amount of B Tickets sold: "))
ticket_C = int(input("Enter total amount of C Tickets sold: "))

class_a = 20 * ticket_A
class_b = 15 * ticket_B
class_c = 10 * ticket_C

print("Total Amount for Seating A")
print("------------------------------")
print("$", format(class_a, ',.2f'))

print("Total Amount for Seating B")
print("------------------------------")
print("$", format(class_b, ",.2f"))

print("Total Amount for Seating C")
print("------------------------------")
print("$", format(class_c, ',.2f'))