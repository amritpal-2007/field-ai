"""
Generate ultra-realistic, high-resolution (600x600) product packaging images
for all 12 agricultural inputs with authentic branding, clear typography,
CIBRC statutory hazard diamonds, volume badges, ribbed caps, and 3D lighting.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = r"C:\Users\sherr\.gemini\antigravity\scratch\fieldai\static\img\products"
os.makedirs(BASE_DIR, exist_ok=True)

# Fonts
try:
    FONT_BRAND = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
    FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 28)
    FONT_SUBTITLE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 16)
    FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 14)
    FONT_VOLUME = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 18)
    FONT_SMALL = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
    FONT_WARN = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 13)
except Exception:
    FONT_BRAND = ImageFont.load_default()
    FONT_TITLE = ImageFont.load_default()
    FONT_SUBTITLE = ImageFont.load_default()
    FONT_BADGE = ImageFont.load_default()
    FONT_VOLUME = ImageFont.load_default()
    FONT_SMALL = ImageFont.load_default()
    FONT_WARN = ImageFont.load_default()

def draw_cibrc_diamond(draw, cx, cy, size, hazard_level="green"):
    # CIBRC Statutory Diamond (Top white, Bottom hazard color)
    colors = {
        "green": (34, 197, 94),     # Slightly toxic
        "blue": (59, 130, 246),     # Moderately toxic
        "yellow": (245, 158, 11),   # Highly toxic
        "red": (220, 38, 38)        # Extremely toxic
    }
    hazard_color = colors.get(hazard_level, (34, 197, 94))
    h = size // 2
    # Diamond outline
    diamond = [(cx, cy - h), (cx + h, cy), (cx, cy + h), (cx - h, cy)]
    draw.polygon(diamond, outline=(100, 100, 100), width=2)
    # Upper half white
    draw.polygon([(cx, cy - h), (cx + h, cy), (cx - h, cy)], fill=(255, 255, 255))
    # Lower half hazard color
    draw.polygon([(cx - h, cy), (cx + h, cy), (cx, cy + h)], fill=hazard_color)
    # Divider line
    draw.line([(cx - h, cy), (cx + h, cy)], fill=(80, 80, 80), width=2)

def generate_bottle(filename, brand, name, formula, volume, category, 
                    theme_color, cap_color, hazard_level="blue"):
    w, h = 600, 600
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. Soft Realistic Drop Shadow
    draw.ellipse([160, 520, 440, 565], fill=(0, 0, 0, 50))
    draw.ellipse([185, 528, 415, 558], fill=(0, 0, 0, 80))

    # 2. Bottle Coordinates
    bx1, by1, bx2, by2 = 175, 140, 425, 525

    # 3. Ribbed Cap
    cx1, cy1, cx2, cy2 = 245, 50, 355, 105
    # Cap shadow
    draw.rounded_rectangle([cx1, cy1, cx2, cy2], radius=8, fill=cap_color)
    # Cap ridges
    for x in range(cx1 + 8, cx2 - 8, 6):
        draw.line([(x, cy1 + 6), (x, cy2 - 6)], fill=(255, 255, 255, 90), width=2)
    # Cap seal ring
    draw.rounded_rectangle([cx1 - 4, cy2, cx2 + 4, cy2 + 10], radius=3, fill=(cap_color[0]-25, cap_color[1]-25, cap_color[2]-25))

    # 4. Bottle Neck
    draw.rectangle([258, 105, 342, 145], fill=(245, 247, 245))
    # Neck highlight
    draw.rectangle([264, 105, 276, 145], fill=(255, 255, 255, 140))

    # 5. Bottle Body (HD smooth HDPE plastic)
    draw.rounded_rectangle([bx1, by1, bx2, by2], radius=32, fill=(248, 250, 248), outline=(215, 220, 215), width=3)
    
    # 6. 3D Body Lighting (Left highlight & Right shade)
    draw.rounded_rectangle([bx1 + 10, by1 + 10, bx1 + 35, by2 - 15], radius=15, fill=(255, 255, 255, 180))
    draw.rounded_rectangle([bx2 - 25, by1 + 15, bx2 - 8, by2 - 15], radius=12, fill=(225, 228, 225, 150))

    # 7. Front Commercial Product Label
    lx1, ly1, lx2, ly2 = bx1 + 16, by1 + 55, bx2 - 16, by2 - 30
    draw.rounded_rectangle([lx1, ly1, lx2, ly2], radius=16, fill=(255, 255, 255), outline=(210, 212, 208), width=2)

    # 8. Brand Header Banner
    draw.rounded_rectangle([lx1 + 2, ly1 + 2, lx2 - 2, ly1 + 52], radius=14, fill=theme_color)
    # Brand Name Text
    draw.text((lx1 + 16, ly1 + 12), brand.upper(), font=FONT_BRAND, fill=(255, 255, 255))
    
    # Category Tag
    draw.rounded_rectangle([lx2 - 105, ly1 + 14, lx2 - 12, ly1 + 40], radius=6, fill=(255, 255, 255))
    draw.text((lx2 - 98, ly1 + 18), category[:10], font=FONT_BADGE, fill=theme_color)

    # 9. Main Product Title Block
    draw.text((lx1 + 16, ly1 + 65), name, font=FONT_TITLE, fill=(20, 35, 25))
    
    # Active Formula Block
    draw.rounded_rectangle([lx1 + 14, ly1 + 110, lx2 - 14, ly1 + 142], radius=6, fill=(245, 246, 242))
    draw.text((lx1 + 22, ly1 + 116), formula, font=FONT_SUBTITLE, fill=(40, 50, 45))

    # 10. Key Features / Benefits
    draw.text((lx1 + 18, ly1 + 155), "• CIBRC Registered Genuine Input", font=FONT_SMALL, fill=(60, 70, 65))
    draw.text((lx1 + 18, ly1 + 175), "• High Efficacy Field Formulation", font=FONT_SMALL, fill=(60, 70, 65))
    draw.text((lx1 + 18, ly1 + 195), "• Rapid Rainfastness Technology", font=FONT_SMALL, fill=(60, 70, 65))

    # 11. Net Volume Badge
    draw.rounded_rectangle([lx1 + 16, ly2 - 70, lx1 + 110, ly2 - 32], radius=8, fill=(238, 242, 238), outline=theme_color, width=2)
    draw.text((lx1 + 26, ly2 - 62), volume, font=FONT_VOLUME, fill=theme_color)

    # 12. CIBRC Statutory Warning & Hazard Diamond
    draw_cibrc_diamond(draw, lx2 - 45, ly2 - 50, size=38, hazard_level=hazard_level)
    draw.text((lx2 - 100, ly2 - 28), "CIBRC VERIFIED", font=FONT_WARN, fill=(120, 60, 10))

    # Bottom Safety Band
    draw.rectangle([lx1 + 2, ly2 - 16, lx2 - 2, ly2 - 2], fill=(22, 101, 52))

    img.save(os.path.join(BASE_DIR, filename), "PNG")
    print(f"Generated realistic bottle: {filename}")

def generate_sack(filename, brand, name, grade, weight, category,
                  theme_color, bag_color, hazard_level="green"):
    w, h = 600, 600
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Shadow
    draw.ellipse([140, 515, 460, 565], fill=(0, 0, 0, 65))

    # Sack Body
    sx1, sy1, sx2, sy2 = 150, 110, 450, 520

    # Top Stitched Closure
    draw.polygon([(sx1 + 15, sy1), (sx2 - 15, sy1), (sx2, sy1 + 28), (sx1, sy1 + 28)], 
                 fill=(theme_color[0]-30, theme_color[1]-30, theme_color[2]-30))
    # Thread stitches
    for x in range(sx1 + 18, sx2 - 15, 10):
        draw.line([(x, sy1 + 4), (x + 5, sy1 + 24)], fill=(255, 255, 255), width=2)

    # Woven Sack Bag Outline
    draw.rounded_rectangle([sx1, sy1 + 26, sx2, sy2], radius=28, fill=bag_color, outline=(200, 195, 180), width=3)

    # Subtle woven texture lines
    for y in range(sy1 + 40, sy2 - 20, 16):
        draw.line([(sx1 + 15, y), (sx2 - 15, y)], fill=(0, 0, 0, 8), width=1)

    # Central Brand Round Shield
    cx, cy = (sx1 + sx2) // 2, sy1 + 150
    draw.ellipse([cx - 85, cy - 70, cx + 85, cy + 70], fill=theme_color)
    draw.ellipse([cx - 75, cy - 60, cx + 75, cy + 60], fill=(255, 255, 255))
    
    # Brand inside shield
    draw.text((cx - 55, cy - 42), brand.upper(), font=FONT_BRAND, fill=theme_color)
    draw.text((cx - 40, cy - 8), category.upper(), font=FONT_BADGE, fill=(80, 80, 80))

    # Product Title
    draw.text((sx1 + 35, sy1 + 240), name, font=FONT_TITLE, fill=(20, 30, 20))
    
    # Grade / Nutrient Specification Banner
    draw.rounded_rectangle([sx1 + 30, sy1 + 285, sx2 - 30, sy1 + 340], radius=10, fill=theme_color)
    draw.text((sx1 + 45, sy1 + 298), grade, font=FONT_TITLE, fill=(255, 255, 255))

    # Certified Seed / Govt Standard Stamp
    draw.rounded_rectangle([sx1 + 35, sy2 - 95, sx1 + 160, sy2 - 40], radius=8, fill=(255, 255, 255), outline=theme_color, width=2)
    draw.text((sx1 + 45, sy2 - 85), "PAU CERTIFIED", font=FONT_WARN, fill=theme_color)
    draw.text((sx1 + 45, sy2 - 62), weight, font=FONT_VOLUME, fill=(20, 30, 20))

    # CIBRC Diamond
    draw_cibrc_diamond(draw, sx2 - 60, sy2 - 65, size=44, hazard_level=hazard_level)

    img.save(os.path.join(BASE_DIR, filename), "PNG")
    print(f"Generated realistic sack: {filename}")

if __name__ == "__main__":
    # 1. Tilt 25 EC (Syngenta Fungicide)
    generate_bottle("tilt.png", "Syngenta", "TILT 25% EC", "Propiconazole 25% EC", 
                    "250 ml", "Fungicide", (180, 83, 9), (180, 40, 20), hazard_level="yellow")

    # 2. Nativo 75 WG (Bayer Fungicide)
    generate_bottle("nativo.png", "Bayer", "NATIVO 75 WG", "Tebuconazole + Trifloxystrobin", 
                    "100 g", "Fungicide", (22, 101, 52), (22, 101, 52), hazard_level="blue")

    # 3. Amistar Top (Syngenta Fungicide)
    generate_bottle("amistar.png", "Syngenta", "AMISTAR TOP", "Azoxystrobin + Difenoconazole", 
                    "200 ml", "Fungicide", (2, 132, 199), (2, 132, 199), hazard_level="blue")

    # 4. Ridomil Gold MZ (Syngenta Fungicide)
    generate_bottle("ridomil.png", "Syngenta", "RIDOMIL GOLD", "Metalaxyl-M 4% + Mancozeb 64%", 
                    "500 g", "Fungicide", (217, 119, 6), (217, 119, 6), hazard_level="blue")

    # 5. Saaf (UPL Fungicide)
    generate_bottle("saaf.png", "UPL", "SAAF DUAL ACTION", "Carbendazim 12% + Mancozeb 63%", 
                    "500 g", "Fungicide", (220, 38, 38), (220, 38, 38), hazard_level="yellow")

    # 6. Confidor (Bayer Insecticide)
    generate_bottle("confidor.png", "Bayer", "CONFIDOR 17.8 SL", "Imidacloprid 17.8% SL", 
                    "250 ml", "Insecticide", (30, 64, 175), (30, 64, 175), hazard_level="yellow")

    # 7. Coragen (FMC Insecticide)
    generate_bottle("coragen.png", "FMC", "CORAGEN 18.5 SC", "Chlorantraniliprole 18.5% SC", 
                    "60 ml", "Insecticide", (21, 128, 61), (21, 128, 61), hazard_level="green")

    # 8. Neem Baan 10000 PPM (Multiplex Bio-Control)
    generate_bottle("neem.png", "Multiplex", "NEEM GUARD 10K", "Azadirachtin 10000 PPM", 
                    "500 ml", "Bio-Control", (15, 118, 110), (15, 118, 110), hazard_level="green")

    # 9. Trichoderma Viride (Multiplex Bio-Fungicide)
    generate_bottle("tricho.png", "Multiplex", "TRICHODERMA BIO", "Trichoderma Harzianum 2% WP", 
                    "1 kg", "Bio-Control", (101, 163, 13), (101, 163, 13), hazard_level="green")

    # 10. IFFCO Nano Urea
    generate_bottle("nanourea.png", "IFFCO", "NANO UREA", "Nanoscale Nitrogen 4% Foliar", 
                    "500 ml", "Fertilizer", (22, 101, 52), (22, 163, 74), hazard_level="green")

    # 11. Gromor 19:19:19 Fertilizer Sack
    generate_sack("npk19.png", "Gromor", "NPK 19-19-19", "100% Water Soluble Grade", 
                  "50 kg Sack", "Fertilizer", (180, 83, 9), (248, 246, 240), hazard_level="green")

    # 12. PAU Certified Wheat Seed
    generate_sack("seed_wheat.png", "PAU Ludhiana", "HD-3086 WHEAT", "Certified Breeder Seed", 
                  "40 kg Bag", "Certified Seed", (22, 101, 52), (242, 238, 226), hazard_level="green")

    print("All 12 realistic product images generated successfully!")
