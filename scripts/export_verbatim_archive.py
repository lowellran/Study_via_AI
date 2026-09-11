# -*- coding: utf-8 -*-
"""
Study_via_AI - Standardized Deterministic Verbatim Archive Extractor
彻底杜绝 AI 偷懒撰写提纲摘要的机械化物理拦截引擎。
100% 保证从 transcript_full.jsonl / transcript.jsonl 中无损提取逐字实录并落地。
"""

import os
import sys
import json
import re
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Deterministic Verbatim Archive Extractor for Study_via_AI")
    parser.add_argument("--brain_dir", type=str, required=True, help="Path to the conversation brain directory")
    parser.add_argument("--plan_num", type=int, required=True, help="Plan number (1 to 10 or 255)")
    parser.add_argument("--plan_title", type=str, required=True, help="Full title of the plan")
    parser.add_argument("--output_file", type=str, required=True, help="Target markdown file path")
    parser.add_argument("--cheatsheet_file", type=str, required=True, help="Path to markdown file containing the One-Page Cheat Sheet")
    parser.add_argument("--start_step", type=int, default=None, help="Optional start step index in transcript")
    parser.add_argument("--end_step", type=int, default=None, help="Optional end step index in transcript")
    parser.add_argument("--start_turn", type=int, default=None, help="Optional start turn index in extracted turns")
    parser.add_argument("--end_turn", type=int, default=None, help="Optional end turn index in extracted turns")
    parser.add_argument("--mode", type=str, choices=["quick", "deep"], default="deep", help="Execution mode: quick sprint or deep mastery")
    return parser.parse_args()

def extract_turns(brain_dir):
    full_log = os.path.join(brain_dir, ".system_generated", "logs", "transcript_full.jsonl")
    comp_log = os.path.join(brain_dir, ".system_generated", "logs", "transcript.jsonl")
    
    log_path = full_log if os.path.exists(full_log) else comp_log
    if not os.path.exists(log_path):
        raise FileNotFoundError(f"Transcript log file not found in {brain_dir}")

    turns = []
    with open(log_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            try:
                data = json.loads(line)
            except Exception:
                continue
            stype = data.get("type")
            if stype == "USER_INPUT":
                content = data.get("content", "")
                clean = re.sub(r"<USER_REQUEST>\s*", "", content)
                clean = re.sub(r"\s*</USER_REQUEST>.*", "", clean, flags=re.DOTALL)
                clean = clean.strip()
                if clean:
                    turns.append({"step": idx, "role": "USER", "content": clean})
            elif stype == "PLANNER_RESPONSE":
                content = data.get("content", "")
                if content and content.strip():
                    turns.append({"step": idx, "role": "MODEL", "content": content.strip()})
    return turns

def main():
    args = parse_args()
    turns = extract_turns(args.brain_dir)
    print(f"Extracted {len(turns)} total dialog turns from system transcript.")

    # Determine slice of turns
    if args.start_turn is not None and args.end_turn is not None:
        target_turns = turns[args.start_turn : args.end_turn + 1]
    elif args.start_step is not None and args.end_step is not None:
        target_turns = [t for t in turns if args.start_step <= t["step"] <= args.end_step]
    else:
        target_turns = turns

    if not target_turns:
        raise ValueError("No dialog turns found matching specified range!")

    if not os.path.exists(args.cheatsheet_file):
        raise FileNotFoundError(f"Cheatsheet file not found at {args.cheatsheet_file}")

    with open(args.cheatsheet_file, "r", encoding="utf-8") as f:
        cheatsheet_content = f.read().strip()

    doc_lines = []
    if args.mode == "quick":
        doc_lines.append(f"# 极速实战归档：{args.plan_title}（100% 逐字互动全量实录）\n")
    else:
        doc_lines.append(f"# Plan {args.plan_num:02d} 归档：{args.plan_title}（100% 逐字互动全量实录）\n")
    doc_lines.append("[TOC]\n")
    doc_lines.append("---\n")

    turn_counter = 1
    i = 0
    while i < len(target_turns):
        t = target_turns[i]
        if t["role"] == "USER":
            user_text = t["content"]
            model_texts = []
            j = i + 1
            while j < len(target_turns) and target_turns[j]["role"] == "MODEL":
                model_texts.append(target_turns[j]["content"])
                j += 1
            
            doc_lines.append(f"## 交互实录 {turn_counter:02d}\n")
            doc_lines.append("### 👤 学员发言 / 指令：\n")
            doc_lines.append("```text\n" + user_text + "\n```\n")
            doc_lines.append("### 🤖 导师讲授 / 回复 / 代码：\n")
            if model_texts:
                for m in model_texts:
                    doc_lines.append(m + "\n\n")
            else:
                doc_lines.append("*（系统直接进入下一阶段）*\n\n")
            doc_lines.append("---\n")
            turn_counter += 1
            i = j if j > i + 1 else i + 1
        else:
            doc_lines.append(f"## 交互实录 {turn_counter:02d}（系统推进）\n")
            doc_lines.append("### 🤖 导师讲授 / 回复 / 代码：\n")
            doc_lines.append(t["content"] + "\n\n")
            doc_lines.append("---\n")
            turn_counter += 1
            i += 1

    if args.mode == "quick":
        doc_lines.append(f"## 附录：极速实战一页速查表 (One-Page Cheat Sheet)\n")
    else:
        doc_lines.append(f"## 附录：【Plan {args.plan_num:02d}】一页速查表 (One-Page Cheat Sheet)\n")
    doc_lines.append(cheatsheet_content + "\n")

    full_text = "\n".join(doc_lines)

    # Hard physical assertions
    min_turns = 2 if args.mode == "quick" else 5
    min_chars = 1500 if args.mode == "quick" else 5000
    print(f"Checking assertions (mode={args.mode}): turn_counter={turn_counter}, total_chars={len(full_text)} (limits: turns>={min_turns}, chars>={min_chars})")
    assert turn_counter >= min_turns, f"【防偷懒物理断言失败】交互轮次仅 {turn_counter} 轮，不足 {min_turns} 轮门禁！"
    assert len(full_text) >= min_chars, f"【防偷懒物理断言失败】实录总字数仅 {len(full_text)} 字，少于 {min_chars} 字门禁！"
    assert "### 👤 学员发言 / 指令：" in full_text, "【防偷懒物理断言失败】缺失学员发言栏目！"
    assert "### 🤖 导师讲授 / 回复 / 代码：" in full_text, "【防偷懒物理断言失败】缺失导师讲授栏目！"
    assert "## 附录：" in full_text, "【防偷懒物理断言失败】缺失速查表附录！"

    os.makedirs(os.path.dirname(os.path.abspath(args.output_file)), exist_ok=True)
    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(full_text)

    print(f"SUCCESS: Verbatim archive written to {args.output_file} ({len(full_text)} chars, {turn_counter-1} dialog rounds)")

if __name__ == "__main__":
    main()
