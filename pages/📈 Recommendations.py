from styles import *
from backend import *
import smtplib

streamlit_style()

if st.session_state['validated'] == True:
    st.subheader("Select an Item to Generate Recommendations")
    option = st.selectbox(' ', options=names)
    label = show_recommendations(option)

    st.write(label)

    button = st.button("Email Customer")

    if button:
        st.success("Email sent to customer")
        # text = label.split(":")[1].split("\n")[0]
        # server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.starttls()
        # server.login('flashstore123098@gmail.com', 'maxflash1')
        # server.sendmail('aliamkh123007@gmail.com', f'You bought {option}, if you buy {text}, you will get a discount of 10% off', 'Subject: Flash Store')

else:
    st.title("Kindly Log In!!")

