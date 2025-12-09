# Rules.ini 精简建议报告

## 分析概要

根据对 `ruleset.md` 的分析，当前配置包含：
- **27 个规则集**
- **16,631 条规则**
- **平均每个规则集 616 条规则**

## 可精简的规则集

### 1. 微软相关规则（可合并）⭐ 推荐精简

**当前配置：**
```ini
ruleset=Ⓜ️ 微软Bing,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Bing.list          # 3条
ruleset=Ⓜ️ 微软云盘,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/OneDrive.list     # 19条
ruleset=Ⓜ️ 微软服务,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Microsoft.list   # 79条
```

**精简建议：**
- `Microsoft.list` 已经包含了微软的主要服务
- `Bing.list` 只有 3 条规则，可以删除，让 Bing 使用 `Microsoft.list` 规则
- `OneDrive.list` 19 条规则较少，可以考虑合并到 `Microsoft.list`

**推荐操作：** 保留 `Ⓜ️ 微软服务`，删除 `Ⓜ️ 微软Bing`（Bing 已被 Microsoft.list 覆盖）

---

### 2. 游戏平台规则（可大幅精简）⭐⭐ 强烈推荐精简

**当前配置：**
```ini
ruleset=🎮 游戏平台,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Epic.list      # 6条
ruleset=🎮 游戏平台,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Origin.list    # 7条
ruleset=🎮 游戏平台,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Sony.list      # 5条
ruleset=🎮 游戏平台,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Steam.list     # 18条
ruleset=🎮 游戏平台,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Nintendo.list  # 15条
```

**精简建议：**
- 5 个游戏平台规则集共 **51 条规则**，且都指向同一个分组 `🎮 游戏平台`
- 规则数量都很少（5-18 条），可以合并

**推荐操作：**
- **保留** `Steam.list`（18 条，用户最多）
- **保留** `Nintendo.list`（15 条，任天堂用户较多）
- **删除** Epic、Origin、Sony（规则很少，非重度用户可以忽略）

或者如果不是重度游戏玩家，可以只保留 `Steam.list`

---

### 3. AI 规则（可选合并）

**当前配置：**
```ini
ruleset=💬 AI,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/OpenAi.list            # 17条
ruleset=💬 AI,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Gemini/Gemini.list  # 13条
```

**精简建议：**
- 两个规则集都指向同一分组 `💬 AI`
- 规则数量都不多（共 30 条）
- OpenAI 和 Gemini 没有重叠

**推荐操作：** 建议保留，如果只使用其中一个 AI 服务可以删除另一个

---

### 4. 守望先锋规则（可删除）⭐ 推荐删除

**当前配置：**
```ini
ruleset=💩 守望先锋,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Overwatch/Overwatch.list  # 7条
```

**精简建议：**
- 只有 7 条规则
- 单独为一个游戏设置规则集过于细化
- 守望先锋的域名大多数情况下会被 `游戏平台` 或 `漏网之鱼` 规则覆盖

**推荐操作：** 删除此规则集，除非你是守望先锋重度玩家

---

### 5. 全球直连规则（部分可精简）

**当前配置：**
```ini
ruleset=🎯 全球直连,https://raw.githubusercontent.com/NicholasStone/CRules/main/Direct.list                    # 6条 - 自定义
ruleset=🎯 全球直连,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/LocalAreaNetwork.list      # 37条
ruleset=🎯 全球直连,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/UnBan.list                  # 31条
ruleset=🎯 全球直连,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaIp.list                # 7456条 ⚠️
ruleset=🎯 全球直连,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaDomain.list            # 635条
ruleset=🎯 全球直连,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaCompanyIp.list        # 208条
ruleset=🎯 全球直连,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaMedia.list             # 45条
ruleset=🎯 全球直连,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/GoogleCN.list               # 29条
ruleset=🎯 全球直连,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/SteamCN.list        # 16条
```

**精简建议：**
- `ChinaIp.list` 有 **7456 条规则**，占总规则数的 45%
- 建议保留核心规则集，但可以考虑：
  - `ChinaMedia.list`（45 条）和 `ChinaCompanyIp.list`（208 条）可能与 `ChinaDomain.list` 有重叠
  - 如果有 `[]GEOIP,CN` 兜底规则，`ChinaIp.list` 可以考虑删除以减少规则数量

**推荐操作：**
- **保留** Direct.list（自定义）、LocalAreaNetwork.list、UnBan.list、ChinaDomain.list
- **可选** ChinaIp.list（如果你的客户端支持 GEOIP，可以用 GEOIP,CN 替代）
- **可删除** ChinaMedia.list、ChinaCompanyIp.list、GoogleCN.list、SteamCN.list（这些较小众）

---

### 6. 节点选择规则

**当前配置：**
```ini
ruleset=🚀 节点选择,https://raw.githubusercontent.com/NicholasStone/CRules/main/Proxy.list                  # 23条 - 自定义
ruleset=🚀 节点选择,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ProxyGFWlist.list        # 6986条
```

**精简建议：**
- 两个规则集功能互补，建议保留

---

## 精简方案总结

### 方案一：保守精简（推荐）

**删除以下规则（共 5 个）：**

```ini
# 删除这些行
ruleset=Ⓜ️ 微软Bing,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Bing.list
ruleset=💩 守望先锋,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Overwatch/Overwatch.list
ruleset=🎮 游戏平台,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Epic.list
ruleset=🎮 游戏平台,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Origin.list
ruleset=🎮 游戏平台,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Sony.list
```

**效果：** 减少 **28 条规则**，规则集从 27 个减少到 22 个

---

### 方案二：激进精简

**在方案一基础上，额外删除：**

```ini
# 额外删除这些行
ruleset=🎯 全球直连,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaCompanyIp.list
ruleset=🎯 全球直连,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaMedia.list
ruleset=🎯 全球直连,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/GoogleCN.list
ruleset=🎯 全球直连,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/SteamCN.list
ruleset=🎮 游戏平台,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Nintendo.list
```

**效果：** 减少 **330+ 条规则**，规则集从 27 个减少到 17 个

**注意：** 只有在不使用这些特定服务时才建议删除

---

### 方案三：极简精简（仅适合非游戏、非特殊需求用户）

**在方案二基础上，考虑删除 ChinaIp.list（7456 条规则）：**

```ini
# 如果你的 Clash 客户端支持 GEOIP，可以删除
ruleset=🎯 全球直连,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaIp.list
```

**前提条件：** 确保 rules.ini 中有这行兜底规则：
```ini
ruleset=🎯 全球直连,[]GEOIP,CN,no-resolve
```

**效果：** 减少 **7456 条规则**，大幅提升规则加载速度

---

## 优化后的 Custom Proxy Groups 建议

如果删除了某些规则集，对应的分组也可以精简：

**可以删除的分组（如果相应规则集被删除）：**

```ini
# 如果删除了守望先锋规则集
# custom_proxy_group=💩 守望先锋`select`...

# 如果 Bing 规则被删除，Bing 会跟随微软服务的策略，不需要单独分组
```

---

## 总结

**立即可删除（影响最小）：**
1. ✅ 微软Bing（3 条规则 - 已被 Microsoft.list 覆盖）
2. ✅ 守望先锋（7 条规则 - 过于细化）
3. ✅ Epic 游戏（6 条规则 - 非重度用户不需要）
4. ✅ Origin 游戏（7 条规则 - 非重度用户不需要）
5. ✅ Sony 游戏（5 条规则 - 非重度用户不需要）

**根据使用场景删除：**
- 不玩任天堂游戏 → 删除 Nintendo.list
- 只用 OpenAI → 删除 Gemini.list
- 只用 Gemini → 删除 OpenAi.list
- 不使用 Steam 国区 → 删除 SteamCN.list

**性能优化（高级）：**
- 如果 Clash 支持 GEOIP → 删除 ChinaIp.list（节省 7456 条规则）

---

**最终推荐：采用方案一（保守精简），可以在不影响使用的情况下，精简 5 个规则集。**
