# AI 能力画像（ai-profile）

让你最常用的 AI，根据你和它的真实使用记录，给你做一份 30 项的能力画像：六个领域、雷达图、每项的证据和改进建议。

当前版本：**0.7**

## 安装

在电脑终端里运行（需要先装好 Node.js）：

```
npx skills add billwonghk/ai-profile
```

支持 Claude Code、Codex、Gemini CLI、Cursor、Antigravity 等支持 Agent Skills 标准的工具。

不熟悉命令行的话，也可以下载本仓库的压缩包，把里面的 `ai-profile` 文件夹放进对应工具的 skills 目录，例如 Claude Code 是 `~/.claude/skills/`，Codex 是 `~/.codex/skills/`。

## 使用

在 AI 工具里说一句：

> 给我做一份 AI 能力画像

AI 会读取它能看到的记录（只读、只统计，不改任何文件），生成 `ai-profile.html` 报告网页，双击就能在浏览器里打开。网页右上角可以导出 Markdown 原报告。

## 更新

```
npx skills update ai-profile
```

## 只有网页版 AI 怎么办

DeepSeek、千问等网页版 AI 一般不能安装 skill。把 [`docs/AI能力画像-评估指令-v0.7.md`](docs/AI能力画像-评估指令-v0.7.md) 整份发给它，按文档开头的说明使用即可。

## 说明

- 这份评估由 AI 根据自己能看到的使用记录生成，不是标准化心理测评。
- 只评能力，不评品行；不输出项目名、目录名、人名和个人敏感信息。
- 在任何一个 AI 上使用不足半年的，报告会提示参考意义有限。

## 更新记录

- **0.7**：30 项；新增“AI 使用资历”“优先级管理”“复盘与沉淀”；“成型与收敛”“价值与反馈”合并评估，“价值与反馈”权重减半；统一使用电脑系统时区；统一报告模板。
