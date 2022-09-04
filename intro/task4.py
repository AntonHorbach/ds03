import random
import math


def rand_vec(dim=3):
    return [random.uniform(0, 100) for i in range(dim)]


def vec_len(vec):
    return math.sqrt(sum(i**2 for i in vec))


def cosine_similarity(f_vec, s_vec):
    return sum(f * s for f, s in zip(f_vec, s_vec)) / (vec_len(f_vec) * vec_len(s_vec))


def cosine_distance(f_vec, s_vec):
    return 1.0 - cosine_similarity(f_vec, s_vec)


vectors = [rand_vec() for i in range(3)]

for first_vec in vectors:
    for second_vec in vectors:
        dist = cosine_distance(first_vec, second_vec)
        print(f"Cosine distance between {first_vec} and {second_vec} is {dist}")
