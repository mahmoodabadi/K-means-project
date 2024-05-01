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

def k_means(points, k):
    
    centroids = np.random.uniform(low=-10.0, high=10.0, size=(k, 3))

    print(centroids)
    while True:
        clusters = [[] for _ in range(k)]
        for point in points:
            centroid_idx = np.argmin(np.linalg.norm(points - centroid, axis=1) for centroid in centroids)
            clusters[centroid_idx].append(point)

        # Update the centroids to be the mean of the points in each cluster
        new_centroids = []
        for cluster in clusters:
            if cluster:
                new_centroids.append(np.mean(cluster, axis=0))
            else:
                new_centroids.append(np.zeros(3))

        # Check if the centroids have converged
        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

    final_clusters = [[] for _ in range(k)]
    for point in points:
        centroid_idx = np.argmin(np.linalg.norm(points - centroid, axis=1) for centroid in centroids)
        final_clusters[centroid_idx].append(point)

    return final_clusters

filename = 'H:\daneshkar\points.txt'
points = read_points(filename)

points = clean_points(points)
k = int(input("Enter the number of clusters:"))
clusters = k_means(points, k)

for i, cluster in enumerate(clusters):
    print(f'Cluster {i}: {cluster}')