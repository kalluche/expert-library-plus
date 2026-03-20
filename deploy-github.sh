#!/bin/bash
# 自动化 GitHub 发布脚本

set -e

echo "🚀 开始自动化 GitHub 发布..."

# 检查是否已登录 GitHub CLI
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI 未安装"
    echo "请先安装: brew install gh"
    exit 1
fi

# 检查 GitHub CLI 登录状态
if ! gh auth status &>/dev/null; then
    echo "🔑 GitHub CLI 未登录，正在启动登录流程..."
    gh auth login
fi

# 获取当前目录名作为仓库名
REPO_NAME="expert-library-plus"
DESCRIPTION="AI expert library with name-based quality anchors - Enhance task execution quality through historical figure quality anchors"

echo "📁 仓库名称: $REPO_NAME"
echo "📝 描述: $DESCRIPTION"

# 创建 GitHub 仓库
echo "🔄 创建 GitHub 仓库..."
gh repo create "$REPO_NAME" \
    --public \
    --description "$DESCRIPTION" \
    --disable-issues=false \
    --disable-wiki=false

# 设置远程仓库
echo "🔗 设置远程仓库..."
git remote set-url origin "https://github.com/$(gh api user --jq '.login')/$REPO_NAME.git"

# 推送代码
echo "📤 推送代码到 GitHub..."
git push -u origin main

echo "✅ GitHub 发布完成!"
echo "🌐 仓库地址: https://github.com/$(gh api user --jq '.login')/$REPO_NAME"