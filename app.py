import csv
import numpy as np
import matplotlib.pyplot as plt
from linear_regression import LinearRegression
from PIL import Image
import streamlit as st
import pandas as pd

# Run the app by typing into your terminal: 'streamlit run [Directory Path]'

st.title("Student Mark Prediction")

st.write("Upload an excel file with the content formatted as such:")
image = Image.open('file_format.png')
st.image(image)

# Add a file uploader widget
file_uploader = st.file_uploader("Choose an Excel file and insert it bellow", type=["xlsx", "xls"])

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
    st.write("Here are the score prediction for your students: ")

    for length in range(len(n)):
        st.write(f"Student Name = {n[length]} | Predicted mark = {round(y_predres[length], 2)}")

    st.write("=" * 88)

    # Plotting the data
    plt.scatter(x, y, color='b')

    # Plot the best fit line
    plt.plot(x, y_predres, color='k')

    # Add labels and title
    plt.xlabel('Hours')
    plt.ylabel('Scores')
    plt.title('Linear Regression Model')

    # Plot result
    st.write("Here is the Linear Regression graph: ")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    # TODO: FIX THIS
    # Create a download link for the results file
    results_file = open(csv_file, "rb")
    st.write("Download the results here: ")
    st.file_downloader(csv_file, bytes_file=results_file, file_type="csv")

    # Create a download link for the graph
    st.write("Download the graph here: ")
    st.file_downloader("graph.png", "graph.png", "image/png")




