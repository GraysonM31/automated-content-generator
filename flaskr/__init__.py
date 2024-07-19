# Imports
from flask import Flask, render_template, request, redirect, url_for

# Print Input
def printInput(input):
    print("Input: " + input)

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