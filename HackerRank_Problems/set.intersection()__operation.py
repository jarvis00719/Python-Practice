#1-Line:- n = no of students sub to English newspaper
#2-Line:- n no of student's Roll no.(subbed to eng newspaper)

#3-Line:- b = no of students sub to French newspaper
#4-Line:- b no number of student's Roll no.(subbed to french newspaper)

##Input Statements !!

#----English Newspaper----#
eng_newspaper_count = int(input())

eng_roll_no = [int(i) for i in range(eng_newspaper_count)]
eng_roll_no = input().split()

#-----French Newspaper-----#
french_newspaper_count = int(input())

french_roll_no = [int(i) for i in range(french_newspaper_count)]
french_roll_no = input().split()

eng_set = set(eng_roll_no)
french_set = set(french_roll_no)

intersect = (eng_set & french_set)
print(len(intersect))

