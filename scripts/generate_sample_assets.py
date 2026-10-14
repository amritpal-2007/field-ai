"""
Generate high-fidelity agricultural visual assets:
- Authentic leaf pathology patterns (Wheat Yellow Rust, Rice Blast, Cotton Leaf Curl, etc.)
- Product packaging graphics
- Hero banner visual
"""
import os
import math
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

BASE_DIR = r"C:\Users\sherr\.gemini\antigravity\scratch\fieldai\static\img"
SAMPLES_DIR = os.path.join(BASE_DIR, "samples")
PRODUCTS_DIR = os.path.join(BASE_DIR, "products")

os.makedirs(SAMPLES_DIR, exist_ok=True)
os.makedirs(PRODUCTS_DIR, exist_ok=True)

def create_wheat_yellow_rust():
    w, h = 800, 600
    img = Image.new("RGB", (w, h), (38, 70, 40))
    draw = ImageDraw.Draw(img)
    
    # Gradient wheat leaf background
    for y in range(h):
        r = int(35 + 20 * (y / h))
        g = int(75 + 30 * math.sin(y / 100))
        b = int(32 + 10 * (y / h))
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    
    # Veins
    for x in range(40, w, 22):
        draw.line([(x, 0), (x, h)], fill=(48, 92, 42), width=2)
    # Midrib
    draw.line([(w//2, 0), (w//2, h)], fill=(75, 125, 60), width=8)
    draw.line([(w//2-1, 0), (w//2-1, h)], fill=(90, 140, 75), width=3)
    
    # Yellow rust linear pustule stripes
    random.seed(42)
    stripe_x_positions = [140, 180, 220, 260, 310, 480, 520, 560, 610, 650]
    for sx in stripe_x_positions:
        cur_y = random.randint(30, 80)
        while cur_y < h - 50:
            p_len = random.randint(15, 65)
            # draw strip of yellow/orange uredinia pustules
            for py in range(cur_y, cur_y + p_len, 4):
                px = sx + random.randint(-4, 4)
                pw = random.randint(5, 9)
                col = random.choice([
                    (234, 179, 8),    # bright yellow
                    (250, 204, 21),   # yellow-gold
                    (217, 119, 6),    # golden amber
                    (245, 158, 11),   # rich orange
                    (180, 83, 9)      # dark rusty edge
                ])
                draw.ellipse([px, py, px + pw, py + 5], fill=col)
            cur_y += p_len + random.randint(8, 25)
            
    # Add subtle blur for organic spore texture
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img.save(os.path.join(SAMPLES_DIR, "wheat_yellow_rust.jpg"), quality=92)
    print("Generated wheat_yellow_rust.jpg")

def create_rice_blast():
    w, h = 800, 600
    img = Image.new("RGB", (w, h), (34, 85, 45))
    draw = ImageDraw.Draw(img)
    
    for y in range(h):
        draw.line([(0, y), (w, y)], fill=(int(30 + 15 * (y/h)), int(85 + 25 * math.cos(y/120)), 42))
        
    for x in range(30, w, 28):
        draw.line([(x, 0), (x, h)], fill=(45, 110, 55), width=2)
    draw.line([(w//2, 0), (w//2, h)], fill=(70, 135, 75), width=7)
    
    # Diamond / Spindle blast lesions
    random.seed(101)
    lesions = [
        (260, 160, 90, 45), (420, 240, 120, 55), (310, 380, 110, 50),
        (540, 190, 80, 40), (490, 390, 95, 48), (200, 310, 75, 38)
    ]
    for lx, ly, lw, lh in lesions:
        # Yellow chlorotic halo
        draw.ellipse([lx - 15, ly - 10, lx + lw + 15, ly + lh + 10], fill=(160, 140, 40))
        # Brown necrotic ring
        draw.ellipse([lx - 5, ly - 4, lx + lw + 5, ly + lh + 4], fill=(120, 45, 25))
        # Grey-ash center
        draw.ellipse([lx + 10, ly + 8, lx + lw - 10, ly + lh - 8], fill=(165, 165, 165))
        # Spindle tips
        draw.polygon([(lx - 12, ly + lh//2), (lx + lw//2, ly - 8), (lx + lw + 12, ly + lh//2), (lx + lw//2, ly + lh + 8)], outline=(95, 30, 20), width=2)

    img = img.filter(ImageFilter.SMOOTH)
    img.save(os.path.join(SAMPLES_DIR, "rice_blast.jpg"), quality=92)
    print("Generated rice_blast.jpg")

def create_cotton_leaf_curl():
    w, h = 800, 600
    img = Image.new("RGB", (w, h), (26, 68, 38))
    draw = ImageDraw.Draw(img)
    
    # Curled undulating leaf texture
    for y in range(h):
        for x in range(0, w, 20):
            val = int(55 + 30 * math.sin(x/50) * math.cos(y/60))
            draw.rectangle([x, y, x+20, y+2], fill=(22, val, 30))
            
    # Thickened prominent veins (characteristic enations & vein thickening)
    main_veins = [
        [(w//2, h), (w//2, 120)],
        [(w//2, 380), (140, 180)],
        [(w//2, 380), (660, 180)],
        [(w//2, 480), (120, 340)],
        [(w//2, 480), (680, 340)]
    ]
    for pts in main_veins:
        draw.line(pts, fill=(120, 175, 75), width=9)
        draw.line(pts, fill=(165, 215, 95), width=4)
        
    # Secondary thickened twisted network
    random.seed(88)
    for _ in range(45):
        vx1 = random.randint(180, 620)
        vy1 = random.randint(150, 480)
        vx2 = vx1 + random.randint(-60, 60)
        vy2 = vy1 + random.randint(-50, 50)
        draw.line([(vx1, vy1), (vx2, vy2)], fill=(140, 190, 80), width=3)
        
    img = img.filter(ImageFilter.SMOOTH)
    img.save(os.path.join(SAMPLES_DIR, "cotton_leaf_curl.jpg"), quality=92)
    print("Generated cotton_leaf_curl.jpg")

def create_mustard_white_rust():
    w, h = 800, 600
    img = Image.new("RGB", (w, h), (42, 88, 48))
    draw = ImageDraw.Draw(img)
    
    # Mustard broad leaf surface
    for y in range(h):
        draw.line([(0, y), (w, y)], fill=(int(36 + 18 * (y/h)), int(88 + 20 * math.sin(y/80)), 46))
        
    # Chalky white blister pustules
    random.seed(67)
    for _ in range(70):
        bx = random.randint(120, 680)
        by = random.randint(80, 520)
        br = random.randint(6, 18)
        # pale yellow chlorotic ring around blister
        draw.ellipse([bx - br - 4, by - br - 4, bx + br + 4, by + br + 4], fill=(125, 145, 55))
        # chalky white raised blister
        draw.ellipse([bx - br, by - br, bx + br, by + br], fill=(245, 248, 245))
        draw.ellipse([bx - br + 2, by - br + 2, bx + br - 2, by + br - 2], fill=(255, 255, 255))
        
    img = img.filter(ImageFilter.SMOOTH)
    img.save(os.path.join(SAMPLES_DIR, "mustard_white_rust.jpg"), quality=92)
    print("Generated mustard_white_rust.jpg")

def create_potato_late_blight():
    w, h = 800, 600
    img = Image.new("RGB", (w, h), (45, 95, 50))
    draw = ImageDraw.Draw(img)
    
    for y in range(h):
        draw.line([(0, y), (w, y)], fill=(int(40 + 12 * (y/h)), int(90 + 20 * math.sin(y/90)), 48))
        
    # Large water-soaked dark brownish-black necrotic blotches
    random.seed(99)
    spots = [
        (220, 180, 160, 140), (450, 260, 190, 160), (320, 390, 150, 120),
        (520, 120, 130, 110), (140, 310, 110, 100)
    ]
    for sx, sy, sw, sh in spots:
        # Water-soaked greasy edge
        draw.ellipse([sx - 15, sy - 15, sx + sw + 15, sy + sh + 15], fill=(70, 85, 38))
        # Dark necrotic blotch
        draw.ellipse([sx, sy, sx + sw, sy + sh], fill=(35, 25, 20))
        # Inner rotting black core
        draw.ellipse([sx + 20, sy + 20, sx + sw - 20, sy + sh - 20], fill=(22, 16, 14))
        # Delicate white mold rim
        draw.arc([sx - 5, sy - 5, sx + sw + 5, sy + sh + 5], start=45, end=225, fill=(230, 235, 230), width=4)
        
    img = img.filter(ImageFilter.SMOOTH)
    img.save(os.path.join(SAMPLES_DIR, "potato_late_blight.jpg"), quality=92)
    print("Generated potato_late_blight.jpg")

def create_tomato_early_blight():
    w, h = 800, 600
    img = Image.new("RGB", (w, h), (38, 88, 44))
    draw = ImageDraw.Draw(img)
    
    for y in range(h):
        draw.line([(0, y), (w, y)], fill=(int(35 + 15*(y/h)), int(85 + 25*math.cos(y/100)), 40))
        
    # Concentric target-board rings
    targets = [(280, 220, 70), (480, 310, 85), (360, 420, 60), (550, 180, 50)]
    for tx, ty, tr in targets:
        # Chlorotic yellow halo
        draw.ellipse([tx - tr - 25, ty - tr - 25, tx + tr + 25, ty + tr + 25], fill=(160, 145, 35))
        # Concentric dark brown rings
        for r_step in range(tr, 10, -12):
            col = (65, 32, 15) if (r_step // 12) % 2 == 0 else (45, 20, 10)
            draw.ellipse([tx - r_step, ty - r_step, tx + r_step, ty + r_step], fill=col)
        # Center core
        draw.ellipse([tx - 12, ty - 12, tx + 12, ty + 12], fill=(28, 12, 6))

    img = img.filter(ImageFilter.SMOOTH)
    img.save(os.path.join(SAMPLES_DIR, "tomato_early_blight.jpg"), quality=92)
    print("Generated tomato_early_blight.jpg")

def create_product_graphic(filename, brand, prod_name, formula, badge_col, bg_col):
    w, h = 500, 500
    img = Image.new("RGB", (w, h), (247, 246, 242)) # Warm cream card bg
    draw = ImageDraw.Draw(img)
    
    # Rounded container bottle shape
    bx, by, bw, bh = 140, 90, 220, 330
    
    # Cap
    draw.rectangle([190, 60, 310, 95], fill=(40, 45, 42))
    draw.rectangle([200, 50, 300, 60], fill=(25, 30, 28))
    
    # Bottle neck & body
    draw.rectangle([bx, by, bx + bw, by + bh], fill=bg_col)
    # Highlights / reflections
    draw.rectangle([bx + 15, by + 10, bx + 35, by + bh - 10], fill=(255, 255, 255))
    
    # Product Label
    lx, ly, lw, lh = bx + 20, by + 60, bw - 40, bh - 100
    draw.rectangle([lx, ly, lx + lw, ly + lh], fill=(255, 255, 255))
    
    # Label Header Banner
    draw.rectangle([lx, ly, lx + lw, ly + 40], fill=badge_col)
    
    # CIBRC triangle (statutory safety mark)
    draw.polygon([(lx + lw - 30, ly + lh - 10), (lx + lw - 10, ly + lh - 10), (lx + lw - 20, ly + lh - 30)], fill=badge_col)
    
    # Text lines on label
    draw.rectangle([lx + 15, ly + 55, lx + lw - 15, ly + 68], fill=(30, 35, 30))
    draw.rectangle([lx + 15, ly + 76, lx + lw - 35, ly + 85], fill=(80, 85, 80))
    draw.rectangle([lx + 15, ly + 95, lx + lw - 20, ly + 102], fill=(140, 145, 140))
    draw.rectangle([lx + 15, ly + 108, lx + lw - 40, ly + 115], fill=(140, 145, 140))
    
    # Green triangle stamp
    draw.rectangle([lx + 15, ly + lh - 25, lx + 70, ly + lh - 10], fill=(22, 101, 52))
    
    img = img.filter(ImageFilter.SMOOTH)
    img.save(os.path.join(PRODUCTS_DIR, filename), quality=92)
    print(f"Generated product {filename}")

def create_hero_visual():
    w, h = 960, 640
    img = Image.new("RGB", (w, h), (26, 62, 38))
    draw = ImageDraw.Draw(img)
    
    # Sky & golden agricultural horizon
    for y in range(240):
        r = int(190 + 35 * (y / 240))
        g = int(215 + 25 * (y / 240))
        b = int(210 - 20 * (y / 240))
        draw.line([(0, y), (w, y)], fill=(r, g, b))
        
    # Distant lush trees & field horizon
    for x in range(0, w, 15):
        tree_h = int(220 + 20 * math.sin(x / 40))
        draw.ellipse([x - 20, tree_h - 25, x + 35, tree_h + 30], fill=(42, 85, 45))
        
    # Vast lush green wheat field foreground
    for y in range(240, h):
        factor = (y - 240) / (h - 240)
        r = int(28 + 22 * factor)
        g = int(85 + 40 * factor + 10 * math.sin(y / 15))
        b = int(32 + 18 * factor)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
        
    # Golden wheat awns & stalks swaying
    random.seed(55)
    for _ in range(400):
        wx = random.randint(0, w)
        wy = random.randint(280, h)
        w_len = random.randint(35, 75)
        w_tilt = random.randint(-15, 20)
        draw.line([(wx, wy), (wx + w_tilt, wy - w_len)], fill=(185, 175, 65), width=2)
        draw.ellipse([wx + w_tilt - 3, wy - w_len - 8, wx + w_tilt + 4, wy - w_len + 4], fill=(215, 195, 85))

    # Realistic Farmer holding phone silhouette & warm lighting
    fx, fy = 480, 180
    # Head & turban (saffron/cream turban)
    draw.ellipse([fx - 38, fy, fx + 38, fy + 75], fill=(217, 119, 6)) # Turban top
    draw.ellipse([fx - 34, fy + 20, fx + 34, fy + 78], fill=(245, 158, 11))
    draw.ellipse([fx - 26, fy + 48, fx + 26, fy + 95], fill=(180, 120, 85)) # Face tone
    
    # Torso (Kurta - subtle cream white)
    draw.polygon([(fx - 75, fy + 120), (fx + 75, fy + 120), (fx + 95, fy + 380), (fx - 95, fy + 380)], fill=(240, 238, 230))
    
    # Arms holding modern smartphone
    # Left forearm to center
    draw.line([(fx - 70, fy + 170), (fx - 15, fy + 240)], fill=(180, 120, 85), width=24)
    # Right forearm to center
    draw.line([(fx + 70, fy + 170), (fx + 25, fy + 235)], fill=(180, 120, 85), width=24)
    
    # Modern Smartphone in hands
    sp_x, sp_y, sp_w, sp_h = fx - 28, fy + 195, 62, 108
    # Phone body
    draw.rectangle([sp_x, sp_y, sp_x + sp_w, sp_y + sp_h], fill=(20, 24, 28))
    # Glowing screen with crop scanning viewfinder
    draw.rectangle([sp_x + 3, sp_y + 4, sp_x + sp_w - 3, sp_y + sp_h - 4], fill=(30, 75, 45))
    # Screen UI line elements (scanning line)
    draw.line([(sp_x + 8, sp_y + 48), (sp_x + sp_w - 8, sp_y + 48)], fill=(34, 197, 94), width=2)
    draw.rectangle([sp_x + 12, sp_y + 25, sp_x + sp_w - 12, sp_y + 70], outline=(74, 222, 128), width=1)
    
    img = img.filter(ImageFilter.SMOOTH)
    img.save(os.path.join(BASE_DIR, "hero_farmer.jpg"), quality=94)
    print("Generated hero_farmer.jpg")

if __name__ == "__main__":
    create_wheat_yellow_rust()
    create_rice_blast()
    create_cotton_leaf_curl()
    create_mustard_white_rust()
    create_potato_late_blight()
    create_tomato_early_blight()
    
    create_product_graphic("tilt.png", "Syngenta", "Tilt 25% EC", "Propiconazole", (180, 83, 9), (220, 235, 220))
    create_product_graphic("nativo.png", "Bayer", "Nativo 75 WG", "Tebuconazole+Trifloxy", (22, 101, 52), (240, 245, 238))
    create_product_graphic("amistar.png", "Syngenta", "Amistar Top", "Azoxystrobin+Difen", (2, 132, 199), (230, 240, 245))
    create_product_graphic("ridomil.png", "Syngenta", "Ridomil Gold", "Metalaxyl+Mancozeb", (217, 119, 6), (245, 240, 230))
    create_product_graphic("saaf.png", "UPL", "Saaf Fungicide", "Carbendazim+Mancozeb", (220, 38, 38), (240, 230, 230))
    create_product_graphic("confidor.png", "Bayer", "Confidor", "Imidacloprid 17.8%", (22, 101, 52), (235, 245, 235))
    create_product_graphic("coragen.png", "FMC", "Coragen 18.5 SC", "Chlorantraniliprole", (21, 128, 61), (225, 245, 230))
    create_product_graphic("neem.png", "Multiplex", "Neem Baan 10,000", "Azadirachtin Bio", (67, 56, 202), (235, 235, 245))
    create_product_graphic("tricho.png", "IPL", "Trichoderma Viride", "Bio-Fungicide", (21, 128, 61), (230, 240, 230))
    create_product_graphic("nanourea.png", "IFFCO", "Nano Urea", "Liquid Nitrogen", (22, 101, 52), (235, 245, 235))
    create_product_graphic("npk19.png", "Mahadhan", "NPK 19:19:19", "Water Soluble", (147, 51, 234), (245, 235, 248))
    create_product_graphic("seed_wheat.png", "PAU", "PBW-826 Wheat", "Certified Seed", (180, 83, 9), (245, 240, 225))
    
    create_hero_visual()
    print("All sample agricultural assets generated successfully!")
