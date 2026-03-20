# Windows 安装指南

> **注意**: 本指南由 AI 专家团队编写，由于项目维护者使用 Mac 系统，Windows 安装流程基于 OpenClaw 的标准目录结构推断。如有问题，请提交 Issue！

## 📋 前提条件

### 1. **OpenClaw 已安装**
确保你已经在 Windows 上正确安装了 OpenClaw。

### 2. **找到 OpenClaw 配置目录**
在 Windows 上，OpenClaw 的配置目录通常位于：
```
%USERPROFILE%\.openclaw\
```

你可以通过以下方式确认：
- 打开命令提示符 (CMD) 或 PowerShell
- 输入: `echo %USERPROFILE%` 
- OpenClaw 目录应该是: `C:\Users\<你的用户名>\.openclaw\`

## 🚀 安装步骤

### 步骤 1: 克隆项目
```cmd
# 打开命令提示符或 PowerShell
git clone https://github.com/your-username/expert-library-plus.git
cd expert-library-plus
```

### 步骤 2: 验证安装（推荐）
在复制文件之前，先运行验证脚本确认当前环境：

```powershell
# 运行 Python 验证脚本
python verify-installation.py

# 或运行快速验证脚本  
.\verify-installation.sh
```

如果验证显示 OpenClaw 目录不存在，说明需要先运行 OpenClaw 创建配置目录。

### 步骤 2: 复制专家库文件
```cmd
# 复制 experts 目录到 OpenClaw 配置目录
xcopy experts "%USERPROFILE%\.openclaw\experts" /E /I /Y
```

或者手动复制：
1. 打开文件资源管理器
2. 导航到项目目录中的 `experts` 文件夹
3. 复制整个 `experts` 文件夹
4. 粘贴到 `%USERPROFILE%\.openclaw\` 目录中

### 步骤 3: 验证安装
```cmd
# 检查专家目录是否存在
dir "%USERPROFILE%\.openclaw\experts"
```

你应该看到以下子目录：
- `engineering`
- `design`  
- `business`
- `safety`
- 以及其他专家文件

### 步骤 4: 验证安装
复制完成后，运行验证脚本确认安装成功：

```powershell
# 在项目目录中运行
python verify-installation.py
```

脚本会显示详细的验证结果和成功率。

### 步骤 5: 测试使用
对 OpenClaw 说：
```
请专家帮我设计一个产品
```

系统应该能够识别并加载专家库。如果验证脚本显示安装成功但专家未被识别，请重启 OpenClaw 服务。

## ⚠️ 常见问题

### 1. **权限错误**
如果遇到权限错误，请以管理员身份运行命令提示符。

### 2. **路径不存在**
如果 `%USERPROFILE%\.openclaw\` 目录不存在，请先运行一次 OpenClaw 创建配置目录。

### 3. **专家未被识别**
- 确保文件完整复制，包括所有子目录和文件
- 重启 OpenClaw 服务以重新加载专家库
- 检查 OpenClaw 日志查看是否有加载错误

## 🤝 贡献改进

**重要说明**: 由于项目维护者不使用 Windows，此安装指南可能不够完善。

**如果你成功在 Windows 上安装并使用了专家库，请帮助我们改进此指南！**

- 提交 Issue 报告任何问题
- 提交 Pull Request 改进安装步骤
- 分享你的 Windows 使用经验

## 🔧 高级选项

### 自动安装脚本 (PowerShell)
创建 `install.ps1` 文件：

```powershell
# install.ps1 - Windows 自动安装脚本
Write-Host "Installing Expert Library Plus for Windows..." -ForegroundColor Green

# 获取 OpenClaw 目录
$openclawDir = "$env:USERPROFILE\.openclaw"
$expertsDir = "$openclawDir\experts"

# 创建目录（如果不存在）
if (!(Test-Path $openclawDir)) {
    New-Item -ItemType Directory -Path $openclawDir -Force
}

# 备份现有专家库
if (Test-Path $expertsDir) {
    $backupDir = "$expertsDir.backup.$(Get-Date -Format 'yyyyMMdd')"
    Copy-Item -Path $expertsDir -Destination $backupDir -Recurse -Force
    Write-Host "Backup created: $backupDir" -ForegroundColor Yellow
}

# 复制新的专家库
Copy-Item -Path "experts" -Destination $openclawDir -Recurse -Force

# 验证安装
if (Test-Path "$expertsDir\engineering\names") {
    Write-Host "✅ Installation successful!" -ForegroundColor Green
    Write-Host "You can now use: '请专家帮我...'" -ForegroundColor Cyan
} else {
    Write-Host "❌ Installation failed!" -ForegroundColor Red
}
```

运行脚本：
```powershell
# 设置执行策略（如果需要）
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 运行安装脚本
.\install.ps1
```

---

**感谢你的耐心！希望这个 Windows 指南能帮助你在 Windows 系统上成功使用专家库增强方案。**