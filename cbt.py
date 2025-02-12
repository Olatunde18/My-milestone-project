question_one = """
1. What is 2 + 2?
a) 3
b) 4
c) 5
d) 6
"""

question_two = """
2. What color is the sky on a clear day?
a) Red
b) Blue
c) Green
d) Yellow
"""

question_three = """
3. How many legs does a spider have?
a) 6
b) 7
c) 8
d) 9
"""

question_four = """
4. What sound does a cow make?
a) Meow
b) Bark
c) Moo
d) Quack
"""

question_five = """
5. What is the opposite of 'hot'?
a) Warm
b) Cold
c) Cool
d) Boiling
"""


questions = [
    {
        "question": question_one,
        "answer": "b",
        "score": 1
    },
    {
        "question": question_two,
        "answer": "b",
        "score": 2
    },
    {
        "question": question_three,
        "answer": "c",
        "score": 5
    },
    {
        "question": question_four,
        "answer": "c",
        "score": 3
    },
    {
        "question": question_five,
        "answer": "b",
        "score": 5
    },
]


final_score = 0
max_score = sum(question["score"] for question in questions)
print(max_score)

for question in questions:
    print(question["question"])
    student_answer = input("Choose an option above: ").lower().strip()
    if student_answer == question["answer"]:
        final_score += question["score"]
    
print(f"At the end of the CBT exam, you scored {final_score} out of {max_score} points.")