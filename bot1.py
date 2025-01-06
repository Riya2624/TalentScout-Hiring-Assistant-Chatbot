import streamlit as st
from langchain_groq import ChatGroq

# Initialize the ChatGroq LLM model
llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0.5,
    max_tokens=500,
    timeout=10,
    max_retries=2,
    api_key="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",
)

# Streamlit App
def main():
    # App Title
    st.title("TalentScout Hiring Assistant")
    st.write("Welcome! I am here to assist with your initial candidate screening process.")

    # Information Gathering
    st.header("Candidate Information")
    with st.form("candidate_form"):
        full_name = st.text_input("Full Name", placeholder="Enter your full name")
        email = st.text_input("Email Address", placeholder="Enter your email address")
        phone = st.text_input("Phone Number", placeholder="Enter your phone number")
        experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
        position = st.text_input("Desired Position", placeholder="Enter the position you are applying for")
        location = st.text_input("Current Location", placeholder="Enter your current location")
        tech_stack = st.text_area("Tech Stack", placeholder="e.g., Python, Django, React, etc.")

        submitted = st.form_submit_button("Submit")

    if submitted:
        if not full_name or not email or not phone or not tech_stack:
            st.error("Please fill in all required fields.")
        else:
            st.success("Thank you for providing your details!")
            st.write("### Candidate Summary")
            st.write(f"- **Full Name:** {full_name}")
            st.write(f"- **Email:** {email}")
            st.write(f"- **Phone Number:** {phone}")
            st.write(f"- **Years of Experience:** {experience}")
            st.write(f"- **Desired Position:** {position}")
            st.write(f"- **Current Location:** {location}")
            st.write(f"- **Tech Stack:** {tech_stack}")

            # Generate technical questions
            st.write("\n### Generated Technical Questions")
            prompt = (
                f"You are an interviewer. Generate 3-5 technical interview questions "
                f"for the following tech stack: {tech_stack}."
            )
            try:
                with st.spinner("Generating technical questions..."):
                    response = llm.invoke([("system", prompt)])
                    st.write(response.content)
            except Exception as e:
                st.error(f"Error: Unable to generate questions. {str(e)}")

    # Graceful Exit
    st.subheader("End Conversation")
    if st.button("End Chat"):
        st.write("Thank you for using the TalentScout Hiring Assistant. Best of luck!")

# Run the Streamlit App
if __name__ == "__main__":
    main()
