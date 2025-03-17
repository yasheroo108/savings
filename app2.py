import streamlit as st

st.set_page_config(page_title="Budgeting Calculator | ISU 3", layout="centered")

st.title("Budgeting Calculator")
st.markdown("[Income Percentile Calculator](https://income-percentile.streamlit.app/)")

time = st.selectbox("How often do you plan on saving? Every...", ("day", "week", "month", "year"))

total = st.number_input("How much do you plan on saving (in dollars)?")

pledge = st.number_input(f"How much do you plan on saving every {time}?", min_value=0.0, step=1.0)

def format_time(periods, unit):
    if periods >= 100:
        return f"{round(periods / 100, 2)} century(ies)"
    elif periods >= 10:
        return f"{round(periods / 10, 2)} decade(s)"
    elif periods >= 1:
        return f"{round(periods, 2)} {unit}(s)"
    return f"{round(periods, 2)} {unit}(s)"

try:
    if pledge > 0:
        if time == "day":
            final_days = total / pledge
            st.success(f"You will reach your goal in {format_time(final_days / 365, 'year')}, which is about {format_time(final_days / 30, 'month')}, or {round(final_days, 2)} day(s).")
        
        elif time == "week":
            final_weeks = total / pledge
            final_days = final_weeks * 7
            st.success(f"You will reach your goal in {format_time(final_days / 365, 'year')}, which is about {format_time(final_days / 30, 'month')}, or {round(final_weeks, 2)} week(s).")
        
        elif time == "month":
            final_months = total / pledge
            st.success(f"You will reach your goal in {format_time(final_months / 12, 'year')}, or {round(final_months, 2)} month(s).")
        
        elif time == "year":
            final_years = total / pledge
            st.success(f"You will reach your goal in {format_time(final_years, 'year')}, or {round(final_years, 2)} year(s).")
    else:
        st.warning("Insert numbers accordingly.")
except ZeroDivisionError:
    st.warning("Insert numbers accordingly.")
