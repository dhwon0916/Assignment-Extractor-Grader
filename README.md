# Assignment Extractor & Grader

The **Assignment Extractor and Grader** is a Python-based application designed to streamline the process of managing and grading assignments submitted via Microsoft Teams. This tool allows educators to extract, organize, and grade assignments efficiently with the help of AI-based grading estimates and manual grading options.

---

## Features

### Assignment Extraction

- **Microsoft Teams Integration**: Extract assignments from the structured directories created by Microsoft Teams.
- **Customizable Export Options**:
  - Export assignments to a single folder.
  - Organize assignments into individual folders for each student.
- **Version Control**: Automatically identifies and extracts the latest version of each assignment.

### AI-Powered Grading

- **Rubric Upload**:
  - Upload a grading rubric in a supported format.
  - The program uses AI to estimate grades based on the rubric.
- **Grade Estimates**:
  - AI-generated grades are provided as an estimate to assist educators.
  - Educators should review and adjust grades as necessary.
- **Integrated Grading System**:
  - Grade extracted assignments directly within the application.
  - Input scores and comments for each student alongside the AI estimate.
- **Export Grades**: Save grades and comments to a report for record-keeping or sharing.

---

## How to Use

1. **Launch the Program**:

   ```bash
   python assignment_extractor_v2.py
   ```

2. **Set Paths**:

   - **Import Folder**: Select the folder containing student submissions from Microsoft Teams.
   - **Assignment Folder**: Specify the assignment folder to extract.
   - **Export Folder**: Set the destination folder for extracted assignments.

3. **Customize Export Options**:

   - Enable or disable the option to export assignments into individual folders for each student.

4. **Extract Assignments**:

   - Click **Extract** to begin the process.
   - The tool will copy files to the specified export folder, ensuring only the latest versions are included.

5. **Upload Rubric and Grade Assignments**:

   - Upload a grading rubric through the interface.
   - The AI will analyze the assignments based on the rubric and provide grade estimates.
   - Manually adjust grades and add comments if needed.
   - Export a grading report when finished.

---

## Requirements

- Python 3.x
- Required Libraries:
  ```bash
  pip install PySimpleGUI
  ```

---

## Recommendations

- **Rubric and Grades**:
  - Review AI-generated grades carefully as they are intended as estimates.
  - Use the integrated grading system to finalize scores and provide personalized feedback.
- **Directory Structure**:
  - Ensure the import folder follows the default Microsoft Teams assignment directory structure.
- **File Naming**:
  - Avoid using special characters in folder or file names to prevent extraction errors.

---

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Clone or download this repository.
3. Install the required library using the command above.
4. Run the program using the `python` command.

---

## Support

For questions, issues, or feature requests, please contact [DonghyunWon2@gmail.com](mailto\:DonghyunWon2@gmail.com).

---

## Future Enhancements

- **Enhanced Grading**:
  - Support for batch grading and automated rubric-based evaluation.
- **Analytics**:
  - Generate analytics reports for student performance.
- **File Preview**:
  - Integrated preview of assignments for faster grading.

---

