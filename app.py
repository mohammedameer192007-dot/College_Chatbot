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

    elif "course" in question.lower() or "courses" in question.lower() or "ug courses" in question.lower() or "available courses" in question.lower() or "pg courses" in question.lower():
        st.write("Available courses: AI & DS, CSE, ECE, EEE, Mechanical, Available PG courses: M.E in Computer Science and Engineering, M.E in Industrial Safety Engineering, M.B.A.")

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
  
    elif "college website" in question.lower() or "website" in question.lower() or "official website" in question.lower():
        st.write("Our college website is https://alameen.ac.in/contact-us/")
  
    elif "college email" in question.lower() or "email" in question.lower() or "official email" in question.lower():
        st.write("You can contact the college via email at alameenengg@yahoo.com.")
  
    elif "office timing" in question.lower() or "office hours" in question.lower() or "working hours" in question.lower():
        st.write("Our college office timing is 9:00 AM to 4:00 PM.")

    elif "department" in question.lower() or "departments" in question.lower() or "available departments" in question.lower():
        st.write("""
        📚 Departments

        • Artificial Intelligence & Data Science (AI & DS)
        HOD: Dr. Arulmozhi
        Focus: Artificial Intelligence, Machine Learning, Deep Learning, NLP and Data Analytics.

        • Computer Science and Engineering (CSE)
        HOD: Dr. Afiya
        Focus: Programming, Software Engineering, Computer Networks and Algorithms.

        • Electronics and Communication Engineering (ECE)
        HOD: Dr. Sadhicbasa
        Focus: Electronic Devices, Communication Systems, Signal Processing and Embedded Systems.

        • Electrical and Electronics Engineering (EEE)
        HOD: Dr. Vimal
        Focus: Power Systems, Electrical Machines, Power Electronics and Renewable Energy.

        • Mechanical Engineering
        HOD: Dr. Santhosh
        Focus: Thermodynamics, Fluid Mechanics, Manufacturing Processes and Robotics.
        """)
        
    elif "nba accreditation" in question.lower() or "nba" in question.lower() or "accreditation" in question.lower():
        st.write("Our college is accredited by the National Board of Accreditation (NBA) for its various programs, ensuring quality education and continuous improvement for ECE & EEE Departments.")

    elif "naac grade " in question.lower() or "naac" in question.lower() or "grade" in question.lower():
        st.write("Our college has been awarded an 'A' grade by the National Assessment and Accreditation Council (NAAC), reflecting our commitment to academic excellence and quality education.")

    elif "autonomous status" in question.lower() or "automous or not " in question.lower() or "autonomous" in question.lower():
        st.write("Yes, Al Ameen Engineering College is an Autonomous Institution ")

    elif "affiliated university" in question.lower() or "university" in quetion.lower()  or "affiliation" in question.lower():
        st.write("Al Ameeen College is an Autonomous Instition affilicated with Anna University,Chennai ")  

    elif ("admission apply" in question.lower() or"admission" in question.lower() or "eligibility" in question.lower() or
      "documents" in question.lower() or
      "admission process" in question.lower() or
      "online admission" in question.lower() or
      "offline admission" in question.lower() or
      "last date" in question.lower() or
      "lateral entry" in question.lower() or
      "management quota" in question.lower() or
      "counselling" in question.lower() or
      "admission office" in question.lower()):

        st.write("""
        📌 Admission Information

        • Eligibility: Pass in 10+2 with the required marks.
        • Required Documents: 10th & 12th Mark Sheets, TC, Community Certificate (if applicable), Aadhaar Card and Passport Size Photos.
        • Admission Process: Apply through TNEA Counselling or directly at the college.
        • Online Admission: Available through the college website.
        • Offline Admission: Visit the college admission office.
        • Lateral Entry: Available for eligible diploma students.
        • Management Quota: Available. Contact the admission office.
        • Admission Last Date: Visit the college website or admission office for updates.
        • Admission Office Timing: 9:00 AM to 4:00 PM.
        """)

    elif ("campus facilities" in question.lower() or
      "facility" in question.lower() or
      "facilities" in question.lower() or
      "computer lab" in question.lower() or
      "lab" in question.lower() or
      "science lab" in question.lower() or
      "auditorium" in question.lower() or
      "sports" in question.lower() or
      "gym" in question.lower() or
      "medical" in question.lower() or
      "parking" in question.lower() or
      "cctv" in question.lower()):

         st.write("""
        📌 Campus Facilities

        • Smart Classrooms: Smart classrooms are available.
        • Computer Labs: CC1, CC2, CC3 and CC4 computer labs are available.
        • Science Labs: Well-equipped Physics Lab and Chemistry Lab.
        • Auditorium: A large auditorium is available for seminars and events.
        • Sports: Sports facilities are available for students.
        • Gym: Gym facility is available for boys.
        • Medical Facility: Basic medical facility is available on campus.
        • Parking: A spacious parking area is available for students and staff.
        • CCTV: CCTV cameras are installed throughout the college campus for safety and security.
        """)
        
    else:
        st.write("Sorry, I don't know the answer.")

st.markdown("---")
st.caption("🎓 College Chatbot Mini Project / Developed by Mohammed Ameer")