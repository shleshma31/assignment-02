#Assignment-2 (lottery game) 
 
import random
numbers = []
for i in range(15):
    numbers.append(random.randint(1, 100))

print("Generated Numbers:", numbers)


group1 = numbers[:5]
group2 = numbers[5:10]
group3 = numbers[10:]


print("Group 1:", group1)
print("Group 2:", group2)
print("Group 3:", group3)


sum1 = sum(group1)
sum2 = sum(group2)
sum3 = sum(group3)

print("Sum of Group 1:", sum1)
print("Sum of Group 2:", sum2)
print("Sum of Group 3:", sum3)


if sum1 > sum2 and sum1 > sum3:
    print("Group 1 wins the lottery with a sum of", sum1)
elif sum2 > sum3:
    print("Group 2 wins the lottery with a sum of", sum2)
else:
    print("Group 3 wins the lottery with a sum of", sum3)
 