import math

friends=10
#friends +=1
# friends = friends+1
# friends =friends-2
# friends-=2
# friends =friends*3
# friends *=3
# friends =friends/2
# friends /=2
# friends =friends **2 (to the power of )
# friends **=2
# friends =friends
remainder= friends % 3
print(remainder)


x=3.14
y=-4
z=5

#result =round(y) = -4
#result=abs(y)  =4
#result= pow(4,3)   =64
#result=max(x,y,z) =5
#result1= min(x,y,z) =-4
#print(result)
#print(result1)


print(math.pi)
print(math.e)


result=math.sqrt(25)
print(result)

t=9.1
result1= math.ceil(t)
print(f"Ceiling result is {result1}\n")
result2= math.floor(t)
print(f"floor result is {result2}\n")




#Circumference of a circle
#radius= float(input("Enter the radius of your circle: "))
#pi=math.pi

#circumference= radius *pi*2
#print(f"the circumference of your circle is {round(circumference,2)}cm")
#Area of a circle

#area= (radius)**2 *math.pi
#print(f"the area of your circle is {round(area,2)}cm²")

#hypotenuse calculator

a= float(input("Enter your length of a: "))
b= float(input("Enter your length of b: "))
c= math.sqrt(a**2+b**2)
print(f"the Hypotenuse of your R-Triangle is {c}")