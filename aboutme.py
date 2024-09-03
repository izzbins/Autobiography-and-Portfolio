import streamlit as st

# Title and Sidebar Navigation
st.title("Francis Vinz Racaza - Portfolio")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me", "Portfolio"])

# About Me Page
if page == "About Me":
    st.write("## About Me")
    st.write("I'm **Francis Vinz Racaza**, a passionate software developer with experience in both frontend and backend development.")
    st.write("### Details:")
    st.write("- **Age:** 23")
    st.write("- **Gender:** Male")
    st.write("- **School:** Cebu Institute of Technology - University")
    st.write("- **Hobby:** Photo and video editing")

# Portfolio Page
elif page == "Portfolio":
    st.write("## Portfolio")
    
    st.write("### 1. Student Organization System")
    st.write("- **Role:** Software Developer")
    st.write("- **Location:** Cebu City")
    st.write("- **Duration:** January – May 2023")
    st.write("- **Description:** Designed and implemented a Student Organization System using Java Swing, focusing on creating an intuitive user interface for managing student activities. Integrated Java JDBC to connect the system with a database, ensuring seamless data management and efficient handling of student records.")
    
    st.write("### 2. Internet Voucher System")
    st.write("- **Role:** Frontend & Backend Developer")
    st.write("- **Location:** Cebu City")
    st.write("- **Duration:** September – December 2023")
    st.write("- **Description:** Developed the frontend using Python, focusing on a clean and user-friendly design. Built the backend using Django, ensuring reliable and secure management of voucher operations.")
    
    st.write("### 3. Wheels On Go (Rent a Car System)")
    st.write("- **Role:** Frontend Developer")
    st.write("- **Location:** Cebu City")
    st.write("- **Duration:** January – May 2024")
    st.write("- **Description:** Assisted in developing the front end of the website using ReactJS, contributing to a responsive and visually appealing user interface. Worked with a team to implement and test new features, ensuring seamless integration with the current system.")

