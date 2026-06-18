# Decap CMS 后台配置说明

后台入口：`/admin/`

本项目沿用 Hugo Blox 的 Decap CMS 插件：

- 页面入口：`content/admin/index.md`
- 配置源文件：`data/decap_cms_config.yaml`
- 构建输出：`public/admin/index.html` 和 `public/admin/config.yml`

## 当前后台能力

后台已配置以下 collections：

- Publications 论文成果
- News 新闻动态
- People 团队成员
- Research 研究方向
- Platforms / Facilities 平台设备
- Journal Articles / Books / Conference Papers / Patents（均归入 Publications 内容体系）
- Gallery by Year 按年份维护实验室相册
- Tour 页面

Projects 已从当前后台和菜单中移除；如后续需要恢复，可以重新添加 `content/projects` 与 CMS collection。

## GitHub 登录配置

当前配置使用 GitHub backend：

```yaml
backend:
  name: github
  repo: MicroNanoRobotics/MNRLab.github.io
  branch: main
  site_domain: zesty-marigold-84172f.netlify.app
```

当前没有开启 Open Authoring。任何电脑都可以打开 `/admin/` 后台页面，但只有拥有本仓库写权限的 GitHub 账号才能登录并修改内容。也就是说，只要你的 GitHub 账号是仓库 owner 或 collaborator，就可以在任意电脑登录后台维护网站；其他账号不能写入。

GitHub Pages 本身不提供 Decap CMS 所需的 GitHub OAuth 登录代理，因此本项目使用 Netlify 站点 `zesty-marigold-84172f.netlify.app` 作为后台登录认证站点。前台正式访问仍可以继续使用 GitHub Pages。

如果未来更换 Netlify 站点，推荐做法是：

1. 创建 GitHub OAuth App。
2. 部署一个 Decap CMS GitHub OAuth proxy。
3. 将 OAuth App 的 client secret 放在 proxy 的环境变量中。
4. 在 `data/decap_cms_config.yaml` 的 `backend` 下增加 proxy 地址，例如：

```yaml
backend:
  name: github
  repo: MicroNanoRobotics/MNRLab.github.io
  branch: main
  site_domain: your-netlify-site.netlify.app
```

不要把 client secret、token 或个人密码写入本仓库。

## 本地后台测试

本地测试不需要 OAuth：

```powershell
npx decap-server
hugo server
```

然后打开 `http://localhost:1313/admin/`。

如果后台提示找不到 local backend，确认 `npx decap-server` 正在运行，并且 Hugo 是开发模式启动的。

## 直接提交与审核模式

默认启用 editorial workflow：

```yaml
publish_mode: editorial_workflow
```

管理员可以在后台审核后发布内容。若当前认证方案不支持该模式，删除这一行即可改为直接提交模式。

建议实验室长期维护时使用审核模式，尤其是允许学生提交新闻、论文或相册内容时。

## Team 组内排序

团队成员在 People collection 中维护。`User Groups` 决定成员属于哪些分类，`Group Order` 决定成员在每个分类里的顺序。

例如同一位成员属于 `PhD Students` 和 `Alumni`，可以分别添加两条排序：

- `group: PhD Students`，`order: 2`
- `group: Alumni`，`order: 10`

数字越小越靠前。没有填写的分类会使用默认排序。

## 媒体上传路径

后台上传文件保存到 `static/uploads/` 下的分类目录。保存后 Markdown 中会写入 `/uploads/<类型>/<文件名>`。

如果使用 GitHub Pages 仓库子路径并发现媒体 404，请参考 `docs/MAINTENANCE_CN.md` 中的子路径说明。
