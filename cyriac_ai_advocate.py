import streamlit as st

# Title and introduction
st.title("Cyriac's AI Advocate")
st.markdown("""
Welcome to Cyriac Kurian's AI Advocate chatbot!  
I’m here to demonstrate why Cyriac is an excellent candidate for the role.  
Ask me about Cyriac’s:
- Role and career aspirations
- Mindwise project contributions
- Technical skills and expertise
- Problem-solving abilities
- Alignment with the position
""")

# Input from the user
user_input = st.text_input("Type your question below:")

# Knowledge base
knowledge_base = {
    "role": "Cyriac Kurian is a software engineering student at UMBC with hands-on experience in AI and software development projects. He has contributed significantly to the Mindwise app and is passionate about using technology to create meaningful solutions.",
    "mindwise": "Mindwise is an AI-driven mental health companion app that Cyriac helped develop. He worked on mood tracking, chatbot integration, and personalized recommendations, focusing on cross-platform compatibility and seamless user experiences.",
    "skills": "Cyriac is proficient in Python, React Native, Django/FastAPI, and Google Cloud Platform. He has experience building scalable back-end systems, implementing user-friendly front-end designs, and optimizing AI models.",
    "problem-solving": "In the Mindwise project, Cyriac tackled challenges like integrating video datasets and fine-tuning AI models. He demonstrated resourcefulness by refining preprocessing techniques and experimenting with advanced architectures to improve performance.",
    "career": "Cyriac is passionate about creating meaningful technology solutions. He values innovation, teamwork, and solving real-world problems. This role aligns with his goal to develop impactful software applications and advance his expertise.",
    "alignment": "Cyriac is an excellent match for this position because he brings a unique blend of technical expertise, problem-solving capabilities, and a user-centric mindset. His work on the Mindwise project demonstrates his ability to design, develop, and deploy innovative AI-driven applications, making him well-suited for roles requiring technical proficiency, adaptability, and passion for impactful solutions.",
    "challenges": "Cyriac has overcome significant challenges, such as resolving dataset compatibility issues in the Mindwise project and optimizing AI models for accuracy. These experiences highlight his ability to handle complex problems effectively.",
}

# Simple chatbot logic
if user_input:
    user_input_lower = user_input.lower()
    if "role" in user_input_lower:
        response = knowledge_base["role"]
    elif "mindwise" in user_input_lower:
        response = knowledge_base["mindwise"]
    elif "skills" in user_input_lower:
        response = knowledge_base["skills"]
    elif "problem-solving" in user_input_lower or "problem" in user_input_lower:
        response = knowledge_base["problem-solving"]
    elif "career" in user_input_lower:
        response = knowledge_base["career"]
    elif "alignment" in user_input_lower or "position" in user_input_lower:
        response = knowledge_base["alignment"]
    elif "challenge" in user_input_lower or "difficulties" in user_input_lower:
        response = knowledge_base["challenges"]
    else:
        response = "I'm sorry, I don't have information on that. Could you ask something related to Cyriac's skills, projects, or experience?"
    
    st.write(f"**AI Advocate**: {response}")

# Footer
st.markdown("Feel free to ask me more questions to learn about Cyriac Kurian's expertise and fit for the role!")



