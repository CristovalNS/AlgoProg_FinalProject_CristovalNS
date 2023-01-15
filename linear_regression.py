
class LinearRegression:
    """
    A Function used to predict a student's mark using LinearRegression.

    Attributes:
        epochs (int): Number of iterations for the algorithm to run.
        learning_rate (float): Step size of the algorithm's updates to the model's parameters.
        student_name (str): Name of the student.

    Methods:
        fit: Trains the model by adjusting the parameters to minimize the cost function.
        predict: Makes predictions based on the trained model by multiplying input by slope and adding y-intercept.
    """

    def __init__(self, epochs=1000, learning_rate=0.0001, student_name=str):
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.student_name = student_name

    def calculation(self, x, y, m_current=0, b_current=0, student_name='hi'):
        N = float(len(y))
        for i in range(self.epochs):
            y_current = (m_current * x) + b_current
            # cost = sum([data ** 2 for data in (y - y_current)]) / N
            m_gradient = -(2 / N) * sum(x * (y - y_current))
            b_gradient = -(2 / N) * sum(y - y_current)
            m_current = m_current - (self.learning_rate * m_gradient)
            b_current = b_current - (self.learning_rate * b_gradient)
        self.m = m_current
        self.b = b_current
        self.n = student_name

    def predict(self, x):
        return (self.m * x) + self.b
