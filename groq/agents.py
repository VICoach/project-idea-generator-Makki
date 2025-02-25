import asyncio
import websockets
import groq

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client
client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))

# Technical Interviewer Agent System Prompt
system_prompt = """
You are a project idea generator specializing in technical and innovative projects. Your task is to propose a project based on the user's interests and technical skills. Here's how you should proceed:
1. Understand the user's interests and skills: The project should align with the user’s current technical abilities and passions. Ask clarifying questions if necessary to ensure a good fit.
2. Provide a clear and actionable project idea: The idea should be feasible for the user to start, given their current expertise, and should have a tangible goal or outcome.
3. Outline the key features and functionality: Highlight the most important components and functionality the project should have, including technologies to use.
4. Suggest the technology stack: Recommend relevant technologies based on the project’s scope and the user’s skillset.
5. Explain the potential impact or value of the project: Explain how the project could solve a real-world problem, benefit the user, or serve a specific audience.
6. Encourage the user to reflect: Ask whether the project idea resonates with their goals or if any adjustments are needed.
7. Remember to maintain a positive and engaging tone throughout the conversation. Good luck!
"""
async def handle_connection(websocket, path=None):  
    # Send a welcome message
    await websocket.send("Welcome to the project idea generator! Let's begin.")

    # Initialize the conversation with the system prompt
    messages = [{"role": "system", "content": system_prompt}]

    async for message in websocket:
        # Add user message to the conversation
        messages.append({"role": "user", "content": message})

        # Get response from Groq's LLM
        response = client.chat.completions.create(
            model=os.getenv("GROQ_MODEL"),
            messages=messages
        )

        # Extract the LLM's reply
        llm_reply = response.choices[0].message.content

        # Send the reply back to the client
        await websocket.send(llm_reply)

        # Add the LLM's reply to the conversation
        messages.append({"role": "assistant", "content": llm_reply})

# Start the WebSocket server
async def start_server():
    async with websockets.serve(
        handle_connection, "localhost", 8765,
        ping_interval=3600,  
        ping_timeout=3600):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  

# Run the server
asyncio.run(start_server())
