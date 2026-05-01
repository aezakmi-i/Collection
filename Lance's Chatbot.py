from google import genai
client = genai.Client(api_key="")

"""response = client.models.generate_content(
    model = "gemini-2.0-flash",
    contents = "Hi, nice to meet you"
)

print(response)"""
print("Connected")