import streamlit as st
import google.generativeai as genai
from PIL import Image
import textwrap
st.title("Kabbalistic Numbers Program")
st.markdown(
    """
    
    **Author:** Cha0smagick the Technowizard
    **Created for the blog:** [El Rincon Paranormal](https://elrinconparanormal.blogspot.com)  
    **Project's main page:** [Cha0smagick's Cabalistic Number interpretator](https://elrinconparanormal.blogspot.com/2023/12/Free%20online%20Kabbalah%20Name%20to%20Sacred%20Numbers..html)  
    
    **Donate crypto to support the project:**
    
    - Bitcoin: 3KcF1yrY44smTJpVW68m8dw8q64kPtzvtX
    - Litecoin: LME9oq8BRQ6dDdqEKg3HJB9UL6byhJka1X
    - Gridcoin: RyAcDpYRMWfDHLTizCTLzy58qBgzcfo5eZ
    - Dodgecoin: DDSxowLFPyBHVdV16hGhWdhyfa8ors3VPd
    - Blackcoin: B62pVSG1hjvBDbCeKbEnYmKxUg5rsnZKwt
    - Dash: Xj1MjAgxZPRqysMHox4sUV9XYZixrsk4e6
    - Peercoin: PA43iLNooKU76u4yPTtL5j97W6zwWkwxV2
    - Syscoin: sys1qg6npncq4xe7ruz4e4xlnvuyrzj90qvv3gg0yag
    
    """
)
GOOGLE_API_KEY = "Your_google_api_key"  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

def get_kabbalistic_number(name):
    kabbalistic_assignment = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 10, 'K': 20, 'L': 30, 'M': 40, 'N': 50, 'O': 60, 'P': 70, 'Q': 80,
        'R': 90, 'S': 100, 'T': 200, 'U': 300, 'V': 400, 'W': 500, 'X': 600,
        'Y': 700, 'Z': 800
    }

    name = name.upper()
    unique_name = ''.join(dict.fromkeys(name))
    kabbalistic_number = sum(kabbalistic_assignment.get(letter, 0) for letter in unique_name)

    return kabbalistic_number

def generate_explanation(kabbalistic_number):
    explanations = {
        1: "The number 1 represents individuality and leadership. It is a number that emphasizes self-sufficiency and self-confidence.",
        2: "The number 2 symbolizes duality and cooperation. It represents harmony and the need for balance and collaboration in life.",
        3: "The number 3 represents creativity and expression. It is associated with communication and optimism.",
        4: "The number 4 represents stability and concrete manifestation. It is considered a foundational number, symbolizing the four primary elements and cardinal directions, providing structure and balance in the material world.",
        5: "The number 5 represents freedom and connection to the divine. It is considered a number of expansion and spirituality, symbolizing the ability to transcend earthly limitations and reach a higher level of spiritual consciousness and perception.",
        6: "The number 6 represents harmony and integration. It is considered a number of balance and beauty, symbolizing the union between the divine and the human, as well as the integration of polarities to achieve spiritual wholeness and perfection.",
        7: "The number 7 represents perfection and wholeness. It is considered a sacred and powerful number, symbolizing the connection to the divine and spiritual fulfillment. It represents the manifestation of creation in its fullness and divine rest after the work is completed.",
        8: "The number 8 represents transcendence and overcoming limits. It is considered a number of fullness and spiritual power, symbolizing expansion beyond earthly confines towards the infinite and eternal. It represents the connection to higher levels of consciousness and the ability to attain elevated states of enlightenment.",
        9: "The number 9 represents completion and the culmination of a cycle. It is considered a number of fulfillment and wisdom, symbolizing spiritual integrity and the achievement of wholeness. It represents the point of culmination before beginning a new cycle of transformation and growth.",
        0: "The number 0 (zero) does not have a specific representation in Jewish Kabbalah. However, in some modern Kabbalah approaches, the number 0 may symbolize infinite potential and connection with the Divine Source, representing a state of unity and transcendence beyond conventional numerical limits."
    }

    individual_explanations = []

    if kabbalistic_number < 10:
        if kabbalistic_number in explanations:
            individual_explanations.append(explanations[kabbalistic_number])
    else:
        for digit in str(kabbalistic_number):
            digit = int(digit)
            if digit in explanations:
                individual_explanations.append(explanations[digit])

    return individual_explanations

def get_hebrew_equivalence(name):
    hebrew_equivalence = {
        'A': 'א', 'B': 'ב', 'C': 'כ', 'D': 'ד', 'E': 'ה', 'F': 'ו', 'G': 'ג', 'H': 'ה', 'I': 'י',
        'J': 'י', 'K': 'כ', 'L': 'ל', 'M': 'מ', 'N': 'נ', 'O': 'ע', 'P': 'פ', 'Q': 'ק',
        'R': 'ר', 'S': 'ש', 'T': 'ת', 'U': 'ו', 'V': 'ו', 'W': 'ו', 'X': 'צ',
        'Y': 'י', 'Z': 'ז'
    }

    name = name.upper()
    equivalence = []

    for letter in name:
        if letter in hebrew_equivalence:
            equivalence.append(hebrew_equivalence[letter])
        else:
            equivalence.append(letter)

    hebrew_equivalence = ''.join(equivalence)
    return hebrew_equivalence
    
def get_gemini_response(question):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(question)
        return response.text
    except ValueError as e:
        st.error("The name you are trying to evaluate may be against Google Gemini policies. Please try another name.")
        st.stop()

name = st.text_input("Enter a name:")
st.write("\n")

if st.button("Calculate"):
    kabbalistic_number = get_kabbalistic_number(name)
    explanations = generate_explanation(kabbalistic_number)

    hebrew_equivalence = get_hebrew_equivalence(name)
    st.write(f"The linguistic equivalence in Hebrew of the name '{name}' is: {hebrew_equivalence}")
    st.write("\n")

    if explanations:
        combined_explanations = ' '.join(explanations)
    else:
        combined_explanations = "No explanation found for that number."

    # Gemini API Interaction
    gemini_question = f"act as a magic cabalistic oracle and explain the follow cabalistic numeric information profously to the user. {name} - {hebrew_equivalence} -\n\n{get_gemini_response(name)}"
    gemini_response = get_gemini_response(gemini_question)

    # Display only the final results in a centered and larger font
    st.markdown("<p style='text-align: center; font-size: 20px;'>Linguistic Equivalence in Hebrew:</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 24px;'>{hebrew_equivalence}</p>", unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; font-size: 20px;'>Numeric Cabalistic Interpretation:</p>", unsafe_allow_html=True)
    st.markdown(f"{gemini_response}", unsafe_allow_html=True)
