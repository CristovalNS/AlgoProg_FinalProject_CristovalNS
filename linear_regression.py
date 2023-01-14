
class LinearRegression:
    """
    A Function used to predict a student's mark using LinearRegression.

    Attributes:
        epochs (int):
        learning_rate (float):
        student_name (str)

    Methods:
        fit:
        predict:
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
