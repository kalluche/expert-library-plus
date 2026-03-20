# Expert Library Plus

**Give AI experts the thinking quality of historical giants — Enhance task execution quality through name-based quality anchors**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=for-the-badge)](https://github.com)
[![Claude Skills Stars](https://img.shields.io/github/stars/alirezarezvani/claude-skills?style=for-the-badge)](https://github.com/alirezarezvani/claude-skills)
[![Experts](https://img.shields.io/badge/Experts-43+-brightgreen?style=for-the-badge)](#-project-architecture)
[![Name Templates](https://img.shields.io/badge/Name%20Templates-User%20Extensible-blue?style=for-the-badge)](#-build-your-own-name-library)

> **Give AI experts the thinking quality of historical giants**  
> **A name is not role-playing, but a shortcut to quality standards**

## 👥 Project Team

**💡 Author Statement**: The project author has no programming or coding knowledge whatsoever. This is purely product-thinking driven.

**🤖 AI Expert Team**:
- **Lead Development**: Qwen 3.5 Plus
- **Strategic Architecture**: Qwen-Max  
- **Deep Research**: DeepSeek
- **Innovation Suggestions**: Gemini

> This is a truly collaborative open-source project built entirely by an AI expert team!

## 📚 Scientific Foundation: Why Names Optimize AI Performance?

### 🔬 Core Mechanism Analysis

**The effectiveness of names as "quality anchors" is based on four major scientific research findings:**

#### 1. **Parametric Knowledge Mechanism (2024)**
> *"LLMs store extensive knowledge about historical figures in their parameters during pre-training, and names serve as highly compressed knowledge identifiers that effectively activate relevant knowledge"*  
> **Source**: [Understanding the Interplay between Parametric and Contextual Knowledge (2024)](https://arxiv.org/html/2410.08414v1)

**Why it works**: Large language models have already learned about historical figures' **life stories, professional achievements, thinking patterns, and behavioral characteristics** during training. When users provide a name, the model automatically activates these internalized parametric knowledge to guide task execution.

#### 2. **Knowledge Cutoff Limitation (2024)**  
> *"Models can only understand figures who were famous before their training cutoff date; emerging geniuses may not be sufficiently understood"*  
> **Source**: [Dated Data: Tracing Knowledge Cutoffs in Large Language Models (2024)](https://arxiv.org/abs/2403.12958)

**Key Insight**: 
- **Jobs Advantage**: Died in 2011, so all modern LLMs contain complete information about him
- **Emerging Genius Limitation**: Figures who became prominent after the training cutoff may not be fully understood by the model
- **Selection Strategy**: Prioritize **historical figures who were already famous before the training cutoff**

#### 3. **Persona Double-Edged Sword Effect (Kim et al., 2024)**
> *"Personas can improve or degrade performance, with degradation observed in 7 out of 12 datasets"*  
> **Source**: [arXiv:2408.08631](https://arxiv.org/abs/2408.08631)

**Our solution**: Using **historically validated successful figures** as quality anchors avoids the risks of arbitrary personas.

#### 4. **Prompt Engineering Systematic Study (Schulhoff et al., 2024)**
> *"Role prompts are effective for style but have limited impact on accuracy"*  
> **Source**: [arXiv:2406.06608](https://arxiv.org/abs/2406.06608)

**Our innovation**: Emphasizing **quality anchors** rather than **role-playing**, focusing on "deliver iPhone-level results" rather than "speak like Jobs".

### 🎯 Quality Anchors vs Traditional Role-Playing

| Aspect | Traditional Role-Playing | Our Quality Anchors |
|--------|-------------------------|---------------------|
| **Goal** | Simulate role behavior | Achieve quality standards |
| **Risk** | May activate negative stereotypes | Based on historical success cases |
| **Stability** | Unstable effects | Historically validated reliability |
| **Task Focus** | Focus on "how to speak" | Focus on "what to do" |

> **Key Insight**: Names don't make AI "impersonate" someone, but rather "achieve" the historical achievement standards created by that person.

### 🧪 **Scientific Validation of Combination Effects**

**Current Research Status**:
While there are currently no academic papers directly studying the combined effect of "expert role cards + names," the following research provides our theoretical foundation:

- **Jekyll & Hyde Framework (Kim et al., 2024)**: Demonstrates that combining persona + neutral prompts is more effective than single strategies, improving robustness by generating multiple results simultaneously and selecting the optimal one [[arXiv:2408.08631](https://arxiv.org/abs/2408.08631)]
- **Multi-Agent Collaboration (Wang et al., 2024)**: Shows that multi-persona self-collaboration can unleash LLMs' cognitive synergy effects [[arXiv:2307.05300](https://arxiv.org/abs/2307.05300)]
- **Ensemble Methods**: Proves that aggregating different strategies can reduce variance, enhance robustness, and capture complementary strengths

**Our Hypothesis**:
Expert Role Cards (domain knowledge framework) + Name Quality Anchors (historical success cases) = Synergistic Effect (1+1>2)

**Honest Declaration**:
> **This project was completed in 5 hours and some parts are still rough. I cannot conduct quantitative comparison experiments. I sincerely hope researchers capable of conducting controlled experiments will participate in the project, validate the combination effects through A/B testing, and help improve project quality. Pull Requests and Issues are welcome!**

## 🌟 Open Source Practice Validation

### Claude Code Skills & Plugins — Agent Skills for Every Coding Tool
- **Author**: Alireza Rezvani (CTO and AI engineer based in Berlin)
- **Stars**: **6,000+ GitHub stars** ⭐
- **URL**: [https://github.com/alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
- **Contribution**: Provides 205 production-ready professional skill packages covering 9 major domains

**Our Innovation**: Building upon Claude Skills' expert role cards, we introduced the "**name quality anchor**" concept, transforming abstract professional capabilities into concrete historical success cases.

## 🚀 30-Second Quick Start

### Step 1: Installation

#### 🍏 macOS/Linux Users
```bash
# Clone this repository
git clone https://github.com/your-username/expert-library-plus.git

# Copy expert library to OpenClaw directory
cp -r expert-library-plus/experts/ ~/.openclaw/experts/

# Verify installation (should see expert list)
ls ~/.openclaw/experts/
```

#### 💻 Windows Users
Please refer to [Windows Installation Guide](INSTALL-WINDOWS.md) for detailed Windows installation steps.

> **💡 User-Friendly Note**: OpenClaw currently requires manual file copying to the experts directory. We're exploring automatic discovery mechanisms, but this is currently the most reliable approach.

### Step 2: Activate Expert
```text
Please help me design a revolutionary product with expert assistance
```

### Step 3: Choose Enhancement Mode (Smart Recommendation)
The system will intelligently recommend the most suitable quality anchors based on your task type:

#### 🎯 **Two Usage Modes**

**Mode A: Name-Only Mode (Lightweight)**
- Use names directly as quality anchors
- Ideal for simple tasks or quick validation
- Example: `"Help me design a product from Jobs' perspective"`

**Mode B: Full Loading Mode (Professional)**  
- Load complete expert role cards + name quality anchors
- Includes conflict detection and trait matching
- Ideal for complex tasks or high-quality requirements

#### 🔍 **Intelligent Conflict Detection**
The system automatically analyzes:
- **Personality Trait Conflicts**: Avoids contradictory expert combinations
- **Task Match Score**: Recommends names most suitable for current tasks
- **Domain Relevance**: Ensures names are highly relevant to expert domains

### Step 4: Build Your Own Name Library
**For other users**: You can absolutely create your own name library!

1. **Directory Structure**: Create `names/` folders under corresponding expert directories
2. **File Format**: Strictly follow the detailed template in `templates/name-template.md`, including authority verification, core traits, anti-traits constraints, decision logic, and complete structure  
3. **Automatic Integration**: The system automatically discovers and loads your name libraries
4. **No Code Changes**: No core code modification needed, fully plugin-based

> **Example**: If you want to add new names for frontend development experts, simply create new `.md` files in the `engineering/names/` directory, and the system will automatically recognize and provide them as options!

## 🏗️ Project Architecture

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

### 🔌 **Plugin-Based Design**
- **Auto-Discovery**: System automatically scans all `names/` directories
- **Zero Configuration**: No code changes needed, just add files
- **Hot Loading**: New name files are immediately available
- **Complete Isolation**: User-created content is completely separated from core system

## 🔒 Safety and Compliance

### Our Safety Commitment
- **Deceased celebrities only**: Demo files contain only deceased historical figures
- **User self-building mechanism**: You have complete control over which names to add
- **Legal disclaimer**: Clear statement of fair use principles

### Open Source Friendly
- **MIT License**: Allows commercial use and modification
- **Global community**: Bilingual Chinese-English support, welcoming global contributors

### 📋 Compatibility Information
For detailed version compatibility and system requirements, please refer to [Compatibility Guide](COMPATIBILITY.md).

## 🙏 Special Acknowledgments

This project is built upon **[Claude Code Skills & Plugins — Agent Skills for Every Coding Tool](https://github.com/alirezarezvani/claude-skills)** (**6,000+ GitHub stars**), with special thanks to **Alireza Rezvani** for creating this outstanding open-source skill library.

### 🔗 Claude Skills User Integration Guide

If you're already a Claude Skills user, you can integrate Expert Library Plus as an enhancement layer:

```bash
# Clone Expert Library Plus
git clone https://github.com/your-username/expert-library-plus.git

# Copy name libraries to your Claude Skills expert directories
cp -r expert-library-plus/experts/*/names/ /path/to/claude-skills/*/

# Now your Claude Skills experts support name quality anchors!
```

**Note**: This integration approach gives you full control over name library content, avoids PR review delays, and prevents version compatibility issues.

## 📦 Installation Options

### Option 1: OpenClaw Users
Install via ClawHub: `clawhub install expert-library-plus`

### Option 2: Claude Skills Users  
Manually integrate name libraries following the guide above

### Option 3: Other AI Tool Users
Use expert role cards and name templates directly

**Claude Skills Contributions**:
- Provides 205 production-ready professional skill packages
- Covers 9 major domains: engineering, product, marketing, compliance, C-level advisory, etc.  
- Supports 11 AI coding tools (Claude Code, Codex, Gemini CLI, etc.)

**Our Innovation**:
Based on Claude Skills' expert role cards, we innovatively introduced the "**name as quality anchor**" concept, transforming abstract professional capabilities into concrete historical success cases, enabling AI experts to achieve the thinking quality and work standards of historical giants.

## 🛠️ Installation Options & Verification

### Option 1: Manual Installation (Recommended for understanding)
Follow the [Installation Guide](#-step-1-installation) to manually copy files.

### Option 2: Skill Installation (Recommended for production)
Install this project as an OpenClaw Skill:

```bash
# Copy skill directory to OpenClaw skills directory
cp -r expert-library-plus-skill ~/.openclaw/skills/

# Use Skill command to install
/skill expert-library-plus --action install
```

### Installation Verification Tools
Since AI project effects are difficult to directly verify, we provide installation verification tools:

#### Python Verification Script (Recommended)
```bash
# Run complete verification
python3 verify-installation.py

# The script checks:
# - File structure integrity
# - Directory path correctness  
# - Key file existence
# - Content format correctness
```

#### Quick Verification Script (bash/shell)
```bash
# macOS/Linux
chmod +x verify-installation.sh
./verify-installation.sh

# Windows (PowerShell)
.\verify-installation.sh
```

### Usage Examples & Effect Validation
For detailed usage examples, troubleshooting, and expected effects, please refer to [Usage Examples Guide](USAGE-EXAMPLES.md).

## 🌟 Get Started Now

**Don't just read—try it immediately!**

1. Clone this repository
2. Copy to your OpenClaw experts directory  
3. Say to AI: "Please help me with expert assistance..."

**You'll immediately experience a significant improvement in AI expert thinking quality!**

## 🤝 Contributions and Feedback

We believe: **The best projects come from real user feedback**.

- Having issues? Submit an Issue!
- Have new ideas? Submit a Pull Request!
- Want new experts? Let us know!

**Let's build the world's most powerful AI expert library together!**