# -*- coding: utf-8 -*-
"""踩坑总索引生成器：扫描 pitfalls/ 下各领域 md，提取症状式卡标题/标签/状态，输出总索引表。

用法: python build_index.py [踩坑库根目录]   （例：python tools/build_index.py pitfalls/）
产物: <根>/踩坑总索引.md  —— 自动生成勿手改，卡片有增删后重跑本脚本。
容错: 缺 标签/状态 行的卡在表中显示 "—"，不代表卡有问题，点回原文件查看。
"""
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "踩坑总索引.md")
SKIP = {"踩坑总索引.md"}
SKIP_DIRS = {"_tools", ".tmp", "assets"}

def g(field_re, seg):
    m = re.search(field_re, seg, flags=re.M)
    return m.group(1).strip() if m else "—"

rows = []
for fn in sorted(os.listdir(ROOT)):
    if not fn.endswith(".md") or fn in SKIP:
        continue
    path = os.path.join(ROOT, fn)
    txt = open(path, encoding="utf-8").read()
    parts = re.split(r"^## ", txt, flags=re.M)
    for i, seg in enumerate(parts):
        if i == 0:  # 文件头，不是卡
            continue
        title = seg.splitlines()[0].strip() if seg.strip() else "(空标题)"
        tags = g(r"^- \*\*标签\*\*[:：]\s*(.+)$", seg)
        stm = re.search(r"^- \*\*状态\*\*[:：]\s*(.+)$", seg, flags=re.M)
        if stm:
            st = stm.group(1).strip()
            m2 = re.search(r"[✅⏳❌]", st)
            st = m2.group(0) if m2 else st.split("(")[0].strip()[:6]
        else:
            st = "—"
        rows.append((fn[:-3], title, tags, st))

lines = [
    "# 踩坑总索引",
    "",
    f"> 由 `_tools/build_index.py` 自动生成 · 共 {len(rows)} 张卡 · 检索用 Grep：命中症状行 → 打开对应领域文件读卡全文。",
    "> 单项目坑（车载日志等）不入此表；改卡后重跑生成脚本，勿手改本文件。",
    "",
    "| # | 症状（搜它） | 领域文件 | 标签 | 状态 |",
    "|---|------------|---------|------|------|",
]
for i, (f, t, tag, st) in enumerate(rows, 1):
    t = t.replace("|", "／")
    lines.append(f"| {i} | {t} | {f} | {tag} | {st} |")

open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"生成完成: {OUT}  ({len(rows)} 卡)")
