#!/usr/bin/env python3
"""
专家库安装验证工具

这个脚本帮助用户验证 Expert Library Plus 是否正确安装。
由于 AI 项目的效果难以直接验证，我们通过检查文件结构、
路径和基本功能来确认安装状态。
"""

import os
import sys
import json
from pathlib import Path

class InstallationValidator:
    def __init__(self):
        self.openclaw_dir = self.get_openclaw_directory()
        self.experts_dir = self.openclaw_dir / "experts"
        self.results = []
        
    def get_openclaw_directory(self):
        """获取 OpenClaw 配置目录"""
        if sys.platform == "win32":
            return Path(os.environ["USERPROFILE"]) / ".openclaw"
        else:
            return Path.home() / ".openclaw"
            
    def check_basic_structure(self):
        """检查基本目录结构"""
        checks = [
            ("OpenClaw 目录存在", self.openclaw_dir.exists()),
            ("专家目录存在", self.experts_dir.exists()),
            ("工程专家目录存在", (self.experts_dir / "engineering").exists()),
            ("设计专家目录存在", (self.experts_dir / "design").exists()),
            ("商业专家目录存在", (self.experts_dir / "business").exists()),
            ("安全专家目录存在", (self.experts_dir / "safety").exists()),
        ]
        
        for check_name, result in checks:
            self.results.append((check_name, result))
            if not result:
                print(f"❌ {check_name}: 失败")
            else:
                print(f"✅ {check_name}: 成功")
                
    def check_name_library_structure(self):
        """检查人名库目录结构"""
        name_dirs = [
            "engineering/names",
            "design/names", 
            "business/names",
            "safety/names"
        ]
        
        for name_dir in name_dirs:
            full_path = self.experts_dir / name_dir
            exists = full_path.exists()
            has_files = exists and len(list(full_path.glob("*.md"))) > 0
            
            check_name = f"人名库目录 {name_dir} 存在"
            self.results.append((check_name, exists))
            if not exists:
                print(f"❌ {check_name}: 失败")
            else:
                print(f"✅ {check_name}: 成功")
                
            if exists:
                file_check = f"人名库 {name_dir} 包含文件"
                self.results.append((file_check, has_files))
                if has_files:
                    file_count = len(list(full_path.glob("*.md")))
                    print(f"✅ {file_check}: {file_count} 个文件")
                else:
                    print(f"⚠️  {file_check}: 目录为空")
                    
    def check_steve_jobs_file(self):
        """检查 Steve Jobs 示范文件"""
        steve_jobs_path = self.experts_dir / "engineering" / "names" / "steve-jobs.md"
        exists = steve_jobs_path.exists()
        
        self.results.append(("Steve Jobs 示范文件存在", exists))
        if exists:
            # 检查文件内容是否完整
            try:
                content = steve_jobs_path.read_text(encoding='utf-8')
                has_required_fields = (
                    "史蒂夫·乔布斯" in content and
                    "领域" in content and
                    "权威性证明" in content and
                    "核心特质" in content
                )
                self.results.append(("Steve Jobs 文件内容完整", has_required_fields))
                if has_required_fields:
                    print("✅ Steve Jobs 文件: 内容完整")
                else:
                    print("⚠️  Steve Jobs 文件: 内容可能不完整")
            except Exception as e:
                print(f"⚠️  Steve Jobs 文件: 读取错误 - {e}")
                self.results.append(("Steve Jobs 文件可读", False))
        else:
            print("❌ Steve Jobs 文件: 不存在")
            
    def check_experts_md(self):
        """检查 EXPERTS.md 文件"""
        experts_md_path = self.experts_dir / "EXPERTS.md"
        exists = experts_md_path.exists()
        
        self.results.append(("EXPERTS.md 文件存在", exists))
        if exists:
            print("✅ EXPERTS.md 文件: 存在")
        else:
            print("❌ EXPERTS.md 文件: 不存在")
            
    def run_all_checks(self):
        """运行所有检查"""
        print("🔍 开始验证 Expert Library Plus 安装...")
        print(f"📁 OpenClaw 目录: {self.openclaw_dir}")
        print("-" * 50)
        
        self.check_basic_structure()
        print()
        self.check_name_library_structure()
        print()
        self.check_steve_jobs_file()
        print()
        self.check_experts_md()
        print()
        
        # 总结
        passed = sum(1 for _, result in self.results if result)
        total = len(self.results)
        success_rate = passed / total if total > 0 else 0
        
        print("=" * 50)
        print(f"📊 验证结果: {passed}/{total} 项通过 ({success_rate:.1%})")
        
        if success_rate == 1.0:
            print("🎉 安装验证成功！专家库应该能正常工作。")
            print("💡 建议: 现在可以测试 '请专家帮我...' 命令。")
        elif success_rate >= 0.8:
            print("✅ 安装基本成功，但有一些小问题。")
            print("💡 建议: 检查警告项，然后测试基本功能。")
        elif success_rate >= 0.5:
            print("⚠️  安装存在问题，可能影响功能。")
            print("💡 建议: 重新安装或手动修复问题项。")
        else:
            print("❌ 安装失败，请重新安装。")
            print("💡 建议: 参考 INSTALL-WINDOWS.md 或 README 中的安装指南。")
            
        return success_rate
        
def main():
    """主函数"""
    validator = InstallationValidator()
    success_rate = validator.run_all_checks()
    
    # 返回退出码（用于脚本调用）
    if success_rate >= 0.8:
        sys.exit(0)  # 成功
    else:
        sys.exit(1)  # 失败
        
if __name__ == "__main__":
    main()