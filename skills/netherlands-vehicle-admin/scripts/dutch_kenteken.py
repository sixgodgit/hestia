#!/usr/bin/env python3
"""
荷兰车牌（kenteken）解析器
========================
功能：
- 清洗和规范化车牌号
- 判定 sidecode（分代）
- 校验字母池合规性
- 判断车辆大致年代

用法：
    python3 dutch_kenteken.py XX999X
    python3 dutch_kenteken.py "XX-999-X"
    python3 dutch_kenteken.py --batch plates.txt

说明：XX-999-X / XX999X 是占位示例（sidecode 11 掩码），换成你要查的车牌。
"""

import re
import sys
import argparse

# 荷兰牌照可用字母（不含元音 A E I O U 和易混淆 C Q W Y）
LETTERS = "BDFGHJKLMNPRSTVXZ"

# Sidecode 格式定义：(正则, 描述, 年代)
SIDECODES = [
    (r"^[A-Z]{2}-\d{2}-\d{2}$", "XX-99-99", 1951),
    (r"^\d{2}-\d{2}-[A-Z]{2}$", "99-99-XX", 1965),
    (r"^\d{2}-[A-Z]{2}-\d{2}$", "99-XX-99", 1973),
    (r"^[A-Z]{2}-\d{2}-[A-Z]{2}$", "XX-99-XX", 1978),
    (r"^[A-Z]{2}-[A-Z]{2}-\d{2}$", "XX-XX-99", 1991),
    (r"^\d{2}-[A-Z]{2}-[A-Z]{2}$", "99-XX-XX", 1999),
    (r"^\d{2}-[A-Z]{3}-\d$", "99-XXX-9", 2004),
    (r"^\d-[A-Z]{3}-\d{2}$", "9-XXX-99", 2006),
    (r"^[A-Z]{3}-\d{2}-[A-Z]$", "XXX-99-X", 2009),
    (r"^[A-Z]-\d{3}-[A-Z]{2}$", "X-999-XX", 2011),
    (r"^[A-Z]{2}-\d{3}-[A-Z]$", "XX-999-X", 2013),
    (r"^[A-Z]-\d{2}-[A-Z]{3}$", "X-99-XXX", 2015),
    (r"^\d{2}-[A-Z]-[A-Z]{3}$", "99-X-XXX", 2017),
    (r"^[A-Z]{3}-[A-Z]-\d{2}$", "XXX-X-99", 2019),
    (r"^\d-[A-Z]{2}-\d{2}-[A-Z]$", "9-XX-99-X", 2021),
    (r"^[A-Z]{2}-\d-[A-Z]{2}-\d{2}$", "XX-9-XX-99", 2023),
]


def parse_kenteken(plate: str) -> dict:
    """解析荷兰车牌，返回结构化结果。"""
    raw = plate.strip().upper().replace("-", "").replace(" ", "")
    result = {
        "input": plate,
        "normalized": raw,
        "valid": False,
        "sidecode": None,
        "display": None,
        "era": None,
        "letter_compliant": None,
        "non_compliant_letters": [],
    }

    if len(raw) == 6:
        candidates = {
            1: f"{raw[0:2]}-{raw[2:4]}-{raw[4:6]}",
            2: f"{raw[0:2]}-{raw[2:4]}-{raw[4:6]}",
            3: f"{raw[0:2]}-{raw[2:4]}-{raw[4:6]}",
            4: f"{raw[0:2]}-{raw[2:4]}-{raw[4:6]}",
            5: f"{raw[0:2]}-{raw[2:4]}-{raw[4:6]}",
            6: f"{raw[0:2]}-{raw[2:4]}-{raw[4:6]}",
            7: f"{raw[0:2]}-{raw[2:5]}-{raw[5:6]}",
            8: f"{raw[0:1]}-{raw[1:4]}-{raw[4:6]}",
            9: f"{raw[0:3]}-{raw[3:5]}-{raw[5:6]}",
            10: f"{raw[0:1]}-{raw[1:4]}-{raw[4:6]}",
            11: f"{raw[0:2]}-{raw[2:5]}-{raw[5:6]}",
            12: f"{raw[0:1]}-{raw[1:3]}-{raw[3:6]}",
            13: f"{raw[0:2]}-{raw[2:3]}-{raw[3:6]}",
            14: f"{raw[0:3]}-{raw[3:4]}-{raw[4:6]}",
        }
    elif len(raw) == 7:
        candidates = {
            15: f"{raw[0:1]}-{raw[1:3]}-{raw[3:5]}-{raw[5:6]}",
            16: f"{raw[0:2]}-{raw[2:3]}-{raw[3:5]}-{raw[5:7]}",
        }
    else:
        result["error"] = f"长度 {len(raw)} 不是 6 或 7 字符"
        return result

    for code, (pattern, desc, year) in enumerate(SIDECODES, 1):
        c = candidates.get(code)
        if c and re.fullmatch(pattern, c):
            result["valid"] = True
            result["sidecode"] = code
            result["display"] = c
            result["era"] = f"{year}  {desc}"
            # 字母池校验
            bad = [ch for ch in raw if ch.isalpha() and ch not in LETTERS]
            result["non_compliant_letters"] = bad
            result["letter_compliant"] = len(bad) == 0
            return result

    result["error"] = "不匹配任何已知 sidecode 格式"
    return result


def main():
    parser = argparse.ArgumentParser(description="荷兰车牌解析器")
    parser.add_argument("plates", nargs="*", help="车牌号（可多个）")
    parser.add_argument("--batch", "-b", help="从文件批量读取车牌（每行一个）")
    parser.add_argument("--json", action="store_true", help="JSON 格式输出")
    args = parser.parse_args()

    plates = args.plates or []
    if args.batch:
        with open(args.batch) as f:
            plates += [line.strip() for line in f if line.strip()]

    if not plates:
        # 交互模式
        print("荷兰车牌解析器 — 输入车牌号（空行退出）")
        while True:
            try:
                plate = input("> ").strip()
                if not plate:
                    break
                plates.append(plate)
            except (EOFError, KeyboardInterrupt):
                break

    for plate in plates:
        r = parse_kenteken(plate)
        if args.json:
            import json
            print(json.dumps(r, ensure_ascii=False))
        elif r["valid"]:
            note = ""
            if not r["letter_compliant"]:
                note = f"  [含非常规字母: {r['non_compliant_letters']}]"
            print(f"{r['input']:12} → ✅ {r['display']}  sidecode {r['sidecode']} ({r['era']}){note}")
        else:
            print(f"{r['input']:12} → ❌ {r.get('error', '未知错误')}")


if __name__ == "__main__":
    main()
