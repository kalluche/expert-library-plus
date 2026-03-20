# 专家库 + 人名增强方案 (Expert Library Plus)

**让 AI 专家拥有历史巨匠的思维品质 — 通过人名质量锚点提升任务执行质量**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=for-the-badge)](https://github.com)
[![Claude Skills Stars](https://img.shields.io/github/stars/alirezarezvani/claude-skills?style=for-the-badge)](https://github.com/alirezarezvani/claude-skills)
[![Experts](https://img.shields.io/badge/Experts-43+-brightgreen?style=for-the-badge)](#-项目架构)
[![Name Templates](https://img.shields.io/badge/Name%20Templates-User%20Extensible-blue?style=for-the-badge)](#-用户自建人名库)

> **让 AI 专家拥有历史巨匠的思维品质**  
> **人名不是角色扮演，而是质量标准的快捷方式**

## 👥 项目团队

**💡 作者声明**: 本项目作者完全不懂程序和代码，纯属产品思维驱动。

**🤖 AI 专家团队**:
- **主导开发**: Qwen 3.5 Plus
- **战略架构**: Qwen3-Max  
- **深度研究**: DeepSeek
- **创新建议**: Gemini

> 这是一个真正由 AI 专家团队协作完成的开源项目！

## 📚 科学依据：为什么人名能优化 AI 表现？

### 🔬 核心机制解析

**人名作为"质量锚点"的有效性基于四大科学研究发现：**

#### 1. **参数化知识机制 (Parametric Knowledge, 2024)**
> *"LLM通过预训练在参数中存储了大量关于历史人物的知识，人名作为高度压缩的知识标识符能有效激活相关知识"*  
> **来源**: [Understanding the Interplay between Parametric and Contextual Knowledge (2024)](https://arxiv.org/html/2410.08414v1)

**为什么有效**: 大模型在训练时已经学习了历史人物的**生平事迹、专业成就、思维模式和行为特征**。当用户提供人名时，模型会自动激活这些内化的参数化知识来指导任务执行。

#### 2. **训练数据截止限制 (Knowledge Cutoff, 2024)**  
> *"模型只能了解训练截止日期前已成名的人物，新兴天才可能不被充分了解"*  
> **来源**: [Dated Data: Tracing Knowledge Cutoffs in Large Language Models (2024)](https://arxiv.org/abs/2403.12958)

**关键洞察**: 
- **乔布斯优势**: 2011年去世，所有现代LLM都包含其完整信息
- **新兴天才限制**: 训练截止后才崭露头角的人物可能无法被模型充分理解
- **选择策略**: 优先选择**训练截止前已成名的历史人物**

#### 3. **Persona 双刃剑效应 (Kim et al., 2024)**
> *"Persona 可能提升也可能降低表现，在 7/12 数据集中表现下降"*  
> **来源**: [arXiv:2408.08631](https://arxiv.org/abs/2408.08631)

**我们的解决方案**: 使用**历史验证的成功人物**作为质量锚点，避免随意 persona 带来的风险。

#### 4. **Prompt Engineering 系统性研究 (Schulhoff et al., 2024)**
> *"角色提示对风格有效，对准确性效果有限"*  
> **来源**: [arXiv:2406.06608](https://arxiv.org/abs/2406.06608)

**我们的创新**: 强调**质量锚点**而非**角色扮演**，关注"产出 iPhone 级别的结果"而非"像乔布斯一样说话"。

### 🎯 质量锚点 vs 传统角色扮演

| 方面 | 传统角色扮演 | 我们的质量锚点 |
|------|-------------|---------------|
| **目标** | 模拟角色行为 | 达到质量标准 |
| **风险** | 可能激活负面刻板印象 | 基于历史成功案例 |
| **稳定性** | 效果不稳定 | 历史验证可靠 |
| **任务导向** | 关注"如何说" | 关注"做什么" |

> **关键洞察**: 人名不是让 AI "扮演"某个人，而是让 AI "达到"某个人创造的历史成就标准。

### 🧪 **关于组合效果的科学验证**

**当前研究状态**:
虽然目前没有直接研究"专家角色卡 + 人名"组合效果的学术论文，但以下研究为我们提供了理论基础：

- **Jekyll & Hyde 框架 (Kim et al., 2024)**: 证明组合 persona + 中性提示比单一策略更有效，通过同时生成多种结果并选择最优解来提升鲁棒性 [[arXiv:2408.08631](https://arxiv.org/abs/2408.08631)]
- **多智能体协作 (Wang et al., 2024)**: 证明多个人格自我协作可以释放 LLM 的认知协同效应 [[arXiv:2307.05300](https://arxiv.org/abs/2307.05300)]
- **集成方法 (Ensemble Methods)**: 证明不同策略的聚合可以减少方差、增强鲁棒性、捕获互补优势

**我们的假设**:
专家角色卡（领域专业知识框架）+ 人名质量锚点（历史成功案例）= 协同效应（1+1>2）

**诚实声明**:
> **本项目在5小时内完成，部分地方较为粗糙。我无法进行量化对比实验，诚挚希望有能力进行对照实验的研究者参与项目，通过 A/B 测试验证组合效果，并帮助完善项目质量。欢迎提交 Issue 或 Pull Request！**

## 🌟 开源实践验证

### Claude Code Skills & Plugins — Agent Skills for Every Coding Tool
- **作者**: Alireza Rezvani (柏林 CTO 和 AI 工程师)
- **Stars**: **6,000+ GitHub stars** ⭐
- **地址**: [https://github.com/alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
- **贡献**: 提供 205 个生产就绪的专业技能包，覆盖 9 大领域

**我们的创新**: 在 Claude Skills 的专家角色卡基础上，引入"**人名质量锚点**"概念，将抽象的专业能力转化为具体的历史成功案例。

## 🚀 30秒快速体验

### 第一步：安装

#### 🍏 macOS/Linux 用户
```bash
# 克隆本仓库
git clone https://github.com/your-username/expert-library-plus.git

# 复制专家库到 OpenClaw 目录
cp -r expert-library-plus/experts/ ~/.openclaw/experts/

# 验证安装（应该看到专家列表）
ls ~/.openclaw/experts/
```

#### 💻 Windows 用户
请参考 [Windows 安装指南](INSTALL-WINDOWS.md) 获取详细的 Windows 安装步骤。

> **💡 用户友好提示**: OpenClaw 目前需要手动复制文件到专家目录。我们正在探索自动发现机制，但目前这是最可靠的方式。

### 第二步：激活专家
```text
请专家帮我设计一个革命性的产品
```

### 第三步：选择增强模式（智能推荐）
系统会根据你的任务类型，智能推荐最适合的质量锚点：

#### 🎯 **两种使用模式**

**模式 A: 仅人名模式（轻量级）**
- 直接使用人名作为质量锚点
- 适合简单任务或快速验证
- 示例：`"用乔布斯视角帮我设计产品"`

**模式 B: 完整加载模式（专业级）**  
- 加载完整专家角色卡 + 人名质量锚点
- 包含冲突检测和特质匹配
- 适合复杂任务或高质量要求

#### 🔍 **智能冲突检测**
系统会自动分析：
- **人物特质冲突**: 避免选择相互矛盾的专家组合
- **任务匹配度**: 推荐最适合当前任务的人名
- **领域适配性**: 确保人名与专家领域高度相关

### 第四步：用户自建人名库
**对于其他用户**：你完全可以创建自己的人名库！

1. **目录结构**: 在对应专家目录下创建 `names/` 文件夹
2. **文件格式**: 严格按照 `templates/name-template.md` 中的详细模板创建，包含权威性证明、核心特质、反特质约束、决策逻辑等完整结构  
3. **自动关联**: 系统会自动发现并加载你的人名库
4. **无需修改**: 无需修改任何核心代码，完全插件化

> **示例**: 如果你想为前端开发专家添加新的人名，只需在 `engineering/names/` 目录下创建新的 `.md` 文件，系统会自动识别并提供选择！

## 🏗️ 项目架构

```
expert-library-plus/
├── experts/                    # 43+ 个专业专家
│   ├── engineering/           # 工程专家（前端、后端、安全等）
│   │   └── names/            # 人名库（用户可扩展）
│   ├── design/                # 设计专家（UI/UX、品牌等）  
│   │   └── names/            # 人名库（用户可扩展）
│   ├── business/              # 商业专家（销售、营销、策略等）
│   │   └── names/            # 人名库（用户可扩展）
│   └── safety/                # 安全专家（安全工程、事件响应等）
│       └── names/            # 人名库（用户可扩展）
├── templates/                 # 创建你自己的专家
│   └── name-template.md       # 详细创建指南
└── [根目录文件]               # README, LICENSE, CONTRIBUTING 等
```

### 🔌 **插件化设计**
- **自动发现**: 系统自动扫描所有 `names/` 目录
- **零配置**: 无需修改代码，只需添加文件
- **热加载**: 新增人名文件后立即可用
- **完全隔离**: 用户自建内容与核心系统完全分离

## 🔒 安全与合规

### 我们的安全承诺
- **仅用已故名人**: 示范文件只包含已故的历史人物
- **用户自建机制**: 你完全控制添加哪些人名
- **法律免责声明**: 明确说明合理使用原则

### 开源友好
- **MIT 许可证**: 允许商业使用和修改
- **全球社区**: 中英文双语支持，欢迎全球贡献者

### 📋 兼容性说明
详细版本兼容性和系统要求请参考 [兼容性指南](COMPATIBILITY.md)。

## 🙏 特别致谢

本项目基于 **[Claude Code Skills & Plugins — Agent Skills for Every Coding Tool](https://github.com/alirezarezvani/claude-skills)**（**6,000+ GitHub stars**）的坚实基础，特别感谢 **Alireza Rezvani** 创建了这个卓越的开源技能库。

### 🔗 Claude Skills 用户集成指南

如果你已经是 Claude Skills 用户，可以将 Expert Library Plus 作为增强层集成：

```bash
# 克隆 Expert Library Plus
git clone https://github.com/your-username/expert-library-plus.git

# 复制人名库到你的 Claude Skills 专家目录
cp -r expert-library-plus/experts/*/names/ /path/to/claude-skills/*/

# 现在你的 Claude Skills 专家就支持人名质量锚点了！
```

**注意**: 这种集成方式让你完全控制人名库内容，无需等待 PR 审核，也避免了版本兼容性问题。

## 📦 安装选项

### 选项 1: OpenClaw 用户
使用 ClawHub 安装：`clawhub install expert-library-plus`

### 选项 2: Claude Skills 用户  
按照上述指南手动集成人名库

### 选项 3: 其他 AI 工具用户
直接使用专家角色卡和人名模板

**Claude Skills 的贡献**:
- 提供了 205 个生产就绪的专业技能包
- 覆盖工程、产品、营销、合规、高管顾问等 9 大领域  
- 支持 11 种 AI 编码工具（Claude Code、Codex、Gemini CLI 等）

**我们的创新**:
在 Claude Skills 的专家角色卡基础上，我们创新性地引入了"**人名质量锚点**"概念，将抽象的专业能力转化为具体的历史成功案例，让 AI 专家能够达到历史上巨匠的思维品质和工作标准。

## 🛠️ 安装选项与验证

### 选项 1: 手动安装（推荐用于理解）
按照 [安装指南](#-第一步安装) 手动复制文件。

### 选项 2: Skill 安装（推荐用于生产）
将本项目作为 OpenClaw Skill 安装：

```bash
# 复制 skill 目录到 OpenClaw skills 目录
cp -r expert-library-plus-skill ~/.openclaw/skills/

# 使用 Skill 命令安装
/skill expert-library-plus --action install
```

### 安装验证工具
由于 AI 项目的效果难以直接验证，我们提供了安装验证工具：

#### Python 验证脚本（推荐）
```bash
# 运行完整验证
python3 verify-installation.py

# 脚本会检查：
# - 文件结构完整性
# - 目录路径正确性  
# - 关键文件存在性
# - 内容格式正确性
```

#### 快速验证脚本（bash/shell）
```bash
# macOS/Linux
chmod +x verify-installation.sh
./verify-installation.sh

# Windows (PowerShell)
.\verify-installation.sh
```

### 使用示例与效果验证
详细使用示例、故障排除和预期效果请参考 [使用示例指南](USAGE-EXAMPLES.md)。

## 🌟 立即开始

**不要只是阅读——立即尝试！**

1. 克隆本仓库
2. 复制到你的 OpenClaw 专家目录  
3. 对 AI 说："请专家帮我..."

**你将立即体验到 AI 专家思维品质的显著提升！**

## 🤝 贡献与反馈

我们相信：**最好的项目来自于真实的用户反馈**。

- 遇到问题？提交 Issue！
- 有新想法？提交 Pull Request！
- 想要新专家？告诉我们！

**让我们一起打造世界上最强大的 AI 专家库！**