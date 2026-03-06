import numpy as np

class Homography:
    def __init__(self, points_source=None, points_target=None):
        self.points_source = points_source
        self.points_target = points_target
        self.matrixHomography = None

   
    def find_homography(self):
        A  = self.construct_A()
        u, s, vh = np.linalg.svd(A, full_matrices=True)
        
        # Solution to H is the last column of V, or last row of V transpose
        self.matrixHomography = vh[-1].reshape((3,3))
        return self.matrixHomography/self.matrixHomography[2,2]
    
    def getHomography(self):
        if self.matrixHomography is None:
            raise ValueError("La matriz de homografía no ha sido calculada. Llama a find_homography() primero.")
        return self.matrixHomography

    def construct_A(self):
        assert self.points_source.shape == self.points_target.shape, "Shape does not match"
        num_points = self.points_source.shape[0]

        matrices = []
        for i in range(num_points):
            partial_A = self.construct_A_partial(self.points_source[i], self.points_target[i])
            matrices.append(partial_A)
        return np.concatenate(matrices, axis=0)

    def construct_A_partial(self,point_source, point_target):
        x, y, z = point_source[0], point_source[1], 1
        x_t, y_t, z_t = point_target[0], point_target[1], 1

        A_partial = np.array([
            [0, 0, 0, -z_t*x, -z_t*y, -z_t*z, y_t*x, y_t*y, y_t*z],
            [z_t*x, z_t*y, z_t*z, 0, 0, 0, -x_t*x, -x_t*y, -x_t*z]
        ])
        return A_partial