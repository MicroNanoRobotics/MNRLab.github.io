# 中英文双语网站维护说明

本网站使用 Hugo 原生 multilingual mode 实现双语，不是两套独立网站。英文是默认语言，访问根路径；中文访问 `/zh/`。现有英文内容不需要移动，中文内容以同目录的 `.zh.md` 文件维护。

## 语言和路径

- 英文配置：`config/_default/languages.yaml` 中的 `en`
- 中文配置：`config/_default/languages.yaml` 中的 `zh`
- 英文首页：`/`
- 中文首页：`/zh/`
- 英文内容文件：`index.md` 或 `_index.md`
- 中文内容文件：`index.zh.md` 或 `_index.zh.md`

`config/_default/hugo.yaml` 中保持 `defaultContentLanguage: en` 和 `defaultContentLanguageInSubdir: false`，这样英文站仍然在根路径，中文站自动放在 `/zh/`。

## 内容放在哪里

- 首页英文：`content/_index.md`
- 首页中文：`content/_index.zh.md`
- Tour 英文：`content/tour/index.md`
- Tour 中文：`content/tour/index.zh.md`
- 新闻英文：`content/post/<slug>/index.md`
- 新闻中文：`content/post/<slug>/index.zh.md`
- 论文英文：`content/publication/<slug>/index.md`
- 论文中文：`content/publication/<slug>/index.zh.md`
- 成员英文：`content/authors/<slug>/_index.md`
- 成员中文：`content/authors/<slug>/_index.zh.md`
- 研究方向英文：`content/research/<slug>/index.md`
- 研究方向中文：`content/research/<slug>/index.zh.md`
- 平台设备英文：`content/facilities/<slug>/index.md`
- 平台设备中文：`content/facilities/<slug>/index.zh.md`
- 相册英文：`content/gallery/<year>/index.md`
- 相册中文：`content/gallery/<year>/index.zh.md`

后台配置源文件是 `data/decap_cms_config.yaml`。后台 `/admin/` 中对应入口会显示为 `News EN`、`News 中文`、`People EN`、`People 中文` 这类成对 collection。

## translationKey 是什么

`translationKey` 用来告诉 Hugo 哪两个页面是同一内容的中英文版本。中英文页面需要填写同一个值，例如：

```yaml
translationKey: news-soft-robotics-award
```

如果 `translationKey` 不一致，语言切换按钮可能找不到对应页面，表现为跳到栏目页或首页。推荐使用稳定的小写英文、数字和连字符。

## 新增一篇中英文新闻

1. 在后台进入 `News EN`，新建英文新闻。
2. 保存后会生成类似 `content/post/example/index.md`。
3. 在后台进入 `News 中文`，新建中文新闻。
4. 尽量使用相同 slug；至少保证 `translationKey` 与英文新闻一致。
5. 中文文件应是 `content/post/example/index.zh.md`。

正文、标题、摘要应分别使用英文和中文，不要在同一个前台页面混写两种语言。

## 新增一篇中英文论文

BibTeX 导入流程保持不变。`import-publications.yml` 默认生成英文论文条目，例如：

```text
content/publication/example/index.md
```

需要中文简介时，在后台进入 `Publications 中文` 或对应分类的中文 collection，补充：

```text
content/publication/example/index.zh.md
```

中文版论文可以保留英文标题、英文期刊名、DOI、PDF 链接和图形摘要。可额外填写 `title_zh`、中文摘要或中文简介。

## 新增中英文成员信息

英文成员使用：

```text
content/authors/<slug>/_index.md
```

中文成员使用：

```text
content/authors/<slug>/_index.zh.md
```

英文页面填写英文姓名、英文职位、英文简介和英文研究方向。中文页面填写中文姓名、中文职位、中文简介和中文研究方向。头像和社交链接可以复用。

团队排序在后台的 `Group Order` / `分类内排序` 里维护。同一个成员可以为不同分类设置不同顺序，数字越小越靠前。

## 新增中英文专利页面

专利已归入 Publications，不再作为独立顶级栏目维护。英文专利使用 `Patents EN`，中文专利使用 `Patents 中文`。两者都写入 `content/publication/<slug>/`，通过：

```yaml
publication_types:
  - patent
```

来进入专利分类页。中英文专利同样需要共享 `translationKey`。

## 相册维护

相册按年份维护：

- 2024：`content/gallery/2024/`
- 2025：`content/gallery/2025/`
- 2026：`content/gallery/2026/`

每个年份页面的 `images` 是图片列表。前台 Gallery 先显示年份卡片，进入年份后显示幻灯片和图片画布。图片建议上传到 `static/uploads/gallery/`，前台路径使用 `/uploads/gallery/<文件名>`。

## 哪些内容可以只维护英文

以下内容可以在中英文页面中保持英文或原始格式：

- DOI
- 期刊名、会议名、出版社名
- PDF、Code、Dataset、Project 链接
- BibTeX 生成的作者名
- 英文论文标题
- 图形摘要文件名和图片路径

## 保存后如何上线

后台发布内容后，本质上会向 GitHub 仓库 `main` 分支提交 Markdown、图片或 PDF 文件。GitHub Actions 会自动运行 Hugo 构建并发布到 GitHub Pages。通常几十秒到几分钟后生效。

本地修改不会自动上传。若是在本地直接改文件，需要手动执行：

```powershell
git add -A
git commit -m "Update bilingual site content"
git push
```

## 常见问题

中文页面 404：确认中文文件名是否为 `index.zh.md` 或 `_index.zh.md`，并确认已推送到 GitHub 且 Actions 构建成功。

语言切换跳到首页：检查中英文页面的 `translationKey` 是否完全一致。

图片不显示：检查文件是否在 `static/uploads/` 下，路径大小写是否一致。部署在 GitHub Pages 子路径时，尽量使用后台上传路径或 Hugo Blox 的 page bundle 图片机制。

菜单语言错误：检查 `config/_default/menus.yaml` 的英文菜单，以及 `config/_default/languages.yaml` 中 `zh.menu.main` 的中文菜单。

后台没有中文入口：检查 `data/decap_cms_config.yaml` 是否包含对应的 `*_zh` collection，并重新构建部署。

构建失败：本地运行 `hugo --minify --ignoreVendorPaths=""`，根据错误中的文件路径检查 front matter、日期格式或 YAML 缩进。
