from pptx import Presentation


def delete_slide(prs, index):

    slide_id = prs.slides._sldIdLst[index]

    prs.part.drop_rel(
        slide_id.rId
    )

    prs.slides._sldIdLst.remove(
        slide_id
    )


def build_ppt(
    template_path,
    selected_slides,
    generated_slides,
    output_path
):

    prs = Presentation(
        template_path
    )

    keep = set(
        selected_slides
    )

    # Delete unwanted slides
    for i in range(
        len(prs.slides) - 1,
        -1,
        -1
    ):

        if i not in keep:

            delete_slide(
                prs,
                i
            )

    slide_lookup = {}

    for slide in generated_slides:

        slide_lookup[
            slide["slide_no"]
        ] = slide

    current_index = 0

    for original_slide_no in selected_slides:

        slide = prs.slides[
            current_index
        ]

        data = slide_lookup[
            original_slide_no
        ]

        try:

            if len(
                slide.placeholders
            ) >= 1:

                slide.placeholders[
                    0
                ].text = data[
                    "title"
                ]

            if len(
                slide.placeholders
            ) >= 2:

                slide.placeholders[
                    1
                ].text = "\n".join(
                    data["content"]
                )

        except Exception as e:

            print(
                f"Slide Error: {e}"
            )

        current_index += 1

    prs.save(
        output_path
    )

    return output_path