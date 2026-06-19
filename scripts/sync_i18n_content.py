#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TOP_KEY_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*\s*:")


def split_markdown(text: str) -> tuple[str, str, str]:
    newline = "\r\n" if "\r\n" in text[:200] else "\n"
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return "", text, newline
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text, newline
    return text[4:end], text[end + 5 :], newline


def join_markdown(front_matter: str, body: str, newline: str = "\n") -> str:
    body = body.lstrip()
    if body:
        text = f"---\n{front_matter.strip()}\n---\n\n{body}"
    else:
        text = f"---\n{front_matter.strip()}\n---\n"
    return text.replace("\n", newline)


def block_bounds(front_matter: str, key: str) -> tuple[int, int] | None:
    lines = front_matter.splitlines(True)
    start = None
    for index, line in enumerate(lines):
        if line.startswith(f"{key}:"):
            start = index
            break
    if start is None:
        return None
    end = len(lines)
    for index in range(start + 1, len(lines)):
        if TOP_KEY_RE.match(lines[index]):
            end = index
            break
    return sum(len(line) for line in lines[:start]), sum(len(line) for line in lines[:end])


def get_block(front_matter: str, key: str) -> str | None:
    bounds = block_bounds(front_matter, key)
    return None if bounds is None else front_matter[bounds[0] : bounds[1]]


def set_block(front_matter: str, key: str, block: str) -> str:
    block = block.rstrip("\n") + "\n"
    bounds = block_bounds(front_matter, key)
    if bounds is None:
        return front_matter.rstrip("\n") + "\n" + block
    return front_matter[: bounds[0]] + block + front_matter[bounds[1] :]


def remove_block(front_matter: str, key: str) -> str:
    bounds = block_bounds(front_matter, key)
    if bounds is None:
        return front_matter
    return front_matter[: bounds[0]] + front_matter[bounds[1] :]


def rename_block(block: str, old_key: str, new_key: str) -> str:
    return re.sub(rf"^{re.escape(old_key)}\s*:", f"{new_key}:", block, count=1)


def scalar_or_block(front_matter: str, key: str) -> str | None:
    block = get_block(front_matter, key)
    if block is None:
        return None
    lines = block.splitlines()
    value = lines[0].split(":", 1)[1].strip()
    if value.startswith("|") or value.startswith(">"):
        out = []
        for line in lines[1:]:
            if line.startswith("  "):
                out.append(line[2:])
            elif not line.strip():
                out.append("")
        return "\n".join(out).rstrip("\n") + "\n"
    if value in {"", "''", '""'}:
        return ""
    if (value.startswith("'") and value.endswith("'")) or (value.startswith('"') and value.endswith('"')):
        value = value[1:-1]
    return value + "\n"


def set_scalar(front_matter: str, key: str, value: str) -> str:
    return set_block(front_matter, key, f"{key}: {value}\n")


def target_for(source: Path) -> Path:
    return source.with_name("_index.zh.md" if source.name == "_index.md" else "index.zh.md")


def sync_pair(source: Path, field_pairs: list[tuple[str, str]], body_key: str = "body_zh") -> None:
    target = target_for(source)
    source_fm, source_body, newline = split_markdown(source.read_text(encoding="utf-8"))
    if not source_fm:
        return
    old_target_fm = ""
    old_target_body = ""
    if target.exists():
        old_target_fm, old_target_body, _ = split_markdown(target.read_text(encoding="utf-8"))

    out_fm = source_fm
    for target_key, source_key in field_pairs:
        source_block = get_block(source_fm, source_key)
        if source_block:
            out_fm = set_block(out_fm, target_key, rename_block(source_block, source_key, target_key))

    aliases = get_block(old_target_fm, "aliases") if old_target_fm else None
    if aliases:
        out_fm = set_block(out_fm, "aliases", aliases)
    out_fm = set_scalar(out_fm, "cms_language", "zh")
    collection = scalar_or_block(source_fm, "cms_collection")
    if collection:
        out_fm = set_scalar(out_fm, "cms_collection", collection.strip().replace("_en", "_zh"))

    for _, source_key in field_pairs:
        out_fm = remove_block(out_fm, source_key)
    out_fm = remove_block(out_fm, body_key)

    body = scalar_or_block(source_fm, body_key)
    if body is None:
        body = old_target_body or source_body
    target.write_text(join_markdown(out_fm, body, newline), encoding="utf-8")


COMMON = [("title", "title_zh"), ("summary", "summary_zh"), ("abstract", "abstract_zh")]

DIRECT = [
    (ROOT / "content" / "_index.md", [("title", "title_zh"), ("sections", "sections_zh")]),
    (ROOT / "content" / "tour" / "index.md", [("title", "title_zh"), ("sections", "sections_zh")]),
]

FOLDERS = [
    (ROOT / "content" / "post", "index.md", COMMON),
    (ROOT / "content" / "research", "index.md", COMMON + [("related_publications", "related_publications_zh")]),
    (ROOT / "content" / "facilities", "index.md", COMMON + [("category", "category_zh"), ("location", "location_zh"), ("responsible_person", "responsible_person_zh"), ("equipment_list", "equipment_list_zh")]),
    (ROOT / "content" / "gallery", "index.md", COMMON + [("event", "event_zh"), ("location", "location_zh")]),
    (ROOT / "content" / "publication", "index.md", COMMON + [("publication", "publication_zh"), ("publication_short", "publication_short_zh")]),
    (ROOT / "content" / "authors", "_index.md", [("title", "title_zh"), ("name", "name_zh"), ("role", "role_zh"), ("bio", "bio_zh"), ("interests", "interests_zh"), ("education", "education_zh")]),
]


def main() -> None:
    for path, fields in DIRECT:
        if path.exists():
            sync_pair(path, fields)
    for folder, filename, fields in FOLDERS:
        if not folder.exists():
            continue
        for path in folder.rglob(filename):
            if filename == "index.md" and path.parent == folder:
                continue
            sync_pair(path, fields)


if __name__ == "__main__":
    main()
