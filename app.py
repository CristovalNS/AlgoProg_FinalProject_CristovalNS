import csv
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from linear_regression import LinearRegression
from PIL import Image

# Run the app by typing into your terminal: 'streamlit run [Directory Path]'

st.title("Student Mark Prediction")

st.write("Upload an excel file with the content formatted as such as a starting dataset:")
image = Image.open('file_format.png')
st.image(image)

# Add a file uploader widget
file_uploader = st.file_uploader("Choose an Excel file as the dataset and insert it bellow", type=["xlsx", "xls"])

if file_uploader:
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_uploader)

    # Write the DataFrame to a CSV file
    csv_file = file_uploader.name.replace(".xlsx", ".csv").replace(".xls", ".csv")
    df.to_csv(csv_file, index=False)

    # Show a message to confirm that the file has been converted
    st.success("File converted and saved as {}".format(csv_file))

    # Read the data from the CSV file
    n = []
    x = []
    y = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Skip the header row
        for row in reader:
            n.append(str(row[0]))
            x.append(float(row[1]))
            y.append(float(row[2]))

    # Convert the data to numpy arrays
    n = np.array(n)
    x = np.array(x)
    y = np.array(y)

    # Create an instance of the LinearRegression class and fit it to the data
    model = LinearRegression()
    model.calculation(x, y)

    # Result
    y_predres = model.predict(x)

    st.write("=" * 88)

    # Plotting the data
    plt.scatter(x, y, color='b')

    # Plot the best fit line
    plt.plot(x, y_predres, color='k')

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

    # Get user input for name and study hours
    st.write("Enter the student's name and their study hour: ")
    name = st.text_input("Enter student name: ")
    study_hours = st.text_input("Enter study hours: ")

    if st.button("Predict Student Score"):
        # Predict the score for the user's input
        s = np.array(float(study_hours))
        y_user_predres = model.predict(s)

        # Display the predicted score for the user
        if y_user_predres > 100:
            result = 100.0
            st.write(f"Predicted mark for {name} with {study_hours} study hours is {round(result, 2)}")
        else:
            st.write(f"Predicted mark for {name} with {study_hours} study hours is {round(y_user_predres, 2)}")

    st.write(" ")

    # Predict the scores of one class of students
    st.write("Predict the scores of a class of students: ")

    file_uploader2 = st.file_uploader(
        "Choose an Excel file containing your students' study time and insert it bellow", type=["xlsx", "xls"])
    if st.button("Predict Multiple Students Scores"):
        if file_uploader2:
            # Read the Excel file into a DataFrame
            df = pd.read_excel(file_uploader2)

            # Write the DataFrame to a CSV file
            csv_file2 = file_uploader2.name.replace(".xlsx", ".csv").replace(".xls", ".csv")
            df.to_csv(csv_file2, index=False)

            # Show a message to confirm that the file has been converted
            st.success("File converted and saved as {}".format(csv_file2))

            # Read the data from the CSV file
            n2 = []
            x2 = []
            # y2 = []
            with open(csv_file2, 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                next(reader)  # Skip the header row
                for row in reader:
                    n2.append(str(row[0]))
                    x2.append(float(row[1]))

            # Convert the data to numpy arrays
            n = np.array(n2)
            x2 = np.array(x2)

            # Create an instance of the LinearRegression class and fit it to the data
            model = LinearRegression()
            model.calculation(x2, y)

            # Result
            y_class_predres = model.predict(x2)
            st.write("=" * 88)
            st.write("Here are the score prediction for your students: ")

            for length in range(len(n)):
                if y_class_predres[length] > 100:
                    result = 100.0
                    st.write(f"Student Name = {n[length]} | Predicted mark = {round(result, 2)}")
                else:
                    st.write(f"Student Name = {n[length]} | Predicted mark = {round(y_class_predres[length], 2)}")

            st.write("=" * 88)

