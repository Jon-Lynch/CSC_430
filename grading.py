# Jonathan Lynch
# 4/4/20
# https://youtu.be/66_aWBk5f04
# "I have not given or received any unauthorized assistance on this assignment."

def grading():
    'determines assignment grade from user input'
    score=0
    file = input('Was the file submitted in a single uncompressed .py file? ')    #determine if file in right format
    if file == 'no' or file == 'No':
        return score
    else:
        name_date = input('Did the student include both their name and the date? ')   #determine if name & date included
        if name_date == 'no' or name_date == 'No':
            return score
        else:
            honor_stmt = input('Did the student include the honor statement? ')    #determine if honor statement included
            if honor_stmt == 'no' or honor_stmt == 'No':
                return score
            else:
                video = input('Did the student include a link to an unlisted 3-minute YouTube video presenting their work? ')   #determine if video created
                if video == 'no' or video == 'No':
                    return score
                else:
                    correct = input('Out of ten points, how would you rate the correctness of the code? ')   #points awarded for code correctness
                    correct = int(correct)
                    score += correct
                    
                    elegance = input('Out of ten points, how would you rate the elegance of the code? ')    #points awarded for elegance
                    elegance = int(elegance)
                    score += elegance
                    
                    hygiene = input('Out of ten points, how would you rate the code hygiene? ')      #points awarded for code hygiene
                    hygiene = int(hygiene)
                    score += hygiene
                    
                    discuss = input('Out of ten points, how would you rate the quality of the YouTube video discussion? ')   #points awarded for video discussion
                    discuss = int(discuss)
                    score += discuss

                    late = input('Was the assignment submitted late? ')   #determine if file submitted late
                    if late == 'no' or late == 'No':
                        return score                                    #return score (if file submitted on time)
                    else:
                        time = input('How many hours after the project deadline was the assignment submitted? ')     #determine how many hours late (if file not submitted on time)
                        time = int(time)/100
                        if score < score - score*time:      #determine if file was submitted too late to receive any points
                            return 0
                        else:
                            return score - score*time       #late submission (but eligible to receive points), return (reduced) score
        
                    
