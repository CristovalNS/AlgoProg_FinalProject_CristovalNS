# Algorithm and Programming Final Project
# Student Mark Prediction Program in Python Using Linear Regression
# Made by: Cristoval Neo Sasono
# NIM: 2602158235

class DataModel:
    """
    A class containing the functions to predict one or multiple students' scores using linear regression.

    Attributes:
        epochs (int): Number of iterations for the algorithm to run.
        learning_rate (float): Step size of the algorithm's updates to the model's parameters.
        student_name (str): Name of the student.

    Methods:
        create_model_with_linear_regression: Trains the model by adjusting the parameters to minimize the cost function.
        predict_student_score: Makes predictions based on the trained model by
        multiplying input by slope and adding y-intercept.
    """

    def __init__(self, epochs=1000, learning_rate=0.0001, student_name=str):
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.student_name = student_name

    def create_model_with_linear_regression(self, x, y, m_current=0, c_current=0, student_name=''):
        # x = student study hours
        # y = student scores
        N = float(len(y))
        for i in range(self.epochs):
            y_current = (m_current * x) + c_current
            m_gradient = -(2 / N) * sum(x * (y - y_current))
            c_gradient = -(2 / N) * sum(y - y_current)
            m_current = m_current - (self.learning_rate * m_gradient)
            c_current = c_current - (self.learning_rate * c_gradient)
        self.m = m_current
        self.c = c_current
        self.n = student_name

    def predict_student_score(self, x):
        # y = mx + c
        return (self.m * x) + self.c

