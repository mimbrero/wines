import matplotlib.pyplot as plt


def generate_pie_chart(title, values, labels=None, inner_label=None):
    plt.title(title)
    plt.pie(values, labels=labels, shadow=True, autopct=inner_label)

    plt.show()
