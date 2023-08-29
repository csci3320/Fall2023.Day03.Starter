import time

list1 = [1,2,3,4,5,6,7,8,9,1]
list2 = [1,2,3,4,5,6,7,8,9,10]

list3 = [i for i in range(10000)]
list4 = [i for i in range(10000)]
list4.append(1)

def hasDuplicate(list):
    for i in range(len(list)):
      for j in range(i):
         if list[i] == list[j]:
            return True
    return False

print(hasDuplicate(list1))
print(hasDuplicate(list2))

# Slow it down
# start = time.time()

# print(hasDuplicate(list3))
# print(hasDuplicate(list4))

# end = time.time()
# print(end- start)

# Do multiple speeds
# for i in range(100):
#    list = [i for i in range(pow(2,i))]
#    start = time.time()
#    hasDuplicate(list)
#    end = time.time()
#    print(str(i) + "; " + str(end-start))