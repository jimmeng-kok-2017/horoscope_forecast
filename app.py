import streamlit as st
import pyaztro

st.title("Welcome to the Daily Real-Time Horoscope Forecasting App")
st.write("")
st.write("")
st.sidebar.write("Have fun using this app!")
st.sidebar.subheader("Jim Meng Kok")
st.sidebar.markdown(
    'Please feel free to connect with me on LinkedIn: [www.linkedin.com/in/jimmengkok](www.linkedin.com/in/jimmengkok)')
st.sidebar.markdown('Medium: [https://medium.com/@jimintheworld](https://medium.com/@jimintheworld)')

astrology_choose = st.selectbox("What's your horoscope sign? (Please select from the dropdown menu)", ["", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])

if astrology_choose != "":
    lowercase_astrology_choose = astrology_choose.lower()
    horoscope = pyaztro.Aztro(sign=lowercase_astrology_choose)
    st.markdown("Today's Date: " + str(horoscope.current_date))
    st.markdown("Date Range Availability of the Forecast: " + str(horoscope.date_range[0]) + " to " + str(horoscope.date_range[1]))
    st.markdown("Your Horoscope Compatibility: " + str(horoscope.compatibility))
    st.markdown("Your Horoscope Lucky Number: " + str(horoscope.lucky_number))
    st.markdown("Your Horoscope Lucky Time: " + str(horoscope.lucky_time))
    st.markdown("Your Horoscope Lucky Colour: " + str(horoscope.color))
    st.markdown("Your Horoscope Mood: " + str(horoscope.mood))
    st.markdown("Your Horoscope Forecast: " + str(horoscope.description))