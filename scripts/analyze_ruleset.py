#!/usr/bin/env python3
"""
分析 ruleset.md 文件，找出可以精简的规则集
"""

import re
from pathlib import Path
from collections import defaultdict


def parse_ruleset_md(file_path: str):
    """解析 ruleset.md 文件，提取每个规则集的信息"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 分割每个规则集
    sections = content.split('---\n\n')

    rulesets = []

    for section in sections:
        if not section.strip() or section.startswith('# Ruleset'):
            continue

        # 提取规则名称
        name_match = re.search(r'^## (.+)$', section, re.MULTILINE)
        if not name_match:
            continue
        name = name_match.group(1)

        # 提取 URL
        url_match = re.search(r'> URL: (.+)$', section, re.MULTILINE)
        if not url_match:
            continue
        url = url_match.group(1)

        # 提取规则内容（在 ``` 代码块中）
        code_block_match = re.search(r'```\n(.*?)\n```', section, re.DOTALL)
        if not code_block_match:
            continue
        rules_content = code_block_match.group(1)

        # 统计有效规则行（非注释、非空行）
        rules = []
        for line in rules_content.split('\n'):
            line = line.strip()
            # 跳过空行、注释行和元数据行
            if line and not line.startswith('#') and not line.startswith(';'):
                rules.append(line)

        rulesets.append({
            'name': name,
            'url': url,
            'rules': rules,
            'rule_count': len(rules),
            'content': rules_content
        })

    return rulesets


def analyze_rulesets(rulesets):
    """分析规则集，找出可以精简的部分"""

    print("=" * 80)
    print("规则集分析报告")
    print("=" * 80)
    print()

    # 1. 统计每个分类的规则数量
    print("## 1. 规则集统计（按分类）")
    print("-" * 80)

    category_stats = defaultdict(list)
    for rs in rulesets:
        category_stats[rs['name']].append(rs)

    for category, items in sorted(category_stats.items()):
        total_rules = sum(item['rule_count'] for item in items)
        print(f"\n【{category}】 - {len(items)} 个规则集，共 {total_rules} 条规则")
        for item in items:
            url_short = item['url'].split('/')[-1]
            print(f"  • {url_short:40s} - {item['rule_count']:5d} 条规则")

    print("\n" + "=" * 80)

    # 2. 检查空规则集或规则极少的规则集
    print("\n## 2. 规则数量较少的规则集（< 20 条，可能可以合并）")
    print("-" * 80)

    small_rulesets = [rs for rs in rulesets if rs['rule_count'] < 20]
    if small_rulesets:
        for rs in sorted(small_rulesets, key=lambda x: x['rule_count']):
            print(f"• {rs['name']:30s} - {rs['rule_count']:3d} 条规则")
            print(f"  URL: {rs['url']}")
    else:
        print("未找到规则数量较少的规则集")

    print("\n" + "=" * 80)

    # 3. 检查同一分类下是否有重复规则
    print("\n## 3. 同分类下的潜在重复或可合并项")
    print("-" * 80)

    for category, items in sorted(category_stats.items()):
        if len(items) > 1:
            print(f"\n【{category}】有 {len(items)} 个规则集，建议检查是否可以合并：")
            for item in items:
                url_short = item['url'].split('/')[-1]
                print(f"  • {url_short} ({item['rule_count']} 条规则)")

    print("\n" + "=" * 80)

    # 4. 检查错误或空内容
    print("\n## 4. 错误或异常的规则集")
    print("-" * 80)

    error_rulesets = [rs for rs in rulesets if '错误:' in rs['content']]
    if error_rulesets:
        for rs in error_rulesets:
            print(f"• {rs['name']}")
            print(f"  URL: {rs['url']}")
            print(f"  错误: {rs['content'][:100]}")
    else:
        print("✓ 所有规则集均正常获取")

    print("\n" + "=" * 80)

    # 5. 统计总体信息
    print("\n## 5. 总体统计")
    print("-" * 80)

    total_rulesets = len(rulesets)
    total_rules = sum(rs['rule_count'] for rs in rulesets)
    avg_rules = total_rules / total_rulesets if total_rulesets > 0 else 0

    print(f"规则集总数: {total_rulesets}")
    print(f"规则总数: {total_rules}")
    print(f"平均每个规则集: {avg_rules:.1f} 条规则")

    # 找出最大和最小的规则集
    if rulesets:
        max_rs = max(rulesets, key=lambda x: x['rule_count'])
        min_rs = min(rulesets, key=lambda x: x['rule_count'])

        print(f"\n最大规则集: {max_rs['name']} ({max_rs['rule_count']} 条规则)")
        print(f"最小规则集: {min_rs['name']} ({min_rs['rule_count']} 条规则)")

    print("\n" + "=" * 80)

    # 6. 精简建议
    print("\n## 6. 精简建议")
    print("-" * 80)

    suggestions = []

    # 建议1: 规则数量少于10的可以考虑合并
    very_small = [rs for rs in rulesets if rs['rule_count'] < 10]
    if very_small:
        suggestions.append(f"• 发现 {len(very_small)} 个规则集少于 10 条规则，建议合并到相关分类")

    # 建议2: 同分类多个规则集
    multi_category = [cat for cat, items in category_stats.items() if len(items) > 2]
    if multi_category:
        suggestions.append(f"• 以下分类有多个规则集，建议检查是否可以精简:")
        for cat in multi_category:
            suggestions.append(f"  - {cat}: {len(category_stats[cat])} 个规则集")

    # 建议3: 检查是否真的需要这么细分的游戏平台
    game_rulesets = [rs for rs in rulesets if '游戏平台' in rs['name']]
    if len(game_rulesets) >= 5:
        total_game_rules = sum(rs['rule_count'] for rs in game_rulesets)
        suggestions.append(f"• 游戏平台有 {len(game_rulesets)} 个独立规则集，共 {total_game_rules} 条规则")
        suggestions.append(f"  建议: 如果不是重度游戏用户，可以合并为单个'游戏平台'规则集")

    if suggestions:
        for s in suggestions:
            print(s)
    else:
        print("✓ 当前配置较为精简，无明显可优化项")

    print("\n" + "=" * 80)


def main():
    script_dir = Path(__file__).parent
    ruleset_md_path = script_dir / "ruleset.md"

    if not ruleset_md_path.exists():
        print(f"错误: 找不到文件 {ruleset_md_path}")
        return

    print(f"正在分析: {ruleset_md_path}\n")

    rulesets = parse_ruleset_md(str(ruleset_md_path))
    analyze_rulesets(rulesets)


if __name__ == "__main__":
    main()
