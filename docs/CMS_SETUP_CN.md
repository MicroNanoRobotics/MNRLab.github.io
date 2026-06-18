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
- Projects 科研项目
- Patents 专利成果
- Gallery 实验室相册

## GitHub 登录配置

当前配置使用 GitHub backend：

```yaml
backend:
  name: github
  repo: MicroNanoRobotics/MNRLab.github.io
  branch: main
```

GitHub Pages 需要一个 OAuth proxy 才能完成浏览器登录。推荐做法是：

1. 创建 GitHub OAuth App。
2. 部署一个 Decap CMS GitHub OAuth proxy。
3. 将 OAuth App 的 client secret 放在 proxy 的环境变量中。
4. 在 `data/decap_cms_config.yaml` 的 `backend` 下增加 proxy 地址，例如：

```yaml
backend:
  name: github
  repo: MicroNanoRobotics/MNRLab.github.io
  branch: main
  base_url: https://your-oauth-proxy.example.com
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

## 媒体上传路径

后台上传文件保存到 `static/uploads/` 下的分类目录。保存后 Markdown 中会写入 `/uploads/<类型>/<文件名>`。

如果使用 GitHub Pages 仓库子路径并发现媒体 404，请参考 `docs/MAINTENANCE_CN.md` 中的子路径说明。
