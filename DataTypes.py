# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number: ")

cov=str(two_digit_number)
res=int(cov[0])+int(cov[1])
# result=(cov[0]+" + "+cov[1]+" = "+str(res))
print(res)