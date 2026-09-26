# Qiming Huang 的学术主页

这是一个静态网站。`index.html` 由 `content/` 中的文件生成，并保存在仓库中，因此 GitHub Pages 可以直接发布，不需要额外的构建服务。**请编辑源文件，不要直接修改 `index.html`。**

## 编辑位置

- `content/profile.html`：个人简介、头像和联系方式。
- `content/news.html`：News，最新消息放在最上面。
- `content/research.html`：研究方向。
- `content/publications/`：每篇论文一个 HTML 文件。文件名使用 `YYYY-MM-简称.html`，生成时按文件名倒序排列。
- `stylesheet.css`：布局和样式。
- `templates/index.html`：整个页面的外壳；只有调整页面结构时才需要编辑。
- `images/`、`data/`：页面引用的图片和下载文件。

新增论文时，可以复制 `content/publications/` 中的一篇，改好文件名、图片路径、标题、作者、会议、链接和简介。图片放在 `images/` 下。需要黄色高亮时，在该论文的 `<tr>` 上加 `class="featured-publication"`。

新增 News 时，在 `content/news.html` 的列表顶部添加一条 `<li>`。

## 生成和预览

在仓库根目录运行：

```sh
python3 scripts/build.py
python3 -m http.server 8000
```

浏览器打开 `http://localhost:8000/`。每次编辑源文件后，重新运行 `python3 scripts/build.py` 并刷新浏览器。提交时，记得将生成的 `index.html`、源文件和新增图片一起提交。

检查 `index.html` 是否已经按最新内容生成：

```sh
python3 scripts/build.py --check
```

生成脚本只使用 Python 标准库，无需安装依赖。
