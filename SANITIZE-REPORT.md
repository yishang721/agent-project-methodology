# Phase E 脱敏终扫报告（agent-project-methodology）

日期：2026-09-07 深夜 · 扫描范围：全仓 .md/.py（.git 除外）· 两轮扫描 + 整改 + 复扫

## 扫描模式（8 类）

人名（忆殇/小殇/周泉）· 绝对盘符路径 · 邮箱 · 密钥字样（sk-/ghp_/PRIVATE KEY）· B站 mid/up_id · 私库名（memory-vault/memory-value/skill-vault/对策库/.zcode/.workbuddy）· workbuddy.cn 内网域名 · app.asar 逆向细节

## 第一轮结果与整改

| 命中 | 处置 |
|---|---|
| `pitfalls/踩坑总索引.md` 标题含「对策库一览」、脚本 docstring 三处「对策库」 | ✅ 已整改：泛化为「踩坑总索引 / pitfalls 库」，重跑索引器验证通过，commit `sanitize` |
| 脚本自动生成的索引引用路径 `_tools/build_index.py` | ✅ 已整改为 `tools/build_index.py`（repo 相对），commit `fix index generator path hint` |

## 终扫残留 → 白名单（全部为有意保留，逐条说明）

| 残留 | 位置 | 白名单理由 |
|---|---|---|
| 「忆殇 × 小殇」人名（10 处） | CREDITS.md 体系归属段、README 落款 | **作者署名**，你已拍板「README 作者行写 忆殇 × 小殇（WorkBuddy 协作构建）」。非隐私泄漏——是版权与致谢归属 |
| `up_id 945411`（1 处） | CREDITS.md 一只桌子_table 条目 | **公开致谢必需**——B站 UP 公开 ID，用于指引读者找到上游作者 |
| 「对策库体系」名称（1 处） | CREDITS.md 体系归属段 | 体系名称本身是致谢对象（对应上游#4 卡结构），无私库路径泄露 |
| `~/.workbuddy/skills/`、`~/.zcode/skills/`（3 处） | README 安装段、SKILL.md §2 | **安装指令必需**——这两个是产品（WorkBuddy/zcode）的公开标准技能目录约定，非本机私有路径 |
| `app.asar`/`memory-collector`、`workbuddy.cn`、绝对盘符、邮箱、密钥 | — | **零命中** ✅ |

## 后续同步差异登记（2026-09-11）

模式 B 新增「主动提醒交接触发器」同步时的已知脱敏差异（母本 → 发布版单向）：

| 项 | 母本（本地） | 发布版 | 理由 |
|---|---|---|---|
| 小节标题后缀 | `（收尾口令的补充，2026-09-11 拍板合入）` | `（收尾口令的补充）` | 去掉本机协作事件叙事，发布版只留机制说明 |
| 触发阈值表述 | 含本机项目语境示例 | 泛化为通用阶段描述 | 泛化，语义不变 |
| project-bootstrap §3.2 | 指向「handoff 技能」 | 指向「同仓库 `skills/handoff/`」 | 发布版改仓库相对引用 |

正文其余逐字一致。新内容复扫：八类零新增命中。

## 结论

全部残留均为「署名/致谢/安装指令」三类有意内容，零隐私泄漏（无邮箱、无密钥、无私库路径、无逆向细节、无项目内部路径）。**可以发布。**
