# 实验室网站维护说明

本项目是基于 Hugo Blox / Wowchemy Research Group Template 的静态网站，当前部署到 GitHub Pages。网站内容主要存放在 `content/`，后台表单由 Decap CMS 生成，入口为 `/admin/`。

## 本地运行网站

1. 安装 Hugo Extended，版本建议与 GitHub Actions 一致：`0.150.1`。
2. 在仓库根目录运行：

```powershell
hugo server
```

3. 浏览器打开终端显示的本地地址，通常是 `http://localhost:1313/`。
4. 正式构建检查使用：

```powershell
hugo --minify --ignoreVendorPaths=""
```

## 本地测试后台

后台入口由 `content/admin/index.md` 和 Hugo Blox 的 Decap CMS 插件生成。CMS 配置源文件是 `data/decap_cms_config.yaml`，构建后会输出到 `/admin/config.yml`。

本地测试步骤：

1. 启动本地 Git 后端：

```powershell
npx decap-server
```

2. 另开一个终端启动 Hugo：

```powershell
hugo server
```

3. 打开 `http://localhost:1313/admin/`。

开发环境下插件会自动把 `local_backend` 设为 `true`。生产环境下 `local_backend` 会关闭，后台需要 GitHub 登录。

## 线上后台登录

当前后台配置为 GitHub backend：

- 仓库：`MicroNanoRobotics/MNRLab.github.io`
- 分支：`main`
- 站点域名：`micronanorobotics.github.io`
- 未开启 Open Authoring：任何电脑都可打开后台页面，但只有拥有仓库写权限的 GitHub 账号能登录修改
- 配置文件：`data/decap_cms_config.yaml`
- 不保存任何 token、secret、OAuth client secret 或个人凭证

GitHub Pages 自身不提供 OAuth 登录代理，因此需要额外配置一种 Decap CMS 支持的认证方式：

1. 使用自建或第三方 Decap GitHub OAuth proxy，并在 `backend` 下增加 `base_url`。
2. 如果未来改由 Netlify 托管，可切换到 Netlify Identity + Git Gateway，并把 `backend.name` 改为 `git-gateway`。
3. 也可以使用组织已有的 Decap-compatible OAuth 服务。

OAuth secret 只能放在 OAuth 服务端或托管平台环境变量里，不能提交到仓库。

如果希望课题组成员直接发布内容，请在 GitHub 仓库中把对应账号加入 Collaborators 并给予写权限。不在仓库权限列表中的账号即使能打开 `/admin/` 页面，也不能修改网站内容。

## 内容审核流程

当前 `data/decap_cms_config.yaml` 默认启用：

```yaml
publish_mode: editorial_workflow
```

这表示学生或组员在后台保存内容后，可以先进入草稿/审核状态，由管理员在后台发布。发布后内容会进入 `main` 分支，GitHub Actions 自动重新构建并部署网站。

如果当前 OAuth 服务不支持 editorial workflow，或者希望后台保存后直接提交到 `main`，可以删除或注释 `publish_mode: editorial_workflow` 这一行，然后重新构建部署。

## 添加协作者

1. 在 GitHub 仓库的 Settings -> Collaborators and teams 中邀请成员。
2. 需要通过后台写内容的成员至少需要可以向仓库提交内容的权限。
3. 建议学生先使用 editorial workflow，由管理员审核后发布。
4. 对外公开的匿名访客不能写入后台，后台写入必须经过 GitHub 登录和仓库权限校验。

## 内容目录

主要内容路径如下：

- 论文：`content/publication/<slug>/index.md`
- 新闻：`content/post/<slug>/index.md`
- 成员：`content/authors/<slug>/_index.md`
- 研究方向：`content/research/<slug>/index.md`
- 平台设备：`content/facilities/<slug>/index.md`
- 论文、书籍、会议论文、专利：都在 `content/publication/<slug>/index.md`，通过 `publication_types` 区分
- 相册：`content/gallery/<year>/index.md`，按年份组织
- Tour 页面：`content/tour/index.md`

旧页面不会删除：

- 原 Research 页面仍在 `/blog/`
- 原 Platforms 页面仍在 `/event/`
- 原 Team 页面仍在 `/people/`

导航已经逐步指向新的 `/research/` 和 `/facilities/`，旧路径继续可访问。

## 图片和 PDF

后台上传目录规划如下：

- `static/uploads/publications/`
- `static/uploads/patents/`
- `static/uploads/news/`
- `static/uploads/people/`
- `static/uploads/research/`
- `static/uploads/facilities/`
- `static/uploads/gallery/`

Projects 当前不作为独立菜单和后台模块维护。Patents 当前归入 Publications，下拉菜单中可进入总览、Journal Articles、Books、Conference Papers 和 Patents 分类。

Team 成员排序在后台 People collection 的 `Group Order` 中维护。每条记录包含一个分组名和一个顺序号，数字越小越靠前；同一个人可以为不同分组设置不同顺序。

前台访问路径通常是 `/uploads/<类型>/<文件名>`。Hugo Blox 对论文 PDF 等按钮会通过 `relURL` 处理，部署到 GitHub Pages 子路径时通常能随 `baseURL` 工作。

封面图最稳定的方式仍是 Hugo Blox 的 page bundle 方式：把图片放在对应内容文件夹内，并命名为 `featured.jpg`、`featured.png` 或在 front matter 的 `image.filename` 指定同文件夹图片。后台静态上传图片适合正文插图、证书、PDF 和相册图片。

如果网站部署在 `https://micronanorobotics.github.io/MNRLab.github.io/` 并发现正文里手写的 `/uploads/...` 图片 404，可以选择：

1. 配置自定义域名，让 `/uploads/...` 成为站点根路径。
2. 把 `data/decap_cms_config.yaml` 中各 collection 的 `public_folder` 临时改为 `/MNRLab.github.io/uploads/<类型>`。
3. 尽量使用 Hugo Blox 的 page bundle 图片机制，避免手写绝对图片路径。

## 自动上线原理

GitHub Actions 中的 `.github/workflows/publish.yaml` 监听 `main` 分支 push。后台发布内容后，本质上是向仓库写入 Markdown、图片或 PDF 文件；这些提交会触发 Actions，Actions 使用 Hugo Extended 构建 `public/`，然后发布到 GitHub Pages。

更新时间通常为几十秒到几分钟。GitHub Actions 队列繁忙、图片较多或 Hugo 模块下载较慢时会更久。

## 常见问题

图片不显示：检查文件是否在 `static/uploads/` 或页面文件夹内，路径大小写是否一致，GitHub Pages 子路径是否需要调整 `public_folder`。

后台登录失败：检查 OAuth proxy 是否可访问，GitHub OAuth App callback URL 是否正确，登录账号是否有仓库权限。

保存后网站没有立刻更新：到 GitHub 仓库的 Actions 页面查看 `Deploy website to GitHub Pages` 是否正在运行或失败。

构建失败：先本地运行 `hugo --minify --ignoreVendorPaths=""`，通常可以看到具体的 front matter、日期或 Markdown 语法错误。

看不到学生提交内容：如果启用 editorial workflow，内容可能仍在草稿或审核状态，需要管理员在后台发布。
