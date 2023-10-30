from pathlib import Path

import streamlit  as  st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "Website" / "static" / "styles"  / "main.css"
resume_file = current_dir / "Website" / "static" / "Assets" / "CV.pdf"
profile_pic = current_dir / "Website" / "static" / "Assets" / "PPFme.png"


# --- General Settings ---
PAGE_TITLE = " M.A.K | CV "
PAGE_ICON = ":random:"
NAME = "Muhammed Ashraf Alkulaib"
DESCRIPTION = """
I have a bachelor's in computer science, and I'm looking for a job that will help me make the most of my potential position in a company where I can start my career and learn useful skills.
"""
EMAIL = " Muhammedalmugera21@gmail.com "
PHONE_NUMBER = "+966547187859"
SOCIAL_MEDIA =  {
    "LinkedIn" : "https://linkedin.com/in/muhammed-alkulaib-773492238",
    "Github" : "https://github.com/BuAshraf ",
    "Twitter" : "https://twitter.com/bo_ashraf",
}
PROJECTS = {
    "🏆 Websites ",
    "🏆 Melanoma Classification Model Using Deep Learning"
}
EDUCATION = {
    "Imam Mohammad Ibn Saud Islamic University",
     "Bachelors of Computer science",
      "2018-2023"
}
SKILLS = {
    "♦ Computer Programming",
    "♦ Ability to Work With a Team",
    "♦ Microsoft Office",
    "♦ Analysis Thinking Skills",
    "♦ Fast Learning",
    "♦ Time Management Skills",
    "♦ Ability to Multitasking",
    "♦ Problem Solving Skills",
    "♦ Ability to Work Under Pressure",
    "♦ Excellent Communication Skills",
}

LANGUAGE = {
    "🤍","English"
    "🤍","Arabic"

}





st.set_page_config (page_title=PAGE_TITLE, page_icon = PAGE_ICON)





# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)







# --- HERO SECTION ---
col1, col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic, width= 320)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label= " 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

    st.write("📫",EMAIL)
    st.write("📱",PHONE_NUMBER)


# ---SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for PROJECTS in PROJECTS:
    st.write(f"{PROJECTS}")


# --- EDUCATION ---
st.write('\n')
st.subheader("EDUCATION")
st.write("---")
for EDUCATION in EDUCATION:
    st.write(f"{EDUCATION}")



# --- SKILLS ---
st.write('\n')
st.subheader(" SKILLS")
st.write("---")
for SKILLS  in SKILLS:
    st.write (" " + SKILLS + " " )
    #st.write(f"{SKILLS}")
#st.write(
    #"- Computer Programming"           ,    "- Ability to Work With a Team",
    #"- Microsoft Office"               ,    "- Analysis Thinking Skills",
    #"- Fast Learning"                  ,    "- Time Management Skills",
    #"- Ability to Multitasking"        ,    "- Problem Solving Skills",
    #"- Ability to Work Under Pressure" ,    "- Excellent Communication Skills",#)














