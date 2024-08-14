#BigGPT, a personal chatbot that is on device and trained for you.

import csv
import os

# Define the CSV file path
csv_file = 'chatbot_data.csv'

# Function to load existing data from the CSV file
def load_data(file_path):
    prompts = []
    responses = []
    if os.path.exists(file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    prompts.append(row[0].strip())
                    responses.append(row[1].strip())
    return prompts, responses

# Function to save data to the CSV file
def save_data(file_path, prompts, responses):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for prompt, response in zip(prompts, responses):
            writer.writerow([prompt, response])

# Main chatbot function
def main_chatbot(prompts, responses):
    while True:
        user_input = input("You: ").strip()
        user_input_lower = user_input.lower()
        
        if user_input_lower in prompts:
            index = prompts.index(user_input_lower)
            print(f"BigGPT: {responses[index]}")
            
        elif user_input_lower == "exit":
            print("Exiting....")
            exit()
            
        else:
            print("BigGPT: I do not know. Yet.")


# Training chatbot function
def training_chatbot(prompts, responses):
    while True:
        print("\nTraining Chatbot")
        user_input = input("You: ").strip()
        user_input_lower = user_input.lower()
        
        if user_input_lower in prompts:
            index = prompts.index(user_input_lower)
            print(f"Training Bot: The current response is '{responses[index]}'.")
            
        elif user_input_lower == "exit":
            print("Exiting....")
            exit()
        else:
            print("Training Bot: I don't know the answer. Let's add this to the training data.")
            new_response = input("Training Bot: What should I respond? ").strip()
            prompts.append(user_input_lower)
            responses.append(new_response)
            save_data(csv_file, prompts, responses)
            print("Training Bot: Thank you! I've added this new input to the training data.")

# Load existing data
prompts, responses = load_data(csv_file)

# Choose which chatbot to run
print("Select chatbot mode: 1) Main Chatbot 2) Training Chatbot: ")
choice = input().strip()

if choice == '1':
    main_chatbot(prompts, responses)
elif choice == '2':
    training_chatbot(prompts, responses)
else:
    print("Invalid choice. Exiting.")
