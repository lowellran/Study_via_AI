<p align="right">
  <b>中文</b> | <a href="./README_EN.md">English</a>
</p>

<p align="center">
  <h1 align="center">🚀 Study via AI</h1>
  <p align="center"><b>10x Socratic AI Study OS for Agentic Coding & Knowledge Mastery</b></p>
  <p align="center"><i>From Zero to Deep Mastery: Single-concept Immersion + Dual Inner-Assessment + 12 Structured Markdown Assets Silent Dump</i></p>
</p>

<p align="center">
  <a href="https://github.com/lowellran/Study_via_AI/stargazers"><img src="https://img.shields.io/github/stars/lowellran/Study_via_AI?style=for-the-badge&logo=github&color=gold" alt="Stars" /></a>
  <a href="https://github.com/lowellran/Study_via_AI/releases"><img src="https://img.shields.io/badge/Release-v0.1.2-brightgreen?style=for-the-badge" alt="Release" /></a>
  <img src="https://img.shields.io/badge/Supported-Claude_Code_%7C_Codex_%7C_Antigravity_%7C_Cursor-blue?style=for-the-badge" alt="Platforms" />
  <img src="https://img.shields.io/badge/Pedagogy-Socratic_%2B_Feynman-orange?style=for-the-badge" alt="Pedagogy" />
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="License" /></a>
</p>

---

> 💡 **告别“向 AI 提问关掉窗口全忘光”的浅层学习！**  
> `Study_via_AI` 是专为 **Google Antigravity、Claude Code、OpenAI Codex CLI、Cursor、Windsurf** 等现代化 Agent 环境打造的自适应学习操作系统。拒绝大段填鸭，通过**严谨状态机、单点通俗拆解、AI 考官逐题打分与 12 岁费曼纠错**，自动生成 12 份可直接归档沉淀的 Markdown 终身知识库。

---

## ⚡ 极速一键安装 (Quick Install)

### 方式一：直接在 Agent 对话中发送（0 门槛，最推荐）

直接复制以下一句话发送给 **Google Antigravity / Claude Code / Codex / Cursor**：

```text
安装这个 skill https://github.com/lowellran/Study_via_AI
```
> 💡 *后续若有版本更新，再次发送同一句话即可自动无损升级。*

---

### 方式二：命令行一行安装 (One-Liner CLI)

#### 针对 Codex CLI:
```bash
# Windows (PowerShell)
git clone https://github.com/lowellran/Study_via_AI.git "$env:USERPROFILE\.codex\skills\Study_via_AI"

# macOS / Linux
git clone https://github.com/lowellran/Study_via_AI.git ~/.codex/skills/Study_via_AI
```

#### 针对通用 Agent Skills:
```bash
npx skills add lowellran/Study_via_AI -y -g
```

---

## 🎯 30 秒上手体验 (Quick Start)

安装完成后，在任意对话中直接输入：
```text
使用 Study_via_AI 帮我学习 [主题名称 / 上传教材文档 / 粘贴文章链接]
```

**跨会话断点续学**（随时新开对话窗口，永不迷失进度）：
```text
继续 [文件夹名称或主题名称] 的学习
```

---

## 📊 为什么选择 Study via AI？(Paradigm Comparison)

| 核心维度 | 传统问答 / 总结类 Prompt | 纯大纲路线工具 | 🚀 **Study via AI (学习操作系统)** |
| :--- | :--- | :--- | :--- |
| **教学颗粒度** | 一次性输出长篇大论，认知过载 | 只生成章节标题，缺乏精讲 | **极小单点沉浸**：一次对话仅讲透一个知识点 |
| **自有资料锚定** | 脱离教材，纯靠通用知识发挥 | 仅粗暴提取大纲 | **精准溯源**：精确指出教材第几章第几页 / 视频时间戳 |
| **内化考核深度** | 毫无考核或浅层提问，“假装看懂” | 仅提供自测题目，无即时纠错 | **双重内化闭环**：AI 考官逐题打分 + 12 岁儿童白话费曼诊断 |
| **抗遗忘与上下文** | 长对话后规则遗忘、注意力漂移 | 无状态流转机制 | **机器状态头解耦**：硬盘存储状态 > Context 记忆，杜绝漂移 |
| **成果资产化** | 聊天窗口关闭即丢失，零沉淀 | 仅生成零散日志 | **12 份标准 Markdown**：带大纲树、对话实录与一页速查表 |
| **掌控自由度** | 被动顺着 AI 预设流程走 | 难以动态调整进度 | **全局驾驶舱**：支持 `/skip`, `/jump`, `/status`, `/mode` |

---

## 🔄 全流程工作流与状态机 (Workflow)

```mermaid
stateDiagram-v2
    [*] --> Phase0_Initialization: 用户输入（主题/文档/视频/链接）
    Phase0_Initialization --> Phase1_Roadmap_Gen: 确认学习范围 & 建立专属文件夹
    Phase1_Roadmap_Gen --> Phase2_Plan_Execution: 静默落盘 00_overview_and_roadmap.md
    
    state Phase2_Plan_Execution {
        [*] --> Single_Concept_Teaching: 启动 Plan N (读取首行 SYSTEM_STATE)
        Single_Concept_Teaching --> QnA_and_Discussion: 讲解单个知识点 + 溯源指引
        QnA_and_Discussion --> Single_Concept_Teaching: 答疑直至搞懂（下一个知识点）
        QnA_and_Discussion --> Dual_Validation: 当前 Plan 知识点全部学完
        
        state Dual_Validation {
            [*] --> AI_Examiner: 方法三：AI 考官逐题单题测试与百分制评分
            AI_Examiner --> Feynman_Loop: 考官测试通关 -> 方法六：12岁费曼循环
            Feynman_Loop --> [*]: 费曼纠错通关
        }
        
        Dual_Validation --> Archive_Plan_Document: 原生工具静默写入 01~10 号实录
        Archive_Plan_Document --> Update_Machine_State: 更新 00 首行 SYSTEM_STATE 与进度复选框
        Update_Machine_State --> Display_Full_Cheatsheet: 前台输出成就卡片与完整一页速查表
        Display_Full_Cheatsheet --> Next_Plan_Or_Finish: 阶梯晋级定位 & 询问继续
    }
    
    Phase2_Plan_Execution --> Phase3_Final_Synthesis: 10 次计划全部通关
    Phase3_Final_Synthesis --> [*]: 全域总考官 + 全域大费曼 -> 静默落盘 255 号终极文档
```

---

## 📁 规范化 12 份 Markdown 资产体系

学完整个课程后，系统将在你的专属学习目录下自动生成 12 份排版严谨、包含 `[TOC]` 大纲树的 Markdown 知识库：

```text
📁 你的专属学习目录/
├── 📄 00_overview_and_roadmap.md             # 机器状态头 + 5 级阶梯 + 20 小时计划与总进度
├── 📄 01_plan_01_<topic>.md                  # Plan 01 对话实录 + 附录：Plan 01 一页速查表
├── 📄 02_plan_02_<topic>.md                  # Plan 02 对话实录 + 附录：Plan 02 一页速查表
│   ...
├── 📄 10_plan_10_<topic>.md                  # Plan 10 对话实录 + 附录：Plan 10 一页速查表
└── 📄 255_final_synthesis_and_cheatsheet.md  # 全域总考官与大费曼实录 + 全域大一统速查表 (Master Sheet)
```

---

## 💻 多平台兼容性矩阵 (Compatibility Matrix)

| 开发环境 / AI Agent 平台 | 兼容性支持 | 说明与支持特性 |
| :--- | :---: | :--- |
| **Google Antigravity** | 🌟 **完美原生支持 (推荐)** | 自动识别 Skill、自动文件读写、静默落盘 12 份文档 |
| **Claude Code** | ✅ **完全支持** | 原生工具写入、跨会话断点续学、支持全局与项目级配置 |
| **OpenAI Codex CLI** | ✅ **完全支持** | 原生执行与自动化工作流 |
| **Cursor / Windsurf** | ✅ **完全支持** | 引入作为项目 Rules / Agent Skill 配置 |
| **OpenCode / ZCode / OpenClaw** | ✅ **完全支持** | 完整支持状态机与命令系统 |
| **普通网页端 (Web Chat)** | ⚠️ **需手动落盘** | 网页版因缺少本地磁盘写入权限，需由用户手动复制生成的 Markdown |

---

## 📚 真实场景实战案例 (Real-World Examples)

本仓库在 [`examples/`](./examples/) 目录中提供了三个真实领域的落地档案库：

1. ⚙️ **[GD32F4 嵌入式固件开发与硬件驱动实战](./examples/gd32_embedded_development/)**
   - 包含：`00` 号 RCU 时钟树与外设 5 级阶梯路线图、`01` 号真实工程代码精解、RCU/GPIO 考官打分实录与一页速查表。
2. 💬 **[两性社交动态与博弈心理学实战](./examples/pua_dynamics_mastery/)**
   - 包含：`00` 号进阶大纲规划、`01` 号进化心理学与奖品框架真实对话实录、双重价值符号拆解与一页速查表。
3. 🎵 **[KTV 流行声乐发声与混声实战](./examples/ktv_vocal_mastery/)**
   - 包含：`00` 号声乐进阶阶梯规划、`01` 号横膈膜呼吸支持与声带闭合真实对话实录与速查表。

---

## ⚡ 全局快捷控制指令 (Command Center)

学习过程中随时可以使用以下指令控制节奏：

* `/skip`：跳过当前知识点讲解或考核，快速进入下一环节。
* `/jump <01~10|255>`：直接跳转到指定 Plan。*(自带前序依赖安全气囊，跳级时会提醒确认)*
* `/status`：调出当前学习进度与掌握度阶梯。
* `/cheatsheet [01~10|255]`：直接调出指定 Plan 或全域终极的一页速查表。
* `/mode <quick|deep>`：切换模式（`quick` 极速突击 / `deep` 深度攻坚）。

---

## 🤝 贡献与支持 (Contributing & Support)

欢迎提交 PR 或 Issue！如果你觉得这个 Skill 对你的深度学习有所启发和帮助，请给这个项目点一个 ⭐ **Star**，这是对开源作者最大的鼓励！

## 📄 开源许可证

本项目采用 [MIT 许可证](LICENSE)。
