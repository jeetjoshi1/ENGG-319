import pandas as pd
import matplotlib.pyplot as plt

# Feature names, in the same order as sklearn.datasets.load_breast_cancer().feature_names
measurements = ['radius', 'texture', 'perimeter', 'area', 'smoothness', 'compactness',
                'concavity', 'concave points', 'symmetry', 'fractal dimension']
feature_names = ([f'mean {m}' for m in measurements]
                 + [f'{m} error' for m in measurements]
                 + [f'worst {m}' for m in measurements])

# ---------------------------------------------------------------- Task 1
# wdbc.data columns: ID, diagnosis (M/B), then the 30 features
raw = pd.read_csv('wdbc.data', header=None, names=['id', 'diagnosis'] + feature_names)

a = raw[feature_names].copy()
a['typeofcancer'] = raw['diagnosis'].map({'M': 0, 'B': 1})  # 0 = Malignant, 1 = Benign

# (a)
print('a.shape:', a.shape)

# (b) mean radius, mean perimeter, mean area and typeofcancer
df = a.iloc[:, [0, 2, 3, 30]]

# (i)
print('\nFirst two rows of df:')
print(df.head(2))

# (ii)
print('\nRows 17 to 21 of df:')
print(df.iloc[17:22])



# ---------------------------------------------------------------- Task 2
malignant = a[a['typeofcancer'] == 0]
benign = a[a['typeofcancer'] == 1]

fig, axes = plt.subplots(2, 3, figsize=(18, 9))
axes = axes.flatten()

# Histogram of mean radius for each class
axes[0].hist(malignant['mean radius'], bins=20, fill=False, edgecolor='blue', label='Malignant')
axes[0].hist(benign['mean radius'], bins=20, fill=False, edgecolor='red', label='Benign')
axes[0].set_title('Histogram of Mean Radius')
axes[0].set_xlabel('Mean Radius')
axes[0].set_ylabel('Frequency')
axes[0].legend()

# Scatter plots of mean radius versus another feature
scatter_features = ['mean perimeter', 'mean area', 'mean texture']
for ax, feature in zip(axes[1:4], scatter_features):
    ax.scatter(malignant['mean radius'], malignant[feature], color='blue', alpha=0.7, label='Malignant')
    ax.scatter(benign['mean radius'], benign[feature], color='red', alpha=0.7, label='Benign')
    ax.set_title(f'Mean Radius vs {feature.title()}')
    ax.set_xlabel('Mean Radius')
    ax.set_ylabel(feature.title())
    ax.legend()

# Box plot of mean radius for each class
axes[4].boxplot([malignant['mean radius'], benign['mean radius']], tick_labels=['Malignant', 'Benign'])
axes[4].set_title('Box plot of Mean Radius')
axes[4].set_xlabel('Mean Radius')

axes[5].axis('off')

plt.tight_layout()
plt.savefig('figure1.png', dpi=150)
plt.show()
