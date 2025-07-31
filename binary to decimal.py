def convert(num):
    I=0
    decimal=0
    while num !=0:
        digit=num%10
        decimal += digit*pow(2,I)
        num //=10
        I+=1
    return decimal
num=int(input("Enter number:"))
print(convert(num)) 

# num=input("Enter number:")
# decimal=int(num,2)
# print(decimal)