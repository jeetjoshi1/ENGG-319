import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

# The 13 features and the class of each wine (target: 0, 1 or 2 = cultivar 1, 2 or 3)
a = load_wine(as_frame=True).frame
a = a.rename(columns={'target': 'cultivar', 'flavanoids': 'Flavanoids', 'proline': 'Proline',
                      'od280/od315_of_diluted_wines': 'OD280/OD315', 'alcohol': 'Alcohol',
                      'color_intensity': 'Color intensity'})

# ---------------------------------------------------------------- Task 3
cultivar1 = a[a['cultivar'] == 0]
cultivar2 = a[a['cultivar'] == 1]
cultivar3 = a[a['cultivar'] == 2]

classes = [(cultivar1, 'blue', 'o', 'Cultivar 1'),
           (cultivar2, 'red', 's', 'Cultivar 2'),
           (cultivar3, 'green', '^', 'Cultivar 3')]

# Pair plots of the five features with the largest differences between cultivars
pair_features = ['Flavanoids', 'Proline', 'OD280/OD315', 'Alcohol', 'Color intensity']
n = len(pair_features)

fig, axes = plt.subplots(n, n, figsize=(15, 15.5))

for row, y_feature in enumerate(pair_features):
    for col, x_feature in enumerate(pair_features):
        ax = axes[row, col]
        for data, color, marker, label in classes:
            if row == col:
                # Histogram of each feature for each class on the diagonal
                ax.hist(data[x_feature], bins=15, range=(a[x_feature].min(), a[x_feature].max()),
                        fill=False, edgecolor=color, label=label)
            else:
                # Scatter plot of one feature versus another
                ax.scatter(data[x_feature], data[y_feature], color=color, marker=marker,
                           s=20, alpha=0.7, label=label)
        if row == n - 1:
            ax.set_xlabel(x_feature)
        if col == 0:
            ax.set_ylabel(y_feature)

handles, labels = axes[0, 1].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=3, fontsize=12)

# Caption at the bottom of the figure
caption = ('Figure 1: Pair plot of five features of the UCI Wine dataset (178 wines from three cultivars). '
           'Diagonal subplots are histograms of each\n'
           'feature for each cultivar; all other subplots are scatter plots of one feature versus another, '
           'coloured by cultivar.\nThe three cultivars form mostly separate clusters, with some overlap.')
fig.text(0.5, 0.01, caption, ha='center', va='bottom', fontsize=12)

plt.tight_layout(rect=(0, 0.055, 1, 0.97))
plt.savefig('figure1.png', dpi=150)
plt.show()
