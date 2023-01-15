# Algorithm and Programming Final Project
# Student Mark Prediction Program in Python Using Linear Regression
# Made by: Cristoval Neo Sasono
# NIM: 2602158235

import streamlit as st
import pandas as pd


class ExcelFileConverter:
    """
    A class containing the function to convert Excel files into CSV files.

    Attributes:
        file_type_in: Excel file input
        file_type_out: CSV file output

    Methods:
        convert_excel_to_csv_file: Converts Excel files into CSV files to be used by the DataModel class.
    """

    def __init__(self, file_type_in, file_type_out):
        self.file_type_in = file_type_in
        self.file_type_out = file_type_out

    def convert_excel_to_csv_file(self, file):
        if file:
            # Read the Excel file into a DataFrame
            read_excel_file = pd.read_excel(file)

            # Write the DataFrame to a CSV file
            csv_dataset_file = file.name.replace(self.file_type_in, self.file_type_out)
            read_excel_file.to_csv(csv_dataset_file, index=False)

            # Show a message to confirm that the file has been converted
            st.success("File converted and saved as {}".format(csv_dataset_file))
            return csv_dataset_file
        else:
            st.error("Please upload a file of type {}".format(self.file_type_in))
            return None
