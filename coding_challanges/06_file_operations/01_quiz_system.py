"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:
questions_file = open('questions.txt', 'r')
questions_raw = [line.strip() for line in questions_file.readlines()]
questions_file.close()

n = 0
m = 0
for line in questions_raw:
    question_and_ans = line.split('=')
    question = question_and_ans[0]
    ans = question_and_ans[1]
    user_ans = input(f'{question}=')
    if user_ans == ans:
        n+=1
    m+=1
result_file = open('result.txt', 'w')
result_file.write(f'Your final score is {n}/{m}.')
result_file.close()