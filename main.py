import numpy as np
from PIL import Image
import os
import datetime
import random

def generate_art():
    # 1. 设置图片大小
    width, height = 1080, 300 # 适合做 Banner
    
    # 2. 生成随机像素数据 (这里用简单的随机噪音，你可以换成更复杂的数学公式)
    # 生成一个随机的 RGB 数组
    data = np.random.rand(height, width, 3) * 255
    
    # 3. 转换成图片对象
    img = Image.fromarray(data.astype('uint8')).convert('RGB')
    
    # 4. 确保文件夹存在
    if not os.path.exists('gallery'):
        os.makedirs('gallery')
        
    # 5. 保存图片 (按日期命名)
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"gallery/art_{date_str}.png"
    img.save(filename)
    
    return filename

def update_readme(latest_image):
    content = f"""
# 🎨 Daily Generative Art

每天由 Python 代码随机生成一张数字艺术图。

### 🖼️ 今日作品 ({datetime.datetime.now().strftime("%Y-%m-%d")})
![Daily Art]({latest_image})

---
*查看 [gallery/](gallery/) 目录浏览历史作品*
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    filename = generate_art()
    update_readme(filename)
    print(f"Generated {filename}")
