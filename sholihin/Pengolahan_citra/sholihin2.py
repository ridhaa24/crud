import numpy as np

# Data RGB dari soal
rgb_values = [
    (65, 36, 0), (24, 56, 202), (37, 75, 76), (234, 32, 36),
    (36, 34, 34), (49, 48, 46), (35, 222, 54), (212, 35, 33),
    (54, 49, 48), (56, 23, 103), (35, 45, 55), (10, 11, 12),
    (11, 12, 10), (12, 10, 11), (25, 35, 46), (54, 38, 46),
    (109, 111, 244), (58, 34, 66), (32, 74, 13), (54, 58, 57),
    (235, 34, 63), (63, 63, 73), (54, 64, 54), (207, 252, 43),
    (20, 30, 60)
]

# Ubah RGB ke grayscale secara manual
grayscale_values = [
    int(0.299*r + 0.587*g + 0.114*b) for r, g, b in rgb_values
]

print("Grayscale Values:")
print(grayscale_values)