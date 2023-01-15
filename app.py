# Algorithm and Programming Final Project
# Student Mark Prediction Program in Python Using Linear Regression
# Made by: Cristoval Neo Sasono
# NIM: 2602158235

import csv
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from datamodel import DataModel
from fileconverter import FileConverter
from PIL import Image

# Run the app by typing into your terminal: 'streamlit run [Directory Path]'

st.title("Student Mark Prediction")

st.write("Upload an excel file with the content formatted as such as a starting dataset:")
file_format_image = Image.open('file_format.png')
st.image(file_format_image)


# Add a file uploader widget to upload the Excel file containing the dataset used to train the datamodel.
file_converter = FileConverter(".xlsx", ".csv")
excel_dataset_file = st.file_uploader("Choose an Excel file as the dataset and insert it bellow", type=["xlsx", "xls"])
csv_dataset_file = file_converter.convert_excel_to_csv_file(excel_dataset_file)

if csv_dataset_file:
    # Read the data from the CSV file
    student_name_dataset = []
    student_study_hours_dataset = []
    student_scores_dataset = []
    with open(csv_dataset_file, 'r') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        next(file_reader)  # Skip the header row
        for row in file_reader:
            student_name_dataset.append(str(row[0]))
            student_study_hours_dataset.append(float(row[1]))
            student_scores_dataset.append(float(row[2]))

    # Convert the data to numpy arrays
    student_name_dataset = np.array(student_name_dataset)
    student_study_hours_dataset = np.array(student_study_hours_dataset)
    student_scores_dataset = np.array(student_scores_dataset)

    # Create an instance of the DataModel class and fit it to the data
    model = DataModel()
    model.create_model_with_linear_regression(student_study_hours_dataset, student_scores_dataset)

    # DataModel result
    y_dataset_prediction_results = model.predict_student_score(student_study_hours_dataset)
    st.write("=" * 88)

    # Plotting the data
    plt.scatter(student_study_hours_dataset, student_scores_dataset, color='b')

    # Plot the best fit line
    plt.plot(student_study_hours_dataset, y_dataset_prediction_results, color='k')

    # Add labels and title
    plt.xlabel('Study Hours')
    plt.ylabel('Student Scores')
    plt.title('Linear Regression Model')

    # Plot result
    st.write("Here is the Linear Regression graph based on the dataset you've provided: ")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    st.write(" ")

    # Predict the score of a single student
    st.write("Predict the score of one student:")

    # Get  input for student name and study hours
    st.write("Enter the student's name and their study hour: ")
    enter_student_name = st.text_input("Enter student name: ")
    enter_student_study_hours = st.text_input("Enter study hours: ")

    if st.button("Predict Student Score"):
        # Predict the score of the student using the DataModel
        s = np.array(float(enter_student_study_hours))
        y_student_prediction_result = model.predict_student_score(s)

        # Display the predicted score of the student
        if y_student_prediction_result > 100:
            result = 100.0
            st.write(f"Predicted mark for {enter_student_name} with {enter_student_study_hours}"
                     f" study hours is {round(result, 2)}")
        else:
            st.write(f"Predicted mark for {enter_student_name} with {enter_student_study_hours}"
                     f" study hours is {round(y_student_prediction_result, 2)}")

    st.write(" ")

    # Predict the scores of one class of students
    st.write("Predict the scores of a class of students: ")

    excel_class_data_file = st.file_uploader("Choose an Excel file containing the data of a class of students' "
                                             "study hour and insert it bellow", type=["xlsx", "xls"])
    csv_class_data_file = file_converter.convert_excel_to_csv_file(excel_class_data_file)
    if st.button("Predict Multiple Students Scores"):
        if csv_class_data_file:
            # Read the data from the CSV file
            class_student_names = []
            class_student_study_hours = []
            with open(csv_class_data_file, 'r') as csvfile:
                file_reader = csv.reader(csvfile, delimiter=',')
                next(file_reader)  # Skip the header row
                for row in file_reader:
                    class_student_names.append(str(row[0]))
                    class_student_study_hours.append(float(row[1]))

            # Convert the data to numpy arrays
            class_student_names = np.array(class_student_names)
            class_student_study_hours = np.array(class_student_study_hours)

            # Predict the scores of the class of students using the DataModel
            y_class_student_prediction_results = model.predict_student_score(class_student_study_hours)

            st.write("=" * 88)

            # Display the predicted scores of the class of students
            st.write("Here are the score prediction for your students: ")
            for length in range(len(class_student_names)):
                if y_class_student_prediction_results[length] > 100:
                    result = 100.0
                    st.write(f"Student Name = {class_student_names[length]} | Predicted mark = {round(result, 2)}")
                else:
                    st.write(f"Student Name = {class_student_names[length]} | "
                             f"Predicted mark = {round(y_class_student_prediction_results[length], 2)}")

            st.write("=" * 88)
