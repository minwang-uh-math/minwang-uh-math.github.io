# Min Wang — Academic Homepage

English academic homepage for Min Wang, Assistant Professor of Mathematics at University of Houston. Built with Jekyll for the existing GitHub Pages repository.

## 更新内容

- `_pages/about.md`：照片、个人简介、教育经历、博士后经历和新闻时间轴。
- `_data/news.json`：新闻内容和排序日期；默认展示最新 3 条，其余自动折叠。资助获奖消息目前按 CV 中的项目开始月份排列。
- `_pages/research.md`：研究方向和项目资助，按 Active、Completed 分类，并列出金额。
- `_data/publications.json`：论文、作者、期刊、年份、投稿状态、出版商链接（url）和 arXiv 编号。
- `_pages/teaching.html`：当前课程和可折叠的历史教学经历。
- `_pages/people.md`：Team 页面，按 Current 和 Previous 分类，不展示成员指导时间。
- `_pages/talks.html`：精选报告和学术服务。
- `images/min-wang.jpeg`：首页照片。
- `_data/navigation.yml`：顶部导航。
- `_layouts/academic.html`：共享页面结构、单位和联系方式。
- `assets/css/academic.css`：样式和手机适配。

首页采用浅色个人信息栏与正文左右分栏，其他页面保持简洁单栏，使用深红色点缀和较大的字体；手机上自动上下排列。Research 介绍使用本人提供的文字。网站不提供 CV 下载，不展示准备中的论文或博士委员会信息。

## 快速查看效果（无需 Ruby）

本次已准备好 Python 预览工具。在项目目录运行：

```sh
python3 scripts/preview.py
```

然后打开 http://127.0.0.1:4000 。按 `Ctrl+C` 停止；修改内容后重新运行即可更新预览。

首次使用或临时依赖目录已被清理时，先安装：

```sh
python3 -m pip install --target local/preview-deps python-liquid markdown PyYAML
```

此方式渲染实际页面内容、共享布局和样式，用于本地查看效果；正式发布仍由 Jekyll 构建。

## Jekyll 本地预览

安装 Ruby 和 Bundler 后，在项目目录执行：

```sh
bundle install
bundle exec jekyll serve
```

打开终端显示的本地地址（通常为 `http://127.0.0.1:4000`）。

## GitHub Pages

提交并推送至仓库中配置的 Pages 来源分支后，由 GitHub Pages 构建发布。预期地址为 https://minwang-uh-math.github.io/ 。本地修改本身不会更新线上站点。

原始 Academic Pages 模板及许可证保留。模板示例文章、论文、教学和演讲集合已从构建中排除；未使用的示例页面设为不发布。
