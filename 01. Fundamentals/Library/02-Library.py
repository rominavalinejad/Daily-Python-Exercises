import os
import google.generativeai as genai

#-----------------------------------------------------------------------
my_secret_key = "my_secret_key"
os.environ["Gemini_API_Key"] = my_secret_key
save_key = os.environ.get("Gemini_API_Key")
#-----------------------------------------------------------------------

save_key = os.environ.get("Gemini_API_Key")
if save_key:
    print("OK")
    genai.configure(api_key=save_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    print("Sending Test Message...")
    response = model.generate_content("Hi! I'm ready. if you hear me say 'I'm ready!'")
    print("n\--- AI Answer ---")
    print(response.text)
else:
    print("Error! API Doesn't found.")
    