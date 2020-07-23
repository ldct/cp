
import math

class vec3(tuple):

    @property 
    def x(self): return self[0]
    @property
    def y(self): return self[1]
    @property
    def z(self): return self[2]

    def __matmul__(v1, v2): return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    def __xor__(v1, v2):
        x = v1.y * v2.z - v1.z * v2.y
        y = v1.z * v2.x - v1.x * v2.z
        z = v1.x * v2.y - v1.y * v2.x
        return vec3((x, y, z))

    @staticmethod
    def triangle_area2(a, b, c):
        return ((a-b) ^ (a-c)).norm2()

    @staticmethod
    def coplanar(a, b, c):
        # the lines OB, OC, OA are coplanar
        return 0 == a @ (b ^ c)

    def norm2(self): return self @ self
    def norm(self): return math.sqrt(self.norm2)

    def __add__(self, v): return vec3((self.x + v.x, self.y + v.y, self.z + v.z))
    def __neg__(self): return vec3((-self.x, -self.y, -self.z))
    def __sub__(self, v): return self + (-v)

    def __mul__(self, v):
        if isinstance(v, vec3):
            return vec3(self.x * v.x, self.y * v.y, self.z * v.z)
        else:
            return vec3(self.x * v, self.y * v, self.z * v)

    def __rmul__(self, v):
        return self.__mul__(v)

    def __div__(self, v):
        if isinstance(v, vec3):
            return vec3(self.x / v.x, self.y / v.y, self.z / v.z)
        else:
            return vec3(self.x / v, self.y / v, self.z / v)
