from flask import Flask, render_template, request, jsonify, session
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import re
import os
import pandas as pd

# ✅ Ensure script runs from the correct directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)  
print("📌 Current Directory:", os.getcwd())  

# ✅ Dataset Path Handling
dataset_filename = "Cleaned_Indian_Food_Dataset.csv"
dataset_path = os.path.join(script_dir, dataset_filename)

# 🔍 Debugging: List files in the directory
print("📂 Files in Directory:", os.listdir(script_dir))

# ✅ Check alternative locations if the dataset is missing
if not os.path.exists(dataset_path):
    possible_folders = ["archive (1)", "data", "datasets"]  # Common subfolder names
    for folder in possible_folders:
        possible_path = os.path.join(script_dir, folder, dataset_filename)
        if os.path.exists(possible_path):
            dataset_path = possible_path
            print(f"✅ Found dataset in {folder}/")
            break

# ✅ Load dataset safely
if os.path.exists(dataset_path):
    df = pd.read_csv(dataset_path, encoding="utf-8")
    df.columns = df.columns.str.strip()  # Remove spaces from column names
    print("✅ Dataset loaded successfully!")
    print("📌 Available columns:", df.columns.tolist())  
else:
    raise FileNotFoundError(f"❌ Dataset not found! Move 'Cleaned_Indian_Food_Dataset.csv' to the project folder.")

# ✅ Flask app setup
app = Flask(__name__)
app.secret_key = "your_secret_key_here"
app.config["SESSION_TYPE"] = "filesystem"  # Fix session storage issue

# ✅ Load DialoGPT model
print("⏳ Loading DialoGPT model...")
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")
print("✅ Model loaded!")

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    """Handles chat requests."""
    msg = request.form["msg"]
    response = get_chat_response(msg)
    return jsonify(response=response)

def preprocess_text(text):
    """Preprocess text by removing punctuation and lowercasing."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def search_food_info(food_name):
    """Search for food details in the dataset."""
    food_name = food_name.lower()
    
    # ✅ Use TranslatedRecipeName instead of Food
    food_data = df[df['TranslatedRecipeName'].str.lower().str.contains(food_name, na=False)]
    
    if not food_data.empty:
        return (
            f"🍽️ Recipe: {food_data.iloc[0]['TranslatedRecipeName']}\n"
            f"🌍 Cuisine: {food_data.iloc[0]['Cuisine']}\n"
            f"🥗 Ingredients: {food_data.iloc[0]['TranslatedIngredients']}\n"
            f"📝 Preparation: {food_data.iloc[0]['TranslatedInstructions']}\n"
            f"🔗 Recipe URL: {food_data.iloc[0]['URL']}"
        )
    else:
        return None  # Return None instead of a string for better handling

def get_chat_response(text):
    """Generate chatbot response using either the dataset or DialoGPT."""
    text = preprocess_text(text)

    # ✅ Check if it's a food-related query
    food_info = search_food_info(text)
    if food_info:  
        return food_info

    # ✅ Use DialoGPT for general responses
    new_user_input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors='pt')
    
    # Retrieve previous conversation history safely
    chat_history_ids = session.get('chat_history_ids', [])
    chat_history_tensor = torch.LongTensor(chat_history_ids) if chat_history_ids else torch.zeros((1, 0), dtype=torch.long)
    
    bot_input_ids = torch.cat([chat_history_tensor, new_user_input_ids], dim=-1)
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    
    # ✅ Convert tensor to a list before storing in session
    session['chat_history_ids'] = chat_history_ids.tolist()

    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response.strip() or "I didn't understand that. Can you rephrase?"

if __name__ == '__main__':
    app.run(debug=True, port =8001)
