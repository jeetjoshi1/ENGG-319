import pandas as pd
import matplotlib.pyplot as plt

# Feature names, in the same order as sklearn.datasets.load_breast_cancer().feature_names
measurements = ['radius', 'texture', 'perimeter', 'area', 'smoothness', 'compactness',
                'concavity', 'concave points', 'symmetry', 'fractal dimension']
feature_names = ([f'mean {m}' for m in measurements]
                 + [f'{m} error' for m in measurements]
                 + [f'worst {m}' for m in measurements])

# wdbc.data columns: ID, diagnosis (M/B), then the 30 features
raw = pd.read_csv('wdbc.data', header=None, names=['id', 'diagnosis'] + feature_names)

a = raw[feature_names].copy()
a['typeofcancer'] = raw['diagnosis'].map({'M': 0, 'B': 1})  # 0 = Malignant, 1 = Benign

# ---------------------------------------------------------------- Task 3
malignant = a[a['typeofcancer'] == 0]
benign = a[a['typeofcancer'] == 1]

fig, axes = plt.subplots(1, 3, figsize=(18, 4.5))

# Scatter plots of mean radius versus another feature
scatter_features = ['mean concavity', 'mean concave points', 'mean symmetry']
for ax, feature in zip(axes, scatter_features):
    ax.scatter(malignant['mean radius'], malignant[feature], color='blue', alpha=0.7, label='Malignant')
    ax.scatter(benign['mean radius'], benign[feature], color='red', alpha=0.7, label='Benign')
    ax.set_title(f'Mean Radius vs {feature.capitalize()}')
    ax.set_xlabel('Mean Radius')
    ax.set_ylabel(feature.capitalize())
    ax.legend()

plt.tight_layout()
plt.savefig('figure2.png', dpi=150)
plt.show()
