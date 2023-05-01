import random
from collections import Counter

class GameLogic():
    def __init__(self):
        pass

    def roll_dice(rdt):
        times = 0
        arr_times = []
        #check whether th times is != to argument and if number between 1 and 6 
        while True:
            if times != rdt and rdt <= 6 and rdt > 0:
                #create a random number between 1 to 6 
                rolled_dice = random.randint(1,6)
                arr_times.append(rolled_dice)
                times += 1
            else:
                break
            #assign the array to a tuple 
        tuple_times = tuple(arr_times)
        return tuple_times
    
    def play():
      pass


    def calculate_score(roll_dice):
        sum = 0
        count_result = Counter(roll_dice)
        #define a most common that = to common value for the rolling dice to  return sorted array as a list of tuples  
        most_common = count_result.most_common() 
        # print(most_common)
        #if the length of array for most conmen values = 6  then a 2000 will be add to sum
        if len(most_common) == 6:
            sum += 2000
            return sum
        #else if length of most common = 3 and each key’s value = 2 then add 1500 to sum
        elif len(most_common) == 3 and all(count == 2 for _, count in most_common):
            sum += 1500
            return sum
        #else iterate  the item in the common value array using a loop:
        else:
            for item in most_common:
                if item[0] == 1 and item[1] < 3:
                    sum += 100 * item[1]
                if item[0] == 1 and item[1] == 3:
                    sum += 1000
                if item[0] == 1 and item[1] == 4:
                    sum += 2000
                if item[0] == 1 and item[1] == 5:
                    sum += 4000
                if item == (1, 6):
                    sum += 8000
                if item[0] == 5 and item[1] < 3:
                    sum += 50 * item[1]
                if item[1] == 2:
                    sum += 0
                if item[1] == 3 and item[0] != 1:
                    sum += 100 * item[0]
                if item[1] == 4 and item[0] != 1:
                    sum += 200 * item[0]
                if item[1] == 5 and item[0] != 1:
                    sum += 400 * item[0]
                if item[1] == 6 and item[0] != 1:
                    sum += 800 * item[0]
            return sum
   
    def run_dice(number):
        GameLogic.roll_dice(number)
        GameLogic.calculate_score()

# after_input_ofdice = GameLogic.roll_dice(4)
# after_calculating_score = GameLogic.calculate_score((1,2,5,5,5,6))

# print(after_input_ofdice)
# print(after_calculating_score)   