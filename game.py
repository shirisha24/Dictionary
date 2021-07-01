import random
team_a={"player1":"siri","player2":"shabbu","player3":"shirisha","player4":"shirish","player5":"chinni","player6":"somi","player7":"anushu","player8":"anu","player9":"ammu","player10":"chinna","player11":"laddu"}
team_b={"player1":"a","player2":"b","player3":"c","player4":"d","player5":"e","player6":"f","player7":"g","player8":"h","player9":"i","player10":"j","player11":"k"}
types_balls=["spin","offspin","wide","non ball"]
types_score=["out",1,2,3,4,6,0]
print("team_a is gng to start")
score=0
team_a_wickets=0
balls=0
overs=1
firstover=1
while firstover<=overs:
    countball=1
    while countball<=6:
        random_balls_num=random.randint(0,3)
        k=countball
        which_ball=types_balls[random_balls_num]
        user=input("plese hit the ball")
        if user=="yes":
            if which_ball=="wide ball" or which_ball=="non ball":
                print("which ball",which_ball,"hain")
                score+=1
                countball=k
            else:
                print("which ball",which_ball)
                random_score_num=random.randint(0,6)
                how_much_score=types_score[random_score_num]
                if how_much_score=="out":
                    team_a_wickets+=1
                else:
                    score+=how_much_score
                countball+=1
            print("total_score",score,"team_a_wickets",team_a_wickets,"totalovers",overs,"current overs",firstover,"which ball",countball)
        else:
            countball=k
    firstover+=1
# print("game is over")
team_b={"player1":"a","player2":"b","player3":"c","player4":"d","player5":"e","player6":"f","player7":"g","player8":"h","player9":"i","player10":"j","player11":"k"}
types2_ballsb=["spin","offspin","wide","non ball"]
types2_scoreb=["out",1,2,3,4,6,0]
print("team_b is gng to start")
scoreb=0
team_b_wicketsb=0
ballsb=0
oversb=1
firstoverb=1
while firstoverb<=oversb:
    count_ballb=1
    while count_ballb<=6:
        random_balls_numb=random.randint(0,3)
        j=count_ballb
        which_ballb=types2_ballsb[random_balls_num]
        user=input("plese hit the ball")
        if user=="yes":
            if which_ballb=="wide ball" or which_ballb=="non ball":
                print("which ball",which_ball,"hain")
                scoreb+=1
                count_ballb=j
            else:
                print("this",which_ball,"hian")
                random_score_numb=random.randint(0,6)
                how_much_scoreb=types_score[random_score_num]
                if how_much_scoreb=="out":
                    team_b_wicketsb+=1
                else:
                    scoreb+=how_much_score
                count_ballb+=1
            print("total_score",scoreb,"team_a_wickets",team_b_wicketsb,"totalovers",oversb,"current_over",firstoverb,"which_ball",count_ballb)
        else:
            count_ballb=j
    firstoverb+=1
if score>scoreb:
    print("team_a","won the match")
elif scoreb>score:
    print("team_b","won the match")
else:
    print("draw")


    
