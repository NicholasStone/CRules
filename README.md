# OpenClash 规则集

自用的 OpenClash 规则集与配置文件，基于 ACL4SSR 进行修改和补充。

## 文件说明

### 配置文件 (INI)
用于 OpenClash 的配置文件转换或规则生成。

- **[rules.ini](rules.ini)**
  - **完整版配置文件**
  - 基于 [ACL4SSR_Online_Full.ini](https://github.com/ACL4SSR/ACL4SSR/blob/master/Clash/config/ACL4SSR_Online_Full.ini) 修改。
  - 包含详细的策略组（如 Google、微软、苹果、游戏、流媒体等）和地区节点分组（香港、日本、美国等）。
  - 引用了仓库内的 `Direct.list` 和 `Proxy.list` 作为自定义规则。

- **[rule_mini.ini](rule_mini.ini)**
  - **精简版配置文件**
  - 结构更简单，策略组较少。
  - 同样引用了仓库内的 `Direct.list` 和 `Proxy.list`。

### 规则列表 (List)
被上述配置文件引用的自定义规则列表。

- **[Direct.list](Direct.list)**
  - **直连补充列表**
  - 包含强制不走代理的域名和关键字。
  - 例如：DeepSeek, AWS CheckIP 等。

- **[Proxy.list](Proxy.list)**
  - **代理补充列表**
  - 包含强制走代理的域名、关键字和 IP 段。
  - 例如：国外 DNS 服务 (Google DNS, Cloudflare DNS), 特殊网站关键字等。

## 规则集来源

- [ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)
