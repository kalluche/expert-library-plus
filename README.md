# Expert Library Plus (专家库 + 人名增强方案)

**Give AI experts the thinking quality of historical giants — Enhance task execution quality through name-based quality anchors**  
**让 AI 专家拥有历史巨匠的思维品质 — 通过人名质量锚点提升任务执行质量**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=for-the-badge)](https://github.com)
[![Claude Skills Stars](https://img.shields.io/github/stars/alirezarezvani/claude-skills?style=for-the-badge)](https://github.com/alirezarezvani/claude-skills)
[![Experts](https://img.shields.io/badge/Experts-43+-brightgreen?style=for-the-badge)](#project-architecture-项目架构)
[![Name Templates](https://img.shields.io/badge/Name%20Templates-User%20Extensible-blue?style=for-the-badge)](#build-your-own-name-library-用户自建人名库)

> **Give AI experts the thinking quality of historical giants**  
> **让 AI 专家拥有历史巨匠的思维品质**

## 👥 Project Team (项目团队)

### 💡 Author Statement (作者声明)
**The project author has no programming or coding knowledge whatsoever. This is purely product-thinking driven.**  
**本项目作者完全不懂程序和代码，纯属产品思维驱动。**

### 🤖 AI Expert Team (AI 专家团队)
- **Lead Development**: Qwen 3.5 Plus  
  **主导开发**: Qwen 3.5 Plus
- **Strategic Architecture**: Qwen-Max  
  **战略架构**: Qwen-Max  
- **Deep Research**: DeepSeek
  **深度研究**: DeepSeek
- **Innovation Suggestions**: Gemini
  **创新建议**: Gemini

> **This is a truly collaborative open-source project built entirely by an AI expert team!**  
> **这是一个真正由 AI 专家团队协作完成的开源项目！**

## 📚 Scientific Foundation: Why Names Optimize AI Performance? (科学依据：为什么人名能优化 AI 表现？)

### 🔬 Core Mechanism Analysis (核心机制分析)

**The effectiveness of names as "quality anchors" is based on four major scientific research findings:**  
**人名作为"质量锚点"的有效性基于四大科学研究发现：**

#### 1. **ExpertPrompting Mechanism (Xu et al., 2023)**  
#### 1. **ExpertPrompting 机制 (Xu et al., 2023)**
> *"Detailed expert descriptions significantly improve LLM answer quality, with ExpertLLaMA reaching 96% of ChatGPT's capability"*  
> **来源**: [arXiv:2305.14688](https://arxiv.org/abs/2305.14688)  
> *"详细专家描述可显著提升 LLM 回答质量，ExpertLLaMA 达到 ChatGPT 96% 能力"*  
> **来源**: [arXiv:2305.14688](https://arxiv.org/abs/2305.14688)

**Why it works**: Names serve as **expert identity shortcuts**, activating relevant knowledge and thinking patterns stored in the LLM.  
**为什么有效**: 人名作为**专家身份的快捷标识**，激活 LLM 中存储的相关知识和思维模式。

#### 2. **Role-Play Prompting Mechanism (Kong et al., 2024)**  
#### 2. **Role-Play Prompting 机制 (Kong et al., 2024)**  
> *"Role-playing prompts significantly improve performance on reasoning tasks: AQuA +10.3%, Last Letter +60.4%"*  
> **来源**: [arXiv:2308.07702](https://arxiv.org/abs/2308.07702)  
> *"角色扮演提示在推理任务上显著提升性能：AQuA +10.3%，Last Letter +60.4%"*  
> **来源**: [arXiv:2308.07702](https://arxiv.org/abs/2308.07702)

**Why it works**: Names provide **specific thinking frameworks and behavioral patterns**, more effectively triggering Chain-of-Thought reasoning than simple "think step by step" prompts.  
**为什么有效**: 人名提供**具体的思维框架和行为模式**，比简单的"think step by step"更有效地触发 Chain-of-Thought 推理过程。

#### 3. **Persona Double-Edged Sword Effect (Kim et al., 2024)**
#### 3. **Persona 双刃剑效应 (Kim et al., 2024)
> *"Personas can improve or degrade performance, with degradation observed in 7 out of 12 datasets"*  
> **来源**: [arXiv:2408.08631](https://arxiv.org/abs/2408.08631)  
> *"Persona 可能提升也可能降低表现，在 7/12 数据集中表现下降"*  
> **来源**: [arXiv:2408.08631](https://arxiv.org/abs/2408.08631)

**Our solution**: Using **historically validated successful figures** as quality anchors avoids the risks of arbitrary personas.  
**我们的解决方案**: 使用**历史验证的成功人物**作为质量锚点，避免随意 persona 带来的风险。

#### 4. **Prompt Engineering Systematic Study (Schulhoff et al., 2024)
#### 4. **Prompt Engineering 系统性研究 (Schulhoff et al., 2024)
> *"Role prompts are effective for style but have limited impact on accuracy"*  
> **来源**: [arXiv:2406.06608](https://arxiv.org/abs/2406.06608)  
> *"角色提示对风格有效，对准确性效果有限"*  
> **来源**: [arXiv:2406.06608](https://arxiv.org/abs/2406.06608)

**Our innovation**: Emphasizing **quality anchors** rather than **role-playing**, focusing on "deliver iPhone-level results" rather than "speak like Jobs".  
**我们的创新**: 强调**质量锚点**而非**角色扮演**，关注"产出 iPhone 级别的结果"而非"像乔布斯一样说话"。

### 🎯 Quality Anchors vs Traditional Role-Playing (质量锚点 vs 传统角色扮演)

| Aspect | Traditional Role-Playing | Our Quality Anchors |
|--------|-------------------------|---------------------|
| **Goal** | Simulate role behavior | Achieve quality standards |
| **Risk** | May activate negative stereotypes | Based on historical success cases |
| **Stability** | Unstable effects | Historically validated reliability |
| **Task Focus** | Focus on "how to speak" | Focus on "what to do" |

| 方面 | 传统角色扮演 | 我们的质量锚点 |
|------|-------------|---------------|
| **目标** | 模拟角色行为 | 达到质量标准 |
| **风险** | 可能激活负面刻板印象 | 基于历史成功案例 |
| **稳定性** | 效果不稳定 | 历史验证可靠 |
| **任务导向** | 关注"如何说" | 关注"做什么" |

> **Key Insight**: Names don't make AI "impersonate" someone, but rather "achieve" the historical achievement standards created by that person.  
> **关键洞察**: 人名不是让 AI "扮演"某个人，而是让 AI "达到"某个人创造的历史成就标准。

## 🧪 Scientific Validation of Combination Effects (组合效果的科学验证)

**Current Research Status**:  
**当前研究状态**:
While there are currently no academic papers directly studying the combined effect of "expert role cards + names," the following research provides our theoretical foundation:  
虽然目前没有直接研究"专家角色卡 + 人名"组合效果的学术论文，但以下研究为我们提供了理论基础：

- **Jekyll & Hyde Framework (Kim et al., 2024)**: Demonstrates that combining persona + neutral prompts is more effective than single strategies, improving robustness by generating multiple results simultaneously and selecting the optimal one [[arXiv:2408.08631](https://arxiv.org/abs/2408.08631)]  
- **Jekyll & Hyde 框架 (Kim et al., 2024)**: 证明组合 persona + 中性提示比单一策略更有效，通过同时生成多种结果并选择最优解来提升鲁棒性 [[arXiv:2408.08631](https://arxiv.org/abs/2408.08631)]

- **Multi-Agent Collaboration (Wang et al., 2024)**: Shows that multi-persona self-collaboration can unleash LLMs' cognitive synergy effects [[arXiv:2307.05300](https://arxiv.org/abs/2307.05300)]  
- **多智能体协作 (Wang et al., 2024)**: 证明多个人格自我协作可以释放 LLM 的认知协同效应 [[arXiv:2307.05300](https://arxiv.org/abs/2307.05300)]

- **Ensemble Methods**: Proves that aggregating different strategies can reduce variance, enhance robustness, and capture complementary strengths  
- **集成方法**: 证明不同策略的聚合可以减少方差、增强鲁棒性、捕获互补优势

**Our Hypothesis**:  
**我们的假设**:
Expert Role Cards (domain knowledge framework) + Name Quality Anchors (historical success cases) = Synergistic Effect (1+1>2)  
专家角色卡（领域专业知识框架）+ 人名质量锚点（历史成功案例）= 协同效应（1+1>2）

**Honest Declaration**:  
**诚实声明**:
> **This project was completed in 5 hours and some parts are still rough. I cannot conduct quantitative comparison experiments. I sincerely hope researchers capable of conducting controlled experiments will participate in the project, validate the combination effects through A/B testing, and help improve project quality. Pull Requests and Issues are welcome!**  
> **本项目在5小时内完成，部分地方较为粗糙。我无法进行量化对比实验，诚挚希望有能力进行对照实验的研究者参与项目，通过 A/B 测试验证组合效果，并帮助完善项目质量。欢迎提交 Issue 或 Pull Request！**

## 🌟 Open Source Practice Validation (开源实践验证)

### Claude Code Skills & Plugins — Agent Skills for Every Coding Tool
### Claude Code Skills & Plugins — Agent Skills for Every Coding Tool
- **Author**: Alireza Rezvani (CTO and AI engineer based in Berlin)  
  **作者**: Alireza Rezvani (柏林 CTO 和 AI 工程师)
- **Stars**: **6,000+ GitHub stars** ⭐  
  **Stars**: **6,000+ GitHub stars** ⭐
- **URL**: [https://github.com/alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)  
  **URL**: [https://github.com/alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
- **Contribution**: Provides 205 production-ready professional skill packages covering 9 major domains  
  **贡献**: 提供 205 个生产就绪的专业技能包，覆盖 9 大领域

**Our Innovation**:  
**我们的创新**:
Building upon Claude Skills' expert role cards, we introduced the "**name quality anchor**" concept, transforming abstract professional capabilities into concrete historical success cases.  
在 Claude Skills 的专家角色卡基础上，我们引入了"**人名质量锚点**"概念，将抽象的专业能力转化为具体的历史成功案例。

## 🚀 30-Second Quick Start (30秒快速体验)

### Step 1: Installation (安装步骤)

#### 🍏 macOS/Linux Users
#### 🍏 macOS/Linux 用户
```bash
# Clone this repository
# 克隆本仓库
git clone https://github.com/your-username/expert-library-plus.git

# Copy expert library to OpenClaw directory  
# 复制专家库到 OpenClaw 目录
cp -r expert-library-plus/experts/ ~/.openclaw/experts/

# Verify installation (should see expert list)
# 验证安装（应该看到专家列表）
ls ~/.openclaw/experts/
```

#### 💻 Windows Users
#### 💻 Windows 用户
Please refer to [Windows Installation Guide](INSTALL-WINDOWS.md) for detailed Windows installation steps.  
请参考 [Windows 安装指南](INSTALL-WINDOWS.md) 获取详细的 Windows 安装步骤。

> **💡 User-Friendly Note**: OpenClaw currently requires manual file copying to the experts directory. We're exploring automatic discovery mechanisms, but this is currently the most reliable approach.  
> **💡 用户友好提示**: OpenClaw 目前需要手动复制文件到专家目录。我们正在探索自动发现机制，但目前这是最可靠的方式。

### Step 2: Activate Expert (激活专家)
### Step 2: 激活专家
```text
Please help me design a revolutionary product with expert assistance
请专家帮我设计一个革命性的产品
```

### Step 3: Choose Enhancement Mode (Smart Recommendation) (选择增强模式（智能推荐）)
### Step 3: 选择增强模式（智能推荐）
The system will intelligently recommend the most suitable quality anchors based on your task type:  
系统会根据你的任务类型，智能推荐最适合的质量锚点：

#### 🎯 Two Usage Modes (两种使用模式)

**Mode A: Name-Only Mode (Lightweight)**  
**模式 A: 仅人名模式（轻量级）**
- Use names directly as quality anchors  
  直接使用人名作为质量锚点
- Ideal for simple tasks or quick validation  
  适合简单任务或快速验证
- Example: `"Help me design a product from Jobs' perspective"`  
  示例：`"用乔布斯视角帮我设计产品"`

**Mode B: Full Loading Mode (Professional)**  
**模式 B: 完整加载模式（专业级）**  
- Load complete expert role cards + name quality anchors  
  加载完整专家角色卡 + 人名质量锚点
- Includes conflict detection and trait matching  
  包含冲突检测和特质匹配
- Ideal for complex tasks or high-quality requirements  
  适合复杂任务或高质量要求

#### 🔍 Intelligent Conflict Detection (智能冲突检测)
The system automatically analyzes:  
系统会自动分析：
- **Personality Trait Conflicts**: Avoids contradictory expert combinations  
  **人物特质冲突**: 避免选择相互矛盾的专家组合
- **Task Match Score**: Recommends names most suitable for current tasks  
  **任务匹配度**: 推荐最适合当前任务的人名
- **Domain Relevance**: Ensures names are highly relevant to expert domains  
  **领域适配性**: 确保人名与专家领域高度相关

### Step 4: Build Your Own Name Library (用户自建人名库)
### Step 4: 用户自建人名库
**For other users**: You can absolutely create your own name library!  
**对于其他用户**：你完全可以创建自己的人名库！

1. **Directory Structure**: Create `names/` folders under corresponding expert directories  
   **目录结构**: 在对应专家目录下创建 `names/` 文件夹
2. **File Format**: Reference `templates/name-template.md`  
   **文件格式**: 参考 `templates/name-template.md`  
3. **Automatic Integration**: The system automatically discovers and loads your name libraries  
   **自动关联**: 系统会自动发现并加载你的人名库
4. **No Code Changes**: No core code modification needed, fully plugin-based  
   **无需修改**: 无需修改任何核心代码，完全插件化

> **Example**: If you want to add new names for frontend development experts, simply create new `.md` files in the `engineering/names/` directory, and the system will automatically recognize and provide them as options!  
> **示例**: 如果你想为前端开发专家添加新的人名，只需在 `engineering/names/` 目录下创建新的 `.md` 文件，系统会自动识别并提供选择！

## 🏗️ Project Architecture (项目架构)

```
expert-library-plus/
├── experts/                    # 43+ professional experts
│   ├── engineering/           # Engineering experts (frontend, backend, security, etc.)
│   │   └── names/            # Name library (user-extensible)
│   ├── design/                # Design experts (UI/UX, branding, etc.)  
│   │   └── names/            # Name library (user-extensible)
│   ├── business/              # Business experts (sales, marketing, strategy, etc.)
│   │   └── names/            # Name library (user-extensible)
│   └── safety/                # Safety experts (security engineering, incident response, etc.)
│       └── names/            # Name library (user-extensible)
├── templates/                 # Create your own experts
│   └── name-template.md       # Detailed creation guide
└── [root files]               # README, LICENSE, CONTRIBUTING, etc.
```

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

### 🔌 Plugin-Based Design (插件化设计)
- **Auto-Discovery**: System automatically scans all `names/` directories  
  **自动发现**: 系统自动扫描所有 `names/` 目录
- **Zero Configuration**: No code changes needed, just add files  
  **零配置**: 无需代码更改，只需添加文件
- **Hot Loading**: New name files are immediately available  
  **热加载**: 新人名文件立即可用
- **Complete Isolation**: User-created content is completely separated from core system  
  **完全隔离**: 用户创建内容与核心系统完全分离

## 🔒 Safety and Compliance (安全与合规)

### Our Safety Commitment (我们的安全承诺)
- **Deceased celebrities only**: Demo files contain only deceased historical figures  
  **仅用已故名人**: 示范文件只包含已故的历史人物
- **User self-building mechanism**: You have complete control over which names to add  
  **用户自建机制**: 你完全控制添加哪些人名
- **Legal disclaimer**: Clear statement of fair use principles  
  **法律免责声明**: 明确说明合理使用原则

### Open Source Friendly (开源友好)
- **MIT License**: Allows commercial use and modification  
  **MIT 许可证**: 允许商业使用和修改
- **Global community**: Bilingual Chinese-English support, welcoming global contributors  
  **全球社区**: 中英文双语支持，欢迎全球贡献者

## 🙏 Special Acknowledgments (特别致谢)

This project is built upon **[Claude Code Skills & Plugins — Agent Skills for Every Coding Tool](https://github.com/alirezarezvani/claude-skills)** (**6,000+ GitHub stars**), with special thanks to **Alireza Rezvani** for creating this outstanding open-source skill library.  
本项目基于 **[Claude Code Skills & Plugins — Agent Skills for Every Coding Tool](https://github.com/alirezarezvani/claude-skills)**（**6,000+ GitHub stars**）的坚实基础，特别感谢 **Alireza Rezvani** 创建了这个卓越的开源技能库。

**Claude Skills Contributions**:  
**Claude Skills 的贡献**:
- Provides 205 production-ready professional skill packages  
  提供了 205 个生产就绪的专业技能包
- Covers 9 major domains: engineering, product, marketing, compliance, C-level advisory, etc.  
  覆盖工程、产品、营销、合规、高管顾问等 9 大领域  
- Supports 11 AI coding tools (Claude Code, Codex, Gemini CLI, etc.)  
  支持 11 种 AI 编码工具（Claude Code、Codex、Gemini CLI 等）

**Our Innovation**:  
**我们的创新**:
Based on Claude Skills' expert role cards, we innovatively introduced the "**name as quality anchor**" concept, transforming abstract professional capabilities into concrete historical success cases, enabling AI experts to achieve the thinking quality and work standards of historical giants.  
基于 Claude Skills 的专家角色卡，我们创新性地引入了"**人名作为质量锚点**"概念，将抽象的专业能力转化为具体的历史成功案例，让 AI 专家能够达到历史上巨匠的思维品质和工作标准。

## 📖 Usage Examples & Validation (使用示例与验证)

For detailed usage examples, troubleshooting, and expected effects, please refer to [Usage Examples Guide](USAGE-EXAMPLES.md).  
详细使用示例、故障排除和预期效果请参考 [使用示例指南](USAGE-EXAMPLES.md).

## 📋 Compatibility Information (兼容性说明)
For detailed version compatibility and system requirements, please refer to [Compatibility Guide](COMPATIBILITY.md).  
详细版本兼容性和系统要求请参考 [兼容性指南](COMPATIBILITY.md).

## 🌟 Get Started Now (立即开始)

**Don't just read—try it immediately!**  
**不要只是阅读——立即尝试！**

1. Clone this repository  
   克隆本仓库
2. Copy to your OpenClaw experts directory  
   复制到你的 OpenClaw 专家目录  
3. Say to AI: "Please help me with expert assistance..."  
   对 AI 说："请专家帮我..."

**You'll immediately experience a significant improvement in AI expert thinking quality!**  
**你将立即体验到 AI 专家思维品质的显著提升！**

## 🤝 Contributions and Feedback (贡献与反馈)

We believe: **The best projects come from real user feedback**.  
我们相信：**最好的项目来自于真实的用户反馈**。

- Having issues? Submit an Issue!  
  遇到问题？提交 Issue！
- Have new ideas? Submit a Pull Request!  
  有新想法？提交 Pull Request！
- Want new experts? Let us know!  
  想要新专家？告诉我们！

**Let's build the world's most powerful AI expert library together!**  
**让我们一起打造世界上最强大的 AI 专家库！**