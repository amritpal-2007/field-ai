"""
Generate high-resolution, realistic agricultural product images:
- Pesticides, Fungicides, Insecticides (bottles with CIBRC toxicity triangles, caps, brand labels)
- Fertilizers & Nano Urea (IFFCO bottle with green leaf, NPK bag)
- Certified Seeds (PAU woven seed sack)
"""
import os
import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

BASE_DIR = r"C:\Users\sherr\.gemini\antigravity\scratch\fieldai\static\img\products"
os.makedirs(BASE_DIR, exist_ok=True)

def draw_cibrc_triangle(draw, x, y, size, color):
    # CIBRC statutory diamond / triangle
    half = size // 2
    # Upper triangle white, lower triangle color
    draw.polygon([(x, y - half), (x + half, y), (x - half, y)], fill=(255, 255, 255), outline=(60, 60, 60))
    draw.polygon([(x - half, y), (x + half, y), (x, y + half)], fill=color, outline=(60, 60, 60))

def create_rich_bottle(filename, brand, name, formula, cap_color, bottle_color, badge_color, hazard_color):
    w, h = 600, 600
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0)) # transparent background
    draw = ImageDraw.Draw(img)
    
    # Soft drop shadow under bottle base
    draw.ellipse([170, 520, 430, 560], fill=(0, 0, 0, 45))
    draw.ellipse([190, 525, 410, 555], fill=(0, 0, 0, 70))
    
    # Bottle Body Coordinates
    bx1, by1, bx2, by2 = 180, 160, 420, 520
    
    # Bottle Neck & Cap
    # Neck
    draw.rectangle([260, 110, 340, 165], fill=bottle_color)
    draw.rectangle([260, 110, 275, 165], fill=(255, 255, 255, 70))
    
    # Cap (Ribbed measuring cap)
    draw.rectangle([245, 60, 355, 115], fill=cap_color)
    draw.rectangle([250, 52, 350, 62], fill=(cap_color[0]-25, cap_color[1]-25, cap_color[2]-25))
    for rx in range(252, 348, 6):
        draw.line([(rx, 65), (rx, 110)], fill=(255, 255, 255, 50), width=2)
        
    # Main Bottle Body (Round-corner shape)
    # Base rounded
    draw.rounded_rectangle([bx1, by1, bx2, by2], radius=28, fill=bottle_color)
    
    # 3D Highlight reflection on left shoulder
    draw.rectangle([bx1 + 18, by1 + 10, bx1 + 38, by2 - 15], fill=(255, 255, 255, 60))
    
    # Product Label
    lx1, ly1, lx2, ly2 = bx1 + 15, by1 + 55, bx2 - 15, by2 - 25
    draw.rounded_rectangle([lx1, ly1, lx2, ly2], radius=12, fill=(255, 255, 255, 255), outline=(210, 205, 195), width=2)
    
    # Brand Top Banner
    draw.rectangle([lx1 + 2, ly1 + 2, lx2 - 2, ly1 + 48], fill=badge_color)
    
    # Draw Brand Text
    draw.rectangle([lx1 + 15, ly1 + 14, lx1 + 95, ly1 + 34], fill=(255, 255, 255, 220)) # brand tag
    
    # Product Title Banner
    draw.rectangle([lx1 + 12, ly1 + 60, lx2 - 12, ly1 + 105], fill=(245, 243, 238))
    draw.rectangle([lx1 + 18, ly1 + 70, lx2 - 18, ly1 + 95], fill=(30, 45, 35)) # main name block
    
    # Formula & Active Ingredient block
    draw.rectangle([lx1 + 18, ly1 + 115, lx2 - 18, ly1 + 130], fill=(180, 83, 9)) # sub title
    draw.rectangle([lx1 + 18, ly1 + 140, lx2 - 30, ly1 + 150], fill=(100, 110, 105))
    draw.rectangle([lx1 + 18, ly1 + 158, lx2 - 50, ly1 + 168], fill=(140, 150, 145))
    draw.rectangle([lx1 + 18, ly1 + 176, lx2 - 40, ly1 + 186], fill=(140, 150, 145))
    
    # CIBRC Statutory Warning & Diamond
    draw_cibrc_triangle(draw, lx1 + 50, ly2 - 40, 36, hazard_color)
    
    # Regulatory green text band
    draw.rectangle([lx1 + 80, ly2 - 48, lx2 - 15, ly2 - 32], fill=(22, 101, 52))
    draw.rectangle([lx1 + 80, ly2 - 26, lx2 - 40, ly2 - 16], fill=(160, 165, 160))
    
    # Save Image
    img.save(os.path.join(BASE_DIR, filename), "PNG")
    print(f"Generated rich bottle {filename}")

def create_rich_bag(filename, brand, name, grade, bag_color, accent_color):
    w, h = 600, 600
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Shadow
    draw.ellipse([140, 520, 460, 560], fill=(0, 0, 0, 50))
    
    # Sack body coordinates
    sx1, sy1, sx2, sy2 = 160, 120, 440, 520
    
    # Top stitched border
    draw.polygon([(sx1 + 10, sy1), (sx2 - 10, sy1), (sx2, sy1 + 30), (sx1, sy1 + 30)], fill=(accent_color[0]-30, accent_color[1]-30, accent_color[2]-30))
    for x in range(sx1 + 15, sx2 - 15, 8):
        draw.line([(x, sy1 + 5), (x + 4, sy1 + 25)], fill=(255, 255, 255), width=2)
        
    # Sack polygon with slight outward bulges
    draw.rounded_rectangle([sx1, sy1 + 25, sx2, sy2], radius=24, fill=bag_color, outline=(190, 185, 175), width=3)
    
    # Center Brand Emblem
    cx = (sx1 + sx2) // 2
    draw.ellipse([cx - 95, sy1 + 65, cx + 95, sy1 + 255], fill=accent_color)
    draw.ellipse([cx - 85, sy1 + 75, cx + 85, sy1 + 245], fill=(255, 255, 255))
    
    # Fertilizer / Seed large icon inside emblem
    draw.rectangle([cx - 65, sy1 + 120, cx + 65, sy1 + 150], fill=accent_color)
    draw.rectangle([cx - 50, sy1 + 160, cx + 50, sy1 + 180], fill=(30, 40, 30))
    draw.rectangle([cx - 35, sy1 + 190, cx + 35, sy1 + 205], fill=(120, 130, 120))
    
    # Bottom Nutrient / Spec Bars
    draw.rectangle([sx1 + 25, sy1 + 280, sx2 - 25, sy1 + 330], fill=(245, 240, 230))
    draw.rectangle([sx1 + 35, sy1 + 295, sx2 - 35, sy1 + 315], fill=(20, 60, 35))
    
    # Certified seed tag / ISI stamp
    draw.rectangle([sx1 + 40, sy2 - 70, sx1 + 110, sy2 - 20], fill=(22, 101, 52))
    draw.rectangle([sx1 + 130, sy2 - 60, sx2 - 40, sy2 - 30], fill=(120, 125, 120))
    
    img.save(os.path.join(BASE_DIR, filename), "PNG")
    print(f"Generated rich bag {filename}")

if __name__ == "__main__":
    # Pesticides & Fungicides
    create_rich_bottle("tilt.png", "Syngenta", "TILT 25% EC", "Propiconazole 25% EC", 
                       (180, 40, 20), (242, 245, 240), (180, 83, 9), (217, 119, 6))
    create_rich_bottle("nativo.png", "Bayer", "NATIVO 75 WG", "Tebuconazole + Trifloxy", 
                       (22, 101, 52), (245, 248, 242), (22, 101, 52), (34, 197, 94))
    create_rich_bottle("amistar.png", "Syngenta", "AMISTAR TOP", "Azoxystrobin + Difen", 
                       (2, 132, 199), (240, 246, 250), (2, 132, 199), (56, 189, 248))
    create_rich_bottle("ridomil.png", "Syngenta", "RIDOMIL GOLD", "Metalaxyl-M + Mancozeb", 
                       (217, 119, 6), (248, 244, 236), (217, 119, 6), (234, 179, 8))
    create_rich_bottle("saaf.png", "UPL", "SAAF FUNGICIDE", "Carbendazim + Mancozeb", 
                       (220, 38, 38), (246, 242, 242), (220, 38, 38), (239, 68, 68))
    create_rich_bottle("confidor.png", "Bayer", "CONFIDOR 17.8 SL", "Imidacloprid 17.8%", 
                       (30, 64, 175), (244, 246, 242), (22, 101, 52), (245, 158, 11))
    create_rich_bottle("coragen.png", "FMC", "CORAGEN 18.5 SC", "Chlorantraniliprole", 
                       (21, 128, 61), (245, 250, 245), (21, 128, 61), (34, 197, 94))
    create_rich_bottle("neem.png", "Multiplex", "NEEM BAAN 10000", "Azadirachtin Organic", 
                       (19, 78, 74), (235, 245, 238), (15, 118, 110), (34, 197, 94))
    create_rich_bottle("nanourea.png", "IFFCO", "NANO UREA LIQUID", "Nanoscale Nitrogen 4%", 
                       (34, 197, 94), (250, 250, 248), (22, 101, 52), (34, 197, 94))
    create_rich_bottle("tricho.png", "IPL", "TRICHODERMA VIRIDE", "Bio-Fungicide 1.5%", 
                       (13, 148, 136), (242, 248, 244), (13, 148, 136), (34, 197, 94))
                       
    # Fertilizers & Seeds Bags
    create_rich_bag("npk19.png", "Mahadhan", "NPK 19:19:19", "Water Soluble Foliar", 
                    (245, 240, 232), (147, 51, 234))
    create_rich_bag("seed_wheat.png", "PAU", "PBW-826 WHEAT", "Certified Rust Tolerant", 
                    (238, 232, 220), (180, 83, 9))
    print("All rich product images regenerated successfully!")
