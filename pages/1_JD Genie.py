import streamlit as st
from func import generate_jd

def display_bullet_points(text):
    bullet_points = text.split("\n• ") 
    for i, point in enumerate(bullet_points):
        if i == 0:
            st.write(point)
        else:
            st.write("• " + point)

# def get_base64(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_background(png_file):
#     bin_str = get_base64(png_file)
#     page_bg_img = '''
#     <style>
#         .stApp {
#             background-image: url("data:image/png;base64,%s");
#             background-size: cover;
#             }
#     </style>
#     ''' % bin_str
#     st.markdown(page_bg_img, unsafe_allow_html=True)


def main():
    st.title("JD Genie for Neostats Analytics Solutions")
    st.image("image.png", use_column_width=True) 

    # set_background('image.png')

    # st.markdown(
    #     """
    #     <style>
    #     /* Increase font size and make text bold */
    #     .stTextInput, .stSelectbox, .stNumberInput, .stTextArea {
    #         font-size: 18px;
    #         font-weight: bold;
    #         color: #333333; /* Text color */
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )

    location = st.text_input("Location")
    mode_of_work = st.selectbox("Mode of Work", ["Onsite", "Hybrid", "Remote"])
    years_of_experience = st.number_input("Years of Experience", min_value=0, max_value=10, step=1)
    role_title = st.text_input("Role Title")
    key_skills = st.text_input("Key Skills")
    specific_requirements = st.text_area("Specific Requirements")
    job_responsibilities = st.text_area("Job Responsibilities")

    if st.button("Generate Job Description"):
        job_description = generate_jd(location, mode_of_work, years_of_experience,
                                                   role_title, key_skills, specific_requirements,
                                                   job_responsibilities)
        st.markdown(f"### Generated Job Description:")
        display_bullet_points(job_description)

if __name__ == "__main__":
    main()