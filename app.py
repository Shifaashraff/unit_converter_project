import streamlit as st

# Set page title, icon, and layout
st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    /* Main title styling */
    h1 {
        color: #4CAF50;
        text-align: center;
        font-size: 2.5rem;
    }

    /* Header styling */
    h2 {
        color: #4CAF50;
        font-size: 2rem;
    }

    /* Button styling */
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }

    .stButton button:hover {
        background-color: #45a049;
    }

    /* Input field styling */
    .stNumberInput input {
        border-radius: 5px;
        border: 0px solid #4CAF50;
    }

    /* Select box styling */
    .stSelectbox div {
        border-radius: 5px;
        ;
    }

    /* Success message styling */
    .stSuccess {
        background-color: #d4edda;
        color: #155724;
        border-radius: 5px;
        padding: 10px;
        margin-top: 10px;
    }

    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 20px;
        color: #777;
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("📏 Unit Converter")
st.write("""
Welcome to the **Unit Converter**! This app allows you to convert between different units of measurement effortlessly.
""")

# Define conversion functions
def convert_length(value, from_unit, to_unit):
    # Conversion logic for length
    length_conversions = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "inches": 39.3701,
        "feet": 3.28084,
        "yards": 1.09361,
        "miles": 0.000621371
    }
    return value * (length_conversions[to_unit] / length_conversions[from_unit])

def convert_weight(value, from_unit, to_unit):
    # Conversion logic for weight
    weight_conversions = {
        "grams": 1,
        "kilograms": 0.001,
        "milligrams": 1000,
        "pounds": 0.00220462,
        "ounces": 0.035274
    }
    return value * (weight_conversions[to_unit] / weight_conversions[from_unit])

def convert_temperature(value, from_unit, to_unit):
    # Conversion logic for temperature
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value

# Sidebar for unit selection
st.sidebar.header("⚙️ Settings")
conversion_type = st.sidebar.selectbox(
    "Choose a conversion type:",
    ["Length", "Weight", "Temperature"]
)

# Main conversion logic
if conversion_type == "Length":
    st.header("📏 Length Conversion")
    col1, col2 = st.columns(2)
    with col1:
        value = st.number_input("Enter value:", min_value=0.0, key="length_value")
        from_unit = st.selectbox("From unit:", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards", "miles"], key="length_from")
    with col2:
        to_unit = st.selectbox("To unit:", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards", "miles"], key="length_to")
    result = convert_length(value, from_unit, to_unit)
    st.success(f"**Result:** {value} {from_unit} = **{result:.2f} {to_unit}**")

elif conversion_type == "Weight":
    st.header("⚖️ Weight Conversion")
    col1, col2 = st.columns(2)
    with col1:
        value = st.number_input("Enter value:", min_value=0.0, key="weight_value")
        from_unit = st.selectbox("From unit:", ["grams", "kilograms", "milligrams", "pounds", "ounces"], key="weight_from")
    with col2:
        to_unit = st.selectbox("To unit:", ["grams", "kilograms", "milligrams", "pounds", "ounces"], key="weight_to")
    result = convert_weight(value, from_unit, to_unit)
    st.success(f"**Result:** {value} {from_unit} = **{result:.2f} {to_unit}**")

elif conversion_type == "Temperature":
    st.header("🌡️ Temperature Conversion")
    col1, col2 = st.columns(2)
    with col1:
        value = st.number_input("Enter value:", min_value=-273.15, key="temp_value")
        from_unit = st.selectbox("From unit:", ["celsius", "fahrenheit", "kelvin"], key="temp_from")
    with col2:
        to_unit = st.selectbox("To unit:", ["celsius", "fahrenheit", "kelvin"], key="temp_to")
    result = convert_temperature(value, from_unit, to_unit)
    st.success(f"**Result:** {value} {from_unit} = **{result:.2f} {to_unit}**")

# Footer
st.markdown("---")
st.markdown('<p class="footer">Built with ❤️ using Streamlit</p>', unsafe_allow_html=True)