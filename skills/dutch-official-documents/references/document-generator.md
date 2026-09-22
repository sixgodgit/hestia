# Generator pattern for official Dutch documents (DOCX + PDF from one source)

Use when the user needs a signed form, declaration or letter in Dutch with the
Chinese reference pages he wants alongside it. The architecture first, then the
rendering rules that keep Dutch and Chinese legible in both outputs.

## Shape

1. **One content model**: a flat list of typed blocks — `("title", …)`,
   `("subtitle", …)`, `("h3", …)`, `("kv", (label, value))`, `("num", (n, text))`,
   `("bullet")`, `("sigline")`, `("stamp")`, `("spacer")`, `("rule")`,
   `("para")`. Three block lists: the **Dutch document**, the **Chinese
   translation** (marked 请勿提交 / NIET MEESTUREN), and the **Chinese
   instructions** (fill-in checklist, variants, pitfalls).
2. **Two renderers over that model**: python-docx for the editable DOCX,
   reportlab platypus for the PDF. Never maintain the two by hand.
3. **A `gegevens.json` beside the script** holding the real values plus
   status/notes keys (`_status`, `_rdw`, `clausule_3`). The script substitutes
   them into `[PLACEHOLDER]` tokens; an empty value leaves the token visible so
   nothing is silently dropped.
4. **Substitution via a token→key map**, applied longest-token-first so a short
   token cannot consume a longer one, and applied to both the Dutch and Chinese
   lists so both fill consistently. Populate the map with both the Dutch and the
   Chinese form of a token where the Chinese pages repeat it.
5. **Prune optional empty lines** after filling (phone/email/internal reference/
   optional annex), including dangling ` · ` separators and a line left with
   only its label. Keep structural blocks (`sigline`, `spacer`, `rule`) out of
   the prune set — a naive "drop empty strings" pass deletes the signature rule.
6. **Report what is still open**: regex the filled lists for `\[[^\[\]]+\]`,
   exclude the deliberately-optional tokens, print the remainder. "Nothing open
   in the PDF" is the gate before delivery, and the printed list is what you
   send the user.
7. **Fix typography in the cleanup step**, e.g. collapse `B.V..` to `B.V.` when
   a sentence ends on a company name; a doubled period reads as broken Dutch.
8. **Variant clauses live in the JSON**, not in the text: a key like
   `clausule_3: "A"|"B"` selects which pre-written paragraph goes in, in both
   languages. Which variant carries the rejection risk is stated to the user in
   the chat, not hidden in the document.
9. **Autofit the submission page**: build the section into a throwaway PDF over
   candidate `(fontsize, leading, gap, margins)` configs, keep the first whose
   page count is 1, then render for real with that config. One-page fit is a
   loop, not a guess; tighter spacing also comes from merging letterhead lines
   and shrinking the top/bottom margins.
10. **Archive**: copy the delivered PDF/DOCX/JSON to `archief/<date>_<label>/`
    and keep a README.md with current status, still-missing fields, submission
    checklist and policy basis. Keep the blank template as
    `archief/<YYYY-MM-DD>_leeg/`. Later regeneration must not overwrite an
    archived version.

## Rendering Chinese reliably (both outputs need their own handling)

The `pdf` skill's Pitfalls cover reportlab font embedding, but those notes sit
in a bundled skill and may be reverted — keep this block self-sufficient:

- **Verify glyph coverage before rendering, not by eye afterwards.** After
  registering a font, check the codepoints you actually need:
  `TTFont(path).face.charToGlyph` must contain `ord('A')`, `ord('[')`, `ord('车')`.
  A font lacking Latin silently drops every letter, digit and bracket from the
  PDF — the placeholder text vanishes and only the Chinese survives, which looks
  like a content bug and costs a debugging round.
- **Fonts that work / don't** (TrueType outlines required, since reportlab
  rejects CFF/PostScript): Noto Sans/Serif CJK ship as `.ttc` with PostScript
  outlines → refused with `TTFError: postscript outlines are not supported`.
  `DroidSansFallbackFull.ttf` has CJK but **no Latin** → unusable alone. Use
  `/usr/share/fonts/truetype/arphic/uming.ttc` (UMingCN, `subfontIndex=0`) for
  body text and `ukai.ttc` (UKaiCN) for headings to keep a visible hierarchy (it
  has no bold variant, so distinguish headings by size/face rather than weight).
  `/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc` (`subfontIndex=0`) is a third
  working face, and the one to reach for when you are mixing Chinese into
  paragraphs that also carry Latin and want a single consistent look. On the
  Latin side only `DejaVuSans.ttf` and `DejaVuSans-Bold.ttf` exist on this host
  — registering `DejaVuSans-Oblique.ttf` aborts the whole build with
  `OSError: Cannot open resource`; use `DejaVuSerif.ttf` when a visibly
  secondary face is wanted.
- **Latin pages stay on Helvetica/Helvetica-Bold**; only the CJK pages need the
  embedded face. Helvetica lacks `―` (U+2015): draw rules with `HRFlowable`,
  never with repeated glyphs — the character renders as empty boxes.
- **python-docx writes no East Asian font.** Set it on the style
  (`doc.styles['Normal'].element.rPr.rFonts.set(qn('w:eastAsia'), 'SimSun')`)
  and give each run both `w:ascii`/`w:hAnsi` and `w:eastAsia` in its `rFonts`,
  or Latin and Chinese render in mismatched faces inside one paragraph.
- **Layout baseline**: A4, ~2 cm margins for single-page documents.
- **Two PDF routes, pick one per document.** reportlab (above) when the layout
  is block-based and the one-page autofit loop matters; weasyprint (HTML→PDF)
  when the document is simple enough that HTML+CSS is quicker and the CJK font
  can just be named in the CSS. Do not reach for `fpdf2`: its
  `multi_cell(width=0)` raises "not enough horizontal space" errors on some
  characters.

## Delivery conventions for this user

- Pre-fill everything; list only genuinely missing fields. He signs, nothing
  more.
- Dutch page first and alone on page one; Chinese pages after, clearly marked
  as not for submission.
- Verify by extracting the PDF text (real values present, no leftover tokens,
  submission page = 1 page) and by rendering page 1 for a visual check, before
  reporting done.
- If one value is missing (a kenteken, a date), produce everything else, leave
  that marker, and ask for exactly that value — do not stall the whole document.
- When the user supplies data that looks wrong (model spelling, street spelling,
  implausible period), correct the spelling to the official source, fill his
  version of the substance, and tell him plainly what you changed and what needs
  confirming.
