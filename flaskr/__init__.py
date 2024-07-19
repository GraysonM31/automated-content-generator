# Imports
from flask import Flask, render_template, request, redirect, url_for
from g4f.client import Client
from g4f.Provider import You
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def parser(text):

    # Regular expression to match the facts
    facts = []
    lines = text.split("\n")

    current_fact = ''

    cleaned_facts = []


    for line in lines:
        # Check if the line starts with a number followed by a period
        if line.strip().startswith(tuple(f"{i}." for i in range(1, 6))):
            # If there is an ongoing fact, add it to the list
            if current_fact:
                facts.append(current_fact.strip())
            # Start a new fact
            current_fact = line.strip()
        elif line.strip():  # Continue appending to the current fact if the line is not empty
            current_fact += ' ' + line.strip()

    if current_fact:
        facts.append(current_fact.strip())

    for fact in facts:
        # Remove markdown asterisks and references
        cleaned_fact = fact
        if '**' in cleaned_fact:
            cleaned_fact = cleaned_fact.replace('**', '')
        if '[[' in cleaned_fact:
            cleaned_fact = cleaned_fact[:cleaned_fact.index(' [[')]
        cleaned_facts.append(cleaned_fact)

    print(cleaned_facts)


# Print Input
def printInput(input):

    client = Client()
    prompt = "Give me 5 fun facts about the following topic: " + input
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        provider=You, 
        messages=[{"role": "user", "content": prompt}],
      
    )

    newMessage = response.choices[0].message.content
    parser(newMessage)
    




# Creating Flask App
app = Flask(__name__)

# Flask App Handling
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        # Request Input Field
        input = request.form['input']
        # Method Calls
        printInput(input)

    return render_template('index.html')

# Main
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)