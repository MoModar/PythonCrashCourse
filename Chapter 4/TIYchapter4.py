#4-3.1-20:
#numbers=[value for value in range(1,21)]
#print(numbers)

#4-4. + 4-5. one_million:
#numbers=[]
#for value in range(1,1000001):
#    numbers.append(value)
#print(numbers)
#print(min(numbers))
#print(max(numbers))
#print(sum(numbers))

#4-6.Odd numbers:
#odd_numbers=list(range(1,21,2))
#print(odd_numbers)

#4-7.threes:
#threes=list(range(3,31,3))
#print(threes)

#threes=[]
#for value in range(3,31,3):
#    threes.append(value)
#print(threes)

#threes=[value for value in range(3,31,3)]
#print(threes)

#three_multiples=[value for value in range(0,31,3)]
#print(three_multiples)

#4.8. Cubes:

#cubes=[]
#for value in range(1,11):
#    value=value**3
#    cubes.append(value)
#print(cubes)

cubes=[value**3 for value in range(1,11)]
print(cubes)
