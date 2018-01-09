# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK2

# Solution To Question 3 : Ex 15, CH 5 - Test Average & Grade


def main():
    print('Enter your marks to know your grade and average')
    score1 = float(input('Enter test score 1: '))
    grade1 = determine_grade(score1)
    score2 = float(input('Enter test score 2: '))
    grade2 = determine_grade(score2)
    score3 = float(input('Enter test score 3: '))
    grade3 = determine_grade(score3)
    score4 = float(input('Enter test score 4: '))
    grade4 = determine_grade(score4)
    score5 = float(input('Enter test score 5: '))
    grade5 = determine_grade(score5)
    average = calc_average(score1,score2,score3,score4,score5)
    display_result(score1,score2,score3,score4,score5,grade1,grade2,grade3,grade4,grade5,average)

     
def determine_grade(score) :
    if score >=90 and score<=100 :
        grade ='A'
    elif score >=80 and score<=89 :
        grade ='B'
    elif score >=70 and score<=79 :
        grade ='C'
    elif score >=60 and score<=69 :
        grade ='D'
    elif score <60 and score>=0:
        grade ='F'
    else :
        print()

    return grade


def calc_average(s1,s2,s3,s4,s5) :
    avg = (s1+s2+s3+s4+s5)/5
    return avg


def display_result(s1,s2,s3,s4,s5,g1,g2,g3,g4,g5,avg):
    print()
    print('Score\tGrade')
    print('--------------')
    print(s1, '\t', g1)
    print(s2, '\t', g2)
    print(s3, '\t', g3)
    print(s4, '\t', g4)
    print(s5, '\t', g5)
    print()
    print('Your average is',avg)
                   
main()
