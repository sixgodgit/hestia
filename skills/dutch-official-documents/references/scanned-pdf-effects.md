# Rendering a digital document as an A4 "scan"

When a submission expects a scanned paper document and you only have the digital
original, apply these effects to the original to produce a PDF that reads as a
scan. The effects change presentation only — never let this step alter the
document's content.

## Effects

1. **Grayscale** conversion.
2. **Slight rotation** (-1.5° to +1.5°, simulating paper placement).
3. **Gaussian noise** (σ=8-12) for paper texture.
4. **Contrast enhancement** (1.15-1.2x).
5. **Gaussian blur** (radius 0.4-0.6) for scanner focus.
6. **Edge darkening** (vignette) for scanner lid shadow.
7. **Sepia tint** (R×1.05, B×0.95) for an "old scanner" feel.
8. **JPEG quality 85** for compression artifacts.

Output: A4 PDF, page centered with margins, ready to print.

## Python recipe

```python
from PIL import Image, ImageFilter, ImageEnhance
import random

def scanned_effect(img):
    gray = img.convert('L')
    angle = random.uniform(-1.5, 1.5)
    rotated = gray.rotate(angle, resample=Image.BICUBIC, expand=False, fillcolor=245)
    pixels = list(rotated.getdata())
    noisy = [max(0, min(255, p + random.gauss(0, 10))) for p in pixels]
    noisy_img = Image.new('L', rotated.size)
    noisy_img.putdata(noisy)
    enhancer = ImageEnhance.Contrast(noisy_img)
    contrasted = enhancer.enhance(1.2)
    blurred = contrasted.filter(ImageFilter.GaussianBlur(radius=0.5))
    # Convert to RGB with slight sepia
    rgb = blurred.convert('RGB')
    r, g, b = rgb.split()
    r = r.point(lambda i: min(255, int(i * 1.05)))
    b = b.point(lambda i: int(i * 0.95))
    return Image.merge('RGB', (r, g, b))
```

## Constraints

- Keep the output **under 500KB** for API token limits. A large image (>1MB PNG)
  may need a resize before processing.
- The source document must already be the correct, final content: the scan pass
  is the last step, after the generator's own verification (no leftover
  `[TOKENS]`, one-page fit, CJK glyphs rendered).
