import matplotlib.pyplot as plt

def plot_line(data, title, xlabel, ylabel):
    data.plot(kind='line', figsize=(10, 5), title=title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def plot_bar(data, title, xlabel, ylabel):
    data.plot(kind='bar', figsize=(10, 5), title=title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()
