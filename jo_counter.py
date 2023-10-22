import streamlit as st
import os
import datetime
import time
# set local timezone to Paris
os.environ["TZ"] = "Europe/Paris"

# show remaining days before the olympics in Paris
START_DATETIME = datetime.datetime(2024, 7, 26, 0, 0, 0)  # date and time of the opening of the olympics in Paris

# show a big counter updating each second

def remaining_time():
    """Returns the remaining time before the olympics in Paris
    including days, hours, minutes and seconds"""
    now = datetime.datetime.now()
    remaining = START_DATETIME - now
    return remaining


def main():
    """Main function of the app"""

    # st.title("Countdown to the Paris 2024 Olympic Games 🏅")

    # center the title
    st.markdown("<h1 style='text-align: center;'>Countdown to the Paris 2024 Olympic Games 🏅</h1>", unsafe_allow_html=True)

    remaining = remaining_time()

    # add some space
    st.write("")
    st.write("")


    placeholder = st.empty()
    while remaining.days > 0:
        remaining = remaining_time()

        placeholder.markdown(f"<h1 style='text-align: center;'>{remaining.days} days, {remaining.seconds // 3600} hours, {remaining.seconds // 60 % 60} minutes, {remaining.seconds % 60} seconds</h1>", unsafe_allow_html=True)
        
        time.sleep(1)
        placeholder.empty()
    st.balloons()

if __name__ == "__main__":
    main()