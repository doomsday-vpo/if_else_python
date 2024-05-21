holidays = int(input())

cat_norm = 500

workdays_play = 63 / 60
offdays_play = 127 / 60

workdays = 365 - holidays

play = workdays_play * workdays + offdays_play * holidays

if play > cat_norm:
    print("Tom will run away")
    hours = int(play - cat_norm)
    minutes = int((play - cat_norm) * 60 % 60)
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    hours = int(cat_norm - play)
    minutes = int((cat_norm - play) * 60 % 60)
    print(f"{hours} hours and {minutes} minutes less for play")
