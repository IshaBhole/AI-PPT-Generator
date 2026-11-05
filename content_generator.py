import ollama
import json
import re


def generate_slide_content(topic, slide_title):

    prompt = f"""
Topic:
{topic}

Slide Type:
{slide_title}

Generate ONE PowerPoint slide.

Return ONLY valid JSON.

Example:

{{
    "title":"Introduction",
    "content":[
        "Point 1",
        "Point 2",
        "Point 3",
        "Point 4"
    ]
}}

Rules:
- Exactly ONE JSON object
- Maximum 4 bullet points
- Short professional content
- No markdown
- No explanations
- No extra text
"""

    response = ollama.chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"]

    print("\nRAW CONTENT:\n")
    print(content)

    match = re.search(
        r'\{[\s\S]*\}',
        content
    )

    if match:
        content = match.group()

    try:

        return json.loads(content)

    except Exception as e:

        print("JSON ERROR:", e)

        return {
            "title": slide_title,
            "content": [
                "Content generation failed"
            ]
        }