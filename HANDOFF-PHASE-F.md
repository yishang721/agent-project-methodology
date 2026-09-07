# Phase F — 上线交接包（忆殇操作指引）

日期：2026-09-07 · 状态：本地仓已就绪（branch `main`，3 commits），等你执行 GitHub 侧动作

## 一、GitHub 建仓 + push（你操作，约 2 分钟）

1. 浏览器打开 https://github.com/new
2. Repository name 填：`agent-project-methodology`
3. 选 **Public**；**不要**勾选任何初始化选项（README/.gitignore/license 都不勾——本地已有）
4. 点 Create repository
5. 回到本地，在仓库目录执行（复制即可）：

```bash
cd "D:/ai-code/workbuddy workspace/agent-project-methodology"
git remote add origin git@github.com:yishang721/agent-project-methodology.git
git push -u origin main
```

（SSH key 已配好：`~/.ssh/id_ed25519_vault`，与 memory-vault 同通道，实测认证通过）

6. push 成功后把仓库 URL 发我 → 我复核线上状态 + 完成告知动作（见下）。

## 二、告知文两篇（已定稿，可直接发）

### ① 吴嘉文GW（抖音私信，repo 上线后发）

> 你好，我是 WorkBuddy 用户。看了你《WorkBuddy 项目同步》那期视频，按你公开的交接文档提示词做了本地化适配（加了收尾提纯机制和启动判级），最近把配套的项目启动方法论整理成了开源仓库，你的「交接文档驱动工作法」是其中活文档协议的直接来源，已在 CREDITS.md 首位署名并标注了你的飞书知识库原版出处。仓库地址：`https://github.com/yishang721/agent-project-methodology`。如对署名方式有偏好，随时告诉我，我会立即调整。

### ② 一只桌子_table（GitHub Issue，发到 Table-GitHub-Capability-Router 仓库；或 B站私信）

> 标题：致谢：基于 Table-GitHub-Capability-Router 搭建的个人治理体系 + 开源衍生方法论
>
> 您好！我基于 Table-GitHub-Capability-Router 搭建了自己的能力冷库（cap 卡 + level1 路由 + workflow.py 全流程），并参考您的状态机给个人对策库设计了三态生命周期（⏳/✅/❌）。最近把这些实践蒸馏成一套项目启动方法论，整理成开源仓库 agent-project-methodology（MIT），CREDITS.md 中已将您的仓库列为治理体系来源，三态设计的简化致敬也有注明。附：https://github.com/yishang721/agent-project-methodology 。感谢这套系统，受益良多。

## 三、发布前最后核对清单（push 前扫一眼）

- [x] 本地仓 3 commits（ed7180a 初始 → sanitize 脱敏 → index 修正）
- [x] 脱敏终扫报告在仓内（SANITIZE-REPORT.md，全部残留=署名/致谢/安装指令三类，零隐私）
- [x] README（拍板稿定稿版）/ CREDITS（7 上游双层）/ LICENSE（MIT, yishang721）
- [x] 双技能 frontmatter：name 英文 + display_name 中文名（项目启动三件套 / 交接文档）
- [x] grill-me 两态集成行三处一致（母本/zcode 镜像/发布版）
- [x] build_index.py 在 pitfalls/ 上开箱跑通（2 卡索引已生成）
- [ ] GitHub 建仓（你）
- [ ] push（你）
- [ ] 两篇告知文（你发吴嘉文GW；Issue 我来开或你自贴）

## 四、上线后维护约定（母本 → 仓库单向同步）

本机母本（`~/.workbuddy/skills/`）继续演化；要同步到仓库时：改 repo 内对应文件 → git commit → push。**禁止反向**（repo 直接改母本）。发布版与母本的已知差异（脱敏泛化点）见 SANITIZE-REPORT.md 与 handoff 发布版「操作者约定」段。
