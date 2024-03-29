const openAiModule = require("openai");
const firebaseAdmin = require("firebase-admin");
const express = require("express");

let OPEN_AI_KEY = "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"; // sensitive

const openai = new openAiModule({
    apiKey: OPEN_AI_KEY
});

const port = 6969;

const app = express();

app.get('/test', async (req, res) => {
    console.log(`Request sent to /test`)
    const query = req.query.img
    console.log("QUERY: ", query)
    const response = await openai.chat.completions.create({
        model: "gpt-4-vision-preview",
        messages: [
          {
            role: "user",
            content: [
              { type: "text", text: "Generate study content based on this image. Simply return just what the study material and definitions are. Please give your response as HTML code, and bold all terms."},
              {
                type: "image_url",
                image_url: {
                  "url": query,
                },
              },
            ],
          },
        ],
      });
      console.log(response.choices[0]);
    res.send(response.choices[0]);
})

app.listen(port, () => {
    console.log(`Webserver running on http://localhost:${port}`)
})