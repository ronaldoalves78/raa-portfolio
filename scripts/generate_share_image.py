from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "images" / "compartilhamento-raa.png"
WIDTH, HEIGHT = 1200, 630


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


regular = font(r"C:\Windows\Fonts\arial.ttf", 30)
bold = font(r"C:\Windows\Fonts\arialbd.ttf", 72)
logo = font(r"C:\Windows\Fonts\arialbd.ttf", 50)
mono = font(r"C:\Windows\Fonts\consolab.ttf", 23)
small_bold = font(r"C:\Windows\Fonts\arialbd.ttf", 24)

image = Image.new("RGB", (WIDTH, HEIGHT), "#f6f6f6")
draw = ImageDraw.Draw(image)

for x in range(0, WIDTH, 32):
    draw.line((x, 0, x, HEIGHT), fill="#ececec", width=1)
for y in range(0, HEIGHT, 32):
    draw.line((0, y, WIDTH, y), fill="#ececec", width=1)

draw.rectangle((0, 0, 38, HEIGHT), fill="#000000")
draw.rectangle((78, 72, 142, 136), fill="#000000")
draw.text((110, 104), "R", font=logo, fill="#ffffff", anchor="mm")
draw.text((78, 184), "RONALDO", font=bold, fill="#000000")
draw.text((78, 270), "ALMEIDA ALVES", font=bold, fill="#000000")
draw.rectangle((82, 372, 670, 376), fill="#000000")
draw.text((78, 410), "SUPERVISOR / COORDENADOR INDUSTRIAL", font=mono, fill="#333333")
draw.text((78, 462), "Qualidade · Processos · Produção · PCP", font=regular, fill="#333333")

draw.rectangle((895, 72, 1122, 558), fill="#0d0d0d")
draw.text((930, 112), "20+", font=bold, fill="#ffffff")
draw.text((932, 196), "ANOS DE", font=small_bold, fill="#b3b3b3")
draw.text((932, 230), "EXPERIÊNCIA", font=small_bold, fill="#b3b3b3")
draw.line((930, 302, 1088, 302), fill="#555555", width=2)
draw.text((932, 344), "ISO 9001", font=mono, fill="#ffffff")
draw.text((932, 390), "IATF 16949", font=mono, fill="#ffffff")
draw.text((932, 436), "APQP · PPAP", font=mono, fill="#ffffff")
draw.text((932, 482), "MASP · 8D", font=mono, fill="#ffffff")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
image.save(OUTPUT, "PNG", optimize=True)
print(OUTPUT)
