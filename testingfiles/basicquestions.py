import os
from openai import OpenAI

OPENAI_API_KEY = "​"
MODEL = "gpt-4-turbo-preview"

def getQuestionData():
    subject_of_question = input("Subject?: ")
    type_of_question = input("Type of question?: ")
    
    return type_of_question, subject_of_question

def getQuestion(question_format, input_text):
    client = OpenAI(api_key = OPENAI_API_KEY)
    response = client.chat.completions.create(
        model = MODEL,
        messages = [
            {"role": "user", "content": "Write to me a " + question_format + "question that tests my knowledge about " + input_text + ". Add the answer after question and seperate the answer and question with a '#'. Furthermore, add an explanation to the answer."},
        ],
        temperature = 0,
    )
    
    return response

question_format, input_text = getQuestionData()
completion = getQuestion(question_format, input_text)
question = completion.choices[0].message.content.split('#')[0]
answer = completion.choices[0].message.content.split('#')[1]

if __name__ == "__main__":
    print(question)
    input_answer = input("Answer to question?: ")
    print(answer)
