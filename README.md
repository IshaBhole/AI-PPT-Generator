# AI PPT Generator

An AI-powered PowerPoint Generator that creates presentations using existing PowerPoint templates and locally running Large Language Models (LLMs).

## Overview

The AI PPT Generator automates the presentation creation process. Users can upload an existing PowerPoint template, enter a presentation topic, and generate a new presentation using AI-generated content while reusing the selected slides and design of the uploaded template.

## Features

- **PPT Template Upload:** Upload an existing `.pptx` presentation.
- **Template Analysis:** Analyze the uploaded presentation structure.
- **Slide Selection:** Select suitable slides for the new presentation.
- **AI Content Generation:** Generate slide content using the Phi-3 model.
- **Automated PPT Creation:** Populate selected slides with generated content.
- **PPT Download:** Download the generated presentation.

## Tech Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **AI Model:** Phi-3 (Ollama)
- **PowerPoint Processing:** python-pptx
- **LLM Runtime:** Ollama

## Project Structure

```text
AI-PPT-Generator/
│
├── app.py
├── template_analyzer.py
├── slide_selector.py
├── content_generator.py
├── ppt_builder.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── uploads/
└── output/
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/IshaBhole/AI-PPT-Generator.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-PPT-Generator
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download Ollama from:

https://ollama.com/

### 5. Download the Phi-3 Model

```bash
ollama pull phi3
```

### 6. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## How to Use

1. Open the AI PPT Generator application.
2. Upload a PowerPoint template.
3. Enter your presentation topic.
4. Click on **Generate PPT**.
5. Wait for the presentation to be generated.
6. Download your generated PowerPoint presentation.

## Future Improvements

- Improve AI-based slide selection.
- Support additional LLM models.
- Improve generated slide layouts and formatting.
- Add more customization options.

## Author

**Isha Bhole**

GitHub: https://github.com/IshaBhole