import numpy as np
import pcl
import pcl.pcl_visualization


class line:
    cloud = pcl.PointCloud()

    def __init__(self, x0, y0, z0, m, n, p, start_x, end_x, interval=0.1):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.m = m
        self.n = n
        self.p = p
        self.start_x = start_x
        self.end_x = end_x
        self.interval = interval
        self.x_intervals = np.arange(self.start_x, self.end_x, self.interval)
        self.y_intervals = (self.x_intervals - x0) / m * n + y0
        self.z_intervals = (self.x_intervals - x0) / m * p + z0
        self.points = np.vstack((self.x_intervals, self.y_intervals, self.z_intervals)).T

    def generate_points(self):
        # self.cloud.width = self.x_intervals.size
        # self.cloud.height = 1
        # self.cloud.points.resize(self.cloud.width * self.cloud.height)
        self.cloud.from_array(self.points.astype('float32'))

    def show(self):
        viewer = pcl.pcl_visualization.PCLVisualizering('3D Viewer')
        pccolor = pcl.pcl_visualization.PointCloudColorHandleringCustom(
            self.cloud, 255, 255, 255)
        # OK
        viewer.AddPointCloud_ColorHandler(self.cloud, pccolor)
        v = True
        while v:
            v = not (viewer.WasStopped())
            viewer.SpinOnce()


if __name__ == "__main__":
    test_line = line(0, 0, 0, 1, 1, 1, 0, 100)
    test_line.generate_points()
    test_line.show()
