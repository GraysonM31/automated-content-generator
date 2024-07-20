# Imports
from flask import Flask, render_template, request
from backend.gpt import askGPT
from backend.videos import getStockVideos

# Creating Flask App
app = Flask(__name__)

# Flask App Handling
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        # Request Input Field
        input = request.form['input']

        # Get Script from GPT
        script = askGPT(input)
        # Get Stock Videos
        getStockVideos(input, 5)

        # Print Script
        print("\nScript:\n\n" + script + "\n")

    return render_template('index.html')

# Main
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
