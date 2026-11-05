import streamlit as st
import os

from template_analyzer import analyze_template
from slide_selector import select_slides
from content_generator import generate_slide_content
from ppt_builder import build_ppt

st.set_page_config(
    page_title="AI PPT Generator",
    layout="wide"
)

st.title("AI PPT Generator")

uploaded_ppt = st.file_uploader(
    "Upload PPT Template",
    type=["pptx"]
)

topic = st.text_input(
    "Enter Presentation Topic"
)

if st.button("Generate PPT"):

    if not uploaded_ppt:
        st.error("Please upload a PPT template.")
        st.stop()

    if not topic:
        st.error("Please enter a topic.")
        st.stop()

    

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    template_path = os.path.join(
        "uploads",
        uploaded_ppt.name
    )

    with open(
        template_path,
        "wb"
    ) as f:

        f.write(
            uploaded_ppt.getbuffer()
        )

    # Analyze template

    slides = analyze_template(
        template_path
    )

    # Select slides
    selected = select_slides(
        topic,
        slides
    )

    # Generate content
    generated_slides = []

    progress = st.progress(0)

    total = len(
        selected["selected_slides"]
    )

    for idx, slide_no in enumerate(
        selected["selected_slides"]
    ):

        slide_title = ""

        for slide in slides:

            if (
                slide["slide_no"]
                == slide_no
            ):

                slide_title = (
                    slide["title"]
                )

                break

        content = generate_slide_content(
            topic,
            slide_title
        )

        generated_slides.append({

            "slide_no":
                slide_no,

            "title":
                content["title"],

            "content":
                content["content"]

        })

        progress.progress(
            (idx + 1) / total
        )


    os.makedirs(
        "output",
        exist_ok=True
    )

    output_path = (
        "output/generated_presentation.pptx"
    )


    ppt_path = build_ppt(
        template_path,
        selected["selected_slides"],
        generated_slides,
        output_path
    )

    st.success(
        "Presentation Generated Successfully!"
    )

    with open(
        ppt_path,
        "rb"
    ) as file:

        st.download_button(
            label="📥 Download PPT",
            data=file,
            file_name="generated_presentation.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )