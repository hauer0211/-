import io
from PIL import Image, ImageDraw, ImageFont
import random

def generate_pattern(pattern_type, size):
    if pattern_type == 'shirt':
        return {"pattern": "シャツのパターン", "size": size}
    elif pattern_type == 'dress':
        return {"pattern": "ドレスのパターン", "size": size}
    elif pattern_type == 'pants':
        return {"pattern": "パンツのパターン", "size": size}
    else:
        return {"error": "不明なパターンタイプ"}

def create_dress_pattern_image(size):
    img = Image.new('RGB', (400, 600), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    
    # ドレスの基本カラー
    base_color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
    
    # ドレスのボディ部分 (上部)
    d.polygon([(200, 50), (300, 200), (100, 200)], fill=base_color, outline=(0, 0, 0))
    
    # ウエストのデザイン
    d.rectangle([150, 200, 250, 250], fill=(150, 150, 150), outline=(0, 0, 0))
    
    # スカートの部分
    d.polygon([(100, 250), (300, 250), (350, 500), (50, 500)], fill=base_color, outline=(0, 0, 0))
    
    # ストラップのデザイン
    d.line([(200, 50), (150, 100)], fill=(0, 0, 0), width=5)
    d.line([(200, 50), (250, 100)], fill=(0, 0, 0), width=5)
    
    # パターン名の表示
    font = ImageFont.load_default()
    d.text((10, 10), "ドレスのパターン", fill=(0, 0, 0), font=font)
    
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    return img_bytes.getvalue()

def create_clothing_image(pattern_type, size):
    img = Image.new('RGB', (400, 600), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    
    # ドレスの基本カラー
    base_color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
    
    if pattern_type == 'dress':
        # ドレスのボディ部分 (上部)
        d.polygon([(200, 50), (300, 200), (100, 200)], fill=base_color, outline=(0, 0, 0))
        
        # ウエストのデザイン
        d.rectangle([150, 200, 250, 250], fill=(150, 150, 150), outline=(0, 0, 0))
        
        # スカートの部分
        d.polygon([(100, 250), (300, 250), (350, 500), (50, 500)], fill=base_color, outline=(0, 0, 0))
        
        # ストラップのデザイン
        d.line([(200, 50), (150, 100)], fill=(0, 0, 0), width=5)
        d.line([(200, 50), (250, 100)], fill=(0, 0, 0), width=5)
        
        # 服の名前の表示
        font = ImageFont.load_default()
        d.text((10, 10), "ドレス", fill=(0, 0, 0), font=font)
    elif pattern_type == 'shirt':
        # シャツのボディ部分
        d.rectangle([50, 100, 250, 300], fill=base_color, outline=(0, 0, 0))
        
        # 襟の描画
        collar_color = (random.randint(150, 200), random.randint(150, 200), random.randint(150, 200))
        d.polygon([(100, 100), (200, 100), (150, 150)], fill=collar_color, outline=(0, 0, 0))
        
        # ボタンの描画
        button_color = (random.randint(100, 150), random.randint(100, 150), random.randint(100, 150))
        for y in range(150, 300, 30):
            d.ellipse([140, y, 160, y+20], fill=button_color, outline=(0, 0, 0))
        
        # 服の名前の表示
        d.text((10, 10), "シャツ", fill=(0, 0, 0))
    else:
        return None
    
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    return img_bytes.getvalue()


def create_shirt_image():
    img = Image.new('RGB', (200, 400), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    shirt_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    d.rectangle([50, 100, 150, 300], fill=shirt_color)
    d.text((10, 10), "シャツのパターン", fill=(0, 0, 0))
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    return img_bytes.getvalue()
