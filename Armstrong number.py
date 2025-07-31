# while True:
#     num=int(input("Enter a Number:"))
#     temp=num
#     sum=0
#     while temp!=0:
#         order=len(str(num))
#         digit=temp%10
#         sum=sum+pow(digit,order)
#         temp//=10
#     if sum==num:
#         print(str(num)+" ia armstrong number")
#     else:
#         print(str(num)+" is not armstrong number")

#FOR AN IN RANGE OF NUMBERS
while True:
    def order(num):
        len=0
        while num:
            len+=1
            num=num//10
        return len
    def armstrong(low,high):
        count=0
        for num in range (low,high+1):
            sum=0
            tem,digit,len=num,0,0
            len=order(num)
            while tem!=0:
                digit=tem%10
                sum+=digit**len
                tem//=10
            if sum==num:
                print(num,end=',')
                count+=1
        if count==0:
            print("Given range doesnt have any armstrong number")
    if __name__=="__main__":
        low =int(input("Enter  the lower bound:"))
        high=int(input("Enter higher bound:"))
        print(f"Armstrong numbers between (low) and (high) are:", end='\n')
        armstrong(low,high) 