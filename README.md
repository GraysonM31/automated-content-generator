# Automated Content Generation

This repository contains a Python Flask application that utilizes Bing AI for automated content generation. The application provides an API for generating content based on user input.

## Features

- Generate content using Bing AI
- Flask-based API for easy integration
- Customizable content generation parameters

## Requirements

- Python 3.7+
- Flask
- Requests
- Any additional dependencies for Bing AI API access

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/automated-content-generation.git
    cd automated-content-generation
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables for Bing AI API access:
    ```sh
    export BING_API_KEY='your_bing_api_key'
    ```

## Usage

1. Run the Flask application:
    ```sh
    flask run
    ```

2. The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### Generate Content

- **URL:** `/generate`
- **Method:** `POST`
- **Parameters:**
    - `prompt` (string): The text prompt for content generation.
    - `length` (integer): The desired length of the generated content.
- **Response:**
    ```json
    {
        "generated_content": "..."
    }
    ```

#### Example Request
```sh
curl -X POST http://127.0.0.1:5000/generate -H "Content-Type: application/json" -d '{"prompt": "Generate a story about AI", "length": 100}'
