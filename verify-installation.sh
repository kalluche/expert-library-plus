#!/bin/bash
# 专家库快速验证脚本

echo "🔍 验证 Expert Library Plus 安装..."

# 检测操作系统
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    # Windows
    OPENCLAW_DIR="$USERPROFILE\\.openclaw"
    EXPERTS_DIR="$OPENCLAW_DIR\\experts"
else
    # macOS/Linux  
    OPENCLAW_DIR="$HOME/.openclaw"
    EXPERTS_DIR="$OPENCLAW_DIR/experts"
fi

echo "📁 OpenClaw 目录: $OPENCLAW_DIR"

# 检查基本结构
check_dir() {
    if [ -d "$1" ]; then
        echo "✅ $(basename $1) 目录存在"
        return 0
    else
        echo "❌ $(basename $1) 目录不存在"
        return 1
    fi
}

# 检查文件
check_file() {
    if [ -f "$1" ]; then
        echo "✅ $(basename $1) 文件存在"
        return 0
    else
        echo "❌ $(basename $1) 文件不存在"
        return 1
    fi
}

# 运行检查
echo "检查基本目录结构..."
check_dir "$OPENCLAW_DIR" || exit 1
check_dir "$EXPERTS_DIR" || exit 1
check_dir "$EXPERTS_DIR/engineering" || exit 1  
check_dir "$EXPERTS_DIR/design" || exit 1
check_dir "$EXPERTS_DIR/business" || exit 1
check_dir "$EXPERTS_DIR/safety" || exit 1

echo ""
echo "检查人名库结构..."
check_dir "$EXPERTS_DIR/engineering/names" || exit 1
check_dir "$EXPERTS_DIR/design/names" || exit 1
check_dir "$EXPERTS_DIR/business/names" || exit 1  
check_dir "$EXPERTS_DIR/safety/names" || exit 1

echo ""
echo "检查关键文件..."
check_file "$EXPERTS_DIR/engineering/names/steve-jobs.md" || exit 1
check_file "$EXPERTS_DIR/EXPERTS.md" || exit 1

echo ""
echo "🎉 快速验证成功！专家库应该能正常工作。"
echo "💡 现在可以测试 '请专家帮我...' 命令。"