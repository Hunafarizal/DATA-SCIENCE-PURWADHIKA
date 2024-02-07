a = 54 # integer
b = 54.0 #float
c = '54' #string
d = [54, 56, 58] #list
e = {54} 
# print(type(d))

# f = range(17,43)





# def addnumber(number1, number2):
#     result = number1 + number2
#     return result


# n1 = 10
# n2 = 20
# addNumber = addnumber(n1, n2)
# print(f'result = {addNumber}')

# x = d
# print(x[1])


def calculate_first_name_length(Hunafa_Rizal_Aqli):
    return len(Hunafa_Rizal_Aqli.split()[0]) if Hunafa_Rizal_Aqli else 0

Hunafa_Rizal_Aqli = input("Enter your full name: ")
result = calculate_first_name_length(Hunafa_Rizal_Aqli)

print(f"The length of your first name is: {result}")




