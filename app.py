import streamlit as st

st.set_page_config(page_title="College Chatbot", page_icon="🎓")

st.title("🎓 College Chatbot")
st.write("Welcome ! ask me anything about our college.")

st.sidebar.title("📋 Menu")
st.sidebar.write("You can ask about:")
st.sidebar.write("• Fees")
st.sidebar.write("• Courses")
st.sidebar.write("• Principal")
st.sidebar.write("• Placement")
st.sidebar.write("• Hostel")
st.sidebar.write("• Transport")
st.sidebar.write("• Library")
st.sidebar.write("• Canteen")
st.sidebar.write("• Scholarship")
st.sidebar.write("• Admission")
st.sidebar.write("• Contact")

name = st.text_input("👤 Enter your name")

if name:
    st.write("Hello,", name)

question = st.text_input("❓ Ask your question")
 
if st.button("🗑️ Clear"):
    st.rerun()
if question:

    if "fee" in question.lower() or "fees" in question.lower():
        st.write("College fees is ₹70,000 per year.")

    elif "course" in question.lower() or "courses" in question.lower():
        st.write("Available courses: AI & DS, CSE, ECE, EEE, Mechanical.")

    elif "principal" in question.lower() or "principal name" in question.lower() or "who is the principal" in question.lower() or "name of principal" in question.lower():
        st.write("Our Principal is Dr. A.M.J. Md Zubair Rahman.")

    elif "placement" in question.lower() or "placements" in question.lower() or "job" in question.lower():
        st.write("Our placement cell has a 90% placement record.")

    elif "college name" in question.lower() or "name of college" in question.lower():
        st.write("Our college name is Al Ameen Engineering College.")

    elif "location" in question.lower() or "where" in question.lower() or "address" in question.lower():
        st.write("Our college is located in Karundevan Palayam (Erode Modakurichi Main Road).")

    elif "timing" in question.lower() or "time" in question.lower() or "working hours" in question.lower():
        st.write("Our college timing is 9:00 AM to 4:00 PM.")

    elif "contact" in question.lower() or "phone" in question.lower() or "mobile" in question.lower() or "number" in question.lower():
        st.write("You can contact the college at +91 98420 22458, +91 96777 61786.")

    elif "hostel" in question.lower() or "hostels" in question.lower() or "girls hostel " in question.lower() or "boys hostel" in question.lower():
        st.write("We have separate hostels for boys and girls, near the college campus.")

    elif "transport" in question.lower() or "bus" in question.lower() or "buses" in question.lower():
        st.write("We have a college bus facility for students and staff.")
 
    elif "library" in question.lower() or "books" in question.lower() or "reading room" in question.lower():
        st.write("Our college has a well-equipped central library with a wide range of books and a reading room.")
 
    elif "canteen" in question.lower() or "food" in question.lower() or "mess" in question.lower():
        st.write("Our college has a canteen that serves a variety of food and beverages for students and staff.")
 
    elif "scholarship" in question.lower() or "scholarships" in question.lower() or "financial aid" in question.lower():
        st.write("Our college offers scholarships and financial aid to eligible students based on merit and need.")
 
    elif "admission" in question.lower() or "apply" in question.lower() or "how to apply" in question.lower():
        st.write("You can apply for admission through our college website or by visiting the college office in person.")
  
    elif "college website" in question.lower() or "website" in question.lower() or "official website" in question.lower():
        st.write("Our college website is https://alameen.ac.in/contact-us/")
  
    elif "college email" in question.lower() or "email" in question.lower() or "official email" in question.lower():
        st.write("You can contact the college via email at alameenengg@yahoo.com.")
  
    elif "office timing" in question.lower() or "office hours" in question.lower() or "working hours" in question.lower():
        st.write("Our college office timing is 9:00 AM to 4:00 PM.")
   
    else:
        st.write("Sorry, I don't know the answer.")

st.markdown("---")
st.caption("🎓 College Chatbot Mini Project / Developed by Mohammed Ameer")