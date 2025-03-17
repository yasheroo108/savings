import streamlit as st

st.set_page_config(page_title="Budgeting Calculator | ISU 3", layout="centered")

st.title("Savings Calculator")
st.markdown("[Income Percentile Calculator](https://income-percentile.streamlit.app/)")

time = st.selectbox("How often do you plan on saving? Every...", ("day", "week", "month", "year"))

total = st.number_input("How much do you plan on saving (in dollars)?")

pledge = st.number_input(f"How much do you plan on saving every {time}?", min_value=0.0, step=1.0)

try:
    if time == "day":
        final = round((total/pledge), ndigits=2)
        st.success(f"You will reach your goal in {final} day(s).")

    if time == "week":
        final = round((total/pledge), ndigits=2)
        st.success(f"You will reach your goal in {final} week(s).")

    if time == "month":
        final = round((total/pledge), ndigits=2)
        st.success(f"You will reach your goal in {final} month(s).")

    if time == "year":
        final = round((total/pledge), ndigits=2)
        st.success(f"You will reach your goal in {final} year(s).")
    
except ZeroDivisionError:
    st.warning("Insert numbers accordingly.")

