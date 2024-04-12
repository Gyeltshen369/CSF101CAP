################################
# Your Name: Nima Gyeltshen
# Your Section: 1 Electrical Engg.
# Your Student ID Number: 02230067
################################
# REFERENCES
# Links that you referred while solving
# the problem
# https://www.youtube.com/watch?v=LpZmZs2_BC4
# https://www.youtube.com/watch?v=LpZmZs2_BC4
# https://www.youtube.com/watch?v=aequTxAvQq4
################################
# SOLUTION
# Your Solution Score:46944
# Put your number here:7
################################

def read_input():
    file=open('CSF101CAP/input_7_cap1.txt','r') # The variable stores the file that has to be read. 
    return file

def calculation_score(point):
    score={'A X': 2, 'A Y': 4, 'A Z': 9, 'B X': 1, 'B Y': 5, 'B Z': 7, 'C X': 1, 'C Y': 6, 'C Z': 7} # The dictionary contains the outcome keys and the corresponding values 
    total_score=0
    for line in point:
        each=line.strip() # It reads the line in the input file
        value_in_dictionary=score.get(each,None)
        if value_in_dictionary is not None: # If the key in the input file matches the key from the dictionary the function executes.
            total_score+=value_in_dictionary
    print('total_score:', total_score)
    
calculation_score(read_input())