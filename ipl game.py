import random
import time
import random
Atotal=[]
Btotal=[]
balls=["---------"]
out=["run out","catch out"]
print("choose teams\n")
teams={"A":{"a","b","c","d","e","f","g","h","i","j","k"},"B":{"anushu","shabbu","laddu","mahiks","manu","siri","janu","chinni","chinna","pavani"}}
keys=teams.keys
for keys in teams:
    print(keys)
def select_team(team):
    selected_team =0
    if team in teams:
        selected_team=team
        return selected_team
    else:
        selected_team==str(input("enter name"))
        return "selected_team"
first_team=input("\nenter 1st team choice:")

firstTeam=select_team(first_team)

second_team= input("enter the second choice")
select_team(secondTeam)

if second_Team==firstTeam:
    print("this team is already choice by your ")
    secondTeam=str(input("..."))
    select_team(second_Team)
else:
    pass
print("firstTeam")
print("second_Team") 
players=[firstTeam,secondTeam]
print("start")
print("firstTeam")
# print("toss")
tosscall=["------"]
batball=["------"]
toss=input("enter what u want")
while toss:
    if toss in tosscall:
        print(toss)
        random.shuffle(tosscall)
        print(tosscall)
        break
    else:
        print("-----")
        toss=input("----")
        continue
def tosstime(team_a,team_b):
    print(team_a)
    call=input("-----")
    try:
        if call not in batball:
            print("----")
            call=input("---")
    finally:
        print(team_a,call)
        if call=="bat":
            bating_team,bowling_team=teams[team_a],teams[team_b]
        elif call=="bowl":
            bating_team,bowling_team=teams[team_b],teams[team_a]
            return bating_team,bowling_team
def innings(bating_team,bowling_team,first_score):
    bating_team_list=teams[bating_team]
    bating_option=iter(bating_team_list)  
    on_strike=next(bating_option) 
    on_strike_scores=[]
    players_scores=[]
    wickets=10
    total=[]
    team_total=0
    bowling_options=teams[bowling_team][5:]
    for over in range(0,3):
        bowler=random.choice(bowling_options)
        print(on_strike,bowler)
        print("any key to respond")
    for ball in range(1,7):
        ball_delivered=random.choice(balls)
        played_for=random.choice(balls)
        if wickets==0 or team_total >first_score:
            break
        elif ball_delivered==played_for:
            print(over,ball)
            print(bowler,on_strike)
            player_scores=sum(on_strike_scores)
            


            