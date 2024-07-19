# Imports
from flask import Flask, render_template, request, redirect, url_for
from g4f.client import Client
from g4f.Provider import You
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Print Input
def printInput(input):

    client = Client()
    prompt = "Give me 5 fun facts about the following topic: " + input
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        provider=You, 
        messages=[{"role": "user", "content": prompt}],
    )
    print(response.choices[0].message.content)

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