# 论文成果维护流程

论文成果有两种维护方式，可以同时保留。

## 方式 A：后台手动新增论文

1. 进入 `/admin/`。
2. 打开 Publications。
3. 新建条目，填写标题、作者、日期、期刊、摘要、DOI、PDF 等字段。
4. 保存为草稿或提交审核。
5. 管理员发布后，内容写入 `content/publication/<slug>/index.md`。
6. GitHub Actions 自动构建并发布网站。

适合少量论文、需要手动补充图片/PDF/项目链接的情况。

## 方式 B：BibTeX 自动导入

仓库保留了 `.github/workflows/import-publications.yml`。当根目录的 `publications.bib` 被新增或更新时，该 workflow 会尝试使用 Academic 工具把 BibTeX 转换为 Hugo Blox 的 publication Markdown，并创建 Pull Request。

适合批量导入论文元数据。导入后仍建议人工检查：

- 作者顺序
- 期刊名和简称
- DOI
- publication_types
- 摘要
- PDF 链接
- 封面图

不要删除 `import-publications.yml`，除非确定不再使用 BibTeX 流程。

## PDF 和补充材料

后台 PDF 字段会上传到：

```text
static/uploads/publications/
```

前台通常访问：

```text
/uploads/publications/<文件名>
```

Hugo Blox 也支持把 PDF 放在单篇论文文件夹中，例如：

```text
content/publication/JA-2/JA-2.pdf
```

这种 page bundle 方式对论文附件最稳定。

## 封面图和图形摘要

推荐把论文封面图放在单篇论文目录下并命名为：

```text
featured.jpg
featured.png
```

Hugo Blox 会自动识别并在列表和详情页显示。后台上传到 `static/uploads/publications/` 的图片更适合作为正文插图或图形摘要链接。

## DOI 自动补全预留

当前没有强制实现 DOI 自动补全。后续可以新增脚本，通过 DOI 调用 Crossref 或出版商 API，自动补全：

- title
- authors
- publication
- year
- doi
- abstract

建议将来新增脚本放在 `scripts/` 下，例如：

```text
scripts/fill_publication_from_doi.py
```

脚本只应根据 DOI 生成或更新 Markdown，不应写入任何 token 或个人凭证。
