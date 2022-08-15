username= "Julian Garner"
print("Hello," + username)

for num in range(1, 101):
    if (num % 2 != 0):
        print(num, end = " ")

def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))

def leapyr(n):
    if n%4==0 and n%100!=0:
        if n%400==0:
            print(n, "is a leap year.")
    elif n%4!=0:
        print(n, "is not a leap year.")
print(leapyr(1900))

def consecutive_one(data):
   one_list = []
   size = 0
   for num in data:
       if num == 1:
           one_list.append(num)
       elif num == 0 and size < len(one_list):
           size = len(one_list)
           one_list = []

    return size

if __name__ == '__main__':
    data = [0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0]
    print(consecutive_one(data))


