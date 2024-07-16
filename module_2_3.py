
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
true_num = 0


while true_num < len(my_list):
    num = my_list[true_num]
    true_num = true_num + 1
    if num == 0:
        continue
    elif num < 0:
        break
    elif true_num == len(my_list):
        print(num)
    else:
        print(num)
