from math import sqrt


def euclidian_distance(x1, y1, x2, y2):
    """ return the distance betwenn 2 points in plan(x,y) """
    distance = sqrt(pow((x1-x2), 2)+(pow((y1-y2), 2)))
    return distance


def scalar(vector_1, vector_2):
    x = vector_1[0] * vector_2[0]
    y = vector_1[1] * vector_2[1]
    return (x, y)