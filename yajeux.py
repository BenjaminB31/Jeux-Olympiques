a = int(input( " Entrez une date : "))

if((a!=1916 and a!=1940 and a!= 1944) and (a>=1896) and (a%4==0 and a%100!=0 or a%400==0)):
    print("True")
elif((a!=1916 and a!=1940 and a!= 1944) and (a>=1924) and (a%4==2 and a%100!=2 or a%400==2)):
    print("True")
else:
	print("False")
