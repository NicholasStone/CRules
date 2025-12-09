#!/usr/bin/env python3
"""
生成 ruleset.md 文档
从 rules.ini 文件中提取所有 ruleset URL，访问并获取内容，生成 Markdown 文档
"""

import re
from typing import List, Tuple
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import socket


def parse_rules_ini(file_path: str) -> List[Tuple[str, str]]:
    """
    解析 rules.ini 文件，提取 ruleset 规则

    Args:
        file_path: rules.ini 文件路径

    Returns:
        包含 (规则名称, URL) 的列表
    """
    rulesets = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            # 跳过空行和注释行
            if not line or line.startswith(';'):
                continue

            # 匹配 ruleset 行：ruleset=规则名称,URL
            if line.startswith('ruleset='):
                # 移除 "ruleset=" 前缀
                content = line[8:]

                # 分割规则名称和 URL
                parts = content.split(',', 1)
                if len(parts) == 2:
                    rule_name = parts[0].strip()
                    url = parts[1].strip()

                    # 只处理 http/https URL，跳过特殊规则如 []GEOIP,CN
                    if url.startswith('http://') or url.startswith('https://'):
                        rulesets.append((rule_name, url))

    return rulesets


def fetch_rule_content(url: str, timeout: int = 30) -> str:
    """
    获取规则集内容

    Args:
        url: 规则集 URL
        timeout: 超时时间（秒）

    Returns:
        规则内容字符串，失败返回错误信息
    """
    try:
        with urlopen(url, timeout=timeout) as response:
            content = response.read().decode('utf-8')
            return content
    except socket.timeout:
        return f"错误: 请求超时 ({timeout}秒)"
    except HTTPError as e:
        return f"错误: HTTP {e.code}"
    except URLError as e:
        return f"错误: {str(e.reason)}"
    except Exception as e:
        return f"错误: {str(e)}"


def generate_markdown(rulesets: List[Tuple[str, str]], output_path: str):
    """
    生成 Markdown 文档

    Args:
        rulesets: 规则集列表 [(名称, URL), ...]
        output_path: 输出文件路径
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        # 写入文档标题
        f.write("# Ruleset 规则集文档\n\n")
        f.write(f"本文档包含 {len(rulesets)} 个规则集的详细内容\n\n")
        f.write("---\n\n")

        # 遍历每个规则集
        for idx, (rule_name, url) in enumerate(rulesets, 1):
            print(f"[{idx}/{len(rulesets)}] 正在获取: {rule_name}")
            print(f"    URL: {url}")

            # 写入规则名称和 URL
            f.write(f"## {rule_name}\n\n")
            f.write(f"> URL: {url}\n\n")

            # 获取规则内容
            content = fetch_rule_content(url)

            # 写入规则内容（使用代码块）
            f.write("```\n")
            f.write(content)
            f.write("\n```\n\n")
            f.write("---\n\n")

            print(f"    ✓ 完成\n")

    print(f"\n✓ Markdown 文档已生成: {output_path}")


def main():
    """主函数"""
    # 获取脚本所在目录
    script_dir = Path(__file__).parent

    # 文件路径
    rules_ini_path = script_dir / "rules.ini"
    output_path = script_dir / "ruleset.md"

    print("=" * 60)
    print("Ruleset 文档生成器")
    print("=" * 60)
    print()

    # 检查 rules.ini 是否存在
    if not rules_ini_path.exists():
        print(f"错误: 找不到文件 {rules_ini_path}")
        return

    # 解析 rules.ini
    print(f"正在解析: {rules_ini_path}")
    rulesets = parse_rules_ini(str(rules_ini_path))
    print(f"找到 {len(rulesets)} 个规则集\n")

    if not rulesets:
        print("未找到任何有效的 ruleset 规则")
        return

    # 生成 Markdown 文档
    print("开始生成文档...\n")
    generate_markdown(rulesets, str(output_path))

    print("\n" + "=" * 60)
    print("完成!")
    print("=" * 60)


if __name__ == "__main__":
    main()
