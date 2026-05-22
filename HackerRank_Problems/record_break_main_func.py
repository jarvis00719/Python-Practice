import matplotlib.pyplot as plt

def breaking_records(score):

    max_score = score[0]
    min_score = score[0] 
    
    max_record_break = 0
    lowest_record_break = 0

    for s in score[1:]:
         
        if s > max_score:
            max_score = s
            max_record_break+=1
        
        elif s < min_score:
            min_score = s
            lowest_record_break +=1


    return max_record_break, lowest_record_break


#Input Statements!!
no_of_games = int(input())
scores = list(map(int, input().split()))


max_record_break, lowest_record_break = breaking_records(scores)

print(max_record_break, lowest_record_break)
   





        



