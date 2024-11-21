import streamlit as st

# Sidebar Navigation
def sidebar_navigation():
    st.sidebar.title("Navigation")
    options = ["Home", "About Me", "Projects", "Experience", "Skills", "Contact", "Download CV"]
    return st.sidebar.radio("Go to", options)

# Home Page
def home():
    st.title("Welcome to Shedrack Wambua's Portfolio")
    st.image("profile.jpeg", width=150, caption="Shedrack Wambua")  # Replace with your profile image
    st.markdown("""
        ### Hi, I'm Shedrack Wambua
        A passionate **Computer Scientist** specializing in **AI**, **Machine Learning**, **Web Development**, and **Data Science**.
        I thrive on solving complex problems and building innovative solutions that impact lives positively.
    """)

# About Me
def about_me():
    st.title("About Me")
    st.image("iot.jpg", caption="Innovator | Problem Solver | Engineer, Technologist")  # Replace with an image
    st.markdown("""
        Hello! My name is **Shedrack Wambua**, and I'm currently pursuing a **Bachelor of Science in Computer Science** 
        at Kabarak University, graduating in **2025**. I am a dedicated problem-solver with a flair for learning and 
        applying new technologies.

        - **Certifications**:  
          - Cybersecurity Certificate (Coursera)  
          - Data Science Certificate (IBM)  

        - **What I Bring**:  
          
          - A solid foundation in programming languages and software development.  
          - Proficiency in machine learning frameworks and web development tools.  
          - A passion for creating user-friendly applications and AI-driven systems.  

        In addition to my technical skills, I am an avid believer in collaboration, continuous learning, and 
        the transformative power of technology.
    """)

# Projects Section
def projects():
    st.title("Projects")
    st.image("iot.jpg", caption="Innovator | Problem Solver | Engineer, Technologist")  # Replace with an image

    projects_data = [
        {"name": "AI Virtual Assistant", "desc": "Developed an AI assistant for Ekaita Financial Consultancy to enhance client interactions.", "link": "#"},
        {"name": "Personal Finance Dashboard", "desc": "Created a web app to aggregate and visualize financial data, providing insights for users.", "link": "#"},
        {"name": "Online Code Compiler", "desc": "Built a web platform for coding, compiling, and judging solutions with real-time feedback.", "link": "#"},
        {"name": "News Feed App", "desc": "Aggregated and displayed news using RSS feeds, applying NLP for summarization.", "link": "#"},
        {"name": "Speech-Enabled Chatbot", "desc": "Developed a voice-based chatbot using Python's `speech_recognition` and `pyttsx3` libraries.", "link": "#"},
        {"name": "Twitter Bot", "desc": "Automated a bot to tweet random Martin Luther King Jr. quotes using Python and the Twitter API.", "link": "#"},
        {"name": "Mango Leaf Disease Classifier", "desc": "Built a TensorFlow-based app to classify diseases from mango leaf images.", "link": "#"},
        {"name": "Rackafritech Website", "desc": "Designed a website showcasing tech solutions with Firebase integration for backend.", "link": "#"},
        {"name": "Construction Experts Platform", "desc": "Developed a website for plumbing and construction services with video and image galleries.", "link": "#"},
        {"name": "iot projects", "desc": "Developed different iot projects including smart waste project", "link": "#"},

    ]
    for project in projects_data:
        st.markdown(f"""
        ### {project['name']}
        {project['desc']}
        [View Project]({project['link']})
        """)

# Experience Section
def experience():
    st.title("Experience")
    experiences = [
        {
            "role": "AI Virtual Assistant Developer",
            "company": "Ekaita Financial Consultancy",
            "period": "2024 – Present",
            "description": "Developed an AI-powered virtual assistant to enhance client interactions and streamline customer service."
        },
        {
            "role": "Web Developer",
            "company": "Freelance",
            "period": "2023 – Present",
            "description": "Created responsive web applications, including dashboards and social media-like platforms, using React and Django."
        },
        {
            "role": "Machine Learning Engineer",
            "company": "Freelance",
            "period": "2022 – 2024",
            "description": "Developed classification models for disease detection and gambling outcome predictions."
        },
        {
            "role": "Cybersecurity Intern",
            "company": "Coursera Certification Projects",
            "period": "2022",
            "description": "Learned and implemented best practices in data security and ethical hacking."
        },
        {
            "role": "Cybersecurity Intern",
            "company": "Coursera Certification Projects",
            "period": "2022",
            "description": "Learned and implemented best practices in data security and ethical hacking."
        }
    ]
    for exp in experiences:
        st.markdown(f"""
        **{exp['role']}**  
        **{exp['company']}**  
        *{exp['period']}*  
        {exp['description']}  
        """)

# Skills Section
def skills():
    st.title("Skills")
    st.markdown("### Programming Languages")
    skills_data = {
        "Python": 0.9,
        "JavaScript": 0.85,
        "C#": 0.8,
        "HTML/CSS": 0.9,
        "Django": 0.8,
        "React": 0.75,
        "TensorFlow": 0.7,
        "Flutter": 0.6,
        "Streamlit": 0.8,
    }
    for skill, proficiency in skills_data.items():
        st.markdown(f"**{skill}**")
        st.progress(proficiency)

# Contact Section
def contact():
    st.title("Contact")
    st.markdown("""
        If you'd like to get in touch, feel free to reach out:  
        - **Email**: [shedrackwambu40@gmail.com](mailto:shedrackwambu40@gmail.com)  
        - **Phone**: +254 727 177 155  
        - **GitHub**: [github.com/WambuaRack](https://github.com/WambuaRack)  
        - **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/shedrack-wambua-7752b8255/)  
    """)

# Download CV
def download_cv():
    st.title("Download CV")
    with open("CV.pdf", "rb") as file:  # Replace with your actual CV file path
        btn = st.download_button(
            label="Download CV",
            data=file,
            file_name="Shedrack_Wambua_CV.pdf",
            mime="application/pdf",
        )
    if btn:
        st.success("Your CV has been downloaded successfully!")

# Main Application
def main():
    option = sidebar_navigation()

    if option == "Home":
        home()
    elif option == "About Me":
        about_me()
    elif option == "Projects":
        projects()
    elif option == "Experience":
        experience()
    elif option == "Skills":
        skills()
    elif option == "Contact":
        contact()
    elif option == "Download CV":
        download_cv()

if __name__ == "__main__":
    main()
