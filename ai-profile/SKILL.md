---
name: ai-profile
description: 根据用户和 AI 的真实使用记录，生成 30 项“AI 能力画像”（统一样式的雷达图报告网页 + Markdown 原报告）。当用户说“做一份 AI 能力画像”“评估我用 AI 的能力”“ai-profile”“AI profile”时使用。
---

# AI 能力画像（v0.7）

这个 skill 让你根据自己能看到的使用记录，为用户生成一份诚实、有证据的 AI 能力画像。用户要的是一面镜子，不是一封表扬信。

## 执行步骤

1. **完整阅读 `references/instructions.md`**，那里是全部评估规则：基本原则、证据分级、30 项定义和评分标准、AI 使用资历的分档、合并多份报告的方法。
2. **按规则第一步到第四步执行**：先把记录找全（在用户电脑上运行时，查找这台电脑上所有 AI 工具的本机记录，包括已归档的），说明证据基础，统计使用数据，再逐项打分并写总结。
3. **按下面“输出报告”一节生成报告**，这一节代替规则文件里的第七步。

本机文件一律只读、只统计，不修改任何文件，不输出具体的项目名、目录名、文件名、人名和个人敏感信息。

## 输出报告

### 1. 生成数据 JSON

按 `references/instructions.md` 第六步和下面的格式，生成一个 JSON 对象，保存为当前目录下的 `ai-profile.json`：

```json
{
  "version": "0.7",
  "title": "AI 能力画像",
  "date": "YYYY-MM-DD",
  "tool": "你这个 AI 工具的名称",
  "timezone": "使用的时区（电脑系统时区）",
  "longest_usage_months": 8,
  "summary": ["三到五句大白话总评"],
  "influence": "影响评价的因素，没有就写“未发现”",
  "items": [
    {"no": 1, "score": 7, "grade": "A", "support": "支持证据", "counter": "反面证据或证据边界", "advice": "改进建议"}
  ],
  "strengths": [{"no": 7, "reason": "一句理由"}],
  "priorities": [{"no": 9, "reason": "一句理由", "need_evidence": false}],
  "evidence_basis": {
    "sources": [{"name": "数据来源", "where": "本机或云端", "grade": "A", "status": "读到了什么、多少"}],
    "range": "可见记录的时间范围",
    "sampling": "抽样阅读情况",
    "coverage": "高 / 中 / 低",
    "coverage_reason": "一句理由"
  },
  "usage": [{"label": "对话数量", "value": "数据", "confidence": "高"}],
  "task_types": [{"source": "数据来源", "distribution": "编程开发 50%，文档写作 20%……"}],
  "limitations": ["局限说明，一条一句"]
}
```

要求：`items` 必须有 30 条，`no` 从 1 到 30；`score` 是 1–10 的整数，证据不足写 `null`；权重、平均分、领域分由页面自动计算，不用填。

### 2. 用统一模板生成报告网页

**不要自己设计页面**，一律使用 `assets/report.html` 模板，保证所有人的报告样式一致。

- 能运行 Python 时：

  ```
  python3 <本 skill 目录>/scripts/build_report.py ai-profile.json ai-profile.html
  ```

- 不能运行 Python 时：读取 `assets/report.html`，把其中唯一的一处 `/*__DATA__*/null` 替换成上一步的 JSON 原文（不加引号），另存为 `ai-profile.html`。

页面右上角自带“导出 Markdown”按钮，可以下载或复制带数据块的 Markdown 原报告。

### 3. 告诉用户

用三到五句话说明结论，并告诉用户 `ai-profile.html` 和 `ai-profile.json` 保存在哪里，双击网页文件就能在浏览器里打开。

### 不能写文件时

如果你所在的环境不能创建文件，就直接输出 Markdown 原报告，最后附上第 1 步的 JSON（用 ```json 包起来），并提醒用户：把整份报告复制下来，粘贴到报告查看器里就能看到图文报告。

## 版本

当前版本 0.7。更新方法：`npx skills update ai-profile`。
