from tqdm import tqdm

a = 0
with tqdm() as pbar:
    while True:
        a += 1
        print(a)
        pbar.update(1)
