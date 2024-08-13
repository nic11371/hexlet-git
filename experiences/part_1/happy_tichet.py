def is_happy_ticket(num):
   
   first = num[:len(num)//2]
   second = num[len(num)//2:]
   sum_1 = sum(int(i) for i in first)
   sum_2 = sum(int(i) for i in second)
   
   if sum_1 == sum_2:
      return True
   
   return False





print(is_happy_ticket('123123'))