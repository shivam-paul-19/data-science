import google.generativeai as genai

genai.configure(api_key="AIzaSyBge7gNIe0lGrlEgKbD3x1oQCVXcz_3XdU")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("")
print(response.text)