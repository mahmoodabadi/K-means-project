# K-means Project

The K-Means clustering algorithm is a popular unsupervised machine learning technique used for partitioning a dataset into K distinct clusters. The goal of the algorithm is to minimize the sum of squared distances between data points and their assigned cluster centroids. The algorithm works by first randomly initializing K cluster centroids, and then iteratively updating the cluster assignments and centroid locations until convergence. Specifically, in each iteration, data points are assigned to the nearest centroid, and then the centroids are recalculated as the mean of the data points in each cluster. This process continues until the cluster assignments no longer change significantly between iterations. K-Means is a simple and efficient algorithm, but it has some limitations, such as being sensitive to the initial centroid locations and the assumption that clusters are spherical and have equal variance. Despite these limitations, K-Means is widely used in a variety of applications, such as customer segmentation, image compression, and anomaly detection.
## Introduction

The purpose of this project is to solve K-means problem using some points in a 3d space. We read te points from a txt file and then try to find k centers that are nearest to the points.

## Code

Here's the Python code for a part of the "K-means" project that reads the points from the file:

```python
import numpy as np
from random import randint
from math import sqrt


def read_points(filename):
    with open(filename, 'r') as f:
        points = []
        for line in f:
            if '?' in line:
                continue
            x, y, z = line.strip().split(',')
            if y == '' or x=='' or z=='':
                continue
            x = float(x)
            y = float(y)
            z = float(z)
            points.append((x, y, z))
    return points

def clean_points(points):
    cleaned_points = []
    for point in points:
        if all(np.isfinite(point)):
            cleaned_points.append(point)
    return cleaned_points
'''
