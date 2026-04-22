
import streamlit as st
from PIL import Image
from api_calling import note_generator as nt , quize_generator as qz


st.markdown("""
    <div style='background-color: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px; border-left: 10px solid #7B2CBF; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);'>
        <h1 style='margin: 0; color: #7B2CBF;'>🧠 Adaptive Assessment Engine </h1>
        <code style='color: #9D4EDD;'>Architected by: Sahel</code>
    </div>
    <br>
""", unsafe_allow_html=True)

st.title("Note Summary and quiz Generator")
st.write("Upload upto 3 images to generate Note summary and quizzes")
st.divider()
with st.sidebar:
    images = st.file_uploader("upload your images: ", type = ['jpg','jpeg','png'], accept_multiple_files= True)
    pil_image = []
    for img in images:
        pil_img = Image.open(img)
        pil_image.append(pil_img)
    if images :
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("uploaded images")
            col= st.columns(len(images))
            for i , img in enumerate(images):
                with col[i]:
                    st.image(img)
                        
        
    select = st.selectbox("Enter the difficulty of Quiz", ("Easy","Medium","Hard") ,  index = None)  
        
    press = st.button("Click the button to initiate AI", type = "primary") 
    

if press:
    if not images:
        st.error("upload atleast 1 image")
    if not select:
        st.error("you must select atleast 1 options")    

    if images and select :
        with st.container(border = True):
            st.subheader("YOUR NOTE")
            
            with st.spinner("AI is writing notes for you.."):
                 
                 notes = nt(pil_image)
                 st.text(notes)
                
        
            
                
        with st.container(border = True):
            st.subheader(f"Quize {select} level difficulty show below")
            with st.spinner("Quizzes are making..."):
                quizes = qz(pil_image,select)
                st.text(quizes)
