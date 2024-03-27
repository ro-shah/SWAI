from openai import OpenAI

OPENAI_API_KEY = "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"

client = OpenAI(api_key = OPENAI_API_KEY)
image_link = input("link: ")
def extractText():
  response = client.chat.completions.create(
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

  return response.choices[0]


text = extractText()
print(text)