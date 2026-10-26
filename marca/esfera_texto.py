import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont
F = 'D:/LUNERIE/marca/fuentes/Jost.ttf'
img = cv2.imread('prodD2.png')
C = np.array([940., 1152.])                 # eje de las agujas
v12 = np.array([1093., 1015.]) - C          # hacia las 12 (índice doble)
u3 = np.array([1070., 1245.]) - C           # hacia las 3
eu = u3 / np.linalg.norm(u3); ev = -v12 / np.linalg.norm(v12)   # eje del texto (x) y hacia abajo (y)

def texto(t, alto, peso, espacio, centro, alpha, color=(42, 40, 38)):
    S = 6
    f = ImageFont.truetype(F, alto * S)
    try: f.set_variation_by_axes([peso])
    except Exception: pass
    # letra a letra para poder espaciar
    anchos = [f.getbbox(c)[2] - f.getbbox(c)[0] for c in t]
    W = int(sum(anchos) + espacio * S * (len(t) - 1) + 4 * S); H = int(alto * S * 1.6)
    lay = Image.new('L', (W, H), 0); d = ImageDraw.Draw(lay); x = 2 * S
    for c, a in zip(t, anchos):
        d.text((x - f.getbbox(c)[0], H / 2), c, font=f, fill=255, anchor='lm'); x += a + espacio * S
    lay = lay.crop(lay.getbbox()); w, h = lay.size
    m = np.array(lay).astype(np.float32) / 255
    # 3 puntos: esquina sup-izq, sup-der, inf-izq del texto → su sitio en la esfera (escala 1/S)
    P0 = centro - eu * (w / S) / 2 - ev * (h / S) / 2
    src = np.float32([[0, 0], [w, 0], [0, h]])
    dst = np.float32([P0, P0 + eu * w / S, P0 + ev * h / S])
    M = cv2.getAffineTransform(src, dst)
    a = cv2.warpAffine(m, M, (img.shape[1], img.shape[0]), flags=cv2.INTER_AREA)[..., None] * alpha
    col = np.array(color[::-1], np.float32)
    return a, col

out = img.astype(np.float32)
for t, alto, peso, esp, k, al in (('NAIDU', 17, 500, 3.2, 0.42, 0.88), ('QUARTZ', 9, 400, 2.4, -0.47, 0.75)):
    a, col = texto(t, alto, peso, esp, C + k * v12, al)
    out = out * (1 - a) + col * a
cv2.imwrite('prodD3.png', out.clip(0, 255).astype(np.uint8))
Image.open('prodD3.png').crop((700, 700, 1400, 1450)).save('dial-detalle2.png')
