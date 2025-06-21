# Azure-AZ-204_Quiz

Azure AZ-204 Exam Preparation Quiz App
This repository contains a simple, interactive quiz application built with Streamlit, designed to help you prepare for the Microsoft Azure AZ-204: Developing Solutions for Microsoft Azure exam. The quiz questions are derived directly from a set of AZ-204 exam dumps.


### Repository Structure
```Azure-AZ-204_Quiz/
├── app.py                      # The main Streamlit application code
├── requirements.txt            # Python dependencies for the app
└── dumps/                      # Directory containing the original AZ-204 PDF dumps
    ├── az-204_4.pdf
    ├── az-204_5.pdf
    ├── az-204_7.pdf
    └── az-204_9.pdf
└── README.md
```

**Note:** The original AZ-204 exam dumps, from which these questions were extracted, are included in the dumps/ directory for your reference.

### Getting Started
Follow these instructions to set up and run the quiz application on your local machine.

#### Prerequisites
Python 3.7+

pip (Python package installer)

Installation
Clone the repository:
```
git clone https://github.com/SaiMani-Ritish/Azure-AZ-204_Quiz.git
cd Azure-AZ-204_Quiz
```
Create a virtual environment (recommended):

```python -m venv venv```
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

Install the required dependencies:
```
pip install -r requirements.txt
```
Running the Application
Once the dependencies are installed, you can run the Streamlit app:
```
streamlit run app.py
```
This command will open the quiz application in your default web browser.

Or click the link in the repository description. 

### Features
**Interactive Quiz:** Presents one question at a time with multiple-choice options.

**Instant Feedback:** Provides immediate feedback on whether your answer is correct or incorrect.

**Detailed Explanations:** Offers explanations for each answer to enhance learning.

**Score Tracking:** Keeps track of your score throughout the quiz session.

**Restart Option:** Allows you to restart the quiz once completed.

### Contributing
If you have suggestions for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request!

### License
This project is open-source and available under the MIT License.
