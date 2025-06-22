def game():
    return 1278
with open('highscore.txt') as f:
    score_file=f.read()
score_function=game()
with open('highscore.txt','w') as f:
    if score_file=='' or int(score_file)<score_function:
        f=f.write(str(score_function))
    else:
        exit()
        
