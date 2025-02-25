import streamlit as st
import os
import sys

# Add the parent directory to the system path to allow imports from the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import necessary modules and functions
from src.crew import ProjectAdvisor
from streamlitHelpers import create_sidebar, create_streamlit_UI, create_streamlit_callback

# Set the Streamlit page configuration to wide layout
st.set_page_config(layout="wide")

def main():
    # Create the Streamlit UI with a title and description
    create_streamlit_UI("Project Idea Generator", "Generate tailored project ideas based on your skills and interests.")

    # Create a text input field for the user to enter their interests and skills
    user_input = st.text_input("Enter your skills and interests (e.g., Machine Learning, Web Development):", "Machine Learning, Python, Web Development")
    # Create a button for generating the project idea
    generate_button = st.button("Generate Project Idea")

    # If the generate button is clicked and there is user input
    if generate_button and user_input:
        # Prepare the inputs for generating a project idea
        inputs = {"skills_and_interests": user_input}
        
        # Create an instance of the Demo class and get the project idea generation crew
        crew_instance = ProjectAdvisor().crew()
        # Display a header for the crew execution log
        st.write("### Project Idea Generation Log")
        
        try:
            # Execute the crew and capture the output
            result = crew_instance.kickoff(inputs=inputs)
            
            # Display the generated project idea in the Streamlit UI
            st.write("### Generated Project Idea")
            st.markdown(result)
        except Exception as e:
            # Display an error message if an exception occurs
            st.error(f"An error occurred: {e}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
