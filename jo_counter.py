import streamlit as st
import datetime
import pytz
import time

# set the timezone to Paris
paris_tz = pytz.timezone('Europe/Paris')

START_DATETIME = paris_tz.localize(datetime.datetime(2024, 7, 26, 0, 0, 0))

def remaining_time():
    """Renvoie le temps restant avant les Jeux Olympiques à Paris,
    y compris les jours, les heures, les minutes et les secondes"""

    # get the current time in Paris
    now = datetime.datetime.now(paris_tz)
    
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