import numpy as np

# Создаем массив из массивов разной длины
array_of_arrays = np.array([np.array([1, 2, 3]),
                            np.array([4, 5, 6, 7]),
                            np.array([8, 9])], dtype=object)

# Выводим результат
print(array_of_arrays)
