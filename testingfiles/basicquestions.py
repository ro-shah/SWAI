import os
from openai import OpenAI

OPENAI_API_KEY = "​"
MODEL = "gpt-4-turbo-preview"
client = OpenAI(api_key = OPENAI_API_KEY)

def extractText(image_link):
    client2 = OpenAI(api_key = OPENAI_API_KEY)
    response = client2.chat.completions.create(
    model = "gpt-4-vision-preview",
    messages = [
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "Extract text from this image: "},
            {
            "type": "image_url",
            "image_url": {
                "url": image_link,
            },
            },
        ],
        }
    ],
    max_tokens = 500,
    )

    image_text_str = response.choices[0].message.content
    print(image_text_str)

    return image_text_str

def getQuestionData():
    global from_text
    from_text = int(input("Would you like me to create a question based on my knowledge or on my notes?: "))
    if from_text == 1:
        subject_of_question = input("Subject?: ")
        question_data = "blank"
    if from_text == 2:
        image_text_link = input("image text link: ").encode('utf-8').strip()
        print(image_text_link)

        question_data = extractText(image_text_link)
        subject_of_question = "blank"

    else:
        print("error")
    type_of_question = input("Type of question?: ")
    
    return [type_of_question, subject_of_question, question_data]

def createQuestion(question_format, input_text, subject_text):
    if from_text == 1:
        response = client.chat.completions.create(
            model = MODEL,
            messages = [
                {"role": "user", "content": "Write to me a " + question_format + "question that tests my knowledge about " + input_text + ". Add the answer after question and seperate the answer and question with a '#'. Furthermore, add an explanation to the answer."},
            ],
            temperature = 0,
    )
    elif from_text == 2:
        response = client.chat.completions.create(
            model = MODEL,
            messages = [
                {"role": "user", "content": "Write to me a " + question_format + "question based on this data " + subject_text + ". Add the answer after question and seperate the answer and question with a '#'. Furthermore, add an explanation to the answer."},
            ],
            temperature = 0,
    )      
    return response

question_format, input_text, question_context = getQuestionData()
completion = createQuestion(question_format, input_text, question_context)
question = completion.choices[0].message.content.split('#')[0]
answer = completion.choices[0].message.content.split('#')[1]

if __name__ == "__main__":
    print(question)
    input_answer = input("Answer to question?: ")
    print(answer)
