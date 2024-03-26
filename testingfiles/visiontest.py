from openai import OpenAI

OPENAI_API_KEY = "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"

client = OpenAI(api_key = OPENAI_API_KEY)

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
            "url": "https://cdn.discordapp.com/attachments/729700899005661215/1222225809993891880/image.png?ex=6615717c&is=6602fc7c&hm=380347091eff80e6675532e5f6d4ce20e3608e44e891f21f397a5c0fe0bc6618&",
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