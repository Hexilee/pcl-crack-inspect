import pcl
import numpy as np
import sys

def load(file: str) -> PointCloud:
    with open(file, "r") as file:
        points = pcl.PointCloud(np.array([[float(dot) for dot in line.split()]
                                          for line in file.readlines()], dtype=np.float32))
        return points


def main():
    points = load(sys.argv[1])
    seg = points.make_segmenter()
    seg.set_model_type(pcl.SACMODEL_PLANE)
    seg.set_method_type(pcl.SAC_RANSAC)
    indices, model = seg.segment()


if __name__ == '__main__':
    main()
