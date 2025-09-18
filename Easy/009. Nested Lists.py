if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([name, score])
        
    uni1que_scores = sorted(set([item[1] for item in a]))
    second_low = uni1que_scores[1]
    verify_name = ([student[0] for student in a if student[1] == second_low])
    
    for name in sorted(verify_name):
        print(name)