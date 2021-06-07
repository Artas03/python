def grade(hwscore,assess_score,final_exam):
    percent = hwscore + assess_score + final_exam/3*100 #only accepts float value
    percentage = str(percent)
    return percent


print(grade(12,25,60))
