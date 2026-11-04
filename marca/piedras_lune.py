"""Piedras del reloj Lune en fotos de IA: la IA las pinta verde oscuro con vetas negras; las reales son verde medio con
vetas claras (marca/referencias-reales/reloj-lune-2.jpg). Cambia solo las piedras dentro de un recuadro (el del reloj).
    python marca/piedras_lune.py <entrada.png> <salida.png> x0 y0 x1 y1      (píxeles de la imagen original)
Revisar después a tamaño real junto a la foto real; guarda también <salida>-mask.png para ver qué ha tocado.
"""
import sys, cv2, numpy as np
src, dst, x0, y0, x1, y1 = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7])
im = cv2.imread(src); roi = im[y0:y1, x0:x1].copy()
lab = cv2.cvtColor(roi, cv2.COLOR_BGR2LAB).astype(np.float32)
L, A, B = lab[..., 0], lab[..., 1], lab[..., 2]
cand = ((A < 125) & (L < 150)).astype(np.uint8) * 255
cand = cv2.morphologyEx(cand, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
n, labl, st, _ = cv2.connectedComponentsWithStats(cand)
mask = np.zeros_like(cand)
for i in range(1, n):
    comp = labl == i
    if st[i, cv2.CC_STAT_AREA] < 80 or A[comp].mean() > 124:   # fuera el aro oscuro de la esfera (neutro)
        continue
    cs, _ = cv2.findContours(comp.astype(np.uint8) * 255, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(mask, cs, -1, 255, -1)
mask = cv2.erode(mask, np.ones((3, 3), np.uint8)); m = mask > 0
cuerpo = np.array([98, 112, 143], np.float32)    # LAB OpenCV: verde medio-oscuro (≈ rgb 55,95,70)
veta = np.array([180, 121, 140], np.float32)     # verde muy claro, casi crema
Lm = L[m]; lo, mid, hi = np.percentile(Lm, 8), np.percentile(Lm, 55), np.percentile(Lm, 97)
t = np.clip((mid - cv2.GaussianBlur(L, (5, 5), 0)) / max(mid - lo, 1), 0, 1) ** 0.8          # oscuro en la IA → veta clara
sombra = (L - mid) / max(hi - mid, 1) * 25                       # conserva el relieve (cabujón)
nuevo = cuerpo + (veta - cuerpo) * t[..., None]
nuevo[..., 0] += np.clip(sombra, -25, 25)
brillo = L > np.percentile(Lm, 96)                               # brillos de la IA, intactos
nuevo = np.where(brillo[..., None], lab, nuevo)
out = np.where(m[..., None], nuevo, lab)
out = cv2.cvtColor(np.clip(out, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR)
soft = cv2.GaussianBlur(mask, (5, 5), 0)[..., None] / 255.0
im[y0:y1, x0:x1] = (out * soft + roi * (1 - soft)).astype(np.uint8)
cv2.imwrite(dst, im); cv2.imwrite(dst.replace(".png", "-mask.png"), mask)
print("piedras:", int(m.sum()), "px,", sum(1 for i in range(1, n)), "manchas")
