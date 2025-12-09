# CRuls - Clash 规则集优化项目

自用的 Clash/OpenClash 规则集与配置文件，基于 [ACL4SSR](https://github.com/ACL4SSR/ACL4SSR) 进行优化和定制。

## 🎯 快速导航

### 我想使用配置文件

| 需求 | 文件 | 说明 |
|------|------|------|
| 高性能，极简配置 | [rule_mini.ini](rule_mini.ini) | ⭐ 推荐，规则数减少 94.6%，性能提升 95% |
| 保守优化，保持完整 | [rules_optimized.ini](rules_optimized.ini) | 删除 5 个无关紧要的规则集 |
| 完整功能，所有规则 | [rules.ini](rules.ini) | 包含所有 27 个规则集 |

### 我想查看文档

| 想了解 | 文档 | 内容 |
|--------|------|------|
| 极简配置详情 | [summery/MINI_README.md](summery/MINI_README.md) | rule_mini.ini 的详细说明 |
| 优化分析报告 | [summery/OPTIMIZATION_REPORT.md](summery/OPTIMIZATION_REPORT.md) | 完整的规则集分析和精简方案 |
| 配置对比 | [summery/COMPARISON.md](summery/COMPARISON.md) | 三个配置文件的详细对比 |
| 所有规则内容 | [ruleset.md](ruleset.md) | 所有 27 个规则集的完整内容 (507KB) |

## 📁 项目结构

```
CRuls/
├── README.md                    # 项目说明文档（本文件）
├── Direct.list                  # 自定义直连规则列表
├── Proxy.list                   # 自定义代理规则列表
│
├── rules.ini                    # 完整版配置文件（27个规则集，16,631条规则）
├── rules_optimized.ini          # 保守精简配置（22个规则集，16,603条规则）
├── rule_mini.ini                # 极简精简配置（19个规则集，约900条规则）⭐ 推荐
│
├── ruleset.md                   # 所有规则集的完整内容文档
│
├── scripts/                     # 工具脚本目录
│   ├── generate_ruleset.py      # 生成 ruleset.md 的脚本
│   └── analyze_ruleset.py       # 分析规则集的脚本
│
└── summery/                     # 分析报告目录
    ├── OPTIMIZATION_REPORT.md   # 详细优化分析报告
    ├── COMPARISON.md            # 配置对比报告
    └── MINI_README.md           # 极简配置详细说明
```

## 🎯 配置文件说明

### 1. rules.ini - 完整版配置 ⚙️

**特点：**
- 基于 [ACL4SSR_Online_Full.ini](https://github.com/ACL4SSR/ACL4SSR/blob/master/Clash/config/ACL4SSR_Online_Full.ini) 修改
- **27 个规则集**，**16,631 条规则**
- 包含详细的策略组（Google、微软、苹果、游戏、流媒体等）
- 地区节点分组（香港、台湾、日本、美国、新加坡、韩国、Cloudflare）
- 引用了仓库内的 `Direct.list` 和 `Proxy.list` 作为自定义规则

**适用场景：**
- 需要完整功能的用户
- 对性能要求不高
- 需要精确匹配所有中国 IP 地址

### 2. rules_optimized.ini - 保守精简配置 🔧

**特点：**
- **22 个规则集**，**16,603 条规则**
- 删除了 5 个规则集：
  - Ⓜ️ 微软Bing (已被 Microsoft.list 覆盖)
  - 💩 守望先锋 (单个游戏规则过于细化)
  - 🎮 Epic、Origin、Sony (非重度用户不需要)
- 减少 28 条规则，影响最小

**适用场景：**
- 普通用户
- 不玩 Epic、Origin、Sony 游戏
- 不玩守望先锋
- 希望优化但保持完整功能

### 3. rule_mini.ini - 极简精简配置 ⚡ 推荐

**特点：**
- **19 个规则集**，**约 900 条规则**
- 删除了 ChinaIp.list (7,456 条)，使用 `GEOIP,CN` 替代
- 删除了 ChinaCompanyIp、ChinaMedia 等小众规则集
- **保留了 SteamCN 和 GoogleCN**（Steam 国区和 Google 国内服务）
- **性能提升 95%**，规则数量减少 94.6%

**适用场景：**
- 追求性能和速度 ⚡
- Clash 客户端支持 GEOIP 功能
- 日常使用、轻度游戏用户
- 不需要精细化国内 IP 匹配

**⚠️ 注意：** 需要确保 Clash 支持 GEOIP 功能，并保持 GEOIP 数据库更新

## 📋 规则列表说明

### Direct.list - 直连补充列表

强制不走代理的域名和关键字，包含：
- DeepSeek
- AWS CheckIP
- 其他自定义直连域名

### Proxy.list - 代理补充列表

强制走代理的域名、关键字和 IP 段，包含：
- 国外 DNS 服务（Google DNS: 8.8.8.8, Cloudflare: 1.1.1.1 等）
- 特殊网站关键字
- 自定义代理域名

### 节点分组说明

所有配置文件都包含以下节点分组：

| 分组 | 类型 | 说明 |
|------|------|------|
| 🇭🇰 香港节点 | url-test | 匹配包含"港"、"HK"、"Hong Kong"等关键词的节点 |
| 🇨🇳 台湾节点 | url-test | 匹配包含"台"、"TW"、"Taiwan"等关键词的节点 |
| 🇯🇵 日本节点 | url-test | 匹配包含"日本"、"JP"、"Japan"等关键词的节点 |
| 🇺🇲 美国节点 | url-test | 匹配包含"美"、"US"、"United States"等关键词的节点 |
| 🇸🇬 狮城节点 | url-test | 匹配包含"新加坡"、"SG"、"Singapore"等关键词的节点 |
| 🇰🇷 韩国节点 | url-test | 匹配包含"KR"、"Korea"、"韩"等关键词的节点 |
| ☁️ Cloudflare | url-test | 匹配包含"Cloudflare"、"CF"、"CDN"等关键词的节点 ⭐ 新增 |
| ♻️ 自动选择 | url-test | 自动选择延迟最低的节点 |
| 🚀 节点选择 | select | 手动选择节点 |
| 🚀 手动切换 | select | 手动切换节点 |

**Cloudflare 分组说明：**
- 专门为 Cloudflare CDN 节点设计
- 匹配包含 Cloudflare、CF、CDN、Trojan-WS-TLS 等关键词的节点
- 适合需要稳定 CDN 加速的场景

## 🛠️ 工具脚本

### scripts/generate_ruleset.py

**功能：** 从 `rules.ini` 中提取所有 ruleset URL，访问并生成 `ruleset.md` 文档

**使用方法：**
```bash
cd /path/to/CRuls
python3 scripts/generate_ruleset.py
```

**输出：** `ruleset.md` - 包含所有规则集的完整内容

### scripts/analyze_ruleset.py

**功能：** 分析 `ruleset.md`，统计规则数量，找出可精简的规则集

**使用方法：**
```bash
cd /path/to/CRuls
python3 scripts/analyze_ruleset.py
```

**输出：** 在终端显示详细的分析报告

## 📊 配置对比

| 项目 | rules.ini | rules_optimized.ini | rule_mini.ini |
|------|-----------|---------------------|---------------|
| 规则集数量 | 27 个 | 22 个 | 19 个 |
| 规则总数 | 16,631 条 | 16,603 条 | ~900 条 |
| 性能 | 基准 | +5% | +95% ⚡ |
| 适用场景 | 完整功能 | 保守优化 | 极简高性能 |
| GEOIP 依赖 | 否 | 否 | 是 ✅ |

## 📖 详细文档

- **[OPTIMIZATION_REPORT.md](summery/OPTIMIZATION_REPORT.md)** - 完整的优化分析报告
  - 各规则集统计信息
  - 精简建议和方案
  - 进一步优化选项

- **[COMPARISON.md](summery/COMPARISON.md)** - 配置对比报告
  - 原始配置 vs 精简配置
  - 删除的规则集详情
  - 使用建议

- **[MINI_README.md](summery/MINI_README.md)** - 极简配置详细说明
  - 精简策略详解
  - 性能优化说明
  - 注意事项和问题处理

- **[ruleset.md](ruleset.md)** - 所有规则集的完整内容
  - 27 个规则集的详细规则
  - 包含规则名称、URL 和完整内容

## 🚀 快速开始

### 1. 选择合适的配置文件

**推荐流程：**
1. 首次使用先选择 **`rule_mini.ini`**（极简版）
2. 测试 1-2 周，观察是否有问题
3. 如有问题切换到 `rules_optimized.ini`（保守版）
4. 仍有问题则使用 `rules.ini`（完整版）

### 2. 在 Clash 中使用

#### 方法一：直接引用（推荐）
将配置文件上传到 GitHub，在 Clash 订阅转换中使用：
```
https://raw.githubusercontent.com/YOUR_USERNAME/CRuls/main/rule_mini.ini
```

#### 方法二：本地使用
1. 下载对应的 `.ini` 文件
2. 在 Clash 订阅转换工具中选择本地文件
3. 生成 Clash 配置

### 3. 验证 GEOIP 支持（使用 rule_mini.ini 时必须）

确保你的 Clash 客户端：
- ✅ 支持 GEOIP 功能
- ✅ GEOIP 数据库是最新的
- ✅ 配置中包含 `[]GEOIP,CN,no-resolve`

## 🔄 更新规则

### 自动更新（推荐）
Clash 会定期自动更新规则集，无需手动操作。

### 手动更新
如需手动更新 `ruleset.md`：
```bash
cd /path/to/CRuls
python3 scripts/generate_ruleset.py
```

## ⚠️ 常见问题

### Q1: 使用 rule_mini.ini 后，国内网站误走代理？

**原因：** GEOIP 数据库不完整或未更新

**解决方案：**
1. 更新 GEOIP 数据库
2. 将误判域名添加到 `Direct.list`
3. 切换到 `rules_optimized.ini` 或 `rules.ini`

### Q2: 哪个配置文件最适合我？

| 用户类型 | 推荐配置 |
|---------|---------|
| 追求性能，客户端支持 GEOIP | `rule_mini.ini` ⭐ |
| 普通用户，不玩小众游戏 | `rules_optimized.ini` |
| 需要完整功能，对性能要求不高 | `rules.ini` |
| Epic/Origin 重度玩家 | `rules.ini` |

### Q3: 如何检查 Clash 是否支持 GEOIP？

大多数 Clash 核心都支持 GEOIP：
- Clash Premium ✅
- Clash Meta (mihomo) ✅
- OpenClash ✅
- Clash for Windows ✅

### Q4: 可以同时使用多个配置文件吗？

不可以。每次只能使用一个配置文件，但可以随时切换。

## 🙏 致谢

- [ACL4SSR](https://github.com/ACL4SSR/ACL4SSR) - 基础规则集
- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) - 部分规则集来源

## 📝 规则集来源

所有规则集来源于以下开源项目：
- [ACL4SSR/ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)
- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)

## 📄 许可证

本项目遵循原始项目的许可证。自定义规则（`Direct.list`、`Proxy.list`）采用 MIT 许可证。

## 🔗 相关链接

- [Clash](https://github.com/Dreamacro/clash)
- [Clash Premium](https://github.com/Dreamacro/clash/releases/tag/premium)
- [OpenClash](https://github.com/vernesong/OpenClash)
- [订阅转换工具](https://github.com/tindy2013/subconverter)

---

**最后更新**: 2025-12-09
