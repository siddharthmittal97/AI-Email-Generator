from groq import Groq
import os

client = Groq(api_key=os.environ["GROQ_API_KEY"])

topic = input("Email topic: ")
tone = input("Tone (professional/friendly/urgent) [professional]: ").strip() or "professional"
recipient = input("Recipient (e.g. client, boss, team) [client]: ").strip() or "client"

r = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": """
            You are an expert AI email assistant.
            Write human-like emails.
            Be warm, concise, and professional.
            Adapt tone naturally.
            """
        },
        {
            "role": "user",
            "content": (
                f"Write a {tone} email to a {recipient} about: {topic}. "
                "Include a subject line starting with 'Subject:', then a blank line, then the email body. "
                "Keep it concise and clear. Only return the email, nothing else."
            ),
        }
    ],
    max_tokens=512,
)

print("\n" + r.choices[0].message.content.strip())