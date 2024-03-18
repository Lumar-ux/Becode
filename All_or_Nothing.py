# answers = ['A', '_', 'C', '_', 'B']   # answer key                    TRUE
# key = ['A', 'D', 'C', 'E', 'B']   # student's solution
# answers = ['B', '_', 'B']   # answer key                            FALSE
# key = ['B', 'D', 'C']   # student's solution
# answers = ['T', '_', 'F', 'F', 'F']   # answer key                            TRUE
# key = ['F', 'F', 'T', 'T', 'T']   # student's solution

# answers = ['B', 'A', '_', '_']   # answer key                            TRUE
# key = ['B', 'A', 'C', 'C']   # student's solution
# answers = ['A', 'B', 'A', '_']   # answer key                            TRUE
# key = ['B', 'A', 'C', 'C']   # student's solution
# answers = ['A', 'B', 'C', '_']   # answer key                            FALSE
# key = ['B', 'A', 'C', 'C']   # student's solution

# answers = ['B', '_']   # answer key                            TRUE
# key = ['C', 'A']   # student's solution
# answers = ['B', 'A']   # answer key                            FALSE
# key = ['C', 'A']   # student's solution
# answers = ['B']   # answer key                            TRUE
# key = ['B']   # student's solution

# answers = ['_', 'T', '_', '_']   # answer key                            TRUE
# key = ['T', 'F', 'F', 'F']   # student's solution
# answers = ['_', 'T', '_', '_']   # answer key                            TRUE
# key = ['T', 'T', 'F', 'T']   # student's solution
# answers = ['_', 'T', 'T', 'T']   # answer key                            FALSE
# key = ['T', 'T', 'F', 'T']   # student's solution
# answers = ['_', 'T', 'T', 'T']   # answer key                            TRUE
# key = ['T', 'T', 'T', 'T']   # student's solution
# answers = ['_', 'T', 'T', 'T']   # answer key                            TRUE
# key = ['F', 'F', 'F', 'F']   # student's solution
# answers = ['_', '_', '_', '_']   # answer key                            TRUE
# key = ['F', 'F', 'F', 'F']   # student's solution
answers = ['D', 'C', 'B', 'D', 'D', 'B', 'D', 'A', 'C']
key = ['D', '_', 'B', '_', 'D', 'B', 'D', '_', 'C']


def possibly_perfect(key, answers):
    i=0
    cor_pass=0
    cor_pass_n=0
    if(len(key) == len(answers)):
        for i in range(len(key)):
            if key[i] == answers[i] or answers[i] == "_" or key[i] == "_":
                cor_pass+=1
            if key[i] != answers[i] or answers[i] == "_" or key[i] == "_":
                cor_pass_n+=1
            if (cor_pass == len(answers))or(cor_pass_n == len(answers)):
                print("Tous es correct = 100")
                return(True)
        if (cor_pass != len(answers))or(cor_pass_n != len(answers)):
                print("incorect = 0")
                return(False)
    else:
        return(False)

print(possibly_perfect(key, answers))