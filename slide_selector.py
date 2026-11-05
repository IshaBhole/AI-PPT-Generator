def select_slides(topic, slides):

    print("\nUSING FIXED SLIDE SELECTOR\n")

    selected_slides = []

    # Title Slide
    selected_slides.append(0)

    # Introduction
    selected_slides.append(8)

    # Problem
    selected_slides.append(15)

    # Solution
    selected_slides.append(19)

    # Thanks
    selected_slides.append(31)

    return {
        "selected_slides": selected_slides
    }