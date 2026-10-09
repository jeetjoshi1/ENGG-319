# Deliverable 2 – Written Responses

## Task 2(ii): What the first three subplots of Figure 1 reveal

**Histogram of mean radius.** Malignant tumours tend to have a larger mean radius than benign ones: the median is about 17.3 for malignant and 12.2 for benign. The malignant distribution is also more spread out (roughly 11 to 28) than the benign one (roughly 7 to 18). The two distributions overlap between about 11 and 18, so mean radius on its own separates most cases but not all of them.

**Mean radius vs mean perimeter.** The points fall almost exactly on a straight line (correlation 0.998), which is expected since perimeter is proportional to radius. Mean perimeter therefore carries essentially the same information as mean radius and would add very little to a model that already uses radius.

**Mean radius vs mean area.** The points follow a tight upward curve rather than a straight line, because area grows with the square of the radius. As with perimeter, mean area is almost completely determined by mean radius, so it is a redundant feature. In both scatter plots the benign cases sit at the lower end and the malignant cases at the upper end, with the same overlap in the middle seen in the histogram.

## Task 3(ii): What the subplots of Figure 2 reveal

**Mean radius vs mean concavity.** Unlike perimeter and area, concavity is only moderately related to radius (correlation 0.68), so it adds new information. Benign cases cluster at low radius and low concavity, while malignant cases have higher concavity for a given radius. Using the two features together separates the classes better than radius alone, although a few benign cases have unusually high concavity.

**Mean radius vs mean concave points.** This plot shows the clearest separation of the three. Benign cases are concentrated in the bottom-left corner (median of about 0.023 concave points) and malignant cases extend up and to the right (median of about 0.086), with a fairly narrow band of overlap. The correlation with radius is 0.82, but the scatter is wide enough that concave points still helps distinguish cases in the radius range where the classes overlap.

**Mean radius vs mean symmetry.** Symmetry is only weakly related to radius (correlation 0.15), and the two classes overlap heavily along the symmetry axis: the median is about 0.17 for benign and 0.19 for malignant. Almost all of the separation in this plot comes from radius, so mean symmetry would contribute little to a classifier.
