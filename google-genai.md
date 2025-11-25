现在加入真实的接口并实现ai的介入。这是谷歌官方最新的api指南，读取它并按它的方法调用api。
<br />

<br />

# Gemini API

The developer platform to build and scale with Google's latest AI models. Start in minutes.  

### Python

    from google import genai

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain how AI works in a few words",
    )

    print(response.text)

### JavaScript

    import { GoogleGenAI } from "@google/genai";

    const ai = new GoogleGenAI({});

    async function main() {
      const response = await ai.models.generateContent({
        model: "gemini-2.5-flash",
        contents: "Explain how AI works in a few words",
      });
      console.log(response.text);
    }

    await main();

### Go

    package main

    import (
        "context"
        "fmt"
        "log"
        "google.golang.org/genai"
    )

    func main() {
        ctx := context.Background()
        client, err := genai.NewClient(ctx, nil)
        if err != nil {
            log.Fatal(err)
        }

        result, err := client.Models.GenerateContent(
            ctx,
            "gemini-2.5-flash",
            genai.Text("Explain how AI works in a few words"),
            nil,
        )
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(result.Text())
    }

### Java

    package com.example;

    import com.google.genai.Client;
    import com.google.genai.types.GenerateContentResponse;

    public class GenerateTextFromTextInput {
      public static void main(String[] args) {
        Client client = new Client();

        GenerateContentResponse response =
            client.models.generateContent(
                "gemini-2.5-flash",
                "Explain how AI works in a few words",
                null);

        System.out.println(response.text());
      }
    }

### C#

    using System.Threading.Tasks;
    using Google.GenAI;
    using Google.GenAI.Types;

    public class GenerateContentSimpleText {
      public static async Task main() {
        var client = new Client();
        var response = await client.Models.GenerateContentAsync(
          model: "gemini-2.5-flash", contents: "Explain how AI works in a few words"
        );
        Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
      }
    }

### REST

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -X POST \
      -d '{
        "contents": [
          {
            "parts": [
              {
                "text": "Explain how AI works in a few words"
              }
            ]
          }
        ]
      }'

[Start building](https://ai.google.dev/gemini-api/docs/quickstart)  
Follow our Quickstart guide to get an API key and make your first API call in minutes.

For most models, you can start with our free tier, without having to set up a billing account.

*** ** * ** ***

## Meet the models

[sparkGemini 3 Pro
Our most intelligent model, the best in the world for multimodal understanding, all built on state-of-the-art reasoning.](https://ai.google.dev/gemini-api/docs/models#gemini-3-pro)[sparkGemini 2.5 Pro
Our powerful reasoning model, which excels at coding and complex reasonings tasks.](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-pro)[sparkGemini 2.5 Flash
Our most balanced model, with a 1 million token context window and more.](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-2.5-flash)[sparkGemini 2.5 Flash-Lite
Our fastest and most cost-efficient multimodal model with great performance for high-frequency tasks.](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-2.5-flash-lite)[video_libraryVeo 3.1
Our state-of-the-art video generation model, with native audio.](https://ai.google.dev/gemini-api/docs/video)[🍌Gemini 2.5 Flash Image (Nano Banana)
State-of-the-art image generation and editing model](https://ai.google.dev/gemini-api/docs/image-generation)

## Explore Capabilities

[imagesmode
Native Image Generation (Nano Banana)
Generate and edit highly contextual images natively with Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation)[article
Long Context
Input millions of tokens to Gemini models and derive understanding from unstructured images, videos, and documents.](https://ai.google.dev/gemini-api/docs/long-context)[code
Structured Outputs
Constrain Gemini to respond with JSON, a structured data format suitable for automated processing.](https://ai.google.dev/gemini-api/docs/structured-output)[functions
Function Calling
Build agentic workflows by connecting Gemini to external APIs and tools.](https://ai.google.dev/gemini-api/docs/function-calling)[videocam
Video Generation with Veo 3.1
Create high-quality video content from text or image prompts with our state-of-the-art model.](https://ai.google.dev/gemini-api/docs/video)[android_recorder
Voice Agents with Live API
Build real-time voice applications and agents with the Live API.](https://ai.google.dev/gemini-api/docs/live)[build
Tools
Connect Gemini to the world through built-in tools like Google Search, URL Context, Google Maps, Code Execution and Computer Use.](https://ai.google.dev/gemini-api/docs/tools)[stacks
Document Understanding
Process up to 1000 pages of PDF files.](https://ai.google.dev/gemini-api/docs/document-processing)[cognition_2
Thinking
Explore how thinking capabilities improve reasoning for complex tasks and agents.](https://ai.google.dev/gemini-api/docs/thinking)

## Developer Toolkit

[AI Studio
Test prompts, manage your API keys, monitor usage, and build prototypes in our web-based IDE.
Open AI Studio](https://aistudio.google.com)[groupDeveloper Community
Ask questions and find solutions from other developers and Google engineers.
Join the community](https://discuss.ai.google.dev/c/gemini-api/4)[menu_bookAPI Reference
Find detailed information about the Gemini API in the official reference documentation.
Access the API reference](https://ai.google.dev/api)

<br />

<br />

# Gemini API

The developer platform to build and scale with Google's latest AI models. Start in minutes.  

### Python

    from google import genai

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain how AI works in a few words",
    )

    print(response.text)

### JavaScript

    import { GoogleGenAI } from "@google/genai";

    const ai = new GoogleGenAI({});

    async function main() {
      const response = await ai.models.generateContent({
        model: "gemini-2.5-flash",
        contents: "Explain how AI works in a few words",
      });
      console.log(response.text);
    }

    await main();

### Go

    package main

    import (
        "context"
        "fmt"
        "log"
        "google.golang.org/genai"
    )

    func main() {
        ctx := context.Background()
        client, err := genai.NewClient(ctx, nil)
        if err != nil {
            log.Fatal(err)
        }

        result, err := client.Models.GenerateContent(
            ctx,
            "gemini-2.5-flash",
            genai.Text("Explain how AI works in a few words"),
            nil,
        )
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(result.Text())
    }

### Java

    package com.example;

    import com.google.genai.Client;
    import com.google.genai.types.GenerateContentResponse;

    public class GenerateTextFromTextInput {
      public static void main(String[] args) {
        Client client = new Client();

        GenerateContentResponse response =
            client.models.generateContent(
                "gemini-2.5-flash",
                "Explain how AI works in a few words",
                null);

        System.out.println(response.text());
      }
    }

### C#

    using System.Threading.Tasks;
    using Google.GenAI;
    using Google.GenAI.Types;

    public class GenerateContentSimpleText {
      public static async Task main() {
        var client = new Client();
        var response = await client.Models.GenerateContentAsync(
          model: "gemini-2.5-flash", contents: "Explain how AI works in a few words"
        );
        Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
      }
    }

### REST

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -X POST \
      -d '{
        "contents": [
          {
            "parts": [
              {
                "text": "Explain how AI works in a few words"
              }
            ]
          }
        ]
      }'

[Start building](https://ai.google.dev/gemini-api/docs/quickstart)  
Follow our Quickstart guide to get an API key and make your first API call in minutes.

For most models, you can start with our free tier, without having to set up a billing account.

*** ** * ** ***

## Meet the models

[sparkGemini 3 Pro
Our most intelligent model, the best in the world for multimodal understanding, all built on state-of-the-art reasoning.](https://ai.google.dev/gemini-api/docs/models#gemini-3-pro)[sparkGemini 2.5 Pro
Our powerful reasoning model, which excels at coding and complex reasonings tasks.](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-pro)[sparkGemini 2.5 Flash
Our most balanced model, with a 1 million token context window and more.](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-2.5-flash)[sparkGemini 2.5 Flash-Lite
Our fastest and most cost-efficient multimodal model with great performance for high-frequency tasks.](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-2.5-flash-lite)[video_libraryVeo 3.1
Our state-of-the-art video generation model, with native audio.](https://ai.google.dev/gemini-api/docs/video)[🍌Gemini 2.5 Flash Image (Nano Banana)
State-of-the-art image generation and editing model](https://ai.google.dev/gemini-api/docs/image-generation)

## Explore Capabilities

[imagesmode
Native Image Generation (Nano Banana)
Generate and edit highly contextual images natively with Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation)[article
Long Context
Input millions of tokens to Gemini models and derive understanding from unstructured images, videos, and documents.](https://ai.google.dev/gemini-api/docs/long-context)[code
Structured Outputs
Constrain Gemini to respond with JSON, a structured data format suitable for automated processing.](https://ai.google.dev/gemini-api/docs/structured-output)[functions
Function Calling
Build agentic workflows by connecting Gemini to external APIs and tools.](https://ai.google.dev/gemini-api/docs/function-calling)[videocam
Video Generation with Veo 3.1
Create high-quality video content from text or image prompts with our state-of-the-art model.](https://ai.google.dev/gemini-api/docs/video)[android_recorder
Voice Agents with Live API
Build real-time voice applications and agents with the Live API.](https://ai.google.dev/gemini-api/docs/live)[build
Tools
Connect Gemini to the world through built-in tools like Google Search, URL Context, Google Maps, Code Execution and Computer Use.](https://ai.google.dev/gemini-api/docs/tools)[stacks
Document Understanding
Process up to 1000 pages of PDF files.](https://ai.google.dev/gemini-api/docs/document-processing)[cognition_2
Thinking
Explore how thinking capabilities improve reasoning for complex tasks and agents.](https://ai.google.dev/gemini-api/docs/thinking)

## Developer Toolkit

[AI Studio
Test prompts, manage your API keys, monitor usage, and build prototypes in our web-based IDE.
Open AI Studio](https://aistudio.google.com)[groupDeveloper Community
Ask questions and find solutions from other developers and Google engineers.
Join the community](https://discuss.ai.google.dev/c/gemini-api/4)[menu_bookAPI Reference
Find detailed information about the Gemini API in the official reference documentation.
Access the API reference](https://ai.google.dev/api)
<br />

<br />

# Gemini API

The developer platform to build and scale with Google's latest AI models. Start in minutes.  

### Python

    from google import genai

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain how AI works in a few words",
    )

    print(response.text)

### JavaScript

    import { GoogleGenAI } from "@google/genai";

    const ai = new GoogleGenAI({});

    async function main() {
      const response = await ai.models.generateContent({
        model: "gemini-2.5-flash",
        contents: "Explain how AI works in a few words",
      });
      console.log(response.text);
    }

    await main();

### Go

    package main

    import (
        "context"
        "fmt"
        "log"
        "google.golang.org/genai"
    )

    func main() {
        ctx := context.Background()
        client, err := genai.NewClient(ctx, nil)
        if err != nil {
            log.Fatal(err)
        }

        result, err := client.Models.GenerateContent(
            ctx,
            "gemini-2.5-flash",
            genai.Text("Explain how AI works in a few words"),
            nil,
        )
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(result.Text())
    }

### Java

    package com.example;

    import com.google.genai.Client;
    import com.google.genai.types.GenerateContentResponse;

    public class GenerateTextFromTextInput {
      public static void main(String[] args) {
        Client client = new Client();

        GenerateContentResponse response =
            client.models.generateContent(
                "gemini-2.5-flash",
                "Explain how AI works in a few words",
                null);

        System.out.println(response.text());
      }
    }

### C#

    using System.Threading.Tasks;
    using Google.GenAI;
    using Google.GenAI.Types;

    public class GenerateContentSimpleText {
      public static async Task main() {
        var client = new Client();
        var response = await client.Models.GenerateContentAsync(
          model: "gemini-2.5-flash", contents: "Explain how AI works in a few words"
        );
        Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
      }
    }

### REST

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -X POST \
      -d '{
        "contents": [
          {
            "parts": [
              {
                "text": "Explain how AI works in a few words"
              }
            ]
          }
        ]
      }'

[Start building](https://ai.google.dev/gemini-api/docs/quickstart)  
Follow our Quickstart guide to get an API key and make your first API call in minutes.

For most models, you can start with our free tier, without having to set up a billing account.

*** ** * ** ***

## Meet the models

[sparkGemini 3 Pro
Our most intelligent model, the best in the world for multimodal understanding, all built on state-of-the-art reasoning.](https://ai.google.dev/gemini-api/docs/models#gemini-3-pro)[sparkGemini 2.5 Pro
Our powerful reasoning model, which excels at coding and complex reasonings tasks.](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-pro)[sparkGemini 2.5 Flash
Our most balanced model, with a 1 million token context window and more.](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-2.5-flash)[sparkGemini 2.5 Flash-Lite
Our fastest and most cost-efficient multimodal model with great performance for high-frequency tasks.](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-2.5-flash-lite)[video_libraryVeo 3.1
Our state-of-the-art video generation model, with native audio.](https://ai.google.dev/gemini-api/docs/video)[🍌Gemini 2.5 Flash Image (Nano Banana)
State-of-the-art image generation and editing model](https://ai.google.dev/gemini-api/docs/image-generation)

## Explore Capabilities

[imagesmode
Native Image Generation (Nano Banana)
Generate and edit highly contextual images natively with Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation)[article
Long Context
Input millions of tokens to Gemini models and derive understanding from unstructured images, videos, and documents.](https://ai.google.dev/gemini-api/docs/long-context)[code
Structured Outputs
Constrain Gemini to respond with JSON, a structured data format suitable for automated processing.](https://ai.google.dev/gemini-api/docs/structured-output)[functions
Function Calling
Build agentic workflows by connecting Gemini to external APIs and tools.](https://ai.google.dev/gemini-api/docs/function-calling)[videocam
Video Generation with Veo 3.1
Create high-quality video content from text or image prompts with our state-of-the-art model.](https://ai.google.dev/gemini-api/docs/video)[android_recorder
Voice Agents with Live API
Build real-time voice applications and agents with the Live API.](https://ai.google.dev/gemini-api/docs/live)[build
Tools
Connect Gemini to the world through built-in tools like Google Search, URL Context, Google Maps, Code Execution and Computer Use.](https://ai.google.dev/gemini-api/docs/tools)[stacks
Document Understanding
Process up to 1000 pages of PDF files.](https://ai.google.dev/gemini-api/docs/document-processing)[cognition_2
Thinking
Explore how thinking capabilities improve reasoning for complex tasks and agents.](https://ai.google.dev/gemini-api/docs/thinking)

## Developer Toolkit

[AI Studio
Test prompts, manage your API keys, monitor usage, and build prototypes in our web-based IDE.
Open AI Studio](https://aistudio.google.com)[groupDeveloper Community
Ask questions and find solutions from other developers and Google engineers.
Join the community](https://discuss.ai.google.dev/c/gemini-api/4)[menu_bookAPI Reference
Find detailed information about the Gemini API in the official reference documentation.
Access the API reference](https://ai.google.dev/api)
<br />

<br />

OUR MOST INTELLIGENT MODEL

## Gemini 3 Pro

The best model in the world for multimodal understanding, and our most powerful agentic and vibe-coding model yet, delivering richer visuals and deeper interactivity, all built on a foundation of state-of-the-art reasoning.

### Expand to learn more

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-3-pro-preview)

#### Model details

### Gemini 3 Pro Preview

|                                    Property                                    |                                                                                                                                                                                            Description                                                                                                                                                                                             |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-3-pro-preview`                                                                                                                                                                                                                                                                                                                                                                             |
| saveSupported data types                                                       | **Inputs** Text, Image, Video, Audio, and PDF **Output** Text                                                                                                                                                                                                                                                                                                                                      |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 65,536                                                                                                                                                                                                                                                                                                                                      |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Supported **File search** Supported **Function calling** Supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Not supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Supported **URL context** Supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - `Preview: gemini-3-pro-preview`                                                                                                                                                                                                                                            |
| calendar_monthLatest update                                                    | November 2025                                                                                                                                                                                                                                                                                                                                                                                      |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                       |

### Gemini 3 Pro Image Preview

|                                    Property                                    |                                                                                                                                                                                                    Description                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-3-pro-image-preview`                                                                                                                                                                                                                                                                                                                                                                                       |
| saveSupported data types                                                       | **Inputs** Image and Text **Output** Image and Text                                                                                                                                                                                                                                                                                                                                                                |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 65,536 **Output token limit** 32,768                                                                                                                                                                                                                                                                                                                                                         |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Not supported **Code execution** Not supported **File search** Not supported **Function calling** Not supported **Grounding with Google Maps** Not supported **Image generation** Supported **Live API** Not supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Supported **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - `Preview: gemini-3-pro-image-preview`                                                                                                                                                                                                                                                      |
| calendar_monthLatest update                                                    | November 2025                                                                                                                                                                                                                                                                                                                                                                                                      |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                                       |

OUR ADVANCED THINKING MODEL

## Gemini 2.5 Pro

Our state-of-the-art thinking model, capable of reasoning over complex problems in code, math, and STEM, as well as analyzing large datasets, codebases, and documents using long context.

### Expand to learn more

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-2.5-pro)

#### Model details

### Gemini 2.5 Pro

|                                    Property                                    |                                                                                                                                                                                          Description                                                                                                                                                                                           |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-pro`                                                                                                                                                                                                                                                                                                                                                                               |
| saveSupported data types                                                       | **Inputs** Audio, images, video, text, and PDF **Output** Text                                                                                                                                                                                                                                                                                                                                 |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 65,536                                                                                                                                                                                                                                                                                                                                  |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Supported **File search** Supported **Function calling** Supported **Grounding with Google Maps** Supported **Image generation** Not supported **Live API** Not supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Supported **URL context** Supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - `Stable: gemini-2.5-pro`                                                                                                                                                                                                                                               |
| calendar_monthLatest update                                                    | June 2025                                                                                                                                                                                                                                                                                                                                                                                      |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                   |

### Gemini 2.5 Pro TTS

|                                    Property                                    |                                                                                                                                                                                                          Description                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-pro-preview-tts`                                                                                                                                                                                                                                                                                                                                                                                                   |
| saveSupported data types                                                       | **Inputs** Text **Output** Audio                                                                                                                                                                                                                                                                                                                                                                                               |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 8,192 **Output token limit** 16,384                                                                                                                                                                                                                                                                                                                                                                      |
| handymanCapabilities                                                           | **Audio generation** Supported **Batch API** Not Supported **Caching** Not supported **Code execution** Not supported **File search** Supported **Function calling** Not supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Not supported **Search grounding** Not supported **Structured outputs** Not supported **Thinking** Not supported **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - `gemini-2.5-pro-preview-tts`                                                                                                                                                                                                                                                                           |
| calendar_monthLatest update                                                    | May 2025                                                                                                                                                                                                                                                                                                                                                                                                                       |

FAST AND INTELLIGENT

## Gemini 2.5 Flash

Our best model in terms of price-performance, offering well-rounded capabilities. 2.5 Flash is best for large scale processing, low-latency, high volume tasks that require thinking, and agentic use cases.

### Expand to learn more

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-2.5-flash)

#### Model details

### Gemini 2.5 Flash

|                                    Property                                    |                                                                                                                                                                                          Description                                                                                                                                                                                           |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-flash`                                                                                                                                                                                                                                                                                                                                                                             |
| saveSupported data types                                                       | **Inputs** Text, images, video, audio **Output** Text                                                                                                                                                                                                                                                                                                                                          |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 65,536                                                                                                                                                                                                                                                                                                                                  |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Supported **File search** Supported **Function calling** Supported **Grounding with Google Maps** Supported **Image generation** Not supported **Live API** Not supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Supported **URL context** Supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Stable:`gemini-2.5-flash`                                                                                                                                                                                                                                              |
| calendar_monthLatest update                                                    | June 2025                                                                                                                                                                                                                                                                                                                                                                                      |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                   |

### Gemini 2.5 Flash Preview

|                                    Property                                    |                                                                                                                                                                                            Description                                                                                                                                                                                             |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-flash-preview-09-2025`                                                                                                                                                                                                                                                                                                                                                                 |
| saveSupported data types                                                       | **Inputs** Text, images, video, audio **Output** Text                                                                                                                                                                                                                                                                                                                                              |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 65,536                                                                                                                                                                                                                                                                                                                                      |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Supported **File search** Supported **Function calling** Supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Not supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Supported **URL Context** Supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Preview:`gemini-2.5-flash-preview-09-2025`                                                                                                                                                                                                                                 |
| calendar_monthLatest update                                                    | September 2025                                                                                                                                                                                                                                                                                                                                                                                     |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                       |

### Gemini 2.5 Flash Image

|                                    Property                                    |                                                                                                                                                                                                    Description                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-flash-image`                                                                                                                                                                                                                                                                                                                                                                                           |
| saveSupported data types                                                       | **Inputs** Images and text **Output** Images and text                                                                                                                                                                                                                                                                                                                                                              |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 65,536 **Output token limit** 32,768                                                                                                                                                                                                                                                                                                                                                         |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Not Supported **File search** Supported **Function calling** Not supported **Grounding with Google Maps** Not supported **Image generation** Supported **Live API** Not Supported **Search grounding** Not Supported **Structured outputs** Supported **Thinking** Not Supported **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Stable:`gemini-2.5-flash-image` - Preview:`gemini-2.5-flash-image-preview`                                                                                                                                                                                                                 |
| calendar_monthLatest update                                                    | October 2025                                                                                                                                                                                                                                                                                                                                                                                                       |
| cognition_2Knowledge cutoff                                                    | June 2025                                                                                                                                                                                                                                                                                                                                                                                                          |

### Gemini 2.5 Flash Live

|                                    Property                                    |                                                                                                                                                                                                  Description                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-flash-native-audio-preview-09-2025`                                                                                                                                                                                                                                                                                                                                                                |
| saveSupported data types                                                       | **Inputs** Audio, video, text **Output** Audio and text                                                                                                                                                                                                                                                                                                                                                        |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 131,072 **Output token limit** 8,192                                                                                                                                                                                                                                                                                                                                                     |
| handymanCapabilities                                                           | **Audio generation** Supported **Batch API** Not supported **Caching** Not supported **Code execution** Not supported **File search** Supported **Function calling** Supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Supported **Search grounding** Supported **Structured outputs** Not supported **Thinking** Supported **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Preview:`gemini-2.5-flash-native-audio-preview-09-2025` - Preview:`gemini-live-2.5-flash-preview` - gemini-live-2.5-flash-preview will be deprecated on December 09, 2025                                                                                                              |
| calendar_monthLatest update                                                    | September 2025                                                                                                                                                                                                                                                                                                                                                                                                 |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                                   |

### Gemini 2.5 Flash TTS

|                                    Property                                    |                                                                                                                                                                                                        Description                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-flash-preview-tts`                                                                                                                                                                                                                                                                                                                                                                                             |
| saveSupported data types                                                       | **Inputs** Text **Output** Audio                                                                                                                                                                                                                                                                                                                                                                                           |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 8,192 **Output token limit** 16,384                                                                                                                                                                                                                                                                                                                                                                  |
| handymanCapabilities                                                           | **Audio generation** Supported **Batch API** Supported **Caching** Not supported **Code execution** Not supported **File search** Supported **Function calling** Not supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Not supported **Search grounding** Not supported **Structured outputs** Not supported **Thinking** Not supported **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - `gemini-2.5-flash-preview-tts`                                                                                                                                                                                                                                                                     |
| calendar_monthLatest update                                                    | May 2025                                                                                                                                                                                                                                                                                                                                                                                                                   |

ULTRA FAST

## Gemini 2.5 Flash-Lite

Our fastest flash model optimized for cost-efficiency and high throughput.

### Expand to learn more

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-2.5-flash-lite)

#### Model details

### Gemini 2.5 Flash-Lite

|                                    Property                                    |                                                                                                                                                                                            Description                                                                                                                                                                                             |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-flash-lite`                                                                                                                                                                                                                                                                                                                                                                            |
| saveSupported data types                                                       | **Inputs** Text, image, video, audio, PDF **Output** Text                                                                                                                                                                                                                                                                                                                                          |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 65,536                                                                                                                                                                                                                                                                                                                                      |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Supported **File search** Not supported **Function calling** Supported **Grounding with Google Maps** Supported **Image generation** Not supported **Live API** Not supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Supported **URL context** Supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Stable:`gemini-2.5-flash-lite`                                                                                                                                                                                                                                             |
| calendar_monthLatest update                                                    | July 2025                                                                                                                                                                                                                                                                                                                                                                                          |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                       |

### Gemini 2.5 Flash-Lite Preview

|                                    Property                                    |                                                                                                                                                                                              Description                                                                                                                                                                                               |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-flash-lite-preview-09-2025`                                                                                                                                                                                                                                                                                                                                                                |
| saveSupported data types                                                       | **Inputs** Text, image, video, audio, PDF **Output** Text                                                                                                                                                                                                                                                                                                                                              |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 65,536                                                                                                                                                                                                                                                                                                                                          |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Supported **File search** Not supported **Function calling** Supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Not supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Supported **URL context** Supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Preview:`gemini-2.5-flash-lite-preview-09-2025`                                                                                                                                                                                                                                |
| calendar_monthLatest update                                                    | September 2025                                                                                                                                                                                                                                                                                                                                                                                         |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                           |

<br />

## Previous Gemini models

OUR SECOND GENERATION WORKHORSE MODEL

## Gemini 2.0 Flash

Our second generation workhorse model, with a 1 million token context window.

### Expand to learn more

Gemini 2.0 Flash delivers next-gen features and improved capabilities, including superior speed, native tool use, and a 1M token context window.

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-2.0-flash)

#### Model details

### Gemini 2.0 Flash

|                                    Property                                    |                                                                                                                                                                                              Description                                                                                                                                                                                              |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.0-flash`                                                                                                                                                                                                                                                                                                                                                                                    |
| saveSupported data types                                                       | **Inputs** Audio, images, video, and text **Output** Text                                                                                                                                                                                                                                                                                                                                             |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 8,192                                                                                                                                                                                                                                                                                                                                          |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Supported **File search** Not supported **Function calling** Supported **Grounding with Google Maps** Supported **Image generation** Not supported **Live API** Supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Experimental **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Latest:`gemini-2.0-flash` - Stable:`gemini-2.0-flash-001` - Experimental:`gemini-2.0-flash-exp`                                                                                                                                                                               |
| calendar_monthLatest update                                                    | February 2025                                                                                                                                                                                                                                                                                                                                                                                         |
| cognition_2Knowledge cutoff                                                    | August 2024                                                                                                                                                                                                                                                                                                                                                                                           |

### Gemini 2.0 Flash Image

|                                    Property                                    |                                                                                                                                                                                                      Description                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.0-flash-preview-image-generation`                                                                                                                                                                                                                                                                                                                                                                            |
| saveSupported data types                                                       | **Inputs** Audio, images, video, and text **Output** Text and images                                                                                                                                                                                                                                                                                                                                                   |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 32,768 **Output token limit** 8,192                                                                                                                                                                                                                                                                                                                                                              |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Not Supported **File search** Not supported **Function calling** Not supported **Grounding with Google Maps** Not supported **Image generation** Supported **Live API** Not Supported **Search grounding** Not Supported **Structured outputs** Supported **Thinking** Not Supported **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Preview:`gemini-2.0-flash-preview-image-generation` - gemini-2.0-flash-preview-image-generation is not currently supported in a number of countries in Europe, Middle East \& Africa                                                                                                           |
| calendar_monthLatest update                                                    | May 2025                                                                                                                                                                                                                                                                                                                                                                                                               |
| cognition_2Knowledge cutoff                                                    | August 2024                                                                                                                                                                                                                                                                                                                                                                                                            |

### Gemini 2.0 Flash Live

|                                    Property                                    |                                                                                                                                                                                                Description                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.0-flash-live-001` gemini-2.0-flash-live-001 will be deprecated on December 09, 2025                                                                                                                                                                                                                                                                                                              |
| saveSupported data types                                                       | **Inputs** Audio, video, and text **Output** Text, and audio                                                                                                                                                                                                                                                                                                                                               |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 8,192                                                                                                                                                                                                                                                                                                                                               |
| handymanCapabilities                                                           | **Audio generation** Supported **Batch API** Not supported **Caching** Not supported **Code execution** Supported **File search** Not supported **Function calling** Supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Not supported **URL context** Supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Preview:`gemini-2.0-flash-live-001`                                                                                                                                                                                                                                                |
| calendar_monthLatest update                                                    | April 2025                                                                                                                                                                                                                                                                                                                                                                                                 |
| cognition_2Knowledge cutoff                                                    | August 2024                                                                                                                                                                                                                                                                                                                                                                                                |

OUR SECOND GENERATION FAST MODEL

## Gemini 2.0 Flash-Lite

Our second generation small workhorse model, with a 1 million token context window.

### Expand to learn more

A Gemini 2.0 Flash model optimized for cost efficiency and low latency.

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-2.0-flash-lite)

#### Model details

|                                    Property                                    |                                                                                                                                                                                                      Description                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.0-flash-lite`                                                                                                                                                                                                                                                                                                                                                                                                |
| saveSupported data types                                                       | **Inputs** Audio, images, video, and text **Output** Text                                                                                                                                                                                                                                                                                                                                                              |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 8,192                                                                                                                                                                                                                                                                                                                                                           |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Not supported **File search** Not supported **Function calling** Supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Not supported **Search grounding** Not supported **Structured outputs** Supported **Thinking** Not Supported **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Latest:`gemini-2.0-flash-lite` - Stable:`gemini-2.0-flash-lite-001`                                                                                                                                                                                                                            |
| calendar_monthLatest update                                                    | February 2025                                                                                                                                                                                                                                                                                                                                                                                                          |
| cognition_2Knowledge cutoff                                                    | August 2024                                                                                                                                                                                                                                                                                                                                                                                                            |

<br />

## Model version name patterns

Gemini models are available in either*stable* ,*preview* ,*latest* , or*experimental*versions.
| **Note:** The following list refers to the model string naming convention as of September, 2025. Models released prior to that may have different naming conventions. Refer to the exact model string if you are using an older model.

### Stable

Points to a specific stable model. Stable models usually don't change. Most production apps should use a specific stable model.

For example:`gemini-2.5-flash`.

### Preview

Points to a preview model which may be used for production. Preview models will typically have billing enabled, might come with more restrictive rate limits and will be deprecated with at least 2 weeks notice.

For example:`gemini-2.5-flash-preview-09-2025`.

### Latest

Points to the latest release for a specific model variation. This can be a stable, preview or experimental release. This alias will get hot-swapped with every new release of a specific model variation. A**2-week notice**will be provided through email before the version behind latest is changed.

For example:`gemini-flash-latest`.

### Experimental

Points to an experimental model which will typically be not be suitable for production use and come with more restrictive rate limits. We release experimental models to gather feedback and get our latest updates into the hands of developers quickly.

Experimental models are not stable and availability of model endpoints is subject to change.

## Model deprecations

For information about model deprecations, visit the[Gemini deprecations](https://ai.google.dev/gemini-api/docs/deprecations)page.
<br />

<br />

OUR MOST INTELLIGENT MODEL

## Gemini 3 Pro

The best model in the world for multimodal understanding, and our most powerful agentic and vibe-coding model yet, delivering richer visuals and deeper interactivity, all built on a foundation of state-of-the-art reasoning.

### Expand to learn more

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-3-pro-preview)

#### Model details

### Gemini 3 Pro Preview

|                                    Property                                    |                                                                                                                                                                                            Description                                                                                                                                                                                             |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-3-pro-preview`                                                                                                                                                                                                                                                                                                                                                                             |
| saveSupported data types                                                       | **Inputs** Text, Image, Video, Audio, and PDF **Output** Text                                                                                                                                                                                                                                                                                                                                      |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 65,536                                                                                                                                                                                                                                                                                                                                      |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Supported **File search** Supported **Function calling** Supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Not supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Supported **URL context** Supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - `Preview: gemini-3-pro-preview`                                                                                                                                                                                                                                            |
| calendar_monthLatest update                                                    | November 2025                                                                                                                                                                                                                                                                                                                                                                                      |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                       |

### Gemini 3 Pro Image Preview

|                                    Property                                    |                                                                                                                                                                                                    Description                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-3-pro-image-preview`                                                                                                                                                                                                                                                                                                                                                                                       |
| saveSupported data types                                                       | **Inputs** Image and Text **Output** Image and Text                                                                                                                                                                                                                                                                                                                                                                |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 65,536 **Output token limit** 32,768                                                                                                                                                                                                                                                                                                                                                         |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Not supported **Code execution** Not supported **File search** Not supported **Function calling** Not supported **Grounding with Google Maps** Not supported **Image generation** Supported **Live API** Not supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Supported **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - `Preview: gemini-3-pro-image-preview`                                                                                                                                                                                                                                                      |
| calendar_monthLatest update                                                    | November 2025                                                                                                                                                                                                                                                                                                                                                                                                      |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                                       |

OUR ADVANCED THINKING MODEL

## Gemini 2.5 Pro

Our state-of-the-art thinking model, capable of reasoning over complex problems in code, math, and STEM, as well as analyzing large datasets, codebases, and documents using long context.

### Expand to learn more

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-2.5-pro)

#### Model details

### Gemini 2.5 Pro

|                                    Property                                    |                                                                                                                                                                                          Description                                                                                                                                                                                           |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-pro`                                                                                                                                                                                                                                                                                                                                                                               |
| saveSupported data types                                                       | **Inputs** Audio, images, video, text, and PDF **Output** Text                                                                                                                                                                                                                                                                                                                                 |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 65,536                                                                                                                                                                                                                                                                                                                                  |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Supported **File search** Supported **Function calling** Supported **Grounding with Google Maps** Supported **Image generation** Not supported **Live API** Not supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Supported **URL context** Supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - `Stable: gemini-2.5-pro`                                                                                                                                                                                                                                               |
| calendar_monthLatest update                                                    | June 2025                                                                                                                                                                                                                                                                                                                                                                                      |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                   |

### Gemini 2.5 Pro TTS

|                                    Property                                    |                                                                                                                                                                                                          Description                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-pro-preview-tts`                                                                                                                                                                                                                                                                                                                                                                                                   |
| saveSupported data types                                                       | **Inputs** Text **Output** Audio                                                                                                                                                                                                                                                                                                                                                                                               |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 8,192 **Output token limit** 16,384                                                                                                                                                                                                                                                                                                                                                                      |
| handymanCapabilities                                                           | **Audio generation** Supported **Batch API** Not Supported **Caching** Not supported **Code execution** Not supported **File search** Supported **Function calling** Not supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Not supported **Search grounding** Not supported **Structured outputs** Not supported **Thinking** Not supported **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - `gemini-2.5-pro-preview-tts`                                                                                                                                                                                                                                                                           |
| calendar_monthLatest update                                                    | May 2025                                                                                                                                                                                                                                                                                                                                                                                                                       |

FAST AND INTELLIGENT

## Gemini 2.5 Flash

Our best model in terms of price-performance, offering well-rounded capabilities. 2.5 Flash is best for large scale processing, low-latency, high volume tasks that require thinking, and agentic use cases.

### Expand to learn more

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-2.5-flash)

#### Model details

### Gemini 2.5 Flash

|                                    Property                                    |                                                                                                                                                                                          Description                                                                                                                                                                                           |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-flash`                                                                                                                                                                                                                                                                                                                                                                             |
| saveSupported data types                                                       | **Inputs** Text, images, video, audio **Output** Text                                                                                                                                                                                                                                                                                                                                          |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 65,536                                                                                                                                                                                                                                                                                                                                  |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Supported **File search** Supported **Function calling** Supported **Grounding with Google Maps** Supported **Image generation** Not supported **Live API** Not supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Supported **URL context** Supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Stable:`gemini-2.5-flash`                                                                                                                                                                                                                                              |
| calendar_monthLatest update                                                    | June 2025                                                                                                                                                                                                                                                                                                                                                                                      |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                   |

### Gemini 2.5 Flash Preview

|                                    Property                                    |                                                                                                                                                                                            Description                                                                                                                                                                                             |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-flash-preview-09-2025`                                                                                                                                                                                                                                                                                                                                                                 |
| saveSupported data types                                                       | **Inputs** Text, images, video, audio **Output** Text                                                                                                                                                                                                                                                                                                                                              |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 65,536                                                                                                                                                                                                                                                                                                                                      |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Supported **File search** Supported **Function calling** Supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Not supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Supported **URL Context** Supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Preview:`gemini-2.5-flash-preview-09-2025`                                                                                                                                                                                                                                 |
| calendar_monthLatest update                                                    | September 2025                                                                                                                                                                                                                                                                                                                                                                                     |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                       |

### Gemini 2.5 Flash Image

|                                    Property                                    |                                                                                                                                                                                                    Description                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-flash-image`                                                                                                                                                                                                                                                                                                                                                                                           |
| saveSupported data types                                                       | **Inputs** Images and text **Output** Images and text                                                                                                                                                                                                                                                                                                                                                              |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 65,536 **Output token limit** 32,768                                                                                                                                                                                                                                                                                                                                                         |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Not Supported **File search** Supported **Function calling** Not supported **Grounding with Google Maps** Not supported **Image generation** Supported **Live API** Not Supported **Search grounding** Not Supported **Structured outputs** Supported **Thinking** Not Supported **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Stable:`gemini-2.5-flash-image` - Preview:`gemini-2.5-flash-image-preview`                                                                                                                                                                                                                 |
| calendar_monthLatest update                                                    | October 2025                                                                                                                                                                                                                                                                                                                                                                                                       |
| cognition_2Knowledge cutoff                                                    | June 2025                                                                                                                                                                                                                                                                                                                                                                                                          |

### Gemini 2.5 Flash Live

|                                    Property                                    |                                                                                                                                                                                                  Description                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-flash-native-audio-preview-09-2025`                                                                                                                                                                                                                                                                                                                                                                |
| saveSupported data types                                                       | **Inputs** Audio, video, text **Output** Audio and text                                                                                                                                                                                                                                                                                                                                                        |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 131,072 **Output token limit** 8,192                                                                                                                                                                                                                                                                                                                                                     |
| handymanCapabilities                                                           | **Audio generation** Supported **Batch API** Not supported **Caching** Not supported **Code execution** Not supported **File search** Supported **Function calling** Supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Supported **Search grounding** Supported **Structured outputs** Not supported **Thinking** Supported **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Preview:`gemini-2.5-flash-native-audio-preview-09-2025` - Preview:`gemini-live-2.5-flash-preview` - gemini-live-2.5-flash-preview will be deprecated on December 09, 2025                                                                                                              |
| calendar_monthLatest update                                                    | September 2025                                                                                                                                                                                                                                                                                                                                                                                                 |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                                   |

### Gemini 2.5 Flash TTS

|                                    Property                                    |                                                                                                                                                                                                        Description                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-flash-preview-tts`                                                                                                                                                                                                                                                                                                                                                                                             |
| saveSupported data types                                                       | **Inputs** Text **Output** Audio                                                                                                                                                                                                                                                                                                                                                                                           |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 8,192 **Output token limit** 16,384                                                                                                                                                                                                                                                                                                                                                                  |
| handymanCapabilities                                                           | **Audio generation** Supported **Batch API** Supported **Caching** Not supported **Code execution** Not supported **File search** Supported **Function calling** Not supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Not supported **Search grounding** Not supported **Structured outputs** Not supported **Thinking** Not supported **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - `gemini-2.5-flash-preview-tts`                                                                                                                                                                                                                                                                     |
| calendar_monthLatest update                                                    | May 2025                                                                                                                                                                                                                                                                                                                                                                                                                   |

ULTRA FAST

## Gemini 2.5 Flash-Lite

Our fastest flash model optimized for cost-efficiency and high throughput.

### Expand to learn more

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-2.5-flash-lite)

#### Model details

### Gemini 2.5 Flash-Lite

|                                    Property                                    |                                                                                                                                                                                            Description                                                                                                                                                                                             |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-flash-lite`                                                                                                                                                                                                                                                                                                                                                                            |
| saveSupported data types                                                       | **Inputs** Text, image, video, audio, PDF **Output** Text                                                                                                                                                                                                                                                                                                                                          |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 65,536                                                                                                                                                                                                                                                                                                                                      |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Supported **File search** Not supported **Function calling** Supported **Grounding with Google Maps** Supported **Image generation** Not supported **Live API** Not supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Supported **URL context** Supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Stable:`gemini-2.5-flash-lite`                                                                                                                                                                                                                                             |
| calendar_monthLatest update                                                    | July 2025                                                                                                                                                                                                                                                                                                                                                                                          |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                       |

### Gemini 2.5 Flash-Lite Preview

|                                    Property                                    |                                                                                                                                                                                              Description                                                                                                                                                                                               |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.5-flash-lite-preview-09-2025`                                                                                                                                                                                                                                                                                                                                                                |
| saveSupported data types                                                       | **Inputs** Text, image, video, audio, PDF **Output** Text                                                                                                                                                                                                                                                                                                                                              |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 65,536                                                                                                                                                                                                                                                                                                                                          |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Supported **File search** Not supported **Function calling** Supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Not supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Supported **URL context** Supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Preview:`gemini-2.5-flash-lite-preview-09-2025`                                                                                                                                                                                                                                |
| calendar_monthLatest update                                                    | September 2025                                                                                                                                                                                                                                                                                                                                                                                         |
| cognition_2Knowledge cutoff                                                    | January 2025                                                                                                                                                                                                                                                                                                                                                                                           |

<br />

## Previous Gemini models

OUR SECOND GENERATION WORKHORSE MODEL

## Gemini 2.0 Flash

Our second generation workhorse model, with a 1 million token context window.

### Expand to learn more

Gemini 2.0 Flash delivers next-gen features and improved capabilities, including superior speed, native tool use, and a 1M token context window.

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-2.0-flash)

#### Model details

### Gemini 2.0 Flash

|                                    Property                                    |                                                                                                                                                                                              Description                                                                                                                                                                                              |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.0-flash`                                                                                                                                                                                                                                                                                                                                                                                    |
| saveSupported data types                                                       | **Inputs** Audio, images, video, and text **Output** Text                                                                                                                                                                                                                                                                                                                                             |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 8,192                                                                                                                                                                                                                                                                                                                                          |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Supported **File search** Not supported **Function calling** Supported **Grounding with Google Maps** Supported **Image generation** Not supported **Live API** Supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Experimental **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Latest:`gemini-2.0-flash` - Stable:`gemini-2.0-flash-001` - Experimental:`gemini-2.0-flash-exp`                                                                                                                                                                               |
| calendar_monthLatest update                                                    | February 2025                                                                                                                                                                                                                                                                                                                                                                                         |
| cognition_2Knowledge cutoff                                                    | August 2024                                                                                                                                                                                                                                                                                                                                                                                           |

### Gemini 2.0 Flash Image

|                                    Property                                    |                                                                                                                                                                                                      Description                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.0-flash-preview-image-generation`                                                                                                                                                                                                                                                                                                                                                                            |
| saveSupported data types                                                       | **Inputs** Audio, images, video, and text **Output** Text and images                                                                                                                                                                                                                                                                                                                                                   |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 32,768 **Output token limit** 8,192                                                                                                                                                                                                                                                                                                                                                              |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Not Supported **File search** Not supported **Function calling** Not supported **Grounding with Google Maps** Not supported **Image generation** Supported **Live API** Not Supported **Search grounding** Not Supported **Structured outputs** Supported **Thinking** Not Supported **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Preview:`gemini-2.0-flash-preview-image-generation` - gemini-2.0-flash-preview-image-generation is not currently supported in a number of countries in Europe, Middle East \& Africa                                                                                                           |
| calendar_monthLatest update                                                    | May 2025                                                                                                                                                                                                                                                                                                                                                                                                               |
| cognition_2Knowledge cutoff                                                    | August 2024                                                                                                                                                                                                                                                                                                                                                                                                            |

### Gemini 2.0 Flash Live

|                                    Property                                    |                                                                                                                                                                                                Description                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.0-flash-live-001` gemini-2.0-flash-live-001 will be deprecated on December 09, 2025                                                                                                                                                                                                                                                                                                              |
| saveSupported data types                                                       | **Inputs** Audio, video, and text **Output** Text, and audio                                                                                                                                                                                                                                                                                                                                               |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 8,192                                                                                                                                                                                                                                                                                                                                               |
| handymanCapabilities                                                           | **Audio generation** Supported **Batch API** Not supported **Caching** Not supported **Code execution** Supported **File search** Not supported **Function calling** Supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Supported **Search grounding** Supported **Structured outputs** Supported **Thinking** Not supported **URL context** Supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Preview:`gemini-2.0-flash-live-001`                                                                                                                                                                                                                                                |
| calendar_monthLatest update                                                    | April 2025                                                                                                                                                                                                                                                                                                                                                                                                 |
| cognition_2Knowledge cutoff                                                    | August 2024                                                                                                                                                                                                                                                                                                                                                                                                |

OUR SECOND GENERATION FAST MODEL

## Gemini 2.0 Flash-Lite

Our second generation small workhorse model, with a 1 million token context window.

### Expand to learn more

A Gemini 2.0 Flash model optimized for cost efficiency and low latency.

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-2.0-flash-lite)

#### Model details

|                                    Property                                    |                                                                                                                                                                                                      Description                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_cardModel code                                                              | `gemini-2.0-flash-lite`                                                                                                                                                                                                                                                                                                                                                                                                |
| saveSupported data types                                                       | **Inputs** Audio, images, video, and text **Output** Text                                                                                                                                                                                                                                                                                                                                                              |
| token_autoToken limits^[\[\*\]](https://ai.google.dev/gemini-api/docs/tokens)^ | **Input token limit** 1,048,576 **Output token limit** 8,192                                                                                                                                                                                                                                                                                                                                                           |
| handymanCapabilities                                                           | **Audio generation** Not supported **Batch API** Supported **Caching** Supported **Code execution** Not supported **File search** Not supported **Function calling** Supported **Grounding with Google Maps** Not supported **Image generation** Not supported **Live API** Not supported **Search grounding** Not supported **Structured outputs** Supported **Thinking** Not Supported **URL context** Not supported |
| 123Versions                                                                    | Read the[model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions)for more details. - Latest:`gemini-2.0-flash-lite` - Stable:`gemini-2.0-flash-lite-001`                                                                                                                                                                                                                            |
| calendar_monthLatest update                                                    | February 2025                                                                                                                                                                                                                                                                                                                                                                                                          |
| cognition_2Knowledge cutoff                                                    | August 2024                                                                                                                                                                                                                                                                                                                                                                                                            |

<br />

## Model version name patterns

Gemini models are available in either*stable* ,*preview* ,*latest* , or*experimental*versions.
| **Note:** The following list refers to the model string naming convention as of September, 2025. Models released prior to that may have different naming conventions. Refer to the exact model string if you are using an older model.

### Stable

Points to a specific stable model. Stable models usually don't change. Most production apps should use a specific stable model.

For example:`gemini-2.5-flash`.

### Preview

Points to a preview model which may be used for production. Preview models will typically have billing enabled, might come with more restrictive rate limits and will be deprecated with at least 2 weeks notice.

For example:`gemini-2.5-flash-preview-09-2025`.

### Latest

Points to the latest release for a specific model variation. This can be a stable, preview or experimental release. This alias will get hot-swapped with every new release of a specific model variation. A**2-week notice**will be provided through email before the version behind latest is changed.

For example:`gemini-flash-latest`.

### Experimental

Points to an experimental model which will typically be not be suitable for production use and come with more restrictive rate limits. We release experimental models to gather feedback and get our latest updates into the hands of developers quickly.

Experimental models are not stable and availability of model endpoints is subject to change.

## Model deprecations

For information about model deprecations, visit the[Gemini deprecations](https://ai.google.dev/gemini-api/docs/deprecations)page.
<br />

Gemini models are built to be multimodal from the ground up, unlocking a wide range of image processing and computer vision tasks including but not limited to image captioning, classification, and visual question answering without having to train specialized ML models.
| **Tip:** In addition to their general multimodal capabilities, Gemini models (2.0 and newer) offer**improved accuracy** for specific use cases like[object detection](https://ai.google.dev/gemini-api/docs/image-understanding#object-detection)and[segmentation](https://ai.google.dev/gemini-api/docs/image-understanding#segmentation), through additional training. See the[Capabilities](https://ai.google.dev/gemini-api/docs/image-understanding#capabilities)section for more details.

## Passing images to Gemini

You can provide images as input to Gemini using two methods:

- [Passing inline image data](https://ai.google.dev/gemini-api/docs/image-understanding#inline-image): Ideal for smaller files (total request size less than 20MB, including prompts).
- [Uploading images using the File API](https://ai.google.dev/gemini-api/docs/image-understanding#upload-image): Recommended for larger files or for reusing images across multiple requests.

### Passing inline image data

You can pass inline image data in the request to`generateContent`. You can provide image data as Base64 encoded strings or by reading local files directly (depending on the language).

The following example shows how to read an image from a local file and pass it to`generateContent`API for processing.  

### Python

      from google import genai
      from google.genai import types

      with open('path/to/small-sample.jpg', 'rb') as f:
          image_bytes = f.read()

      client = genai.Client()
      response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[
          types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
          ),
          'Caption this image.'
        ]
      )

      print(response.text)

### JavaScript

    import { GoogleGenAI } from "@google/genai";
    import * as fs from "node:fs";

    const ai = new GoogleGenAI({});
    const base64ImageFile = fs.readFileSync("path/to/small-sample.jpg", {
      encoding: "base64",
    });

    const contents = [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageFile,
        },
      },
      { text: "Caption this image." },
    ];

    const response = await ai.models.generateContent({
      model: "gemini-2.5-flash",
      contents: contents,
    });
    console.log(response.text);

### Go

    bytes, _ := os.ReadFile("path/to/small-sample.jpg")

    parts := []*genai.Part{
      genai.NewPartFromBytes(bytes, "image/jpeg"),
      genai.NewPartFromText("Caption this image."),
    }

    contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
    }

    result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-2.5-flash",
      contents,
      nil,
    )

    fmt.Println(result.Text())

### REST

    IMG_PATH="/path/to/your/image1.jpg"

    if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
    B64FLAGS="--input"
    else
    B64FLAGS="-w0"
    fi

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
        "contents": [{
        "parts":[
            {
                "inline_data": {
                "mime_type":"image/jpeg",
                "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'"
                }
            },
            {"text": "Caption this image."},
        ]
        }]
    }' 2> /dev/null

You can also fetch an image from a URL, convert it to bytes, and pass it to`generateContent`as shown in the following examples.  

### Python

    from google import genai
    from google.genai import types

    import requests

    image_path = "https://goo.gle/instrument-img"
    image_bytes = requests.get(image_path).content
    image = types.Part.from_bytes(
      data=image_bytes, mime_type="image/jpeg"
    )

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=["What is this image?", image],
    )

    print(response.text)

### JavaScript

    import { GoogleGenAI } from "@google/genai";

    async function main() {
      const ai = new GoogleGenAI({});

      const imageUrl = "https://goo.gle/instrument-img";

      const response = await fetch(imageUrl);
      const imageArrayBuffer = await response.arrayBuffer();
      const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

      const result = await ai.models.generateContent({
        model: "gemini-2.5-flash",
        contents: [
        {
          inlineData: {
            mimeType: 'image/jpeg',
            data: base64ImageData,
          },
        },
        { text: "Caption this image." }
      ],
      });
      console.log(result.text);
    }

    main();

### Go

    package main

    import (
      "context"
      "fmt"
      "os"
      "io"
      "net/http"
      "google.golang.org/genai"
    )

    func main() {
      ctx := context.Background()
      client, err := genai.NewClient(ctx, nil)
      if err != nil {
          log.Fatal(err)
      }

      // Download the image.
      imageResp, _ := http.Get("https://goo.gle/instrument-img")

      imageBytes, _ := io.ReadAll(imageResp.Body)

      parts := []*genai.Part{
        genai.NewPartFromBytes(imageBytes, "image/jpeg"),
        genai.NewPartFromText("Caption this image."),
      }

      contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
      }

      result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-2.5-flash",
        contents,
        nil,
      )

      fmt.Println(result.Text())
    }

### REST

    IMG_URL="https://goo.gle/instrument-img"

    MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
    if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
      MIME_TYPE="image/jpeg"
    fi

    # Check for macOS
    if [[ "$(uname)" == "Darwin" ]]; then
      IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
    elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
      IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
    else
      IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
    fi

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
        -H "x-goog-api-key: $GEMINI_API_KEY" \
        -H 'Content-Type: application/json' \
        -X POST \
        -d '{
          "contents": [{
            "parts":[
                {
                  "inline_data": {
                    "mime_type":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                },
                {"text": "Caption this image."}
            ]
          }]
        }' 2> /dev/null

| **Note:** Inline image data limits your total request size (text prompts, system instructions, and inline bytes) to 20MB. For larger requests,[upload image files](https://ai.google.dev/gemini-api/docs/image-understanding#upload-image)using the File API. Files API is also more efficient for scenarios that use the same image repeatedly.

### Uploading images using the File API

For large files or to be able to use the same image file repeatedly, use the Files API. The following code uploads an image file and then uses the file in a call to`generateContent`. See the[Files API guide](https://ai.google.dev/gemini-api/docs/files)for more information and examples.  

### Python

    from google import genai

    client = genai.Client()

    my_file = client.files.upload(file="path/to/sample.jpg")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[my_file, "Caption this image."],
    )

    print(response.text)

### JavaScript

    import {
      GoogleGenAI,
      createUserContent,
      createPartFromUri,
    } from "@google/genai";

    const ai = new GoogleGenAI({});

    async function main() {
      const myfile = await ai.files.upload({
        file: "path/to/sample.jpg",
        config: { mimeType: "image/jpeg" },
      });

      const response = await ai.models.generateContent({
        model: "gemini-2.5-flash",
        contents: createUserContent([
          createPartFromUri(myfile.uri, myfile.mimeType),
          "Caption this image.",
        ]),
      });
      console.log(response.text);
    }

    await main();

### Go

    package main

    import (
      "context"
      "fmt"
      "os"
      "google.golang.org/genai"
    )

    func main() {
      ctx := context.Background()
      client, err := genai.NewClient(ctx, nil)
      if err != nil {
          log.Fatal(err)
      }

      uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.jpg", nil)

      parts := []*genai.Part{
          genai.NewPartFromText("Caption this image."),
          genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
      }

      contents := []*genai.Content{
          genai.NewContentFromParts(parts, genai.RoleUser),
      }

      result, _ := client.Models.GenerateContent(
          ctx,
          "gemini-2.5-flash",
          contents,
          nil,
      )

      fmt.Println(result.Text())
    }

### REST

    IMAGE_PATH="path/to/sample.jpg"
    MIME_TYPE=$(file -b --mime-type "${IMAGE_PATH}")
    NUM_BYTES=$(wc -c < "${IMAGE_PATH}")
    DISPLAY_NAME=IMAGE

    tmp_header_file=upload-header.tmp

    # Initial resumable request defining metadata.
    # The upload url is in the response headers dump them to a file.
    curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -D upload-header.tmp \
      -H "X-Goog-Upload-Protocol: resumable" \
      -H "X-Goog-Upload-Command: start" \
      -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
      -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
      -H "Content-Type: application/json" \
      -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

    upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
    rm "${tmp_header_file}"

    # Upload the actual bytes.
    curl "${upload_url}" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H "Content-Length: ${NUM_BYTES}" \
      -H "X-Goog-Upload-Offset: 0" \
      -H "X-Goog-Upload-Command: upload, finalize" \
      --data-binary "@${IMAGE_PATH}" 2> /dev/null > file_info.json

    file_uri=$(jq -r ".file.uri" file_info.json)
    echo file_uri=$file_uri

    # Now generate content using that file
    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
        -H "x-goog-api-key: $GEMINI_API_KEY" \
        -H 'Content-Type: application/json' \
        -X POST \
        -d '{
          "contents": [{
            "parts":[
              {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
              {"text": "Caption this image."}]
            }]
          }' 2> /dev/null > response.json

    cat response.json
    echo

    jq ".candidates[].content.parts[].text" response.json

## Prompting with multiple images

You can provide multiple images in a single prompt by including multiple image`Part`objects in the`contents`array. These can be a mix of inline data (local files or URLs) and File API references.  

### Python

    from google import genai
    from google.genai import types

    client = genai.Client()

    # Upload the first image
    image1_path = "path/to/image1.jpg"
    uploaded_file = client.files.upload(file=image1_path)

    # Prepare the second image as inline data
    image2_path = "path/to/image2.png"
    with open(image2_path, 'rb') as f:
        img2_bytes = f.read()

    # Create the prompt with text and multiple images
    response = client.models.generate_content(

        model="gemini-2.5-flash",
        contents=[
            "What is different between these two images?",
            uploaded_file,  # Use the uploaded file reference
            types.Part.from_bytes(
                data=img2_bytes,
                mime_type='image/png'
            )
        ]
    )

    print(response.text)

### JavaScript

    import {
      GoogleGenAI,
      createUserContent,
      createPartFromUri,
    } from "@google/genai";
    import * as fs from "node:fs";

    const ai = new GoogleGenAI({});

    async function main() {
      // Upload the first image
      const image1_path = "path/to/image1.jpg";
      const uploadedFile = await ai.files.upload({
        file: image1_path,
        config: { mimeType: "image/jpeg" },
      });

      // Prepare the second image as inline data
      const image2_path = "path/to/image2.png";
      const base64Image2File = fs.readFileSync(image2_path, {
        encoding: "base64",
      });

      // Create the prompt with text and multiple images

      const response = await ai.models.generateContent({

        model: "gemini-2.5-flash",
        contents: createUserContent([
          "What is different between these two images?",
          createPartFromUri(uploadedFile.uri, uploadedFile.mimeType),
          {
            inlineData: {
              mimeType: "image/png",
              data: base64Image2File,
            },
          },
        ]),
      });
      console.log(response.text);
    }

    await main();

### Go

    // Upload the first image
    image1Path := "path/to/image1.jpg"
    uploadedFile, _ := client.Files.UploadFromPath(ctx, image1Path, nil)

    // Prepare the second image as inline data
    image2Path := "path/to/image2.jpeg"
    imgBytes, _ := os.ReadFile(image2Path)

    parts := []*genai.Part{
      genai.NewPartFromText("What is different between these two images?"),
      genai.NewPartFromBytes(imgBytes, "image/jpeg"),
      genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    }

    contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
    }

    result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-2.5-flash",
      contents,
      nil,
    )

    fmt.Println(result.Text())

### REST

    # Upload the first image
    IMAGE1_PATH="path/to/image1.jpg"
    MIME1_TYPE=$(file -b --mime-type "${IMAGE1_PATH}")
    NUM1_BYTES=$(wc -c < "${IMAGE1_PATH}")
    DISPLAY_NAME1=IMAGE1

    tmp_header_file1=upload-header1.tmp

    curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -D upload-header1.tmp \
      -H "X-Goog-Upload-Protocol: resumable" \
      -H "X-Goog-Upload-Command: start" \
      -H "X-Goog-Upload-Header-Content-Length: ${NUM1_BYTES}" \
      -H "X-Goog-Upload-Header-Content-Type: ${MIME1_TYPE}" \
      -H "Content-Type: application/json" \
      -d "{'file': {'display_name': '${DISPLAY_NAME1}'}}" 2> /dev/null

    upload_url1=$(grep -i "x-goog-upload-url: " "${tmp_header_file1}" | cut -d" " -f2 | tr -d "\r")
    rm "${tmp_header_file1}"

    curl "${upload_url1}" \
      -H "Content-Length: ${NUM1_BYTES}" \
      -H "X-Goog-Upload-Offset: 0" \
      -H "X-Goog-Upload-Command: upload, finalize" \
      --data-binary "@${IMAGE1_PATH}" 2> /dev/null > file_info1.json

    file1_uri=$(jq ".file.uri" file_info1.json)
    echo file1_uri=$file1_uri

    # Prepare the second image (inline)
    IMAGE2_PATH="path/to/image2.png"
    MIME2_TYPE=$(file -b --mime-type "${IMAGE2_PATH}")

    if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
      B64FLAGS="--input"
    else
      B64FLAGS="-w0"
    fi
    IMAGE2_BASE64=$(base64 $B64FLAGS $IMAGE2_PATH)

    # Now generate content using both images
    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
        -H "x-goog-api-key: $GEMINI_API_KEY" \
        -H 'Content-Type: application/json' \
        -X POST \
        -d '{
          "contents": [{
            "parts":[
              {"text": "What is different between these two images?"},
              {"file_data":{"mime_type": "'"${MIME1_TYPE}"'", "file_uri": '$file1_uri'}},
              {
                "inline_data": {
                  "mime_type":"'"${MIME2_TYPE}"'",
                  "data": "'"$IMAGE2_BASE64"'"
                }
              }
            ]
          }]
        }' 2> /dev/null > response.json

    cat response.json
    echo

    jq ".candidates[].content.parts[].text" response.json

## Object detection

From Gemini 2.0 onwards, models are further trained to detect objects in an image and get their bounding box coordinates. The coordinates, relative to image dimensions, scale to \[0, 1000\]. You need to descale these coordinates based on your original image size.  

### Python

    from google import genai
    from google.genai import types
    from PIL import Image
    import json

    client = genai.Client()
    prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

    image = Image.open("/path/to/image.png")

    config = types.GenerateContentConfig(
      response_mime_type="application/json"
      )

    response = client.models.generate_content(model="gemini-2.5-flash",
                                              contents=[image, prompt],
                                              config=config
                                              )

    width, height = image.size
    bounding_boxes = json.loads(response.text)

    converted_bounding_boxes = []
    for bounding_box in bounding_boxes:
        abs_y1 = int(bounding_box["box_2d"][0]/1000 * height)
        abs_x1 = int(bounding_box["box_2d"][1]/1000 * width)
        abs_y2 = int(bounding_box["box_2d"][2]/1000 * height)
        abs_x2 = int(bounding_box["box_2d"][3]/1000 * width)
        converted_bounding_boxes.append([abs_x1, abs_y1, abs_x2, abs_y2])

    print("Image size: ", width, height)
    print("Bounding boxes:", converted_bounding_boxes)

| **Note:** The model also supports generating bounding boxes based on custom instructions, such as: "Show bounding boxes of all green objects in this image". It also support custom labels like "label the items with the allergens they can contain".

For more examples, check following notebooks in the[Gemini Cookbook](https://github.com/google-gemini/cookbook):

- [2D spatial understanding notebook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb)
- [Experimental 3D pointing notebook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb)

## Segmentation

Starting with Gemini 2.5, models not only detect items but also segment them and provide their contour masks.

The model predicts a JSON list, where each item represents a segmentation mask. Each item has a bounding box ("`box_2d`") in the format`[y0, x0, y1, x1]`with normalized coordinates between 0 and 1000, a label ("`label`") that identifies the object, and finally the segmentation mask inside the bounding box, as base64 encoded png that is a probability map with values between 0 and 255. The mask needs to be resized to match the bounding box dimensions, then binarized at your confidence threshold (127 for the midpoint).
**Note:** For better results, disable[thinking](https://ai.google.dev/gemini-api/docs/thinking)by setting the thinking budget to 0. See code sample below for an example.  

### Python

    from google import genai
    from google.genai import types
    from PIL import Image, ImageDraw
    import io
    import base64
    import json
    import numpy as np
    import os

    client = genai.Client()

    def parse_json(json_output: str):
      # Parsing out the markdown fencing
      lines = json_output.splitlines()
      for i, line in enumerate(lines):
        if line == "```json":
          json_output = "\n".join(lines[i+1:])  # Remove everything before "```json"
          output = json_output.split("```")[0]  # Remove everything after the closing "```"
          break  # Exit the loop once "```json" is found
      return json_output

    def extract_segmentation_masks(image_path: str, output_dir: str = "segmentation_outputs"):
      # Load and resize image
      im = Image.open(image_path)
      im.thumbnail([1024, 1024], Image.Resampling.LANCZOS)

      prompt = """
      Give the segmentation masks for the wooden and glass items.
      Output a JSON list of segmentation masks where each entry contains the 2D
      bounding box in the key "box_2d", the segmentation mask in key "mask", and
      the text label in the key "label". Use descriptive labels.
      """

      config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # set thinking_budget to 0 for better results in object detection
      )

      response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt, im], # Pillow images can be directly passed as inputs (which will be converted by the SDK)
        config=config
      )

      # Parse JSON response
      items = json.loads(parse_json(response.text))

      # Create output directory
      os.makedirs(output_dir, exist_ok=True)

      # Process each mask
      for i, item in enumerate(items):
          # Get bounding box coordinates
          box = item["box_2d"]
          y0 = int(box[0] / 1000 * im.size[1])
          x0 = int(box[1] / 1000 * im.size[0])
          y1 = int(box[2] / 1000 * im.size[1])
          x1 = int(box[3] / 1000 * im.size[0])

          # Skip invalid boxes
          if y0 >= y1 or x0 >= x1:
              continue

          # Process mask
          png_str = item["mask"]
          if not png_str.startswith("data:image/png;base64,"):
              continue

          # Remove prefix
          png_str = png_str.removeprefix("data:image/png;base64,")
          mask_data = base64.b64decode(png_str)
          mask = Image.open(io.BytesIO(mask_data))

          # Resize mask to match bounding box
          mask = mask.resize((x1 - x0, y1 - y0), Image.Resampling.BILINEAR)

          # Convert mask to numpy array for processing
          mask_array = np.array(mask)

          # Create overlay for this mask
          overlay = Image.new('RGBA', im.size, (0, 0, 0, 0))
          overlay_draw = ImageDraw.Draw(overlay)

          # Create overlay for the mask
          color = (255, 255, 255, 200)
          for y in range(y0, y1):
              for x in range(x0, x1):
                  if mask_array[y - y0, x - x0] > 128:  # Threshold for mask
                      overlay_draw.point((x, y), fill=color)

          # Save individual mask and its overlay
          mask_filename = f"{item['label']}_{i}_mask.png"
          overlay_filename = f"{item['label']}_{i}_overlay.png"

          mask.save(os.path.join(output_dir, mask_filename))

          # Create and save overlay
          composite = Image.alpha_composite(im.convert('RGBA'), overlay)
          composite.save(os.path.join(output_dir, overlay_filename))
          print(f"Saved mask and overlay for {item['label']} to {output_dir}")

    # Example usage
    if __name__ == "__main__":
      extract_segmentation_masks("path/to/image.png")

Check the[segmentation example](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb#scrollTo=WQJTJ8wdGOKx)in the cookbook guide for a more detailed example.
![A table with cupcakes, with the wooden and glass objects highlighted](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg)An example segmentation output with objects and segmentation masks

## Supported image formats

Gemini supports the following image format MIME types:

- PNG -`image/png`
- JPEG -`image/jpeg`
- WEBP -`image/webp`
- HEIC -`image/heic`
- HEIF -`image/heif`

## Capabilities

All Gemini model versions are multimodal and can be utilized in a wide range of image processing and computer vision tasks including but not limited to image captioning, visual question and answering, image classification, object detection and segmentation.

Gemini can reduce the need to use specialized ML models depending on your quality and performance requirements.

Some later model versions are specifically trained improve accuracy of specialized tasks in addition to generic capabilities:

- **Gemini 2.0 models** are further trained to support enhanced[object detection](https://ai.google.dev/gemini-api/docs/image-understanding#object-detection).

- **Gemini 2.5 models** are further trained to support enhanced[segmentation](https://ai.google.dev/gemini-api/docs/image-understanding#segmentation)in addition to[object detection](https://ai.google.dev/gemini-api/docs/image-understanding#object-detection).

## Limitations and key technical information

### File limit

Gemini 2.5 Pro/Flash, 2.0 Flash, 1.5 Pro, and 1.5 Flash support a maximum of 3,600 image files per request.

### Token calculation

- **Gemini 1.5 Flash and Gemini 1.5 Pro**: 258 tokens if both dimensions \<= 384 pixels. Larger images are tiled (min tile 256px, max 768px, resized to 768x768), with each tile costing 258 tokens.
- **Gemini 2.0 Flash and Gemini 2.5 Flash/Pro**: 258 tokens if both dimensions \<= 384 pixels. Larger images are tiled into 768x768 pixel tiles, each costing 258 tokens.

A rough formula for calculating the number of tiles is as follows:

- Calculate the crop unit size which is roughly: floor(min(width, height) / 1.5).
- Divide each dimension by the crop unit size and multiply together to get the number of tiles.

For example, for an image of dimensions 960x540 would have a crop unit size of 360. Divide each dimension by 360 and the number of tile is 3 \* 2 = 6.

### Media resolution

Gemini 3 introduces granular control over multimodal vision processing with the`media_resolution`parameter. The`media_resolution`parameter determines the**maximum number of tokens allocated per input image or video frame.**Higher resolutions improve the model's ability to read fine text or identify small details, but increase token usage and latency.

For more details about the parameter and how it can impact token calculations, see the[media resolution](https://ai.google.dev/gemini-api/docs/media-resolution)guide.

## Tips and best practices

- Verify that images are correctly rotated.
- Use clear, non-blurry images.
- When using a single image with text, place the text prompt*after* the image part in the`contents`array.

## What's next

This guide shows you how to upload image files and generate text outputs from image inputs. To learn more, see the following resources:

- [Files API](https://ai.google.dev/gemini-api/docs/files): Learn more about uploading and managing files for use with Gemini.
- [System instructions](https://ai.google.dev/gemini-api/docs/text-generation#system-instructions): System instructions let you steer the behavior of the model based on your specific needs and use cases.
- [File prompting strategies](https://ai.google.dev/gemini-api/docs/files#prompt-guide): The Gemini API supports prompting with text, image, audio, and video data, also known as multimodal prompting.
- [Safety guidance](https://ai.google.dev/gemini-api/docs/safety-guidance): Sometimes generative AI models produce unexpected outputs, such as outputs that are inaccurate, biased, or offensive. Post-processing and human evaluation are essential to limit the risk of harm from such outputs.
<br />

You can configure Gemini models to generate responses that adhere to a provided JSON Schema. This capability guarantees predictable and parsable results, ensures format and type-safety, enables the programmatic detection of refusals, and simplifies prompting.

Using structured outputs is ideal for a wide range of applications:

- **Data extraction:**Pull specific information from unstructured text, like extracting names, dates, and amounts from an invoice.
- **Structured classification:**Classify text into predefined categories and assign structured labels, such as categorizing customer feedback by sentiment and topic.
- **Agentic workflows:**Generate structured data that can be used to call other tools or APIs, like creating a character sheet for a game or filling out a form.

In addition to supporting JSON Schema in the REST API, the Google GenAI SDKs for Python and JavaScript also make it easy to define object schemas using[Pydantic](https://docs.pydantic.dev/latest/)and[Zod](https://zod.dev/), respectively. The example below demonstrates how to extract information from unstructured text that conforms to a schema defined in code.

Recipe ExtractorContent ModerationRecursive Structures

This example demonstrates how to extract structured data from text using basic JSON Schema types like`object`,`array`,`string`, and`integer`.  

### Python

    from google import genai
    from pydantic import BaseModel, Field
    from typing import List, Optional

    class Ingredient(BaseModel):
        name: str = Field(description="Name of the ingredient.")
        quantity: str = Field(description="Quantity of the ingredient, including units.")

    class Recipe(BaseModel):
        recipe_name: str = Field(description="The name of the recipe.")
        prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
        ingredients: List[Ingredient]
        instructions: List[str]

    client = genai.Client()

    prompt = """
    Please extract the recipe from the following text.
    The user wants to make delicious chocolate chip cookies.
    They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
    1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
    3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
    For the best part, they'll need 2 cups of semisweet chocolate chips.
    First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
    baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
    until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
    ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
    onto ungreased baking sheets and bake for 9 to 11 minutes.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_json_schema": Recipe.model_json_schema(),
        },
    )

    recipe = Recipe.model_validate_json(response.text)
    print(recipe)

### JavaScript

    import { GoogleGenAI } from "@google/genai";
    import { z } from "zod";
    import { zodToJsonSchema } from "zod-to-json-schema";

    const ingredientSchema = z.object({
      name: z.string().describe("Name of the ingredient."),
      quantity: z.string().describe("Quantity of the ingredient, including units."),
    });

    const recipeSchema = z.object({
      recipe_name: z.string().describe("The name of the recipe."),
      prep_time_minutes: z.number().optional().describe("Optional time in minutes to prepare the recipe."),
      ingredients: z.array(ingredientSchema),
      instructions: z.array(z.string()),
    });

    const ai = new GoogleGenAI({});

    const prompt = `
    Please extract the recipe from the following text.
    The user wants to make delicious chocolate chip cookies.
    They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
    1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
    3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
    For the best part, they'll need 2 cups of semisweet chocolate chips.
    First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
    baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
    until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
    ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
    onto ungreased baking sheets and bake for 9 to 11 minutes.
    `;

    const response = await ai.models.generateContent({
      model: "gemini-2.5-flash",
      contents: prompt,
      config: {
        responseMimeType: "application/json",
        responseJsonSchema: zodToJsonSchema(recipeSchema),
      },
    });

    const recipe = recipeSchema.parse(JSON.parse(response.text));
    console.log(recipe);

### Go

    package main

    import (
        "context"
        "fmt"
        "log"

        "google.golang.org/genai"
    )

    func main() {
        ctx := context.Background()
        client, err := genai.NewClient(ctx, nil)
        if err != nil {
            log.Fatal(err)
        }

        prompt := `
      Please extract the recipe from the following text.
      The user wants to make delicious chocolate chip cookies.
      They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
      1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
      3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
      For the best part, they'll need 2 cups of semisweet chocolate chips.
      First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
      baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
      until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
      ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
      onto ungreased baking sheets and bake for 9 to 11 minutes.
      `
        config := &genai.GenerateContentConfig{
            ResponseMIMEType: "application/json",
            ResponseJsonSchema: map[string]any{
                "type": "object",
                "properties": map[string]any{
                    "recipe_name": map[string]any{
                        "type":        "string",
                        "description": "The name of the recipe.",
                    },
                    "prep_time_minutes": map[string]any{
                        "type":        "integer",
                        "description": "Optional time in minutes to prepare the recipe.",
                    },
                    "ingredients": map[string]any{
                        "type": "array",
                        "items": map[string]any{
                            "type": "object",
                            "properties": map[string]any{
                                "name": map[string]any{
                                    "type":        "string",
                                    "description": "Name of the ingredient.",
                                },
                                "quantity": map[string]any{
                                    "type":        "string",
                                    "description": "Quantity of the ingredient, including units.",
                                },
                            },
                            "required": []string{"name", "quantity"},
                        },
                    },
                    "instructions": map[string]any{
                        "type":  "array",
                        "items": map[string]any{"type": "string"},
                    },
                },
                "required": []string{"recipe_name", "ingredients", "instructions"},
            },
        }

        result, err := client.Models.GenerateContent(
            ctx,
            "gemini-2.5-flash",
            genai.Text(prompt),
            config,
        )
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(result.Text())
    }

### REST

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
        -H "x-goog-api-key: $GEMINI_API_KEY" \
        -H 'Content-Type: application/json' \
        -X POST \
        -d '{
          "contents": [{
            "parts":[
              { "text": "Please extract the recipe from the following text.\nThe user wants to make delicious chocolate chip cookies.\nThey need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,\n1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,\n3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.\nFor the best part, they will need 2 cups of semisweet chocolate chips.\nFirst, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,\nbaking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar\nuntil light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry\ningredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons\nonto ungreased baking sheets and bake for 9 to 11 minutes." }
            ]
          }],
          "generationConfig": {
            "responseMimeType": "application/json",
            "responseJsonSchema": {
              "type": "object",
              "properties": {
                "recipe_name": {
                  "type": "string",
                  "description": "The name of the recipe."
                },
                "prep_time_minutes": {
                    "type": "integer",
                    "description": "Optional time in minutes to prepare the recipe."
                },
                "ingredients": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "name": { "type": "string", "description": "Name of the ingredient."},
                      "quantity": { "type": "string", "description": "Quantity of the ingredient, including units."}
                    },
                    "required": ["name", "quantity"]
                  }
                },
                "instructions": {
                  "type": "array",
                  "items": { "type": "string" }
                }
              },
              "required": ["recipe_name", "ingredients", "instructions"]
            }
          }
        }'

**Example Response:**  

    {
      "recipe_name": "Delicious Chocolate Chip Cookies",
      "ingredients": [
        {
          "name": "all-purpose flour",
          "quantity": "2 and 1/4 cups"
        },
        {
          "name": "baking soda",
          "quantity": "1 teaspoon"
        },
        {
          "name": "salt",
          "quantity": "1 teaspoon"
        },
        {
          "name": "unsalted butter (softened)",
          "quantity": "1 cup"
        },
        {
          "name": "granulated sugar",
          "quantity": "3/4 cup"
        },
        {
          "name": "packed brown sugar",
          "quantity": "3/4 cup"
        },
        {
          "name": "vanilla extract",
          "quantity": "1 teaspoon"
        },
        {
          "name": "large eggs",
          "quantity": "2"
        },
        {
          "name": "semisweet chocolate chips",
          "quantity": "2 cups"
        }
      ],
      "instructions": [
        "Preheat the oven to 375°F (190°C).",
        "In a small bowl, whisk together the flour, baking soda, and salt.",
        "In a large bowl, cream together the butter, granulated sugar, and brown sugar until light and fluffy.",
        "Beat in the vanilla and eggs, one at a time.",
        "Gradually beat in the dry ingredients until just combined.",
        "Stir in the chocolate chips.",
        "Drop by rounded tablespoons onto ungreased baking sheets and bake for 9 to 11 minutes."
      ]
    }

## Streaming

You can stream structured outputs, which allows you to start processing the response as it's being generated, without having to wait for the entire output to be complete. This can improve the perceived performance of your application.

The streamed chunks will be valid partial JSON strings, which can be concatenated to form the final, complete JSON object.  

### Python

    from google import genai
    from pydantic import BaseModel, Field
    from typing import Literal

    class Feedback(BaseModel):
        sentiment: Literal["positive", "neutral", "negative"]
        summary: str

    client = genai.Client()
    prompt = "The new UI is incredibly intuitive and visually appealing. Great job. Add a very long summary to test streaming!"

    response_stream = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_json_schema": Feedback.model_json_schema(),
        },
    )

    for chunk in response_stream:
        print(chunk.candidates[0].content.parts[0].text)

### JavaScript

    import { GoogleGenAI } from "@google/genai";
    import { z } from "zod";
    import { zodToJsonSchema } from "zod-to-json-schema";

    const ai = new GoogleGenAI({});
    const prompt = "The new UI is incredibly intuitive and visually appealing. Great job! Add a very long summary to test streaming!";

    const feedbackSchema = z.object({
      sentiment: z.enum(["positive", "neutral", "negative"]),
      summary: z.string(),
    });

    const stream = await ai.models.generateContentStream({
      model: "gemini-2.5-flash",
      contents: prompt,
      config: {
        responseMimeType: "application/json",
        responseJsonSchema: zodToJsonSchema(feedbackSchema),
      },
    });

    for await (const chunk of stream) {
      console.log(chunk.candidates[0].content.parts[0].text)
    }

## Structured outputs with tools

| **Preview:** This is a feature available only with the`gemini-3-pro-preview`model.

Gemini 3 lets you combine Structured Outputs with built-in tools, including[Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search),[URL Context](https://ai.google.dev/gemini-api/docs/url-context), and[Code Execution](https://ai.google.dev/gemini-api/docs/code-execution).  

### Python

    from google import genai
    from pydantic import BaseModel, Field
    from typing import List

    class MatchResult(BaseModel):
        winner: str = Field(description="The name of the winner.")
        final_match_score: str = Field(description="The final match score.")
        scorers: List[str] = Field(description="The name of the scorer.")

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents="Search for all details for the latest Euro.",
        config={
            "tools": [
                {"google_search": {}},
                {"url_context": {}}
            ],
            "response_mime_type": "application/json",
            "response_json_schema": MatchResult.model_json_schema(),
        },  
    )

    result = MatchResult.model_validate_json(response.text)
    print(result)

### JavaScript

    import { GoogleGenAI } from "@google/genai";
    import { z } from "zod";
    import { zodToJsonSchema } from "zod-to-json-schema";

    const ai = new GoogleGenAI({});

    const matchSchema = z.object({
      winner: z.string().describe("The name of the winner."),
      final_match_score: z.string().describe("The final score."),
      scorers: z.array(z.string()).describe("The name of the scorer.")
    });

    async function run() {
      const response = await ai.models.generateContent({
        model: "gemini-3-pro-preview",
        contents: "Search for all details for the latest Euro.",
        config: {
          tools: [
            { googleSearch: {} },
            { urlContext: {} }
          ],
          responseMimeType: "application/json",
          responseJsonSchema: zodToJsonSchema(matchSchema),
        },
      });

      const match = matchSchema.parse(JSON.parse(response.text));
      console.log(match);
    }

    run();

### REST

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-preview:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -X POST \
      -d '{
        "contents": [{
          "parts": [{"text": "Search for all details for the latest Euro."}]
        }],
        "tools": [
          {"googleSearch": {}},
          {"urlContext": {}}
        ],
        "generationConfig": {
            "responseMimeType": "application/json",
            "responseJsonSchema": {
                "type": "object",
                "properties": {
                    "winner": {"type": "string", "description": "The name of the winner."},
                    "final_match_score": {"type": "string", "description": "The final score."},
                    "scorers": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The name of the scorer."
                    }
                },
                "required": ["winner", "final_match_score", "scorers"]
            }
        }
      }'

## JSON schema support

To generate a JSON object, set the`response_mime_type`in the generation configuration to`application/json`and provide a`response_json_schema`. The schema must be a valid[JSON Schema](https://json-schema.org/)that describes the desired output format.

The model will then generate a response that is a syntactically valid JSON string matching the provided schema. When using structured outputs, the model will produce outputs in the same order as the keys in the schema.

Gemini's structured output mode supports a subset of the[JSON Schema](https://json-schema.org)specification.

The following values of`type`are supported:

- **`string`**: For text.
- **`number`**: For floating-point numbers.
- **`integer`**: For whole numbers.
- **`boolean`**: For true/false values.
- **`object`**: For structured data with key-value pairs.
- **`array`**: For lists of items.
- **`null`** : To allow a property to be null, include`"null"`in the type array (e.g.,`{"type": ["string", "null"]}`).

These descriptive properties help guide the model:

- **`title`**: A short description of a property.
- **`description`**: A longer and more detailed description of a property.

### Type-specific properties

**For`object`values:**

- **`properties`**: An object where each key is a property name and each value is a schema for that property.
- **`required`**: An array of strings, listing which properties are mandatory.
- **`additionalProperties`** : Controls whether properties not listed in`properties`are allowed. Can be a boolean or a schema.

**For`string`values:**

- **`enum`**: Lists a specific set of possible strings for classification tasks.
- **`format`** : Specifies a syntax for the string, such as`date-time`,`date`,`time`.

**For`number`and`integer`values:**

- **`enum`**: Lists a specific set of possible numeric values.
- **`minimum`**: The minimum inclusive value.
- **`maximum`**: The maximum inclusive value.

**For`array`values:**

- **`items`**: Defines the schema for all items in the array.
- **`prefixItems`**: Defines a list of schemas for the first N items, allowing for tuple-like structures.
- **`minItems`**: The minimum number of items in the array.
- **`maxItems`**: The maximum number of items in the array.

## Model support

The following models support structured output:

|         Model         | Structured Outputs |
|-----------------------|--------------------|
| Gemini 3 Pro Preview  | ✔️                 |
| Gemini 2.5 Pro        | ✔️                 |
| Gemini 2.5 Flash      | ✔️                 |
| Gemini 2.5 Flash-Lite | ✔️                 |
| Gemini 2.0 Flash      | ✔️\*               |
| Gemini 2.0 Flash-Lite | ✔️\*               |

*\* Note that Gemini 2.0 requires an explicit`propertyOrdering`list within the JSON input to define the preferred structure. You can find an example in this[cookbook](https://github.com/google-gemini/cookbook/blob/main/examples/Pdf_structured_outputs_on_invoices_and_forms.ipynbs).*

## Structured outputs vs. function calling

Both structured outputs and function calling use JSON schemas, but they serve different purposes:

|        Feature         |                                                                                  Primary Use Case                                                                                  |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Structured Outputs** | **Formatting the final response to the user.** Use this when you want the model's*answer*to be in a specific format (e.g., extracting data from a document to save to a database). |
| **Function Calling**   | **Taking action during the conversation.** Use this when the model needs to*ask you*to perform a task (e.g., "get current weather") before it can provide a final answer.          |

## Best practices

- **Clear descriptions:** Use the`description`field in your schema to provide clear instructions to the model about what each property represents. This is crucial for guiding the model's output.
- **Strong typing:** Use specific types (`integer`,`string`,`enum`) whenever possible. If a parameter has a limited set of valid values, use an`enum`.
- **Prompt engineering:**Clearly state in your prompt what you want the model to do. For example, "Extract the following information from the text..." or "Classify this feedback according to the provided schema...".
- **Validation:**While structured output guarantees syntactically correct JSON, it does not guarantee the values are semantically correct. Always validate the final output in your application code before using it.
- **Error handling:**Implement robust error handling in your application to gracefully manage cases where the model's output, while schema-compliant, may not meet your business logic requirements.

## Limitations

- **Schema subset:**Not all features of the JSON Schema specification are supported. The model ignores unsupported properties.
- **Schema complexity:**The API may reject very large or deeply nested schemas. If you encounter errors, try simplifying your schema by shortening property names, reducing nesting, or limiting the number of constraints.
<br />

You can configure Gemini models to generate responses that adhere to a provided JSON Schema. This capability guarantees predictable and parsable results, ensures format and type-safety, enables the programmatic detection of refusals, and simplifies prompting.

Using structured outputs is ideal for a wide range of applications:

- **Data extraction:**Pull specific information from unstructured text, like extracting names, dates, and amounts from an invoice.
- **Structured classification:**Classify text into predefined categories and assign structured labels, such as categorizing customer feedback by sentiment and topic.
- **Agentic workflows:**Generate structured data that can be used to call other tools or APIs, like creating a character sheet for a game or filling out a form.

In addition to supporting JSON Schema in the REST API, the Google GenAI SDKs for Python and JavaScript also make it easy to define object schemas using[Pydantic](https://docs.pydantic.dev/latest/)and[Zod](https://zod.dev/), respectively. The example below demonstrates how to extract information from unstructured text that conforms to a schema defined in code.

Recipe ExtractorContent ModerationRecursive Structures

This example demonstrates how to extract structured data from text using basic JSON Schema types like`object`,`array`,`string`, and`integer`.  

### Python

    from google import genai
    from pydantic import BaseModel, Field
    from typing import List, Optional

    class Ingredient(BaseModel):
        name: str = Field(description="Name of the ingredient.")
        quantity: str = Field(description="Quantity of the ingredient, including units.")

    class Recipe(BaseModel):
        recipe_name: str = Field(description="The name of the recipe.")
        prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
        ingredients: List[Ingredient]
        instructions: List[str]

    client = genai.Client()

    prompt = """
    Please extract the recipe from the following text.
    The user wants to make delicious chocolate chip cookies.
    They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
    1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
    3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
    For the best part, they'll need 2 cups of semisweet chocolate chips.
    First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
    baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
    until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
    ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
    onto ungreased baking sheets and bake for 9 to 11 minutes.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_json_schema": Recipe.model_json_schema(),
        },
    )

    recipe = Recipe.model_validate_json(response.text)
    print(recipe)

### JavaScript

    import { GoogleGenAI } from "@google/genai";
    import { z } from "zod";
    import { zodToJsonSchema } from "zod-to-json-schema";

    const ingredientSchema = z.object({
      name: z.string().describe("Name of the ingredient."),
      quantity: z.string().describe("Quantity of the ingredient, including units."),
    });

    const recipeSchema = z.object({
      recipe_name: z.string().describe("The name of the recipe."),
      prep_time_minutes: z.number().optional().describe("Optional time in minutes to prepare the recipe."),
      ingredients: z.array(ingredientSchema),
      instructions: z.array(z.string()),
    });

    const ai = new GoogleGenAI({});

    const prompt = `
    Please extract the recipe from the following text.
    The user wants to make delicious chocolate chip cookies.
    They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
    1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
    3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
    For the best part, they'll need 2 cups of semisweet chocolate chips.
    First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
    baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
    until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
    ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
    onto ungreased baking sheets and bake for 9 to 11 minutes.
    `;

    const response = await ai.models.generateContent({
      model: "gemini-2.5-flash",
      contents: prompt,
      config: {
        responseMimeType: "application/json",
        responseJsonSchema: zodToJsonSchema(recipeSchema),
      },
    });

    const recipe = recipeSchema.parse(JSON.parse(response.text));
    console.log(recipe);

### Go

    package main

    import (
        "context"
        "fmt"
        "log"

        "google.golang.org/genai"
    )

    func main() {
        ctx := context.Background()
        client, err := genai.NewClient(ctx, nil)
        if err != nil {
            log.Fatal(err)
        }

        prompt := `
      Please extract the recipe from the following text.
      The user wants to make delicious chocolate chip cookies.
      They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
      1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
      3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
      For the best part, they'll need 2 cups of semisweet chocolate chips.
      First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
      baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
      until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
      ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
      onto ungreased baking sheets and bake for 9 to 11 minutes.
      `
        config := &genai.GenerateContentConfig{
            ResponseMIMEType: "application/json",
            ResponseJsonSchema: map[string]any{
                "type": "object",
                "properties": map[string]any{
                    "recipe_name": map[string]any{
                        "type":        "string",
                        "description": "The name of the recipe.",
                    },
                    "prep_time_minutes": map[string]any{
                        "type":        "integer",
                        "description": "Optional time in minutes to prepare the recipe.",
                    },
                    "ingredients": map[string]any{
                        "type": "array",
                        "items": map[string]any{
                            "type": "object",
                            "properties": map[string]any{
                                "name": map[string]any{
                                    "type":        "string",
                                    "description": "Name of the ingredient.",
                                },
                                "quantity": map[string]any{
                                    "type":        "string",
                                    "description": "Quantity of the ingredient, including units.",
                                },
                            },
                            "required": []string{"name", "quantity"},
                        },
                    },
                    "instructions": map[string]any{
                        "type":  "array",
                        "items": map[string]any{"type": "string"},
                    },
                },
                "required": []string{"recipe_name", "ingredients", "instructions"},
            },
        }

        result, err := client.Models.GenerateContent(
            ctx,
            "gemini-2.5-flash",
            genai.Text(prompt),
            config,
        )
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(result.Text())
    }

### REST

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
        -H "x-goog-api-key: $GEMINI_API_KEY" \
        -H 'Content-Type: application/json' \
        -X POST \
        -d '{
          "contents": [{
            "parts":[
              { "text": "Please extract the recipe from the following text.\nThe user wants to make delicious chocolate chip cookies.\nThey need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,\n1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,\n3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.\nFor the best part, they will need 2 cups of semisweet chocolate chips.\nFirst, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,\nbaking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar\nuntil light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry\ningredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons\nonto ungreased baking sheets and bake for 9 to 11 minutes." }
            ]
          }],
          "generationConfig": {
            "responseMimeType": "application/json",
            "responseJsonSchema": {
              "type": "object",
              "properties": {
                "recipe_name": {
                  "type": "string",
                  "description": "The name of the recipe."
                },
                "prep_time_minutes": {
                    "type": "integer",
                    "description": "Optional time in minutes to prepare the recipe."
                },
                "ingredients": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "name": { "type": "string", "description": "Name of the ingredient."},
                      "quantity": { "type": "string", "description": "Quantity of the ingredient, including units."}
                    },
                    "required": ["name", "quantity"]
                  }
                },
                "instructions": {
                  "type": "array",
                  "items": { "type": "string" }
                }
              },
              "required": ["recipe_name", "ingredients", "instructions"]
            }
          }
        }'

**Example Response:**  

    {
      "recipe_name": "Delicious Chocolate Chip Cookies",
      "ingredients": [
        {
          "name": "all-purpose flour",
          "quantity": "2 and 1/4 cups"
        },
        {
          "name": "baking soda",
          "quantity": "1 teaspoon"
        },
        {
          "name": "salt",
          "quantity": "1 teaspoon"
        },
        {
          "name": "unsalted butter (softened)",
          "quantity": "1 cup"
        },
        {
          "name": "granulated sugar",
          "quantity": "3/4 cup"
        },
        {
          "name": "packed brown sugar",
          "quantity": "3/4 cup"
        },
        {
          "name": "vanilla extract",
          "quantity": "1 teaspoon"
        },
        {
          "name": "large eggs",
          "quantity": "2"
        },
        {
          "name": "semisweet chocolate chips",
          "quantity": "2 cups"
        }
      ],
      "instructions": [
        "Preheat the oven to 375°F (190°C).",
        "In a small bowl, whisk together the flour, baking soda, and salt.",
        "In a large bowl, cream together the butter, granulated sugar, and brown sugar until light and fluffy.",
        "Beat in the vanilla and eggs, one at a time.",
        "Gradually beat in the dry ingredients until just combined.",
        "Stir in the chocolate chips.",
        "Drop by rounded tablespoons onto ungreased baking sheets and bake for 9 to 11 minutes."
      ]
    }

## Streaming

You can stream structured outputs, which allows you to start processing the response as it's being generated, without having to wait for the entire output to be complete. This can improve the perceived performance of your application.

The streamed chunks will be valid partial JSON strings, which can be concatenated to form the final, complete JSON object.  

### Python

    from google import genai
    from pydantic import BaseModel, Field
    from typing import Literal

    class Feedback(BaseModel):
        sentiment: Literal["positive", "neutral", "negative"]
        summary: str

    client = genai.Client()
    prompt = "The new UI is incredibly intuitive and visually appealing. Great job. Add a very long summary to test streaming!"

    response_stream = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_json_schema": Feedback.model_json_schema(),
        },
    )

    for chunk in response_stream:
        print(chunk.candidates[0].content.parts[0].text)

### JavaScript

    import { GoogleGenAI } from "@google/genai";
    import { z } from "zod";
    import { zodToJsonSchema } from "zod-to-json-schema";

    const ai = new GoogleGenAI({});
    const prompt = "The new UI is incredibly intuitive and visually appealing. Great job! Add a very long summary to test streaming!";

    const feedbackSchema = z.object({
      sentiment: z.enum(["positive", "neutral", "negative"]),
      summary: z.string(),
    });

    const stream = await ai.models.generateContentStream({
      model: "gemini-2.5-flash",
      contents: prompt,
      config: {
        responseMimeType: "application/json",
        responseJsonSchema: zodToJsonSchema(feedbackSchema),
      },
    });

    for await (const chunk of stream) {
      console.log(chunk.candidates[0].content.parts[0].text)
    }

## Structured outputs with tools

| **Preview:** This is a feature available only with the`gemini-3-pro-preview`model.

Gemini 3 lets you combine Structured Outputs with built-in tools, including[Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search),[URL Context](https://ai.google.dev/gemini-api/docs/url-context), and[Code Execution](https://ai.google.dev/gemini-api/docs/code-execution).  

### Python

    from google import genai
    from pydantic import BaseModel, Field
    from typing import List

    class MatchResult(BaseModel):
        winner: str = Field(description="The name of the winner.")
        final_match_score: str = Field(description="The final match score.")
        scorers: List[str] = Field(description="The name of the scorer.")

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents="Search for all details for the latest Euro.",
        config={
            "tools": [
                {"google_search": {}},
                {"url_context": {}}
            ],
            "response_mime_type": "application/json",
            "response_json_schema": MatchResult.model_json_schema(),
        },  
    )

    result = MatchResult.model_validate_json(response.text)
    print(result)

### JavaScript

    import { GoogleGenAI } from "@google/genai";
    import { z } from "zod";
    import { zodToJsonSchema } from "zod-to-json-schema";

    const ai = new GoogleGenAI({});

    const matchSchema = z.object({
      winner: z.string().describe("The name of the winner."),
      final_match_score: z.string().describe("The final score."),
      scorers: z.array(z.string()).describe("The name of the scorer.")
    });

    async function run() {
      const response = await ai.models.generateContent({
        model: "gemini-3-pro-preview",
        contents: "Search for all details for the latest Euro.",
        config: {
          tools: [
            { googleSearch: {} },
            { urlContext: {} }
          ],
          responseMimeType: "application/json",
          responseJsonSchema: zodToJsonSchema(matchSchema),
        },
      });

      const match = matchSchema.parse(JSON.parse(response.text));
      console.log(match);
    }

    run();

### REST

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-preview:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -X POST \
      -d '{
        "contents": [{
          "parts": [{"text": "Search for all details for the latest Euro."}]
        }],
        "tools": [
          {"googleSearch": {}},
          {"urlContext": {}}
        ],
        "generationConfig": {
            "responseMimeType": "application/json",
            "responseJsonSchema": {
                "type": "object",
                "properties": {
                    "winner": {"type": "string", "description": "The name of the winner."},
                    "final_match_score": {"type": "string", "description": "The final score."},
                    "scorers": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The name of the scorer."
                    }
                },
                "required": ["winner", "final_match_score", "scorers"]
            }
        }
      }'

## JSON schema support

To generate a JSON object, set the`response_mime_type`in the generation configuration to`application/json`and provide a`response_json_schema`. The schema must be a valid[JSON Schema](https://json-schema.org/)that describes the desired output format.

The model will then generate a response that is a syntactically valid JSON string matching the provided schema. When using structured outputs, the model will produce outputs in the same order as the keys in the schema.

Gemini's structured output mode supports a subset of the[JSON Schema](https://json-schema.org)specification.

The following values of`type`are supported:

- **`string`**: For text.
- **`number`**: For floating-point numbers.
- **`integer`**: For whole numbers.
- **`boolean`**: For true/false values.
- **`object`**: For structured data with key-value pairs.
- **`array`**: For lists of items.
- **`null`** : To allow a property to be null, include`"null"`in the type array (e.g.,`{"type": ["string", "null"]}`).

These descriptive properties help guide the model:

- **`title`**: A short description of a property.
- **`description`**: A longer and more detailed description of a property.

### Type-specific properties

**For`object`values:**

- **`properties`**: An object where each key is a property name and each value is a schema for that property.
- **`required`**: An array of strings, listing which properties are mandatory.
- **`additionalProperties`** : Controls whether properties not listed in`properties`are allowed. Can be a boolean or a schema.

**For`string`values:**

- **`enum`**: Lists a specific set of possible strings for classification tasks.
- **`format`** : Specifies a syntax for the string, such as`date-time`,`date`,`time`.

**For`number`and`integer`values:**

- **`enum`**: Lists a specific set of possible numeric values.
- **`minimum`**: The minimum inclusive value.
- **`maximum`**: The maximum inclusive value.

**For`array`values:**

- **`items`**: Defines the schema for all items in the array.
- **`prefixItems`**: Defines a list of schemas for the first N items, allowing for tuple-like structures.
- **`minItems`**: The minimum number of items in the array.
- **`maxItems`**: The maximum number of items in the array.

## Model support

The following models support structured output:

|         Model         | Structured Outputs |
|-----------------------|--------------------|
| Gemini 3 Pro Preview  | ✔️                 |
| Gemini 2.5 Pro        | ✔️                 |
| Gemini 2.5 Flash      | ✔️                 |
| Gemini 2.5 Flash-Lite | ✔️                 |
| Gemini 2.0 Flash      | ✔️\*               |
| Gemini 2.0 Flash-Lite | ✔️\*               |

*\* Note that Gemini 2.0 requires an explicit`propertyOrdering`list within the JSON input to define the preferred structure. You can find an example in this[cookbook](https://github.com/google-gemini/cookbook/blob/main/examples/Pdf_structured_outputs_on_invoices_and_forms.ipynbs).*

## Structured outputs vs. function calling

Both structured outputs and function calling use JSON schemas, but they serve different purposes:

|        Feature         |                                                                                  Primary Use Case                                                                                  |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Structured Outputs** | **Formatting the final response to the user.** Use this when you want the model's*answer*to be in a specific format (e.g., extracting data from a document to save to a database). |
| **Function Calling**   | **Taking action during the conversation.** Use this when the model needs to*ask you*to perform a task (e.g., "get current weather") before it can provide a final answer.          |

## Best practices

- **Clear descriptions:** Use the`description`field in your schema to provide clear instructions to the model about what each property represents. This is crucial for guiding the model's output.
- **Strong typing:** Use specific types (`integer`,`string`,`enum`) whenever possible. If a parameter has a limited set of valid values, use an`enum`.
- **Prompt engineering:**Clearly state in your prompt what you want the model to do. For example, "Extract the following information from the text..." or "Classify this feedback according to the provided schema...".
- **Validation:**While structured output guarantees syntactically correct JSON, it does not guarantee the values are semantically correct. Always validate the final output in your application code before using it.
- **Error handling:**Implement robust error handling in your application to gracefully manage cases where the model's output, while schema-compliant, may not meet your business logic requirements.

## Limitations

- **Schema subset:**Not all features of the JSON Schema specification are supported. The model ignores unsupported properties.
- **Schema complexity:**The API may reject very large or deeply nested schemas. If you encounter errors, try simplifying your schema by shortening property names, reducing nesting, or limiting the number of constraints.
<br />

Tools extend the capabilities of Gemini models, enabling them to take action in the world, access real-time information, and perform complex computational tasks. Models can use tools in both standard request-response interactions and real-time streaming sessions via the[Live API](https://ai.google.dev/gemini-api/docs/live-tools).

The Gemini API provides a suite of fully managed, built-in tools optimized for Gemini models or you can define custom tools using[Function Calling](https://ai.google.dev/gemini-api/docs/function-calling).

## Available built-in tools

|                                     Tool                                     |                                                  Description                                                  |                                                   Use Cases                                                   |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [Google Search](https://ai.google.dev/gemini-api/docs/google-search)         | Ground responses in current events and facts from the web to reduce hallucinations.                           | - Answering questions about recent events - Verifying facts with diverse sources                              |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding)          | Build location-aware assistants that can find places, get directions, and provide rich local context.         | - Planning travel itineraries with multiple stops - Finding local businesses based on user criteria           |
| [Code Execution](https://ai.google.dev/gemini-api/docs/code-execution)       | Allow the model to write and run Python code to solve math problems or process data accurately.               | - Solving complex mathematical equations - Processing and analyzing text data precisely                       |
| [URL Context](https://ai.google.dev/gemini-api/docs/url-context)             | Direct the model to read and analyze content from specific web pages or documents.                            | - Answering questions based on specific URLs or documents - Retrieving information across different web pages |
| [Computer Use (Preview)](https://ai.google.dev/gemini-api/docs/computer-use) | Enable Gemini to view a screen and generate actions to interact with web browser UIs (Client-side execution). | - Automating repetitive web-based workflows - Testing web application user interfaces                         |
| [File Search](https://ai.google.dev/gemini-api/docs/file-search)             | Index and search your own documents to enable Retrieval Augmented Generation (RAG).                           | - Searching technical manuals - Question answering over proprietary data                                      |

See the[Pricing page](https://ai.google.dev/gemini-api/docs/pricing#pricing_for_tools)for details on costs associated with specific tools.

## How tools execution works

Tools allow the model to request actions during a conversation. The flow differs depending on whether the tool is built-in (managed by Google) or custom (managed by you).

### Built-in tool flow

For built-in tools like Google Search or Code Execution, the entire process happens within one API call:

1. **You**send a prompt: "What is the square root of the latest stock price of GOOG?"
2. **Gemini**decides it needs tools and executes them on Google's servers (e.g., searches for the stock price, then runs Python code to calculate the square root).
3. **Gemini**sends back the final answer grounded in the tool results.

### Custom tool flow (Function Calling)

For custom tools and Computer Use, your application handles the execution:

1. **You**send a prompt along with functions (tools) declarations.
2. **Gemini** might send back a structured JSON to call a specific function (for example,`{"name": "get_order_status", "args": {"order_id": "123"}}`).
3. **You**execute the function in your application or environment.
4. **You**send the function results back to Gemini.
5. **Gemini**uses the results to generate a final response or another tool call.

Learn more in the[Function calling guide](https://ai.google.dev/gemini-api/docs/function-calling).

## Structured outputs vs. function Calling

Gemini offers two methods for generating structured outputs. Use[Function calling](https://ai.google.dev/gemini-api/docs/function-calling)when the model needs to perform an intermediate step by connecting to your own tools or data systems. Use[Structured Outputs](https://ai.google.dev/gemini-api/docs/structured-output)when you strictly need the model's final response to adhere to a specific schema, such as for rendering a custom UI.

## Structured outputs with tools

| **Preview:** This is a feature available only with the`gemini-3-pro-preview`model.

You can combine[Structured Outputs](https://ai.google.dev/gemini-api/docs/structured-output)with built-in tools to ensure that model responses grounded in external data or computation still adhere to a strict schema.

See[Structured outputs with tools](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe#structured_outputs_with_tools)for code examples.

## Building agents

Agents are systems that use models and tools to complete multi-step tasks. While Gemini provides the reasoning capabilities (the "brain") and the essential tools (the "hands"), you often need an orchestration framework to manage the agent's memory, plan loops, and perform complex tool chaining.

Gemini integrates with leading open-source agent frameworks:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example): Build stateful, complex application flows and multi-agent systems using graph structures.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index): Connect Gemini agents to your private data for RAG-enhanced workflows.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example): Orchestrate collaborative, role-playing autonomous AI agents.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example): Build AI-powered user interfaces and agents in JavaScript/TypeScript.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): An open-source framework for building and orchestrating interoperable AI agents.

LangGraph is a framework for building stateful LLM applications, making it a good choice for constructing ReAct (Reasoning and Acting) Agents.

ReAct agents combine LLM reasoning with action execution. They iteratively think, use tools, and act on observations to achieve user goals, dynamically adapting their approach. Introduced in ["ReAct: Synergizing Reasoning and Acting in Language Models"](https://arxiv.org/abs/2210.03629) (2023), this pattern tries to mirror human-like, flexible problem-solving over rigid workflows.

While LangGraph offers a prebuilt ReAct agent ([`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)), it shines when you need more control and customization for your ReAct implementations.

LangGraph models agents as graphs using three key components:

- `State`: Shared data structure (typically `TypedDict` or `Pydantic BaseModel`) representing the application's current snapshot.
- `Nodes`: Encodes logic of your agents. They receive the current State as input, perform some computation or side-effect, and return an updated State, such as LLM calls or tool calls.
- `Edges`: Define the next `Node` to execute based on the current `State`, allowing for conditional logic and fixed transitions.

If you don't have an API Key yet, you can get one for free at the [Google AI Studio](https://aistudio.google.com/app/apikey).  

    pip install langgraph langchain-google-genai geopy requests

Set your API key in the environment variable `GEMINI_API_KEY`.  

    import os

    # Read your API key from the environment variable or set it manually
    api_key = os.getenv("GEMINI_API_KEY")

To better understand how to implement a ReAct agent using LangGraph, let's walk through a practical example. You will create a simple agent whose goal is to use a tool to find the current weather for a specified location.

For this weather agent, its `State` will need to maintain the ongoing conversation history (as a list of messages) and a counter for the number of steps taken to further illustrate state management.

LangGraph provides a convenient helper, `add_messages`, for updating message lists in the state. It functions as a [reducer](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers), meaning it takes the current list and new messages, then returns a combined list. It smartly handles updates by message ID and defaults to an "append-only" behavior for new, unique messages.
**Note:** Since having a list of messages in the state is so common, there exists a prebuilt state called `MessagesState` which makes it easy to use messages.  

    from typing import Annotated,Sequence, TypedDict

    from langchain_core.messages import BaseMessage
    from langgraph.graph.message import add_messages # helper function to add messages to the state


    class AgentState(TypedDict):
        """The state of the agent."""
        messages: Annotated[Sequence[BaseMessage], add_messages]
        number_of_steps: int

Next, you define your weather tool.  

    from langchain_core.tools import tool
    from geopy.geocoders import Nominatim
    from pydantic import BaseModel, Field
    import requests

    geolocator = Nominatim(user_agent="weather-app")

    class SearchInput(BaseModel):
        location:str = Field(description="The city and state, e.g., San Francisco")
        date:str = Field(description="the forecasting date for when to get the weather format (yyyy-mm-dd)")

    @tool("get_weather_forecast", args_schema=SearchInput, return_direct=True)
    def get_weather_forecast(location: str, date: str):
        """Retrieves the weather using Open-Meteo API for a given location (city) and a date (yyyy-mm-dd). Returns a list dictionary with the time and temperature for each hour."""
        location = geolocator.geocode(location)
        if location:
            try:
                response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m&start_date={date}&end_date={date}")
                data = response.json()
                return {time: temp for time, temp in zip(data["hourly"]["time"], data["hourly"]["temperature_2m"])}
            except Exception as e:
                return {"error": str(e)}
        else:
            return {"error": "Location not found"}

    tools = [get_weather_forecast]

Next, you initialize your model and bind the tools to the model.  

    from datetime import datetime
    from langchain_google_genai import ChatGoogleGenerativeAI

    # Create LLM class
    llm = ChatGoogleGenerativeAI(
        model= "gemini-2.5-pro",
        temperature=1.0,
        max_retries=2,
        google_api_key=api_key,
    )

    # Bind tools to the model
    model = llm.bind_tools([get_weather_forecast])

    # Test the model with tools
    res=model.invoke(f"What is the weather in Berlin on {datetime.today()}?")

    print(res)

The last step before you can run your agent is to define your nodes and edges. In this example, you have two nodes and one edge.
- `call_tool` node that executes your tool method. LangGraph has a prebuilt node for this called [ToolNode](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/).
- `call_model` node that uses the `model_with_tools` to call the model.
- `should_continue` edge that decides whether to call the tool or the model.

The number of nodes and edges is not fixed. You can add as many nodes and edges as you want to your graph. For example, you could add a node for adding structured output or a self-verification/reflection node to check the model output before calling the tool or the model.  

    from langchain_core.messages import ToolMessage
    from langchain_core.runnables import RunnableConfig

    tools_by_name = {tool.name: tool for tool in tools}

    # Define our tool node
    def call_tool(state: AgentState):
        outputs = []
        # Iterate over the tool calls in the last message
        for tool_call in state["messages"][-1].tool_calls:
            # Get the tool by name
            tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
            outputs.append(
                ToolMessage(
                    content=tool_result,
                    name=tool_call["name"],
                    tool_call_id=tool_call["id"],
                )
            )
        return {"messages": outputs}

    def call_model(
        state: AgentState,
        config: RunnableConfig,
    ):
        # Invoke the model with the system prompt and the messages
        response = model.invoke(state["messages"], config)
        # We return a list, because this will get added to the existing messages state using the add_messages reducer
        return {"messages": [response]}


    # Define the conditional edge that determines whether to continue or not
    def should_continue(state: AgentState):
        messages = state["messages"]
        # If the last message is not a tool call, then we finish
        if not messages[-1].tool_calls:
            return "end"
        # default to continue
        return "continue"

Now you have all the components to build your agent. Let's put them together.  

    from langgraph.graph import StateGraph, END

    # Define a new graph with our state
    workflow = StateGraph(AgentState)

    # 1. Add our nodes 
    workflow.add_node("llm", call_model)
    workflow.add_node("tools",  call_tool)
    # 2. Set the entrypoint as `agent`, this is the first node called
    workflow.set_entry_point("llm")
    # 3. Add a conditional edge after the `llm` node is called.
    workflow.add_conditional_edges(
        # Edge is used after the `llm` node is called.
        "llm",
        # The function that will determine which node is called next.
        should_continue,
        # Mapping for where to go next, keys are strings from the function return, and the values are other nodes.
        # END is a special node marking that the graph is finish.
        {
            # If `tools`, then we call the tool node.
            "continue": "tools",
            # Otherwise we finish.
            "end": END,
        },
    )
    # 4. Add a normal edge after `tools` is called, `llm` node is called next.
    workflow.add_edge("tools", "llm")

    # Now we can compile and visualize our graph
    graph = workflow.compile()

You can visualize your graph using the `draw_mermaid_png` method.  

    from IPython.display import Image, display

    display(Image(graph.get_graph().draw_mermaid_png()))

![png](https://ai.google.dev/static/gemini-api/docs/images/langgraph-react-agent_16_0.png)

Now let's run the agent.  

    from datetime import datetime
    # Create our initial message dictionary
    inputs = {"messages": [("user", f"What is the weather in Berlin on {datetime.today()}?")]}

    # call our graph with streaming to see the steps
    for state in graph.stream(inputs, stream_mode="values"):
        last_message = state["messages"][-1]
        last_message.pretty_print()

You can now continue with your conversation and for example ask for the weather in another city or let it compare it.  

    state["messages"].append(("user", "Would it be in Munich warmer?"))

    for state in graph.stream(state, stream_mode="values"):
        last_message = state["messages"][-1]
        last_message.pretty_print()
<br />

Grounding with Google Search connects the Gemini model to real-time web content and works with all available languages. This allows Gemini to provide more accurate answers and cite verifiable sources beyond its knowledge cutoff.

Grounding helps you build applications that can:

- **Increase factual accuracy:**Reduce model hallucinations by basing responses on real-world information.
- **Access real-time information:**Answer questions about recent events and topics.
- **Provide citations:**Build user trust by showing the sources for the model's claims.

### Python

    from google import genai
    from google.genai import types

    client = genai.Client()

    grounding_tool = types.Tool(
        google_search=types.GoogleSearch()
    )

    config = types.GenerateContentConfig(
        tools=[grounding_tool]
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Who won the euro 2024?",
        config=config,
    )

    print(response.text)

### JavaScript

    import { GoogleGenAI } from "@google/genai";

    const ai = new GoogleGenAI({});

    const groundingTool = {
      googleSearch: {},
    };

    const config = {
      tools: [groundingTool],
    };

    const response = await ai.models.generateContent({
      model: "gemini-2.5-flash",
      contents: "Who won the euro 2024?",
      config,
    });

    console.log(response.text);

### REST

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H "Content-Type: application/json" \
      -X POST \
      -d '{
        "contents": [
          {
            "parts": [
              {"text": "Who won the euro 2024?"}
            ]
          }
        ],
        "tools": [
          {
            "google_search": {}
          }
        ]
      }'

You can learn more by trying the[Search tool notebook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb).

## How grounding with Google Search works

When you enable the`google_search`tool, the model handles the entire workflow of searching, processing, and citing information automatically.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png)

1. **User Prompt:** Your application sends a user's prompt to the Gemini API with the`google_search`tool enabled.
2. **Prompt Analysis:**The model analyzes the prompt and determines if a Google Search can improve the answer.
3. **Google Search:**If needed, the model automatically generates one or multiple search queries and executes them.
4. **Search Results Processing:**The model processes the search results, synthesizes the information, and formulates a response.
5. **Grounded Response:** The API returns a final, user-friendly response that is grounded in the search results. This response includes the model's text answer and`groundingMetadata`with the search queries, web results, and citations.

## Understanding the grounding response

When a response is successfully grounded, the response includes a`groundingMetadata`field. This structured data is essential for verifying claims and building a rich citation experience in your application.  

    {
      "candidates": [
        {
          "content": {
            "parts": [
              {
                "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
              }
            ],
            "role": "model"
          },
          "groundingMetadata": {
            "webSearchQueries": [
              "UEFA Euro 2024 winner",
              "who won euro 2024"
            ],
            "searchEntryPoint": {
              "renderedContent": "<!-- HTML and CSS for the search widget -->"
            },
            "groundingChunks": [
              {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
              {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
            ],
            "groundingSupports": [
              {
                "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
                "groundingChunkIndices": [0]
              },
              {
                "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
                "groundingChunkIndices": [0, 1]
              }
            ]
          }
        }
      ]
    }

The Gemini API returns the following information with the`groundingMetadata`:

- `webSearchQueries`: Array of the search queries used. This is useful for debugging and understanding the model's reasoning process.
- `searchEntryPoint`: Contains the HTML and CSS to render the required Search Suggestions. Full usage requirements are detailed in the[Terms of Service](https://ai.google.dev/gemini-api/terms#grounding-with-google-search).
- `groundingChunks`: Array of objects containing the web sources (`uri`and`title`).
- `groundingSupports`: Array of chunks to connect model response`text`to the sources in`groundingChunks`. Each chunk links a text`segment`(defined by`startIndex`and`endIndex`) to one or more`groundingChunkIndices`. This is the key to building inline citations.

Grounding with Google Search can also be used in combination with the[URL context tool](https://ai.google.dev/gemini-api/docs/url-context)to ground responses in both public web data and the specific URLs you provide.

## Attributing sources with inline citations

The API returns structured citation data, giving you complete control over how you display sources in your user interface. You can use the`groundingSupports`and`groundingChunks`fields to link the model's statements directly to their sources. Here is a common pattern for processing the metadata to create a response with inline, clickable citations.  

### Python

    def add_citations(response):
        text = response.text
        supports = response.candidates[0].grounding_metadata.grounding_supports
        chunks = response.candidates[0].grounding_metadata.grounding_chunks

        # Sort supports by end_index in descending order to avoid shifting issues when inserting.
        sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

        for support in sorted_supports:
            end_index = support.segment.end_index
            if support.grounding_chunk_indices:
                # Create citation string like [1](link1)[2](link2)
                citation_links = []
                for i in support.grounding_chunk_indices:
                    if i < len(chunks):
                        uri = chunks[i].web.uri
                        citation_links.append(f"[{i + 1}]({uri})")

                citation_string = ", ".join(citation_links)
                text = text[:end_index] + citation_string + text[end_index:]

        return text

    # Assuming response with grounding metadata
    text_with_citations = add_citations(response)
    print(text_with_citations)

### JavaScript

    function addCitations(response) {
        let text = response.text;
        const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
        const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

        // Sort supports by end_index in descending order to avoid shifting issues when inserting.
        const sortedSupports = [...supports].sort(
            (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
        );

        for (const support of sortedSupports) {
            const endIndex = support.segment?.endIndex;
            if (endIndex === undefined || !support.groundingChunkIndices?.length) {
            continue;
            }

            const citationLinks = support.groundingChunkIndices
            .map(i => {
                const uri = chunks[i]?.web?.uri;
                if (uri) {
                return `[${i + 1}](${uri})`;
                }
                return null;
            })
            .filter(Boolean);

            if (citationLinks.length > 0) {
            const citationString = citationLinks.join(", ");
            text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
            }
        }

        return text;
    }

    const textWithCitations = addCitations(response);
    console.log(textWithCitations);

The new response with inline citations will look like this:  

    Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)

## Pricing

When you use Grounding with Google Search, your project is billed for each search query that the model decides to execute. If the model decides to execute multiple search queries to answer a single prompt (for example, searching for`"UEFA Euro 2024 winner"`and`"Spain vs England Euro 2024 final score"`within the same API call), this counts as two billable uses of the tool for that request.

For detailed pricing information, see the[Gemini API pricing page](https://ai.google.dev/gemini-api/docs/pricing).

## Supported models

Experimental and Preview models are not included. You can find their capabilities on the[model overview](https://ai.google.dev/gemini-api/docs/models)page.

|         Model         | Grounding with Google Search |
|-----------------------|------------------------------|
| Gemini 2.5 Pro        | ✔️                           |
| Gemini 2.5 Flash      | ✔️                           |
| Gemini 2.5 Flash-Lite | ✔️                           |
| Gemini 2.0 Flash      | ✔️                           |
| Gemini 1.5 Pro        | ✔️                           |
| Gemini 1.5 Flash      | ✔️                           |

| **Note:** Older models use a`google_search_retrieval`tool. For all current models, use the`google_search`tool as shown in the examples.

## Supported tools combinations

You can use Grounding with Google Search with other tools like[code execution](https://ai.google.dev/gemini-api/docs/code-execution)and[URL context](https://ai.google.dev/gemini-api/docs/url-context)to power more complex use cases.

## Grounding with Gemini 1.5 Models (Legacy)

While the`google_search`tool is recommended for Gemini 2.0 and later, Gemini 1.5 supports a legacy tool named`google_search_retrieval`. This tool provides a`dynamic`mode that allows the model to decide whether to perform a search based on its confidence that the prompt requires fresh information. If the model's confidence is above a`dynamic_threshold`you set (a value between 0.0 and 1.0), it will perform a search.  

### Python

    # Note: This is a legacy approach for Gemini 1.5 models.
    # The 'google_search' tool is recommended for all new development.
    import os
    from google import genai
    from google.genai import types

    client = genai.Client()

    retrieval_tool = types.Tool(
        google_search_retrieval=types.GoogleSearchRetrieval(
            dynamic_retrieval_config=types.DynamicRetrievalConfig(
                mode=types.DynamicRetrievalConfigMode.MODE_DYNAMIC,
                dynamic_threshold=0.7 # Only search if confidence > 70%
            )
        )
    )

    config = types.GenerateContentConfig(
        tools=[retrieval_tool]
    )

    response = client.models.generate_content(
        model='gemini-1.5-flash',
        contents="Who won the euro 2024?",
        config=config,
    )
    print(response.text)
    if not response.candidates[0].grounding_metadata:
      print("\nModel answered from its own knowledge.")

### JavaScript

    // Note: This is a legacy approach for Gemini 1.5 models.
    // The 'googleSearch' tool is recommended for all new development.
    import { GoogleGenAI, DynamicRetrievalConfigMode } from "@google/genai";

    const ai = new GoogleGenAI({});

    const retrievalTool = {
      googleSearchRetrieval: {
        dynamicRetrievalConfig: {
          mode: DynamicRetrievalConfigMode.MODE_DYNAMIC,
          dynamicThreshold: 0.7, // Only search if confidence > 70%
        },
      },
    };

    const config = {
      tools: [retrievalTool],
    };

    const response = await ai.models.generateContent({
      model: "gemini-1.5-flash",
      contents: "Who won the euro 2024?",
      config,
    });

    console.log(response.text);
    if (!response.candidates?.[0]?.groundingMetadata) {
      console.log("\nModel answered from its own knowledge.");
    }

### REST

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \

      -H "Content-Type: application/json" \
      -X POST \
      -d '{
        "contents": [
          {"parts": [{"text": "Who won the euro 2024?"}]}
        ],
        "tools": [{
          "google_search_retrieval": {
            "dynamic_retrieval_config": {
              "mode": "MODE_DYNAMIC",
              "dynamic_threshold": 0.7
            }
          }
        }]
      }'

## What's next

- Try the[Grounding with Google Search in the Gemini API Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb).
- Learn about other available tools, like[Function Calling](https://ai.google.dev/gemini-api/docs/function-calling).
- Learn how to augment prompts with specific URLs using the[URL context tool](https://ai.google.dev/gemini-api/docs/url-context).
The URL context tool lets you provide additional context to the models in the
form of URLs. By including URLs in your request, the model will access
the content from those pages (as long as it's not a URL type listed in the
[limitations section](https://ai.google.dev/gemini-api/docs/url-context#limitations)) to inform
and enhance its response.

The URL context tool is useful for tasks like the following:

- **Extract Data**: Pull specific info like prices, names, or key findings from multiple URLs.
- **Compare Documents**: Analyze multiple reports, articles, or PDFs to identify differences and track trends.
- **Synthesize \& Create Content**: Combine information from several source URLs to generate accurate summaries, blog posts, or reports.
- **Analyze Code \& Docs**: Point to a GitHub repository or technical documentation to explain code, generate setup instructions, or answer questions.

The following example shows how to compare two recipes from different websites.  

### Python

    from google import genai
    from google.genai.types import Tool, GenerateContentConfig

    client = genai.Client()
    model_id = "gemini-2.5-flash"

    tools = [
      {"url_context": {}},
    ]

    url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
    url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

    response = client.models.generate_content(
        model=model_id,
        contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
        config=GenerateContentConfig(
            tools=tools,
        )
    )

    for each in response.candidates[0].content.parts:
        print(each.text)

    # For verification, you can inspect the metadata to see which URLs the model retrieved
    print(response.candidates[0].url_context_metadata)

### Javascript

    import { GoogleGenAI } from "@google/genai";

    const ai = new GoogleGenAI({});

    async function main() {
      const response = await ai.models.generateContent({
        model: "gemini-2.5-flash",
        contents: [
            "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
        ],
        config: {
          tools: [{urlContext: {}}],
        },
      });
      console.log(response.text);

      // For verification, you can inspect the metadata to see which URLs the model retrieved
      console.log(response.candidates[0].urlContextMetadata)
    }

    await main();

### REST

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
          "contents": [
              {
                  "parts": [
                      {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
                  ]
              }
          ],
          "tools": [
              {
                  "url_context": {}
              }
          ]
      }' > result.json

    cat result.json

## How it works

The URL Context tool uses a two-step retrieval process to
balance speed, cost, and access to fresh data. When you provide a URL, the tool
first attempts to fetch the content from an internal index cache. This acts as a
highly optimized cache. If a URL is not available in the index (for example, if
it's a very new page), the tool automatically falls back to do a live fetch.
This directly accesses the URL to retrieve its content in real-time.

## Combining with other tools

You can combine the URL context tool with other tools to create more powerful
workflows.

### Grounding with search

When both URL context and
[Grounding with Google Search](https://ai.google.dev/gemini-api/docs/grounding) are enabled,
the model can use its search capabilities to find
relevant information online and then use the URL context tool to get a more
in-depth understanding of the pages it finds. This approach is powerful for
prompts that require both broad searching and deep analysis of specific pages.  

### Python

    from google import genai
    from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

    client = genai.Client()
    model_id = "gemini-2.5-flash"

    tools = [
          {"url_context": {}},
          {"google_search": {}}
      ]

    response = client.models.generate_content(
        model=model_id,
        contents="Give me three day events schedule based on <var translate="no">YOUR_URL</var>. Also let me know what needs to taken care of considering weather and commute.",
        config=GenerateContentConfig(
            tools=tools,
        )
    )

    for each in response.candidates[0].content.parts:
        print(each.text)
    # get URLs retrieved for context
    print(response.candidates[0].url_context_metadata)

### Javascript

    import { GoogleGenAI } from "@google/genai";

    const ai = new GoogleGenAI({});

    async function main() {
      const response = await ai.models.generateContent({
        model: "gemini-2.5-flash",
        contents: [
            "Give me three day events schedule based on <var translate="no">YOUR_URL</var>. Also let me know what needs to taken care of considering weather and commute.",
        ],
        config: {
          tools: [
            {urlContext: {}},
            {googleSearch: {}}
            ],
        },
      });
      console.log(response.text);
      // To get URLs retrieved for context
      console.log(response.candidates[0].urlContextMetadata)
    }

    await main();

### REST

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
          "contents": [
              {
                  "parts": [
                      {"text": "Give me three day events schedule based on <var translate="no">YOUR_URL</var>. Also let me know what needs to taken care of considering weather and commute."}
                  ]
              }
          ],
          "tools": [
              {
                  "url_context": {}
              },
              {
                  "google_search": {}
              }
          ]
      }' > result.json

    cat result.json

## Understanding the response

When the model uses the URL context tool, the response includes a
`url_context_metadata` object. This object lists the URLs the model retrieved
content from and the status of each retrieval attempt, which is useful for
verification and debugging.

The following is an example of that part of the response
(parts of the response have been omitted for brevity):  

    {
      "candidates": [
        {
          "content": {
            "parts": [
              {
                "text": "... \n"
              }
            ],
            "role": "model"
          },
          ...
          "url_context_metadata": {
            "url_metadata": [
              {
                "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
                "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
              },
              {
                "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
                "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
              }
            ]
          }
        }
    }

For complete detail about this object , see the
[`UrlContextMetadata` API reference](https://ai.google.dev/api/generate-content#UrlContextMetadata).

### Safety checks

The system performs a content moderation check on the URL to confirm
they meet safety standards. If the URL you provided fails this check, you will
get an `url_retrieval_status` of `URL_RETRIEVAL_STATUS_UNSAFE`.

### Token count

The content retrieved from the URLs you specify in your prompt is counted
as part of the input tokens. You can see the token count for your prompt and
tools usage in the [`usage_metadata`](https://ai.google.dev/api/generate-content#UsageMetadata)
object of the model output. The following is an example output:  

    'usage_metadata': {
      'candidates_token_count': 45,
      'prompt_token_count': 27,
      'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
        'token_count': 27}],
      'thoughts_token_count': 31,
      'tool_use_prompt_token_count': 10309,
      'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
        'token_count': 10309}],
      'total_token_count': 10412
      }

Price per token depends on the model used, see the
[pricing](https://ai.google.dev/gemini-api/docs/pricing) page for details.

## Supported models

- [gemini-2.5-pro](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-pro)
- [gemini-2.5-flash](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash)
- [gemini-2.5-flash-lite](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash-lite)
- [gemini-live-2.5-flash-preview](https://ai.google.dev/gemini-api/docs/models#live-api)
- [gemini-2.0-flash-live-001](https://ai.google.dev/gemini-api/docs/models#live-api-2.0)

## Best Practices

- **Provide specific URLs**: For the best results, provide direct URLs to the content you want the model to analyze. The model will only retrieve content from the URLs you provide, not any content from nested links.
- **Check for accessibility**: Verify that the URLs you provide don't lead to pages that require a login or are behind a paywall.
- **Use the complete URL**: Provide the full URL, including the protocol (e.g., https://www.google.com instead of just google.com).

## Limitations

- **Pricing** : Content retrieved from URLs counts as input tokens. Rate limit and pricing is the based on the model used. See the [rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) and [pricing](https://ai.google.dev/gemini-api/docs/pricing) pages for details.
- **Request limit**: The tool can process up to 20 URLs per request.
- **URL content size**: The maximum size for content retrieved from a single URL is 34MB.

### Supported and unsupported content types

The tool can extract content from URLs with the following content types:

- Text (text/html, application/json, text/plain, text/xml, text/css, text/javascript , text/csv, text/rtf)
- Image (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

The following content types are **not** supported:

- Paywalled content
- YouTube videos (See [video understanding](https://ai.google.dev/gemini-api/docs/video-understanding#youtube) to learn how to process YouTube URLs)
- Google workspace files like Google docs or spreadsheets
- Video and audio files

## What's next

- Explore the [URL context cookbook](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb#url-context) for more examples.

<br />

*Prompt design*is the process of creating prompts, or natural language requests, that elicit accurate, high quality responses from a language model.

This page introduces basic concepts, strategies, and best practices to get you started designing prompts to get the most out of Gemini AI models.
| **Note:** Prompt engineering is iterative. These guidelines and templates are starting points. Experiment and refine based on your specific use cases and observed model responses.

## Topic-specific prompt guides

Looking for more specific prompt strategies? Check out our other prompting guides on:

- [Prompting with media files](https://ai.google.dev/gemini-api/docs/files#prompt-guide)
- Prompting for image generation with[Imagen](https://ai.google.dev/gemini-api/docs/imagen#imagen-prompt-guide)and[Gemini Native Image Generation](https://ai.google.dev/gemini-api/docs/image-generation#prompt-guide)
- [Prompting for video generation](https://ai.google.dev/gemini-api/docs/video#prompt-guide)

You can find other sample prompts in the[prompt gallery](https://ai.google.dev/gemini-api/prompts)meant to interactively showcase many of the concepts shared in this guide.

## Clear and specific instructions

An effective and efficient way to customize model behavior is to provide it with clear and specific instructions. Instructions can be in the form of a question, step-by-step tasks, or as complex as mapping out a user's experience and mindset.

### Input

Input is the required text in the prompt that you want the model to provide a response to. Inputs can be a question that the model answers (question input), a task the model performs (task input), an entity the model operates on (entity input), or partial input that the model completes or continues (completion input).

| **Input type** |                                                                 **Prompt**                                                                  |                                                                                                                                        **Generated output**                                                                                                                                        |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Question       | What's a good name for a flower shop that specializes in selling bouquets of dried flowers? Create a list of 5 options with just the names. | Here are 10 names for a flower shop specializing in dried flowers: 1. Everlasting Blooms 2. Dried & Delightful 3. The Petal Preserve 4. Whispers of Wildflowers 5. Forever Blooms                                                                                                                  |
| Task           | ``` Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ```                         | ``` 1. **Tent:** Your shelter from the elements. 2. **Sleeping Bag:** Stay warm and comfortable. 3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep. 4. **Headlamp or Flashlight:** Light for nighttime activities. 5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| Entity         | Classify the following items as [large, small]: Elephant Mouse Snail                                                                        | Here's the classification: * **Elephant:** Large * **Mouse:** Small * **Snail:** Small                                                                                                                                                                                                             |

#### Partial input completion

Generative language models work like an advanced auto completion tool. When you provide partial content, the model can provide the rest of the content or what it thinks is a continuation of that content as a response. When doing so, if you include any examples or context, the model can take those examples or context into account.

The following example provides a prompt with an instruction and an entity input:

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Prompt:** ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity. Order: A burger and a drink. ``` **Response:** ``` { "cheeseburger": 0, "hamburger": 1, "fries": 0, "drink": 1 } ``` (gemini-2.5-flash) |

While the model did as prompted, writing out the instructions in natural language can sometimes be challenging and it leaves a lot to the model's interpretation. For example, a restaurants menu might contain many items. To reduce the size of the JSON response, you probably want to omit the items that weren't ordered. In this case, you can give an example and a[response prefix](https://ai.google.dev/gemini-api/docs/prompting-strategies#prefixes)and let the model complete it:

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Prompt:** ```` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` { "cheeseburger": 1, "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```` **Response:** ```` ``` { "hamburger": 2, "drink": 1, "fries": 1 } ``` ```` (gemini-2.5-flash) |

Notice how "cheeseburger" was excluded from the output because it wasn't a part of the order.

### Constraints

Specify any constraints on reading the prompt or generating a response. You can tell the model what to do and not to do. For example, you can specify a constraint in the prompt on how long you want a summary to be:

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Prompt:** ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ``` <br /> **Response:** ``` Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ``` (gemini-2.5-flash) <br /> |

### Response format

You can give instructions that specify the format of the response. For example, you can ask for the response to be formatted as a table, bulleted list, elevator pitch, keywords, sentence, or paragraph. The following system instruction tells the model to be more conversational in its response:

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **System instruction** ``` All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ``` **Prompt** ``` What is a smart way to make a business that sells DVD's in 2025? ``` **Response:** ``` Starting a business selling DVDs in 2025 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption. Here's a breakdown of what a smart DVD business in 2025 would likely entail: 1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include: * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms. .... ``` (gemini-2.5-flash) |

#### Format responses with the completion strategy

The[completion strategy](https://ai.google.dev/gemini-api/docs/prompting-strategies#completion)can also help format the response. The following example prompts the model to create an essay outline:

|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Prompt:** ``` Create an outline for an essay about hummingbirds. ``` **Response:** ``` Here is a possible outline for an essay about hummingbirds: I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds. II. Appearance and Identification ..... ``` (gemini-2.5-flash) |

The prompt didn't specify the format for the outline and the model chose a format for you. To get the model to return an outline in a specific format, you can add text that represents the start of the outline and let the model complete it based on the pattern that you initiated.

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Prompt:** ``` Create an outline for an essay about hummingbirds. I. Introduction * ``` **Response:** ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided: I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ``` (gemini-2.5-flash) |

## Zero-shot vs few-shot prompts

You can include examples in the prompt that show the model what getting it right looks like. The model attempts to identify patterns and relationships from the examples and applies them when generating a response. Prompts that contain a few examples are called*few-shot* prompts, while prompts that provide no examples are called*zero-shot*prompts. Few-shot prompts are often used to regulate the formatting, phrasing, scoping, or general patterning of model responses. Use specific and varied examples to help the model narrow its focus and generate more accurate results.

We recommend to always include few-shot examples in your prompts. Prompts without few-shot examples are likely to be less effective. In fact, you can remove instructions from your prompt if your examples are clear enough in showing the task at hand.

The following zero-shot prompt asks the model to choose the best explanation.

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Prompt:** ``` Please choose the best explanation to the question: Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ``` **Response:** ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ``` (gemini-2.5-flash) |

If your use case requires the model to produce concise responses, you can include examples in the prompt that give preference to concise responses.

The following prompt provides two examples that show preference to the shorter explanations. In the response, you can see that the examples guided the model to choose the shorter explanation (`Explanation2`) as opposed to the longer explanation (`Explanation1`) like it did previously.

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Prompt:** ``` Below are some examples showing a question, explanation, and answer format: Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2 Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1 Now, Answer the following question given the example formats above: Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ``` **Response:** ``` Answer: Explanation2 ``` (gemini-2.5-flash) |

### Optimal number of examples

Models like Gemini can often pick up on patterns using a few examples, though you may need to experiment with the number of examples to provide in the prompt for the best results. At the same time, if you include too many examples, the model may start to[overfit](https://developers.google.com/machine-learning/glossary#overfitting)the response to the examples.

### Patterns vs anti patterns

Using examples to show the model a pattern to follow is more effective than using examples to show the model an anti pattern to avoid.

⛔**Negative pattern:**

|-------------------------------------------------------------------------------------------------------------------|
| **Example** ``` Don't end haikus with a question: Haiku are fun A short and simple poem Don't you enjoy them? ``` |

✅**Positive pattern:**

|---------------------------------------------------------------------------------------------------------------|
| **Example** ``` Always end haikus with an assertion: Haiku are fun A short and simple poem A joy to write ``` |

### Consistent formatting

Make sure that the structure and formatting of few-shot examples are the same to avoid responses with undesired formats. One of the primary objectives of adding few-shot examples in prompts is to show the model the response format. Therefore, it is essential to ensure a consistent format across all examples, especially paying attention to XML tags, white spaces, newlines, and example splitters.

## Add context

You can include instructions and information in a prompt that the model needs to solve a problem, instead of assuming that the model has all of the required information. This contextual information helps the model understand the constraints and details of what you're asking for it to do.

The following example asks the model to give troubleshooting guidance for a router:

|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Prompt:** ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ``` **Response:** ``` A yellow blinking light on your Google Wifi router usually indicates a problem with the internet connection. Here are some steps to troubleshoot and fix the issue: 1. Restart your router and modem: - Unplug your modem from the power outlet and wait for 30 seconds. - Plug your modem back in and wait for it to fully boot up. - Unplug your Google Wifi router and wait for 30 seconds. - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ``` (gemini-2.5-flash) |

The response looks like generic troubleshooting information that's not specific to the router or the status of the LED indicator lights.

To customize the response for the specific router, you can add to the prompt the router's troubleshooting guide as context for it to refer to when providing a response.

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Prompt:** ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button. Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup. Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ``` **Response:** ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ``` (gemini-2.5-flash) |

## Add prefixes

A prefix is a word or phrase that you add to the prompt content that can serve several purposes, depending on where you put the prefix:

- **Input prefix:**Adding a prefix to the input signals semantically meaningful parts of the input to the model. For example, the prefixes "English:" and "French:" demarcate two different languages.
- **Output prefix:**Even though the output is generated by the model, you can add a prefix for the output in the prompt. The output prefix gives the model information about what's expected as a response. For example, the output prefix "JSON:" signals to the model that the output should be in JSON format.
- **Example prefix:**In few-shot prompts, adding prefixes to the examples provides labels that the model can use when generating the output, which makes it easier to parse output content.

In the following example, "Text:" is the input prefix and "The answer is:" is the output prefix.

|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Prompt:** ``` Classify the text as one of the following categories. - large - small Text: Rhino The answer is: large Text: Mouse The answer is: small Text: Snail The answer is: small Text: Elephant The answer is: ``` **Response:** ``` The answer is: large ``` (gemini-2.5-flash) |

## Break down prompts into components

For use cases that require complex prompts, you can help the model manage this complexity by breaking things down into simpler components.

1. **Break down instructions:**Instead of having many instructions in one prompt, create one prompt per instruction. You can choose which prompt to process based on the user's input.

2. **Chain prompts:**For complex tasks that involve multiple sequential steps, make each step a prompt and chain the prompts together in a sequence. In this sequential chain of prompts, the output of one prompt in the sequence becomes the input of the next prompt. The output of the last prompt in the sequence is the final output.

3. **Aggregate responses:**Aggregation is when you want to perform different parallel tasks on different portions of the data and aggregate the results to produce the final output. For example, you can tell the model to perform one operation on the first part of the data, perform another operation on the rest of the data and aggregate the results.

## Experiment with model parameters

Each call that you send to a model includes parameter values that control how the model generates a response. The model can generate different results for different parameter values. Experiment with different parameter values to get the best values for the task. The parameters available for different models may differ. The most common parameters are the following:

1. **Max output tokens:**Specifies the maximum number of tokens that can be generated in the response. A token is approximately four characters. 100 tokens correspond to roughly 60-80 words.

2. **Temperature:** The temperature controls the degree of randomness in token selection. The temperature is used for sampling during response generation, which occurs when`topP`and`topK`are applied. Lower temperatures are good for prompts that require a more deterministic or less open-ended response, while higher temperatures can lead to more diverse or creative results. A temperature of 0 is deterministic, meaning that the highest probability response is always selected.

   | **Note:** When using Gemini 3 models, we strongly recommend keeping the`temperature`at its default value of 1.0. Changing the temperature (setting it below 1.0) may lead to unexpected behavior, such as looping or degraded performance, particularly in complex mathematical or reasoning tasks.
3. **`topK`:** The`topK`parameter changes how the model selects tokens for output. A`topK`of 1 means the selected token is the most probable among all the tokens in the model's vocabulary (also called greedy decoding), while a`topK`of 3 means that the next token is selected from among the 3 most probable using the temperature. For each token selection step, the`topK`tokens with the highest probabilities are sampled. Tokens are then further filtered based on`topP`with the final token selected using temperature sampling.

4. **`topP`:** The`topP`parameter changes how the model selects tokens for output. Tokens are selected from the most to least probable until the sum of their probabilities equals the`topP`value. For example, if tokens A, B, and C have a probability of 0.3, 0.2, and 0.1 and the`topP`value is 0.5, then the model will select either A or B as the next token by using the temperature and exclude C as a candidate. The default`topP`value is 0.95.

5. **`stop_sequences`:**Set a stop sequence to tell the model to stop generating content. A stop sequence can be any sequence of characters. Try to avoid using a sequence of characters that may appear in the generated content.

## Prompt iteration strategies

Prompt design can sometimes require a few iterations before you consistently get the response you're looking for. This section provides guidance on some things you can try when iterating on your prompts:

1. **Use different phrasing:**Using different words or phrasing in your prompts often yields different responses from the model even though they all mean the same thing. If you're not getting the expected results from your prompt, try rephrasing it.

   |---------------------------------------------------------------------------------------------------------------------|
   | ``` Version 1: How do I bake a pie? Version 2: Suggest a recipe for a pie. Version 3: What's a good pie recipe? ``` |

2. **Switch to an analogous task:**If you can't get the model to follow your instructions for a task, try giving it instructions for an analogous task that achieves the same result.

   This prompt tells the model to categorize a book by using predefined categories:

   |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | **Prompt:** ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ``` **Response:** ``` The Odyssey belongs to the category of **mythology**. Here's why: * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his journey home after the Trojan War. It features gods, monsters, and supernatural events common to Greek mythology. ..... ``` (gemini-2.5-flash) |

   The response is correct, but the model didn't stay within the bounds of the options. You also want to model to just respond with one of the options instead of in a full sentence. In this case, you can rephrase the instructions as a multiple choice question and ask the model to choose an option.

   <br />

   |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | **Prompt:** ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: - thriller - sci-fi - mythology - biography ``` **Response:** ``` The correct answer is mythology. ``` (gemini-2.5-flash) |

3. **Change the order of prompt content:**The order of the content in the prompt can sometimes affect the response. Try changing the content order and see how that affects the response.

       Version 1:
       [examples]
       [context]
       [input]

       Version 2:
       [input]
       [examples]
       [context]

       Version 3:
       [examples]
       [input]
       [context]

## Fallback responses

A fallback response is a response returned by the model when either the prompt or the response triggers a safety filter. An example of a fallback response is "I'm not able to help with that, as I'm only a language model."

If the model responds with a fallback response, try increasing the temperature.

## Things to avoid

- Avoid relying on models to generate factual information.
- Use with care on math and logic problems.

## Gemini 3

Gemini 3 models are designed for advanced reasoning and instruction following. They respond best to prompts that are direct, well-structured, and clearly define the task and any constraints. The following practices are recommended for optimal results with Gemini 3:

### Core prompting principles

- **Be precise and direct:**State your goal clearly and concisely. Avoid unnecessary or overly persuasive language.
- **Use consistent structure:** Employ clear delimiters to separate different parts of your prompt. XML-style tags (e.g.,`<context>`,`<task>`) or Markdown headings are effective. Choose one format and use it consistently within a single prompt.
- **Define parameters:**Explicitly explain any ambiguous terms or parameters.
- **Control output verbosity:**By default, Gemini 3 provides direct and efficient answers. If you need a more conversational or detailed response, you must explicitly request it in your instructions.
- **Handle multimodal inputs coherently:**When using text, images, audio, or video, treat them as equal-class inputs. Ensure your instructions clearly reference each modality as needed.
- **Prioritize critical instructions:**Place essential behavioral constraints, role definitions (persona), and output format requirements in the System Instruction or at the very beginning of the user prompt.
- **Structure for long contexts:** When providing large amounts of context (e.g., documents, code), supply all the context first. Place your specific instructions or questions at the very*end*of the prompt.
- **Anchor context:**After a large block of data, use a clear transition phrase to bridge the context and your query, such as "Based on the information above..."

### Enhancing reasoning and planning

You can leverage Gemini 3's advanced thinking capabilities to improve its response quality for complex tasks by prompting it to plan or self-critique before providing the final response.

**Example - Explicit planning:**  

    Before providing the final answer, please:
    1. Parse the stated goal into distinct sub-tasks.
    2. Check if the input information is complete.
    3. Create a structured outline to achieve the goal.

**Example - Self-critique:**  

    Before returning your final response, review your generated output against the user's original constraints.
    1. Did I answer the user's *intent*, not just their literal words?
    2. Is the tone authentic to the requested persona?

### Structured prompting examples

Using tags or Markdown helps the model distinguish between instructions, context, and tasks.

**XML example:**  

    <role>
    You are a helpful assistant.
    </role>

    <constraints>
    1. Be objective.
    2. Cite sources.
    </constraints>

    <context>
    [Insert User Input Here - The model knows this is data, not instructions]
    </context>

    <task>
    [Insert the specific user request here]
    </task>

**Markdown example:**  

    # Identity
    You are a senior solution architect.

    # Constraints
    - No external libraries allowed.
    - Python 3.11+ syntax only.

    # Output format
    Return a single code block.

### Example template combining best practices

This template captures the core principles for prompting with Gemini 3. Always make sure to iterate and modify for your specific use case.

**System Instruction:**  

    <role>
    You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
    You are precise, analytical, and persistent.
    </role>

    <instructions>
    1. **Plan**: Analyze the task and create a step-by-step plan.
    2. **Execute**: Carry out the plan.
    3. **Validate**: Review your output against the user's task.
    4. **Format**: Present the final answer in the requested structure.
    </instructions>

    <constraints>
    - Verbosity: [Specify Low/Medium/High]
    - Tone: [Specify Formal/Casual/Technical]
    </constraints>

    <output_format>
    Structure your response as follows:
    1. **Executive Summary**: [Short overview]
    2. **Detailed Response**: [The main content]
    </output_format>

**User Prompt:**  

    <context>
    [Insert relevant documents, code snippets, or background info here]
    </context>

    <task>
    [Insert specific user request here]
    </task>

    <final_instruction>
    Remember to think step-by-step before answering.
    </final_instruction>

## Generative models under the hood

This section aims to answer the question -***Is there randomness in generative models' responses, or are they deterministic?***

The short answer - yes to both. When you prompt a generative model, a text response is generated in two stages. In the first stage, the generative model processes the input prompt and generates a**probability distribution**over possible tokens (words) that are likely to come next. For example, if you prompt with the input text "The dog jumped over the ... ", the generative model will produce an array of probable next words:  

    [("fence", 0.77), ("ledge", 0.12), ("blanket", 0.03), ...]

This process is deterministic; a generative model will produce this same distribution every time it's input the same prompt text.

In the second stage, the generative model converts these distributions into actual text responses through one of several decoding strategies. A simple decoding strategy might select the most likely token at every timestep. This process would always be deterministic. However, you could instead choose to generate a response by*randomly sampling* over the distribution returned by the model. This process would be stochastic (random). Control the degree of randomness allowed in this decoding process by setting the temperature. A temperature of 0 means only the most likely tokens are selected, and there's no randomness. Conversely, a high temperature injects a high degree of randomness into the tokens selected by the model, leading to more unexpected, surprising model responses. For**Gemini 3**, it's recommended to not change the default temperature of 1.0 to avoid unexpected outcomes.

## Next steps

- Now that you have a deeper understanding of prompt design, try writing your own prompts using[Google AI Studio](http://aistudio.google.com).
- Learn more about the Gemini 3 Pro Preview model.
- To learn about multimodal prompting, see[Prompting with media files](https://ai.google.dev/gemini-api/docs/files#prompt-guide).
- To learn about image prompting, see the[Imagen prompt guide](https://ai.google.dev/gemini-api/docs/image-generation#imagen-prompt-guide)
- To learn about video prompting, see the[Veo prompt guide](https://ai.google.dev/gemini-api/docs/video#prompt-guide)

<br />

Function calling lets you connect models to external tools and APIs. Instead of generating text responses, the model determines when to call specific functions and provides the necessary parameters to execute real-world actions. This allows the model to act as a bridge between natural language and real-world actions and data. Function calling has 3 primary use cases:

- **Augment Knowledge:**Access information from external sources like databases, APIs, and knowledge bases.
- **Extend Capabilities:**Use external tools to perform computations and extend the limitations of the model, such as using a calculator or creating charts.
- **Take Actions:**Interact with external systems using APIs, such as scheduling appointments, creating invoices, sending emails, or controlling smart home devices.

Get WeatherSchedule MeetingCreate Chart  

### Python

    from google import genai
    from google.genai import types

    # Define the function declaration for the model
    schedule_meeting_function = {
        "name": "schedule_meeting",
        "description": "Schedules a meeting with specified attendees at a given time and date.",
        "parameters": {
            "type": "object",
            "properties": {
                "attendees": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of people attending the meeting.",
                },
                "date": {
                    "type": "string",
                    "description": "Date of the meeting (e.g., '2024-07-29')",
                },
                "time": {
                    "type": "string",
                    "description": "Time of the meeting (e.g., '15:00')",
                },
                "topic": {
                    "type": "string",
                    "description": "The subject or topic of the meeting.",
                },
            },
            "required": ["attendees", "date", "time", "topic"],
        },
    }

    # Configure the client and tools
    client = genai.Client()
    tools = types.Tool(function_declarations=[schedule_meeting_function])
    config = types.GenerateContentConfig(tools=[tools])

    # Send request with function declarations
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Schedule a meeting with Bob and Alice for 03/14/2025 at 10:00 AM about the Q3 planning.",
        config=config,
    )

    # Check for a function call
    if response.candidates[0].content.parts[0].function_call:
        function_call = response.candidates[0].content.parts[0].function_call
        print(f"Function to call: {function_call.name}")
        print(f"Arguments: {function_call.args}")
        #  In a real app, you would call your function here:
        #  result = schedule_meeting(**function_call.args)
    else:
        print("No function call found in the response.")
        print(response.text)

### JavaScript

    import { GoogleGenAI, Type } from '@google/genai';

    // Configure the client
    const ai = new GoogleGenAI({});

    // Define the function declaration for the model
    const scheduleMeetingFunctionDeclaration = {
      name: 'schedule_meeting',
      description: 'Schedules a meeting with specified attendees at a given time and date.',
      parameters: {
        type: Type.OBJECT,
        properties: {
          attendees: {
            type: Type.ARRAY,
            items: { type: Type.STRING },
            description: 'List of people attending the meeting.',
          },
          date: {
            type: Type.STRING,
            description: 'Date of the meeting (e.g., "2024-07-29")',
          },
          time: {
            type: Type.STRING,
            description: 'Time of the meeting (e.g., "15:00")',
          },
          topic: {
            type: Type.STRING,
            description: 'The subject or topic of the meeting.',
          },
        },
        required: ['attendees', 'date', 'time', 'topic'],
      },
    };

    // Send request with function declarations
    const response = await ai.models.generateContent({
      model: 'gemini-2.5-flash',
      contents: 'Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about the Q3 planning.',
      config: {
        tools: [{
          functionDeclarations: [scheduleMeetingFunctionDeclaration]
        }],
      },
    });

    // Check for function calls in the response
    if (response.functionCalls && response.functionCalls.length > 0) {
      const functionCall = response.functionCalls[0]; // Assuming one function call
      console.log(`Function to call: ${functionCall.name}`);
      console.log(`Arguments: ${JSON.stringify(functionCall.args)}`);
      // In a real app, you would call your actual function here:
      // const result = await scheduleMeeting(functionCall.args);
    } else {
      console.log("No function call found in the response.");
      console.log(response.text);
    }

### REST

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -X POST \
      -d '{
        "contents": [
          {
            "role": "user",
            "parts": [
              {
                "text": "Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about the Q3 planning."
              }
            ]
          }
        ],
        "tools": [
          {
            "functionDeclarations": [
              {
                "name": "schedule_meeting",
                "description": "Schedules a meeting with specified attendees at a given time and date.",
                "parameters": {
                  "type": "object",
                  "properties": {
                    "attendees": {
                      "type": "array",
                      "items": {"type": "string"},
                      "description": "List of people attending the meeting."
                    },
                    "date": {
                      "type": "string",
                      "description": "Date of the meeting (e.g., '2024-07-29')"
                    },
                    "time": {
                      "type": "string",
                      "description": "Time of the meeting (e.g., '15:00')"
                    },
                    "topic": {
                      "type": "string",
                      "description": "The subject or topic of the meeting."
                    }
                  },
                  "required": ["attendees", "date", "time", "topic"]
                }
              }
            ]
          }
        ]
      }'

## How function calling works

![function calling overview](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png)

Function calling involves a structured interaction between your application, the model, and external functions. Here's a breakdown of the process:

1. **Define Function Declaration:**Define the function declaration in your application code. Function Declarations describe the function's name, parameters, and purpose to the model.
2. **Call LLM with function declarations:**Send user prompt along with the function declaration(s) to the model. It analyzes the request and determines if a function call would be helpful. If so, it responds with a structured JSON object.
3. **Execute Function Code (Your Responsibility):** The Model*does not* execute the function itself. It's your application's responsibility to process the response and check for Function Call, if
   - **Yes**: Extract the name and args of the function and execute the corresponding function in your application.
   - **No:**The model has provided a direct text response to the prompt (this flow is less emphasized in the example but is a possible outcome).
4. **Create User friendly response:**If a function was executed, capture the result and send it back to the model in a subsequent turn of the conversation. It will use the result to generate a final, user-friendly response that incorporates the information from the function call.

This process can be repeated over multiple turns, allowing for complex interactions and workflows. The model also supports calling multiple functions in a single turn ([parallel function calling](https://ai.google.dev/gemini-api/docs/function-calling#parallel_function_calling)) and in sequence ([compositional function calling](https://ai.google.dev/gemini-api/docs/function-calling#compositional_function_calling)).

### Step 1: Define a function declaration

Define a function and its declaration within your application code that allows users to set light values and make an API request. This function could call external services or APIs.  

### Python

    # Define a function that the model can call to control smart lights
    set_light_values_declaration = {
        "name": "set_light_values",
        "description": "Sets the brightness and color temperature of a light.",
        "parameters": {
            "type": "object",
            "properties": {
                "brightness": {
                    "type": "integer",
                    "description": "Light level from 0 to 100. Zero is off and 100 is full brightness",
                },
                "color_temp": {
                    "type": "string",
                    "enum": ["daylight", "cool", "warm"],
                    "description": "Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.",
                },
            },
            "required": ["brightness", "color_temp"],
        },
    }

    # This is the actual function that would be called based on the model's suggestion
    def set_light_values(brightness: int, color_temp: str) -> dict[str, int | str]:
        """Set the brightness and color temperature of a room light. (mock API).

        Args:
            brightness: Light level from 0 to 100. Zero is off and 100 is full brightness
            color_temp: Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.

        Returns:
            A dictionary containing the set brightness and color temperature.
        """
        return {"brightness": brightness, "colorTemperature": color_temp}

### JavaScript

    import { Type } from '@google/genai';

    // Define a function that the model can call to control smart lights
    const setLightValuesFunctionDeclaration = {
      name: 'set_light_values',
      description: 'Sets the brightness and color temperature of a light.',
      parameters: {
        type: Type.OBJECT,
        properties: {
          brightness: {
            type: Type.NUMBER,
            description: 'Light level from 0 to 100. Zero is off and 100 is full brightness',
          },
          color_temp: {
            type: Type.STRING,
            enum: ['daylight', 'cool', 'warm'],
            description: 'Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.',
          },
        },
        required: ['brightness', 'color_temp'],
      },
    };

    /**

    *   Set the brightness and color temperature of a room light. (mock API)
    *   @param {number} brightness - Light level from 0 to 100. Zero is off and 100 is full brightness
    *   @param {string} color_temp - Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.
    *   @return {Object} A dictionary containing the set brightness and color temperature.
    */
    function setLightValues(brightness, color_temp) {
      return {
        brightness: brightness,
        colorTemperature: color_temp
      };
    }

### Step 2: Call the model with function declarations

Once you have defined your function declarations, you can prompt the model to use them. It analyzes the prompt and function declarations and decides whether to respond directly or to call a function. If a function is called, the response object will contain a function call suggestion.  

### Python

    from google.genai import types

    # Configure the client and tools
    client = genai.Client()
    tools = types.Tool(function_declarations=[set_light_values_declaration])
    config = types.GenerateContentConfig(tools=[tools])

    # Define user prompt
    contents = [
        types.Content(
            role="user", parts=[types.Part(text="Turn the lights down to a romantic level")]
        )
    ]

    # Send request with function declarations
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents
        config=config,
    )

    print(response.candidates[0].content.parts[0].function_call)

### JavaScript

    import { GoogleGenAI } from '@google/genai';

    // Generation config with function declaration
    const config = {
      tools: [{
        functionDeclarations: [setLightValuesFunctionDeclaration]
      }]
    };

    // Configure the client
    const ai = new GoogleGenAI({});

    // Define user prompt
    const contents = [
      {
        role: 'user',
        parts: [{ text: 'Turn the lights down to a romantic level' }]
      }
    ];

    // Send request with function declarations
    const response = await ai.models.generateContent({
      model: 'gemini-2.5-flash',
      contents: contents,
      config: config
    });

    console.log(response.functionCalls[0]);

The model then returns a`functionCall`object in an OpenAPI compatible schema specifying how to call one or more of the declared functions in order to respond to the user's question.  

### Python

    id=None args={'color_temp': 'warm', 'brightness': 25} name='set_light_values'

### JavaScript

    {
      name: 'set_light_values',
      args: { brightness: 25, color_temp: 'warm' }
    }

### Step 3: Execute set_light_values function code

Extract the function call details from the model's response, parse the arguments , and execute the`set_light_values`function.  

### Python

    # Extract tool call details, it may not be in the first part.
    tool_call = response.candidates[0].content.parts[0].function_call

    if tool_call.name == "set_light_values":
        result = set_light_values(**tool_call.args)
        print(f"Function execution result: {result}")

### JavaScript

    // Extract tool call details
    const tool_call = response.functionCalls[0]

    let result;
    if (tool_call.name === 'set_light_values') {
      result = setLightValues(tool_call.args.brightness, tool_call.args.color_temp);
      console.log(`Function execution result: ${JSON.stringify(result)}`);
    }

### Step 4: Create user friendly response with function result and call the model again

Finally, send the result of the function execution back to the model so it can incorporate this information into its final response to the user.  

### Python

    from google import genai
    from google.genai import types

    # Create a function response part
    function_response_part = types.Part.from_function_response(
        name=tool_call.name,
        response={"result": result},
    )

    # Append function call and result of the function execution to contents
    contents.append(response.candidates[0].content) # Append the content from the model's response.
    contents.append(types.Content(role="user", parts=[function_response_part])) # Append the function response

    client = genai.Client()
    final_response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=config,
        contents=contents,
    )

    print(final_response.text)

### JavaScript

    // Create a function response part
    const function_response_part = {
      name: tool_call.name,
      response: { result }
    }

    // Append function call and result of the function execution to contents
    contents.push(response.candidates[0].content);
    contents.push({ role: 'user', parts: [{ functionResponse: function_response_part }] });

    // Get the final response from the model
    const final_response = await ai.models.generateContent({
      model: 'gemini-2.5-flash',
      contents: contents,
      config: config
    });

    console.log(final_response.text);

This completes the function calling flow. The model successfully used the`set_light_values`function to perform the request action of the user.

## Function declarations

When you implement function calling in a prompt, you create a`tools`object, which contains one or more`function declarations`. You define functions using JSON, specifically with a[select subset](https://ai.google.dev/api/caching#Schema)of the[OpenAPI schema](https://spec.openapis.org/oas/v3.0.3#schemaw)format. A single function declaration can include the following parameters:

- `name`(string): A unique name for the function (`get_weather_forecast`,`send_email`). Use descriptive names without spaces or special characters (use underscores or camelCase).
- `description`(string): A clear and detailed explanation of the function's purpose and capabilities. This is crucial for the model to understand when to use the function. Be specific and provide examples if helpful ("Finds theaters based on location and optionally movie title which is currently playing in theaters.").
- `parameters`(object): Defines the input parameters the function expects.
  - `type`(string): Specifies the overall data type, such as`object`.
  - `properties`(object): Lists individual parameters, each with:
    - `type`(string): The data type of the parameter, such as`string`,`integer`,`boolean, array`.
    - `description`(string): A description of the parameter's purpose and format. Provide examples and constraints ("The city and state, e.g., 'San Francisco, CA' or a zip code e.g., '95616'.").
    - `enum`(array, optional): If the parameter values are from a fixed set, use "enum" to list the allowed values instead of just describing them in the description. This improves accuracy ("enum": \["daylight", "cool", "warm"\]).
  - `required`(array): An array of strings listing the parameter names that are mandatory for the function to operate.

You can also construct`FunctionDeclarations`from Python functions directly using`types.FunctionDeclaration.from_callable(client=client, callable=your_function)`.

## Function calling with thinking models

Gemini 3 and 2.5 series models use an internal["thinking"](https://ai.google.dev/gemini-api/docs/thinking)process to reason through requests. This significantly improves function calling performance, allowing the model to better determine when to call a function and which parameters to use. Because the Gemini API is stateless, models use[thought signatures](https://ai.google.dev/gemini-api/docs/thought-signatures)to maintain context across multi-turn conversations.

This section covers advanced management of thought signatures and is only necessary if you're manually constructing API requests (e.g., via REST) or manipulating conversation history.

**If you're using the[Google GenAI SDKs](https://ai.google.dev/gemini-api/docs/libraries)(our official libraries), you don't need to manage this process** . The SDKs automatically handle the necessary steps, as shown in the earlier[example](https://ai.google.dev/gemini-api/docs/function-calling#step-4).

### Managing conversation history manually

If you modify the conversation history manually, instead of sending the[complete previous response](https://ai.google.dev/gemini-api/docs/function-calling#step-4)you must correctly handle the`thought_signature`included in the model's turn.

Follow these rules to ensure the model's context is preserved:

- Always send the`thought_signature`back to the model inside its original[`Part`](https://ai.google.dev/api#request-body-structure).
- Don't merge a`Part`containing a signature with one that does not. This breaks the positional context of the thought.
- Don't combine two`Parts`that both contain signatures, as the signature strings cannot be merged.

#### Gemini 3 thought signatures

In Gemini 3, any[`Part`](https://ai.google.dev/api#request-body-structure)of a model response may contain a thought signature. While we generally recommend returning signatures from all`Part`types, passing back thought signatures is mandatory for function calling. Unless you are manipulating conversation history manually, the Google GenAI SDK will handle thought signatures automatically.

If you are manipulating conversation history manually, refer to the[Thoughts Signatures](https://ai.google.dev/gemini-api/docs/thought-signatures)page for complete guidance and details on handling thought signatures for Gemini 3.

### Inspecting thought signatures

While not necessary for implementation, you can inspect the response to see the`thought_signature`for debugging or educational purposes.  

### Python

    import base64
    # After receiving a response from a model with thinking enabled
    # response = client.models.generate_content(...)

    # The signature is attached to the response part containing the function call
    part = response.candidates[0].content.parts[0]
    if part.thought_signature:
      print(base64.b64encode(part.thought_signature).decode("utf-8"))

### JavaScript

    // After receiving a response from a model with thinking enabled
    // const response = await ai.models.generateContent(...)

    // The signature is attached to the response part containing the function call
    const part = response.candidates[0].content.parts[0];
    if (part.thoughtSignature) {
      console.log(part.thoughtSignature);
    }

Learn more about limitations and usage of thought signatures, and about thinking models in general, on the[Thinking](https://ai.google.dev/gemini-api/docs/thinking#signatures)page.

## Parallel function calling

In addition to single turn function calling, you can also call multiple functions at once. Parallel function calling lets you execute multiple functions at once and is used when the functions are not dependent on each other. This is useful in scenarios like gathering data from multiple independent sources, such as retrieving customer details from different databases or checking inventory levels across various warehouses or performing multiple actions such as converting your apartment into a disco.  

### Python

    power_disco_ball = {
        "name": "power_disco_ball",
        "description": "Powers the spinning disco ball.",
        "parameters": {
            "type": "object",
            "properties": {
                "power": {
                    "type": "boolean",
                    "description": "Whether to turn the disco ball on or off.",
                }
            },
            "required": ["power"],
        },
    }

    start_music = {
        "name": "start_music",
        "description": "Play some music matching the specified parameters.",
        "parameters": {
            "type": "object",
            "properties": {
                "energetic": {
                    "type": "boolean",
                    "description": "Whether the music is energetic or not.",
                },
                "loud": {
                    "type": "boolean",
                    "description": "Whether the music is loud or not.",
                },
            },
            "required": ["energetic", "loud"],
        },
    }

    dim_lights = {
        "name": "dim_lights",
        "description": "Dim the lights.",
        "parameters": {
            "type": "object",
            "properties": {
                "brightness": {
                    "type": "number",
                    "description": "The brightness of the lights, 0.0 is off, 1.0 is full.",
                }
            },
            "required": ["brightness"],
        },
    }

### JavaScript

    import { Type } from '@google/genai';

    const powerDiscoBall = {
      name: 'power_disco_ball',
      description: 'Powers the spinning disco ball.',
      parameters: {
        type: Type.OBJECT,
        properties: {
          power: {
            type: Type.BOOLEAN,
            description: 'Whether to turn the disco ball on or off.'
          }
        },
        required: ['power']
      }
    };

    const startMusic = {
      name: 'start_music',
      description: 'Play some music matching the specified parameters.',
      parameters: {
        type: Type.OBJECT,
        properties: {
          energetic: {
            type: Type.BOOLEAN,
            description: 'Whether the music is energetic or not.'
          },
          loud: {
            type: Type.BOOLEAN,
            description: 'Whether the music is loud or not.'
          }
        },
        required: ['energetic', 'loud']
      }
    };

    const dimLights = {
      name: 'dim_lights',
      description: 'Dim the lights.',
      parameters: {
        type: Type.OBJECT,
        properties: {
          brightness: {
            type: Type.NUMBER,
            description: 'The brightness of the lights, 0.0 is off, 1.0 is full.'
          }
        },
        required: ['brightness']
      }
    };

Configure the function calling mode to allow using all of the specified tools. To learn more, you can read about[configuring function calling](https://ai.google.dev/gemini-api/docs/function-calling#function_calling_modes).  

### Python

    from google import genai
    from google.genai import types

    # Configure the client and tools
    client = genai.Client()
    house_tools = [
        types.Tool(function_declarations=[power_disco_ball, start_music, dim_lights])
    ]
    config = types.GenerateContentConfig(
        tools=house_tools,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        ),
        # Force the model to call 'any' function, instead of chatting.
        tool_config=types.ToolConfig(
            function_calling_config=types.FunctionCallingConfig(mode='ANY')
        ),
    )

    chat = client.chats.create(model="gemini-2.5-flash", config=config)
    response = chat.send_message("Turn this place into a party!")

    # Print out each of the function calls requested from this single call
    print("Example 1: Forced function calling")
    for fn in response.function_calls:
        args = ", ".join(f"{key}={val}" for key, val in fn.args.items())
        print(f"{fn.name}({args})")

### JavaScript

    import { GoogleGenAI } from '@google/genai';

    // Set up function declarations
    const houseFns = [powerDiscoBall, startMusic, dimLights];

    const config = {
        tools: [{
            functionDeclarations: houseFns
        }],
        // Force the model to call 'any' function, instead of chatting.
        toolConfig: {
            functionCallingConfig: {
                mode: 'any'
            }
        }
    };

    // Configure the client
    const ai = new GoogleGenAI({});

    // Create a chat session
    const chat = ai.chats.create({
        model: 'gemini-2.5-flash',
        config: config
    });
    const response = await chat.sendMessage({message: 'Turn this place into a party!'});

    // Print out each of the function calls requested from this single call
    console.log("Example 1: Forced function calling");
    for (const fn of response.functionCalls) {
        const args = Object.entries(fn.args)
            .map(([key, val]) => `${key}=${val}`)
            .join(', ');
        console.log(`${fn.name}(${args})`);
    }

Each of the printed results reflects a single function call that the model has requested. To send the results back, include the responses in the same order as they were requested.

The Python SDK supports[automatic function calling](https://ai.google.dev/gemini-api/docs/function-calling#automatic_function_calling_python_only), which automatically converts Python functions to declarations, handles the function call execution and response cycle for you. Following is an example for the disco use case.
**Note:** Automatic Function Calling is a Python SDK only feature at the moment.  

### Python

    from google import genai
    from google.genai import types

    # Actual function implementations
    def power_disco_ball_impl(power: bool) -> dict:
        """Powers the spinning disco ball.

        Args:
            power: Whether to turn the disco ball on or off.

        Returns:
            A status dictionary indicating the current state.
        """
        return {"status": f"Disco ball powered {'on' if power else 'off'}"}

    def start_music_impl(energetic: bool, loud: bool) -> dict:
        """Play some music matching the specified parameters.

        Args:
            energetic: Whether the music is energetic or not.
            loud: Whether the music is loud or not.

        Returns:
            A dictionary containing the music settings.
        """
        music_type = "energetic" if energetic else "chill"
        volume = "loud" if loud else "quiet"
        return {"music_type": music_type, "volume": volume}

    def dim_lights_impl(brightness: float) -> dict:
        """Dim the lights.

        Args:
            brightness: The brightness of the lights, 0.0 is off, 1.0 is full.

        Returns:
            A dictionary containing the new brightness setting.
        """
        return {"brightness": brightness}

    # Configure the client
    client = genai.Client()
    config = types.GenerateContentConfig(
        tools=[power_disco_ball_impl, start_music_impl, dim_lights_impl]
    )

    # Make the request
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Do everything you need to this place into party!",
        config=config,
    )

    print("\nExample 2: Automatic function calling")
    print(response.text)
    # I've turned on the disco ball, started playing loud and energetic music, and dimmed the lights to 50% brightness. Let's get this party started!

## Compositional function calling

Compositional or sequential function calling allows Gemini to chain multiple function calls together to fulfill a complex request. For example, to answer "Get the temperature in my current location", the Gemini API might first invoke a`get_current_location()`function followed by a`get_weather()`function that takes the location as a parameter.

The following example demonstrates how to implement compositional function calling using the Python SDK and automatic function calling.  

### Python

This example uses the automatic function calling feature of the`google-genai`Python SDK. The SDK automatically converts the Python functions to the required schema, executes the function calls when requested by the model, and sends the results back to the model to complete the task.  

    import os
    from google import genai
    from google.genai import types

    # Example Functions
    def get_weather_forecast(location: str) -> dict:
        """Gets the current weather temperature for a given location."""
        print(f"Tool Call: get_weather_forecast(location={location})")
        # TODO: Make API call
        print("Tool Response: {'temperature': 25, 'unit': 'celsius'}")
        return {"temperature": 25, "unit": "celsius"}  # Dummy response

    def set_thermostat_temperature(temperature: int) -> dict:
        """Sets the thermostat to a desired temperature."""
        print(f"Tool Call: set_thermostat_temperature(temperature={temperature})")
        # TODO: Interact with a thermostat API
        print("Tool Response: {'status': 'success'}")
        return {"status": "success"}

    # Configure the client and model
    client = genai.Client()
    config = types.GenerateContentConfig(
        tools=[get_weather_forecast, set_thermostat_temperature]
    )

    # Make the request
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
        config=config,
    )

    # Print the final, user-facing response
    print(response.text)

**Expected Output**

When you run the code, you will see the SDK orchestrating the function calls. The model first calls`get_weather_forecast`, receives the temperature, and then calls`set_thermostat_temperature`with the correct value based on the logic in the prompt.  

    Tool Call: get_weather_forecast(location=London)
    Tool Response: {'temperature': 25, 'unit': 'celsius'}
    Tool Call: set_thermostat_temperature(temperature=20)
    Tool Response: {'status': 'success'}
    OK. I've set the thermostat to 20°C.

### JavaScript

This example shows how to use JavaScript/TypeScript SDK to do comopositional function calling using a manual execution loop.  

    import { GoogleGenAI, Type } from "@google/genai";

    // Configure the client
    const ai = new GoogleGenAI({});

    // Example Functions
    function get_weather_forecast({ location }) {
      console.log(`Tool Call: get_weather_forecast(location=${location})`);
      // TODO: Make API call
      console.log("Tool Response: {'temperature': 25, 'unit': 'celsius'}");
      return { temperature: 25, unit: "celsius" };
    }

    function set_thermostat_temperature({ temperature }) {
      console.log(
        `Tool Call: set_thermostat_temperature(temperature=${temperature})`,
      );
      // TODO: Make API call
      console.log("Tool Response: {'status': 'success'}");
      return { status: "success" };
    }

    const toolFunctions = {
      get_weather_forecast,
      set_thermostat_temperature,
    };

    const tools = [
      {
        functionDeclarations: [
          {
            name: "get_weather_forecast",
            description:
              "Gets the current weather temperature for a given location.",
            parameters: {
              type: Type.OBJECT,
              properties: {
                location: {
                  type: Type.STRING,
                },
              },
              required: ["location"],
            },
          },
          {
            name: "set_thermostat_temperature",
            description: "Sets the thermostat to a desired temperature.",
            parameters: {
              type: Type.OBJECT,
              properties: {
                temperature: {
                  type: Type.NUMBER,
                },
              },
              required: ["temperature"],
            },
          },
        ],
      },
    ];

    // Prompt for the model
    let contents = [
      {
        role: "user",
        parts: [
          {
            text: "If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
          },
        ],
      },
    ];

    // Loop until the model has no more function calls to make
    while (true) {
      const result = await ai.models.generateContent({
        model: "gemini-2.5-flash",
        contents,
        config: { tools },
      });

      if (result.functionCalls && result.functionCalls.length > 0) {
        const functionCall = result.functionCalls[0];

        const { name, args } = functionCall;

        if (!toolFunctions[name]) {
          throw new Error(`Unknown function call: ${name}`);
        }

        // Call the function and get the response.
        const toolResponse = toolFunctions[name](args);

        const functionResponsePart = {
          name: functionCall.name,
          response: {
            result: toolResponse,
          },
        };

        // Send the function response back to the model.
        contents.push({
          role: "model",
          parts: [
            {
              functionCall: functionCall,
            },
          ],
        });
        contents.push({
          role: "user",
          parts: [
            {
              functionResponse: functionResponsePart,
            },
          ],
        });
      } else {
        // No more function calls, break the loop.
        console.log(result.text);
        break;
      }
    }

**Expected Output**

When you run the code, you will see the SDK orchestrating the function calls. The model first calls`get_weather_forecast`, receives the temperature, and then calls`set_thermostat_temperature`with the correct value based on the logic in the prompt.  

    Tool Call: get_weather_forecast(location=London)
    Tool Response: {'temperature': 25, 'unit': 'celsius'}
    Tool Call: set_thermostat_temperature(temperature=20)
    Tool Response: {'status': 'success'}
    OK. It's 25°C in London, so I've set the thermostat to 20°C.

Compositional function calling is a native[Live API](https://ai.google.dev/gemini-api/docs/live)feature. This means Live API can handle the function calling similar to the Python SDK.  

### Python

    # Light control schemas
    turn_on_the_lights_schema = {'name': 'turn_on_the_lights'}
    turn_off_the_lights_schema = {'name': 'turn_off_the_lights'}

    prompt = """
      Hey, can you write run some python code to turn on the lights, wait 10s and then turn off the lights?
      """

    tools = [
        {'code_execution': {}},
        {'function_declarations': [turn_on_the_lights_schema, turn_off_the_lights_schema]}
    ]

    await run(prompt, tools=tools, modality="AUDIO")

### JavaScript

    // Light control schemas
    const turnOnTheLightsSchema = { name: 'turn_on_the_lights' };
    const turnOffTheLightsSchema = { name: 'turn_off_the_lights' };

    const prompt = `
      Hey, can you write run some python code to turn on the lights, wait 10s and then turn off the lights?
    `;

    const tools = [
      { codeExecution: {} },
      { functionDeclarations: [turnOnTheLightsSchema, turnOffTheLightsSchema] }
    ];

    await run(prompt, tools=tools, modality="AUDIO")

## Function calling modes

The Gemini API lets you control how the model uses the provided tools (function declarations). Specifically, you can set the mode within the.`function_calling_config`.

- `AUTO (Default)`: The model decides whether to generate a natural language response or suggest a function call based on the prompt and context. This is the most flexible mode and recommended for most scenarios.
- `ANY`: The model is constrained to always predict a function call and guarantees function schema adherence. If`allowed_function_names`is not specified, the model can choose from any of the provided function declarations. If`allowed_function_names`is provided as a list, the model can only choose from the functions in that list. Use this mode when you require a function call response to every prompt (if applicable).
- `NONE`: The model is*prohibited*from making function calls. This is equivalent to sending a request without any function declarations. Use this to temporarily disable function calling without removing your tool definitions.
- `VALIDATED`(Preview): The model is constrained to predict either function calls or natural language, and ensures function schema adherence. If`allowed_function_names`is not provided, the model picks from all of the available function declarations. If`allowed_function_names`is provided, the model picks from the set of allowed functions.

### Python

    from google.genai import types

    # Configure function calling mode
    tool_config = types.ToolConfig(
        function_calling_config=types.FunctionCallingConfig(
            mode="ANY", allowed_function_names=["get_current_temperature"]
        )
    )

    # Create the generation config
    config = types.GenerateContentConfig(
        tools=[tools],  # not defined here.
        tool_config=tool_config,
    )

### JavaScript

    import { FunctionCallingConfigMode } from '@google/genai';

    // Configure function calling mode
    const toolConfig = {
      functionCallingConfig: {
        mode: FunctionCallingConfigMode.ANY,
        allowedFunctionNames: ['get_current_temperature']
      }
    };

    // Create the generation config
    const config = {
      tools: tools, // not defined here.
      toolConfig: toolConfig,
    };

## Automatic function calling (Python only)

When using the Python SDK, you can provide Python functions directly as tools. The SDK converts these functions into declarations, manages the function call execution, and handles the response cycle for you. Define your function with type hints and a docstring. For optimal results, it is recommended to use[Google-style docstrings.](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)The SDK will then automatically:

1. Detect function call responses from the model.
2. Call the corresponding Python function in your code.
3. Send the function's response back to the model.
4. Return the model's final text response.

The SDK currently does not parse argument descriptions into the property description slots of the generated function declaration. Instead, it sends the entire docstring as the top-level function description.  

### Python

    from google import genai
    from google.genai import types

    # Define the function with type hints and docstring
    def get_current_temperature(location: str) -> dict:
        """Gets the current temperature for a given location.

        Args:
            location: The city and state, e.g. San Francisco, CA

        Returns:
            A dictionary containing the temperature and unit.
        """
        # ... (implementation) ...
        return {"temperature": 25, "unit": "Celsius"}

    # Configure the client
    client = genai.Client()
    config = types.GenerateContentConfig(
        tools=[get_current_temperature]
    )  # Pass the function itself

    # Make the request
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="What's the temperature in Boston?",
        config=config,
    )

    print(response.text)  # The SDK handles the function call and returns the final text

You can disable automatic function calling with:  

### Python

    config = types.GenerateContentConfig(
        tools=[get_current_temperature],
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
    )

### Automatic function schema declaration

The API is able to describe any of the following types.`Pydantic`types are allowed, as long as the fields defined on them are also composed of allowed types. Dict types (like`dict[str: int]`) are not well supported here, don't use them.  

### Python

    AllowedType = (
      int | float | bool | str | list['AllowedType'] | pydantic.BaseModel)

To see what the inferred schema looks like, you can convert it using[`from_callable`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable):  

### Python

    from google import genai
    from google.genai import types

    def multiply(a: float, b: float):
        """Returns a * b."""
        return a * b

    client = genai.Client()
    fn_decl = types.FunctionDeclaration.from_callable(callable=multiply, client=client)

    # to_json_dict() provides a clean JSON representation.
    print(fn_decl.to_json_dict())

## Multi-tool use: Combine native tools with function calling

You can enable multiple tools combining native tools with function calling at the same time. Here's an example that enables two tools,[Grounding with Google Search](https://ai.google.dev/gemini-api/docs/grounding)and[code execution](https://ai.google.dev/gemini-api/docs/code-execution), in a request using the[Live API](https://ai.google.dev/gemini-api/docs/live).
**Note:** Multi-tool use is a-[Live API](https://ai.google.dev/gemini-api/docs/live)only feature at the moment. The`run()`function declaration, which handles the asynchronous websocket setup, is omitted for brevity.  

### Python

    # Multiple tasks example - combining lights, code execution, and search
    prompt = """
      Hey, I need you to do three things for me.

        1.  Turn on the lights.
        2.  Then compute the largest prime palindrome under 100000.
        3.  Then use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024.

      Thanks!
      """

    tools = [
        {'google_search': {}},
        {'code_execution': {}},
        {'function_declarations': [turn_on_the_lights_schema, turn_off_the_lights_schema]} # not defined here.
    ]

    # Execute the prompt with specified tools in audio modality
    await run(prompt, tools=tools, modality="AUDIO")

### JavaScript

    // Multiple tasks example - combining lights, code execution, and search
    const prompt = `
      Hey, I need you to do three things for me.

        1.  Turn on the lights.
        2.  Then compute the largest prime palindrome under 100000.
        3.  Then use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024.

      Thanks!
    `;

    const tools = [
      { googleSearch: {} },
      { codeExecution: {} },
      { functionDeclarations: [turnOnTheLightsSchema, turnOffTheLightsSchema] } // not defined here.
    ];

    // Execute the prompt with specified tools in audio modality
    await run(prompt, {tools: tools, modality: "AUDIO"});

Python developers can try this out in the[Live API Tool Use notebook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb).

## Model context protocol (MCP)

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)is an open standard for connecting AI applications with external tools and data. MCP provides a common protocol for models to access context, such as functions (tools), data sources (resources), or predefined prompts.

The Gemini SDKs have built-in support for the MCP, reducing boilerplate code and offering[automatic tool calling](https://ai.google.dev/gemini-api/docs/function-calling#automatic_function_calling_python_only)for MCP tools. When the model generates an MCP tool call, the Python and JavaScript client SDK can automatically execute the MCP tool and send the response back to the model in a subsequent request, continuing this loop until no more tool calls are made by the model.

Here, you can find an example of how to use a local MCP server with Gemini and`mcp`SDK.  

### Python

Make sure the latest version of the[`mcp`SDK](https://modelcontextprotocol.io/introduction)is installed on your platform of choice.  

    pip install mcp

**Note:** Python supports automatic tool calling by passing in the`ClientSession`into the`tools`parameters. If you want to disable it, you can provide`automatic_function_calling`with disabled`True`.  

    import os
    import asyncio
    from datetime import datetime
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
    from google import genai

    client = genai.Client()

    # Create server parameters for stdio connection
    server_params = StdioServerParameters(
        command="npx",  # Executable
        args=["-y", "@philschmid/weather-mcp"],  # MCP Server
        env=None,  # Optional environment variables
    )

    async def run():
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Prompt to get the weather for the current day in London.
                prompt = f"What is the weather in London in {datetime.now().strftime('%Y-%m-%d')}?"

                # Initialize the connection between client and server
                await session.initialize()

                # Send request to the model with MCP function declarations
                response = await client.aio.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                    config=genai.types.GenerateContentConfig(
                        temperature=0,
                        tools=[session],  # uses the session, will automatically call the tool
                        # Uncomment if you **don't** want the SDK to automatically call the tool
                        # automatic_function_calling=genai.types.AutomaticFunctionCallingConfig(
                        #     disable=True
                        # ),
                    ),
                )
                print(response.text)

    # Start the asyncio event loop and run the main function
    asyncio.run(run())

### JavaScript

Make sure the latest version of the`mcp`SDK is installed on your platform of choice.  

    npm install @modelcontextprotocol/sdk

**Note:** JavaScript supports automatic tool calling by wrapping the`client`with`mcpToTool`. If you want to disable it, you can provide`automaticFunctionCalling`with disabled`true`.  

    import { GoogleGenAI, FunctionCallingConfigMode , mcpToTool} from '@google/genai';
    import { Client } from "@modelcontextprotocol/sdk/client/index.js";
    import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

    // Create server parameters for stdio connection
    const serverParams = new StdioClientTransport({
      command: "npx", // Executable
      args: ["-y", "@philschmid/weather-mcp"] // MCP Server
    });

    const client = new Client(
      {
        name: "example-client",
        version: "1.0.0"
      }
    );

    // Configure the client
    const ai = new GoogleGenAI({});

    // Initialize the connection between client and server
    await client.connect(serverParams);

    // Send request to the model with MCP tools
    const response = await ai.models.generateContent({
      model: "gemini-2.5-flash",
      contents: `What is the weather in London in ${new Date().toLocaleDateString()}?`,
      config: {
        tools: [mcpToTool(client)],  // uses the session, will automatically call the tool
        // Uncomment if you **don't** want the sdk to automatically call the tool
        // automaticFunctionCalling: {
        //   disable: true,
        // },
      },
    });
    console.log(response.text)

    // Close the connection
    await client.close();

### Limitations with built-in MCP support

Built-in MCP support is a[experimental](https://ai.google.dev/gemini-api/docs/models#preview)feature in our SDKs and has the following limitations:

- Only tools are supported, not resources nor prompts
- It is available for the Python and JavaScript/TypeScript SDK.
- Breaking changes might occur in future releases.

Manual integration of MCP servers is always an option if these limit what you're building.

## Supported models

This section lists models and their function calling capabilities. Experimental models are not included. You can find a comprehensive capabilities overview on the[model overview](https://ai.google.dev/gemini-api/docs/models)page.

|         Model         | Function Calling | Parallel Function Calling | Compositional Function Calling |
|-----------------------|------------------|---------------------------|--------------------------------|
| Gemini 2.5 Pro        | ✔️               | ✔️                        | ✔️                             |
| Gemini 2.5 Flash      | ✔️               | ✔️                        | ✔️                             |
| Gemini 2.5 Flash-Lite | ✔️               | ✔️                        | ✔️                             |
| Gemini 2.0 Flash      | ✔️               | ✔️                        | ✔️                             |
| Gemini 2.0 Flash-Lite | X                | X                         | X                              |

## Best practices

- **Function and Parameter Descriptions:**Be extremely clear and specific in your descriptions. The model relies on these to choose the correct function and provide appropriate arguments.
- **Naming:**Use descriptive function names (without spaces, periods, or dashes).
- **Strong Typing:**Use specific types (integer, string, enum) for parameters to reduce errors. If a parameter has a limited set of valid values, use an enum.
- **Tool Selection:**While the model can use an arbitrary number of tools, providing too many can increase the risk of selecting an incorrect or suboptimal tool. For best results, aim to provide only the relevant tools for the context or task, ideally keeping the active set to a maximum of 10-20. Consider dynamic tool selection based on conversation context if you have a large total number of tools.
- **Prompt Engineering:**
  - Provide context: Tell the model its role (e.g., "You are a helpful weather assistant.").
  - Give instructions: Specify how and when to use functions (e.g., "Don't guess dates; always use a future date for forecasts.").
  - Encourage clarification: Instruct the model to ask clarifying questions if needed.
- **Temperature:**Use a low temperature (e.g., 0) for more deterministic and reliable function calls.

  | When using Gemini 3 models, we strongly recommend keeping the`temperature`at its default value of 1.0. Changing the temperature (setting it below 1.0) may lead to unexpected behavior, such as looping or degraded performance, particularly in complex mathematical or reasoning tasks.
- **Validation:**If a function call has significant consequences (e.g., placing an order), validate the call with the user before executing it.

- **Check Finish Reason:** Always check the[`finishReason`](https://ai.google.dev/api/generate-content#FinishReason)in the model's response to handle cases where the model failed to generate a valid function call.

- **Error Handling**: Implement robust error handling in your functions to gracefully handle unexpected inputs or API failures. Return informative error messages that the model can use to generate helpful responses to the user.

- **Security:**Be mindful of security when calling external APIs. Use appropriate authentication and authorization mechanisms. Avoid exposing sensitive data in function calls.

- **Token Limits:**Function descriptions and parameters count towards your input token limit. If you're hitting token limits, consider limiting the number of functions or the length of the descriptions, break down complex tasks into smaller, more focused function sets.

## Notes and limitations

- Only a[subset of the OpenAPI schema](https://ai.google.dev/api/caching#FunctionDeclaration)is supported.
- Supported parameter types in Python are limited.
- Automatic function calling is a Python SDK feature only.