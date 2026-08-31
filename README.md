<p align="right">
  <b>中文</b> | <a href="./README_EN.md">English</a>
</p>

# 🚀 Study via AI (10倍速 AI 辅助自适应学习操作系统)

<p align="center">
  <img src="https://img.shields.io/badge/Release-v0.1.1-brightgreen?style=for-the-badge" alt="Release v0.1.1" />
  <img src="https://img.shields.io/badge/Antigravity-Agent_Skill-blue?style=for-the-badge&logo=google" alt="Antigravity Skill" />
  <img src="https://img.shields.io/badge/Pedagogy-Socratic_%2B_Feynman-orange?style=for-the-badge" alt="Pedagogy" />
  <img src="https://img.shields.io/badge/State_Machine-Decoupled-green?style=for-the-badge" alt="State Machine" />
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="License" />
</p>

> **让 AI 成为你的顶级私教与苏格拉底式引路人。拒绝填鸭与自嗨，以“单点沉浸教学 + 双重内化考核 + 12 份标准化知识资产落盘”，带你 10 倍速彻底吃透任何硬核技能、技术文档或专业教材。**

---

## ⚡ 极简安装与升级 (Quick Install)

### 方式一：直接告诉 AI 智能体（最推荐，0 门槛）

直接复制以下一句话发送给 **Google Antigravity / Claude Code / Codex / OpenCode / ZCode / OpenClaw / Reasonix** 等任何支持导入 GitHub 仓库或 Skill 的 AI 平台：

```text
安装这个 skill https://github.com/lowellran/Study_via_AI
```
> 💡 *后续若有版本更新，再次发送同一句话即可自动无损升级。*

---

### 方式二：命令行一键安装 (CLI)

```bash
# 全局快速安装到 skills 仓库
npx skills add lowellran/Study_via_AI -y -g
```

---

### 方式三：手动放置文件 (Manual)

1. 克隆或下载本仓库：
   ```bash
   git clone https://github.com/lowellran/Study_via_AI.git
   ```
2. 将 `Study_via_AI` 文件夹放置到全局配置目录中：
   - **Windows**: `C:\Users\<用户名>\.gemini\config\skills\Study_via_AI\`
   - **macOS / Linux**: `~/.gemini/config/skills/Study_via_AI/`

---

## 🚀 极速上手 (Quick Start)

安装完成后，在任意对话中直接输入：
```text
使用 Study_via_AI 帮我学习 [主题名称 / 上传教材文档 / 粘贴文章链接]
```

**跨会话断点续学**（随时新开对话窗口）：
```text
继续 [文件夹名称或主题名称] 的学习
```

---

## 📊 架构范式对比 (Paradigm Comparison)

| 核心维度 | 传统问答/总结类 Prompt | 纯大纲路线规划工具 | **Study via AI (学习操作系统)** |
| :--- | :--- | :--- | :--- |
| **教学颗粒度** | 一次性输出长篇大论，容易造成认知过载 | 只生成章节标题，缺乏逐点精讲 | **极小颗粒度**：一次对话仅讲一个知识点，通俗比喻讲透 |
| **自有资料锚定** | 仅根据通用大模型知识作答 | 简单提取文本大纲 | **精准溯源**：精确指出教材第几章第几页 / 视频时间戳 |
| **内化考核深度** | 无考核或浅层提问，易产生“看懂了的假象” | 仅提供自测题目，无即时纠错 | **双重内化闭环**：AI 考官逐题打分 + 12 岁儿童白话费曼诊断 |
| **抗遗忘与上下文** | 长对话（3小时+）后注意力涣散、规则遗忘 | 无状态流转机制 | **机器状态头解耦**：硬盘存储状态 > Context 记忆，杜绝漂移 |
| **成果资产化** | 聊天窗口关闭即丢失，无体系沉淀 | 仅生成简单的日志文件 | **12 份标准 Markdown 档案**：带 `[TOC]` 大纲树与一页速查表 |
| **交互自由度** | 被动顺着 AI 预设流程走 | 难以动态调整进度 | **全局驾驶舱**：支持 `/skip`, `/jump`, `/status`, `/mode` |

---

## 💻 多平台兼容性矩阵 (Compatibility Matrix)

| 开发环境 / AI Agent 平台 | 兼容性支持 | 说明与支持特性 |
| :--- | :---: | :--- |
| **Google Antigravity** | 🌟 **完美原生支持 (推荐)** | 自动识别 Skill、自动文件读写、静默落盘 12 份文档 |
| **Claude Code** | ✅ **完全支持** | 原生工具写入、跨会话断点续学、支持全局与项目级配置 |
| **OpenAI Codex CLI** | ✅ **完全支持** | 原生执行与自动化工作流 |
| **OpenCode / ZCode / OpenClaw** | ✅ **完全支持** | 完整支持状态机与命令系统 |
| **Cursor / Windsurf** | ✅ **支持** | 引入作为项目 Rules / Agent Skill 配置 |
| **普通网页端 (Web Chat)** | ⚠️ **需手动落盘** | 网页版因缺少本地磁盘写入权限，需由用户手动复制生成的 Markdown |

---

## 📚 真实场景实战示例 (Real-World Examples)

本仓库在 [`examples/`](./examples/) 目录中提供了涵盖**硬核嵌入式开发、两性社交心理学、流行声乐发声**三个真实场景的完整真实实录与落地范例：

1. ⚙️ **[GD32F4 嵌入式固件开发与硬件驱动实战](./examples/gd32_embedded_development/)**
   - 包含：`00` 号 RCU 时钟树与外设 5 级阶梯路线图、`01` 号真实工程代码精解、RCU/GPIO 考官打分实录与一页速查表。
2. 💬 **[两性社交动态与博弈心理学实战](./examples/pua_dynamics_mastery/)**
   - 包含：`00` 号进阶大纲规划、`01` 号进化心理学与奖品框架真实对话实录、双重价值符号拆解与一页速查表。
3. 🎵 **[KTV 流行声乐发声与混声实战](./examples/ktv_vocal_mastery/)**
   - 包含：`00` 号声乐进阶阶梯规划、`01` 号横膈膜呼吸支持与声带闭合真实对话实录与速查表。

---

## 🔄 全流程工作流与状态机

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

| 文件名 | 内容概述 |
| :--- | :--- |
| `00_overview_and_roadmap.md` | 首行机器状态头 + 5 级学习阶梯 + 20 小时精选计划总览与实时进度清单 |
| `01_plan_01_<topic>.md` | Plan 01 完整真实实录 + 附录：Plan 01 一页速查表 |
| `02_plan_02_<topic>.md` ~ `10_plan_10_<topic>.md` | Plan 02 ~ Plan 10 各阶段学习实录与速查表 |
| `255_final_synthesis_and_cheatsheet.md` | 全域终极大考与费曼实录 + 附录：全域终极大一统速查表 (Master Sheet) |

---

## ⚡ 全局快捷控制指令 (Command Center)

学习过程中随时可以使用以下指令控制节奏：

* `/skip`：跳过当前知识点讲解或考核，快速进入下一环节。
* `/jump <01~10|255>`：直接跳转到指定 Plan。*(自带前序依赖安全气囊，跳级时会提醒确认)*
* `/status`：调出当前学习进度与掌握度阶梯。
* `/cheatsheet [01~10|255]`：直接调出指定 Plan 或全域终极的一页速查表。
* `/mode <quick|deep>`：切换模式（`quick` 极速突击 / `deep` 深度攻坚）。

---

## 📄 开源许可证

本项目采用 [MIT 许可证](LICENSE)。欢迎提交 PR、提出 Issue，或在日常学习中享受 10 倍速深度的成长！⭐️
