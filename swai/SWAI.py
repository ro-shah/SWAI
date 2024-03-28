from openai import OpenAI

class GenerateStudyMaterial:
    def __init__(self, subject, question_format, image_link):
        self.subject = subject
        self.question_format = question_format
        self.openai_api_key = ""
        self.image_link = image_link

    def generateQuestion(self):
        client = OpenAI(api_key = self.openai_api_key)
        response = client.chat.completions.create(
            model = "gpt-4-vision-preview",
            messages = [
                {"role": "user", "content": "Write to me a " + self.question_format + "question that tests my knowledge about " + self.subject + ". Add the answer after question and seperate the answer and question with a '#'. Furthermore, add an explanation to the answer."},
            ],
            temperature = 0)
        
        question = response.choices[0].message.content.split('#')[0]
        answer = response.choices[0].message.content.split('#')[1]

        return question, answer
    
    def generateQuestionFromImage(self):
        client = OpenAI(api_key = self.openai_api_key)
        response = client.chat.completions.create(
        model = "gpt-4-vision-preview",
        messages = [
            {
            "role": "user",
            "content": [
                {"type": "text", "text": "Extract text from this image: "},
                {"type": "image_url","image_url": {"url": self.image_link,}}]}
        ],
        max_tokens = 500,)

        input_text = response.choices[0].message.content

        response = client.chat.completions.create(
            model = "gpt-4-turbo-preview",
            messages = [
                {"role": "user", "content": "Write to me a " + self.question_format + "question based on this data " + input_text + ". Add the answer after question and seperate the answer and question with a '#'. Furthermore, add an explanation to the answer."},
            ],
            temperature = 0,)
          
        question = response.choices[0].message.content.split('#')[0]
        answer = response.choices[0].message.content.split('#')[1]

        return question, answer