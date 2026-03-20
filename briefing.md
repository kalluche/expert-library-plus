# 任务简报：专家库 + 人名增强方案 GitHub 开源

## 🎯 核心要求
1. **立项规范**：在 projects/ 目录下创建标准项目结构
2. **范围限制**：只做框架和示范，不做完整人名库
3. **法律安全**：仅用已故名人（Steve Jobs）作为示范
4. **用户自建**：提供模板和指南让用户自己创建人名库
5. **双语支持**：中英文版本，全球开发者友好
6. **开源合规**：MIT 许可证，致谢 Claude Skills 原作者

## 📁 交付物结构
```
projects/expert-library-plus-github_20260321-0155/
├── PROJECT.md          # 项目记录
├── briefing.md         # 任务简报  
├── github-upload/      # GitHub 上传内容
│   ├── README.md       # 语言选择器
│   ├── README-en.md    # 英文版
│   ├── README-zh.md    # 中文版
│   ├── LICENSE         # MIT 许可证
│   ├── CONTRIBUTING.md # 双语贡献指南
│   ├── .gitignore      # 忽略配置
│   ├── .github/        # GitHub 配置
│   ├── experts/        # 专家库核心
│   └── templates/      # 用户模板
└── FINAL_CHECKLIST.md  # 最终检查清单
```

## ⚠️ 关键约束
- 不要实际创建430个人名文件
- 只提供一个 Steve Jobs 示范文件
- 确保所有文档都有中英文版本
- 明确致谢 Alireza Rezvani