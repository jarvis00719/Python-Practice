import matplotlib.pyplot as plt


scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
games = range(1, len(scores)+1)

plt.plot(games, scores, marker='o', label ='scores')
plt.xlabel("games")
plt.ylabel("scores")
plt.title("Breaking Records")

#Highlight Min/Max - breaking points!!
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