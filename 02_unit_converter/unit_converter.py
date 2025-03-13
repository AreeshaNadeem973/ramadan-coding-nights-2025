import streamlit as st

# Function to perform unit conversion
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,  # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000,   # 1 kilometer = 1000 meters
        "gram_kilogram": 0.001,    # 1 gram = 0.001 kilogram
        "kilogram_gram": 1000      # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"  # Generate a key based on input & output units

    if key in conversions:
        return value * conversions[key]
    elif unit_from == unit_to:
        return value  # If same units are selected, return the same value
    else:
        return "❌ Conversion not supported"

# Streamlit UI
st.title("🌍 Unit Converter")
st.write("Convert the Value!")

# Input field for the value
value = st.number_input("Enter the value:", min_value=1.0, format="%.4f")

# Dropdowns to select units
unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram"])

# Convert button
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.success(f"**Converted value:** {result}")

