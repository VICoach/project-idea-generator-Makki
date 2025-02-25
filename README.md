# Project Idea Generator

Generate tailored project ideas based on your skills and interests.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setting Up the Project](#setting-up-the-project)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Activate the Virtual Environment](#activate-the-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Create a .env File](#create-a-env-file)
- [Testing Groq Agent](#testing-groq-agent)
  - [Start the Groq Agent](#start-the-groq-agent)
  - [Start the Groq WebSocket](#start-the-groq-websocket)
- [Run the Streamlit App](#run-the-streamlit-app)
- [License](#license)

## Description

The **Project Idea Generator** is a tool designed to generate project ideas tailored to your skills and interests. By providing a set of keywords related to your experience, the app will suggest ideas for projects that you can explore and build, helping you get started on your next big project.

## Features

- Generate project ideas based on skills and interests.
- Integration with Groq for advanced AI-powered suggestions.
- Simple interface built with Streamlit.
- Easy setup with minimal dependencies.

## Technologies Used

- **Python**: For backend logic and interaction with the Groq agent.
- **Streamlit**: For the frontend to provide a simple UI.
- **Groq**: For generating AI-powered project ideas.

## Setting Up the Project

### Create a Virtual Environment

First, create a virtual environment to isolate the dependencies:

```bash
python -m venv venv
```
### Activate the Virtual Environment

#### On Windows:

```bash
.\venv\Scripts\activate
```

#### On macOS and Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

Install the required Python dependencies listed in requirements.txt:

```bash
pip install -r requirements.txt
```
### Create a .env File
Create a .env file in the root directory of your project and add the following variables:

```env
MODEL=your_model_name
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_groq_model
```
Replace your_model_name, your_groq_api_key, and your_groq_model with your specific details.

## Testing Groq Agent
### Start the Groq Agent
To start the Groq agent, run the following command:

```bash

python groq/agents.py
```
### Start the Groq WebSocket
To start the WebSocket for communication, run:

```bash
python groq/ws.py
```
## Run the Streamlit App
Finally, to run the Streamlit app, use the following command:

```bash
streamlit run app/app.py
```
This will start the app, and you can interact with it in your web browser to generate project ideas.
