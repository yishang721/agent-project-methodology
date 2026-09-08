# CREDITS — 致谢与出处

本项目是「从真实项目事故中蒸馏出来的方法论」，构建过程受益于以下分享者与开源项目。分两层致谢：**体系归属**（我们自建的体系）与**内容上游**（体系内部流转的外部来源）。

---

## 体系归属

- **对策库体系**（按问题组织、症状式对策卡、三态生命周期 ⏳✅❌）—— 忆殇 × 小殇（WorkBuddy 协作）原创构建。其中「三态生命周期」对齐 [Table-GitHub-Capability-Router](https://github.com/duoduoler-ops/Table-GitHub-Capability-Router) 的状态机设计（简化致敬）。
- **卡结构模板 / 踩坑索引器**（`templates/pitfall-card-template.md` + `tools/build_index.py`）—— 忆殇 × 小殇原创；卡结构中的召回锚点思想借鉴 LocalVid-Summarizer（见下）。
- **本仓库两个技能的方法论本体**（判级 / 三件套 / 收尾触发 / 提纯四要素 / 坑三级分流）—— 忆殇 × 小殇原创，由 2026-09-07 前后的多起真实事故（记忆注入截断、备份声称失实）淬炼而成。

## 内容上游

| # | 上游 | 贡献 | 使用方式 | 许可 |
|---|---|---|---|---|
| 1 | **吴嘉文GW**（抖音 @吴嘉文GW + [其公开飞书知识库《项目无缝同步》提示词原版](https://my.feishu.cn/wiki/E8XNw07B6iJNEwkR6PWcCGtxnMg)） | 「交接文档驱动」工作法：十板块活文档结构、开场/收尾双口令协议、「按文件接管，不按聊天记录接管」核心思想（`skills/handoff/` 模式 B） | 本地化改写（增补类型适配、反模式清单、收尾纪律） | **遵循 CC BY-NC（作者指定）**：非商用免费、需保留署名与原版链接；商用（整合进付费产品 / 商业服务 / 企业方案 / 本仓库商业化）需事先取得作者授权 |
| 2 | **huntse/agent-skills** `handoff` v1.0.1（原 GitHub 仓库已 404，经 LobeHub 市场缓存页取回） | `skills/handoff/` 模式 A（一次性派单）的模板骨架：Goal & acceptance criteria / Context / Constraints & verification 结构、Must-not 围栏、被排除方案字段 | 大改（重写措辞、泛化约定段、并入模式 B） | 原仓库标注 MIT；原链已失效，特此存档署名 |
| 3 | **一只桌子_table**（B站 up_id 945411；GitHub [duoduoler-ops/Table-GitHub-Capability-Router](https://github.com/duoduoler-ops/Table-GitHub-Capability-Router)） | 能力冷库治理体系（能力登记/状态机/路由表脚本生成）——本仓库作者的自建冷库即基于其 workflow 搭建；另有 Agent 运行逻辑三讲（Chatbot vs Agent 判据、规则文档动作化、子代理闸门）深刻影响了本方法论的执行循环设计 | 治理体系直接使用；思想融入设计 | MIT；其 B站内容为署名引用 |
| 4 | **sunglasses233/LocalVid-Summarizer**（[GitHub](https://github.com/sunglasses233/LocalVid-Summarizer)，MIT） | 对策卡 schema 精华：召回锚点（retrieval questions）、evidence 时间戳逐条验证、AI 补充与素材事实严格分离、父子卡 | 思想借鉴（模板 `templates/pitfall-card-template.md` 的结构来源之一） | MIT |
| 5 | **engrecho / all-platform-video-extract**（MIT，经 sucaizy.com 分发包审计后取其解析脚本） | 作者自建「视频链接→对策卡」工作流中 L3 解析兜底脚本的来源（未随本仓库分发） | 仅体系致谢（该脚本在本机工作流中，与本仓库方法论无代码耦合） | MIT |
| 6 | **mattpocock/skills** `grill-me`（[GitHub](https://github.com/mattpocock/skills)，MIT，255k★） | 启动判级后的方案拷问环节（外部配套技能，本仓库不收录本体）；未安装时降级为 AI 逐题澄清 | 外链推荐 | MIT |
| 7 | **Boris Cherny × Diana Hu**（YC Startup School 2026-07-28 访谈） | 提纯思想：规则三分类（必要 context / workflow control / 安全边界）、「删了不是留白，换写法」（目标 + guardrails + exit criteria）、「验证 > prompt 工程」 | 思想引用（提纯四要素的理论根基） | 署名致谢 |

## 引用与改编的边界说明

- 标注「本地化改写 / 大改」的条目：结构思想保留，文本已重写，适配部分为原创。
- 标注「思想引用 / 思想借鉴」的条目：仅方法论层面受益，无文本复制。
- **双层许可声明**：本仓库整体以 MIT 发布，**仅覆盖**标注为「忆殇 × 小殇原创」的部分及上述已改写的衍生文本；其中引用吴嘉文GW「交接文档驱动」工作法的部分（`skills/handoff/` 模式 B），**遵循 CC BY-NC：非商用免费（须保留署名与[原版文档](https://my.feishu.cn/wiki/E8XNw07B6iJNEwkR6PWcCGtxnMg)链接）、商用需事先取得作者授权**。双层权属以此为准，互不覆盖。
- 各上游内容的版权归原作者所有。
- 若你是上述上游作者，对署名方式或引用范围有异议，欢迎提 issue，我们会第一时间处理。
