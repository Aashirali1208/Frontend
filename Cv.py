import streamlit as st

def generate_cv(name, email, phone, education, experience, skills, about):
    cv = f"""
    # Curriculum Vitae

    ## Personal Information
    - **Name:** {name}
    - **Email:** {email}
    - **Phone:** {phone}

    ## Education
    - {education}

    ## Experience
    - {experience}

    ## Skills
    - {skills}

    ## About Me
    {about}
    """

    return cv

# Streamlit App
st.title("CV Generator")

# User input
name = st.text_input("Full Name:")
email = st.text_input("Email:")
phone = st.text_input("Phone:")

education = st.text_area("Education:")
experience = st.text_area("Experience:")
skills = st.text_area("Skills:")
about = st.text_area("About Me:")

# Color customization
st.markdown(
    """
    <style>
    .css-1aumxhk {
        background-color: #3498db;
        color: #ffffff;
        padding: 0.5rem;
        margin-top: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("Generate CV"):
    cv = generate_cv(name, email, phone, education, experience, skills, about)
    st.markdown(cv, unsafe_allow_html=True)
