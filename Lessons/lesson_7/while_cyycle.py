import time
from datetime import datetime


time_now = time.time() + 10 # 1980 1
time_date = datetime.now().second + 10

# print(time_now)
# counter = 0
# while (time_in_while_now := datetime.now()).second < time_date:
#     counter += 1
#     print(f"I'm requesting to server count {counter} ")
#     print(time_in_while_now)
#     time.sleep(1)
#
#     if counter == 7:
#         break
#
#
# while (time_in_while_now := time.time()) < time_now:
#     counter += 1
#     print(f"I'm requesting to server count {counter} ")
#     print(time_in_while_now)
#     time.sleep(1)



    # if counter == 7:
    #     break

# for k in range(10000000)




counter = 0
# while  True:
#     value_to_compare = int(input('Enter a number: '))
#     if value_to_compare == 1:
#         break
#     counter += 1
#     print(f'Кількість спроб {counter}')
#     print(f'our wrong value: {value_to_compare}')


# while  (value_to_compare := int(input('Enter a number: '))) != 1:
#     counter += 1
#     print(f'Кількість спроб {counter}')
#     print(f'our wrong value: {value_to_compare}')
#
#
# print(value_to_compare)


for key in range(10): #range(10) 0....9
    if key == 7:
        break

print(key)


