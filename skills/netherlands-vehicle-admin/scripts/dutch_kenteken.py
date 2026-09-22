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
# 来源：RDW「Overzicht van kentekenseries」
#   https://www.rdw.nl/de-kentekenplaat/overzicht-van-kentekenseries
# RDW 的系列编号到 14 为止；荷兰车牌一律 6 位字符（连字符只是显示分组）。
# 年代 = RDW 公布的该系列最早启用年份（跨车辆类别取最早；汽车自己的启用年份见
# references/license-plate-sidecodes.md 表格的 Cars since 列）。
SIDECODES = [
    (r"^[A-Z]{2}-\d{2}-\d{2}$", "XX-99-99", 1951),
    (r"^\d{2}-\d{2}-[A-Z]{2}$", "99-99-XX", 1951),
    (r"^\d{2}-[A-Z]{2}-\d{2}$", "99-XX-99", 1951),
    (r"^[A-Z]{2}-\d{2}-[A-Z]{2}$", "XX-99-XX", 1988),
    (r"^[A-Z]{2}-[A-Z]{2}-\d{2}$", "XX-XX-99", 1994),
    (r"^\d{2}-[A-Z]{2}-[A-Z]{2}$", "99-XX-XX", 2000),
    (r"^\d{2}-[A-Z]{3}-\d$", "99-XXX-9", 2005),
    (r"^\d-[A-Z]{3}-\d{2}$", "9-XXX-99", 2009),
    (r"^[A-Z]{2}-\d{3}-[A-Z]$", "XX-999-X", 2006),
    (r"^[A-Z]-\d{3}-[A-Z]{2}$", "X-999-XX", 2008),
    (r"^[A-Z]{3}-\d{2}-[A-Z]$", "XXX-99-X", 2015),
    (r"^[A-Z]-\d{2}-[A-Z]{3}$", "X-99-XXX", 2021),
    (r"^\d-[A-Z]{2}-\d{3}$", "9-XX-999", 2016),
    (r"^\d{3}-[A-Z]{2}-\d$", "999-XX-9", 2019),
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

    if len(raw) != 6:
        result["error"] = f"长度 {len(raw)} 不是 6 字符（荷兰车牌一律 6 位）"
        return result

    # 按每个 sidecode 掩码的连字符分组重新切片（6 位字符切成 3 组）
    candidates = {
        1: f"{raw[0:2]}-{raw[2:4]}-{raw[4:6]}",    # XX-99-99
        2: f"{raw[0:2]}-{raw[2:4]}-{raw[4:6]}",    # 99-99-XX
        3: f"{raw[0:2]}-{raw[2:4]}-{raw[4:6]}",    # 99-XX-99
        4: f"{raw[0:2]}-{raw[2:4]}-{raw[4:6]}",    # XX-99-XX
        5: f"{raw[0:2]}-{raw[2:4]}-{raw[4:6]}",    # XX-XX-99
        6: f"{raw[0:2]}-{raw[2:4]}-{raw[4:6]}",    # 99-XX-XX
        7: f"{raw[0:2]}-{raw[2:5]}-{raw[5:6]}",    # 99-XXX-9
        8: f"{raw[0:1]}-{raw[1:4]}-{raw[4:6]}",    # 9-XXX-99
        9: f"{raw[0:2]}-{raw[2:5]}-{raw[5:6]}",    # XX-999-X
        10: f"{raw[0:1]}-{raw[1:4]}-{raw[4:6]}",   # X-999-XX
        11: f"{raw[0:3]}-{raw[3:5]}-{raw[5:6]}",   # XXX-99-X
        12: f"{raw[0:1]}-{raw[1:3]}-{raw[3:6]}",   # X-99-XXX
        13: f"{raw[0:1]}-{raw[1:3]}-{raw[3:6]}",   # 9-XX-999
        14: f"{raw[0:3]}-{raw[3:5]}-{raw[5:6]}",   # 999-XX-9
    }

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
