import sys

import matplotlib.pyplot as plt
import seaborn as sns


def sales_chart():
    categories = ["Electronics", "Clothing", "Books", "Toys"]
    sales = [45, 60, 30, 55]
    with sns.axes_style("whitegrid"):
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(
            x=categories, y=sales, hue=categories,
            palette="rocket", legend=False, errorbar=None, ax=ax,
        )
    for bars in ax.containers:
        ax.bar_label(bars, padding=3)
    ax.set(title="Monthly Sales by Product Category", ylabel="Sales ($)")
    ax.margins(y=0.15)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    figure = sales_chart()
    if len(sys.argv) > 1:
        figure.savefig(sys.argv[1], dpi=150)
    else:
        plt.show()
    plt.close(figure)
