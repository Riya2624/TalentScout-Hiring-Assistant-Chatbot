# TalentScout-Hiring-Assistant-Chatbot

## Project Overview
The **TalentScout Hiring Assistant Chatbot** is designed to streamline the recruitment process by assisting in the initial screening of candidates. It collects essential information, such as personal details and technical expertise, and generates tailored technical interview questions based on the candidate’s declared tech stack. This project demonstrates the capabilities of **Llama-based Large Language Models (LLMs)** and effective prompt engineering.

---

## Installation Instructions

### Prerequisites
- Python 3.9 or later
- `pip` package manager
- Access to **ChatGroq API** (obtain an API key)

### Installation Steps
1. **Clone the repository or extract the zip file**:
   ```bash
   git clone https://github.com/Riya2624/talentscout-chatbot.git
   cd talentscout-chatbot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your ChatGroq API Key**:
   Replace `your_api_key_here` in the `hiring_assistant.py` file with your API key.

4. **Run the Streamlit app**:
   ```bash
   streamlit run bot1.py
   ```

5. **Access the app in your browser**:
   Navigate to the provided URL, e.g., `http://localhost:8501`.

---

## Usage Guide
1. **Launch the Application**:
   Open the Streamlit app in your browser.

2. **Fill in Candidate Information**:
   Provide details such as:
   - Full Name
   - Email Address
   - Phone Number
   - Years of Experience
   - Desired Position
   - Current Location
   - Tech Stack (e.g., Python, Django, React)

3. **Generate Technical Questions**:
   Submit the form to receive customized technical questions tailored to the specified tech stack.

4. **End the Chat**:
   Use the "End Chat" button to gracefully conclude the interaction.

---

## Technical Details

### Libraries Used
- **Streamlit**: Frontend for user interaction.
- **LangChain**: For interfacing with the ChatGroq API.
- **ChatGroq LLM**: Backend for natural language understanding and question generation.

### Model Details
- Model: **Llama 3.1 70b Versatile** (via ChatGroq API)
- Key Parameters:
  - `temperature=0` for deterministic responses
  - `max_tokens=500` for concise outputs
  - `max_retries=2` for robust API interactions

### Architectural Highlights
- **Prompt Design**: Structured prompts to collect candidate details and generate relevant technical questions.
- **Context Management**: Maintains the conversation’s flow for a coherent user experience.
- **Error Handling**: Provides fallback messages for invalid inputs or API errors.

---

## Prompt Design

### Information Gathering
- **System Prompt**:
  > "You are a helpful assistant for initial candidate screening."
- **User Input Example**:
  > "Full Name: John Doe\nTech Stack: Python, React"

### Technical Question Generation
- Example Prompt:
  > "Generate 3-5 technical interview questions for the following technologies: Python, Django, React."

---

## Challenges & Solutions

1. **Error Handling for Invalid Inputs**:
   - Validation checks ensure all required fields are filled.
   - Fallback responses handle unexpected inputs gracefully.

2. **Latency Optimization**:
   - Reduced response time by optimizing API parameters.
   - Implemented retries for intermittent API failures.

3. **Scalability**:
   - Modular code structure supports adding new features like sentiment analysis or multilingual support.

---

## Optional Enhancements

- **Advanced Features**:
  - Sentiment analysis to gauge candidate emotions.
  - Multilingual support for broader accessibility.
  - Personalized responses based on user history.

- **UI Enhancements**:
  - Custom CSS styling for a polished interface.
  - Interactive elements like progress indicators.

- **Performance Optimization**:
  - Parallel processing for multiple user interactions.

---

## Deliverables

### Source Code
- A complete, well-documented codebase, including:
  - `bot1.py`: Main application file.
  - `requirements.txt`: Dependencies.

### Documentation
- Comprehensive README (this file).
- Inline comments and docstrings within the code.

### Demo
- **Live Demo (Optional)**: Hosted on AWS/GCP/Streamlit Cloud.
- **Video Walkthrough**: A short video showcasing the chatbot’s features and interactions.

---

## Example Commands

### Start the App
```bash
streamlit run bot1.py
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

This README provides all necessary details to set up, run, and extend the chatbot application. For questions or issues, feel free to contact [rtriya2001@gmail.com].

