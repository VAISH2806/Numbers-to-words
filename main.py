single_digits = [" ", "one", "two", "three","four", "five", "six", "seven","eight", "nine"]
two_digits = ["", "ten", "eleven", "twelve","thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen","nineteen"]
tens_multiple = ["","","twenty", "thirty", "forty","fifty", "sixty", "seventy", "eighty","ninety"]
tens_power = ["hundred", "thousand"]

a=input("Enter a number: ")
l=len(a)

if l==1:
    if int(a)==0:
        print(a,"zero")
    else:
        print(a," ",single_digits[int(a)])
    
# two digit numbers
if l==2:
    if int(a[0])==1:
        one=int(a[1])
        ten=int(a[0])
        ans=(a+" "+two_digits[one+1])
        print(ans)
    elif int(a[0])!=1:
        on=int(a[1])
        te=int(a[0])
        an=(a+" "+tens_multiple[te]+" "+single_digits[on])
        print(an)
       
        
        

#three digit numbers
if l==3:
    if int(a[1]) != 1:
        ones=int(a[2])
        tens=int(a[1])
        oo=int(a[0])
        answer=a+" "+single_digits[oo]+' hundred '+tens_multiple[tens]+" "+single_digits[ones]
        print(answer)
    elif int(a[1])==1:
        ones2=int(a[2])
        oo2=int(a[0])
        answer2=a+" "+single_digits[oo2]+' hundred '+two_digits[ones2+1]
        print(answer2)
        
# four digit numbers       
if l==4:
    if int(a[1])==0:
        o1=int(a[3])
        t1=int(a[2])
        h1=int(a[1])
        th1=int(a[0])
        a1=a+" "+single_digits[th1]+" thousand "+tens_multiple[t1]+" "+single_digits[o1]
        print(a1)
        
    if int(a[1])!=0:
        o2=int(a[3])
        t2=int(a[2])
        h2=int(a[1])
        th2=int(a[0])
        a2=a+" "+single_digits[th2]+" thousand "+single_digits[h2]+ " hundred "+tens_multiple[t2]+" "+single_digits[o2]
        print(a2)
        
    if int(a[1])!=0 and int(a[2])==1:
        o3=int(a[3])
        t3=int(a[2])
        h3=int(a[1])
        th3=int(a[0])
        a3=a+" "+single_digits[th3]+" thousand "+single_digits[h3]+ " hundred "+two_digits[t3+2]
        print(a3)
    
