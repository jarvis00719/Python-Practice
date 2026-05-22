import matplotlib.pyplot as plt

# Main_function -- [Records Broken] -- Highest $ Lowest !!

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


#Using games indicies for X-axis !!
games = list(range(1, no_of_games+1))


#Data Visualization !!

plt.plot(games, scores, marker='o', label ='scores')
plt.xlabel("Games")
plt.ylabel("Scores")
plt.title("Breaking Records")

#Highlighting Min/Max breaking points !!

max_score, min_score = scores[0], scores[0]

for i, s in enumerate(scores):
    
    if s > max_score:
        plt.scatter(games[i], s, color='green', label='New Max' if i==0 else "")
        max_score = s
    
    elif s < min_score:
        plt.scatter(games[i], s, color='red', label='New Min' if i==0 else "")
        min_score = s
plt.legend()
plt.show()