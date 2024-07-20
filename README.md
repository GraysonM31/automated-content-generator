# Project Title

This repository contains an application built using Python and Flask which utilizes generative AI for automated content generation.

## Description

Automated Content Generator
Developed by Kayden Chung and Grayson Mongru

### Setup and Execution

* Clone the Repository
```
git clone https://github.com/GraysonM31/automated-content-generator.git
```
* Allow Windows to Run Scripts
```
Set-ExecutionPolicy Unrestricted -Scope Process
```
* Create Virtual Environment
```
python -m venv .venv
```
* Activate Virtual Environment
#### Windows:
```
.venv\Scripts\activate
```
#### MacOS and Linux:
```
source .venv/bin/activate
```
* Install Required Dependencies
```
pip install -r requirements.txt
```
* Run the Flask Application
```
flask --app flaskr:app run --debug
```