from tqdm import tqdm,trange
import time
# 手动更新
with tqdm(total=100) as pbar:
    pbar.set_description("processing")
    for i in range(10):
        time.sleep(0.5)
        pbar.update(10)
# 第二种形式
pbar = trange(100)
for i in pbar:
    pbar.set_description("processing "+str(i))
    time.sleep(0.5)
pbar.close()