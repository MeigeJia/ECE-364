class Rectangle:
    def __init__(self, llpoint, urpoint):
        (xll, yll) = llpoint
        (xur, yur) = urpoint

        if not (xll < xur and yll < yur):
            raise ValueError("Lower-Left point must be less than Upper-Right point")
        self.lowerLeft = llpoint
        self.upperRight = urpoint

    def isSquare(self):
        (xll, yll) = self.lowerLeft
        (xur, yur) = self.upperRight

        if (xur-xll == yur-yll):
            return True
        return False

    def isPointInside(self, point):
        (xll, yll) = self.lowerLeft
        (xur, yur) = self.upperRight
        (x, y) = point

        if xll < x < xur and yll < y < yur:
            return True
        return False

    def intersectsWith(self, rect):
        (xll, yll) = rect.lowerLeft
        (xur, yur) = rect.upperRight
        (xul, yul) = (xll, yur)
        (xlr, ylr) = (xur, yll)

        corners = [(xll, yll), (xur, yur), (xul, yul), (xlr, ylr)]
        for corner in corners:
            if self.isPointInside(corner):
                return True
        return False
