#!/usr/bin/env python3
"""把 ai-profile.json 填进统一模板，生成 ai-profile.html。

用法：python3 build_report.py ai-profile.json ai-profile.html
"""
import json
import sys
from pathlib import Path

PLACEHOLDER = "/*__DATA__*/null"


def main() -> int:
    if len(sys.argv) != 3:
        print("用法：python3 build_report.py <数据.json> <输出.html>")
        return 1
    data_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
    template = Path(__file__).resolve().parent.parent / "assets" / "report.html"

    data = json.loads(data_path.read_text(encoding="utf-8"))
    items = data.get("items")
    if not isinstance(items, list) or len(items) != 30:
        print(f"数据不完整：items 应该有 30 条，现在是 {len(items) if isinstance(items, list) else 0} 条。")
        return 1

    html = template.read_text(encoding="utf-8")
    if html.count(PLACEHOLDER) != 1:
        print("模板异常：找不到数据占位符。")
        return 1

    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out_path.write_text(html.replace(PLACEHOLDER, payload), encoding="utf-8")
    print(f"已生成：{out_path.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
