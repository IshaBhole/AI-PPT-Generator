from pptx import Presentation


def analyze_template(template_path):

    prs = Presentation(template_path)

    slides_info = []

    for i, slide in enumerate(prs.slides):

        title = ""

        try:
            if slide.shapes.title:
                title = slide.shapes.title.text.strip()
        except:
            pass

        placeholders = []

        for shape in slide.placeholders:

            try:

                placeholders.append({
                    "idx": shape.placeholder_format.idx,
                    "name": shape.name
                })

            except:
                pass

        slides_info.append({
            "slide_no": i,
            "title": title,
            "placeholders": placeholders
        })

    return slides_info