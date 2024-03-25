from openai import OpenAI

OPENAI_API_KEY = ""
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
            {"role": "user", "content": "Write to me a " + question_format + "question that tests my knowledge about " + input_text},
        ],
        temperature = 0,
    )
    
    return response

if __name__ == "__main__":    
    question_format, input_text = getQuestionData()
    completion = getQuestion(question_format, input_text)
    print(completion.choices[0].message.content)
