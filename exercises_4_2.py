numbers = [0, 1, 7, 2, 4, 8]
my_numbers = numbers[0:5:2]
my_new_numbers = sum(my_numbers)*numbers[-1]
print(my_new_numbers)

my_list=[0,1,7,2,4,8]
result=0
for i in range(0,len(my_list),2):
    result+=my_list[i]

if my_list!=[]:
    result=result*my_list[-1]
    print(result)




