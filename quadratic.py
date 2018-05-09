
import cmath

a = input('enter the a number:')
b = input('enter the b number:')
c = input('enter the c number:')

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

