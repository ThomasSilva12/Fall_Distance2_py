def fall_distance(time):

    gravity = 9.8
    dist = 0.5 * gravity * (time ** 2)
    return dist

dist = fall_distance(3.2)
print(dist)

