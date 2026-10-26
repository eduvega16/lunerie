"""Pone «NAIDU» legible en la esfera de una foto IA: borra las letras inventadas (inpaint) y escribe la marca con Jost.
    python marca/naidu.py entrada.png salida.png <centro_x> <centro_y> <grados>   (centro del texto actual, giro en grados antihorarios)
"""
import cv2, numpy as np, math, sys
from PIL import Image, ImageDraw, ImageFont
src, dst, cx, cy, ang = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
img = cv2.imread(src)
x0,y0,x1,y1 = int(cx-20), int(cy-22), int(cx+22), int(cy+14)
roi = img[y0:y1, x0:x1]
g = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
bg = cv2.medianBlur(g, 21)
mask = ((bg.astype(int) - g.astype(int)) > 18).astype(np.uint8) * 255   # solo lo más oscuro que el fondo
mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations=1)
img[y0:y1, x0:x1] = cv2.inpaint(roi, mask, 3, cv2.INPAINT_TELEA)
S = 8; W, H = 70*S, 24*S
lay = Image.new('L', (W, H), 0)
f = ImageFont.truetype(str(__import__('pathlib').Path(__file__).resolve().parent / 'fuentes' / 'Jost.ttf'), 17*S)
try: f.set_variation_by_axes([380])
except Exception: pass
d = ImageDraw.Draw(lay)
d.text((W/2, H/2), 'NAIDU', font=f, fill=255, anchor='mm', spacing=0)
bb = lay.getbbox(); lay = lay.crop(bb)
tw = 36*S; lay = lay.resize((tw, int(lay.height*tw/lay.width)), Image.LANCZOS)
lay = lay.rotate(ang, expand=True, resample=Image.BICUBIC)
lay = lay.resize((lay.width//S, lay.height//S), Image.LANCZOS)
a = np.array(lay).astype(float)/255*0.78
h, w = a.shape
ox, oy = int(cx - w/2), int(cy - h/2)
reg = img[oy:oy+h, ox:ox+w].astype(float)
col = np.array([30, 36, 42], float)
reg = reg*(1-a[...,None]) + col*a[...,None]
img[oy:oy+h, ox:ox+w] = reg.astype(np.uint8)
cv2.imwrite(dst, img)
