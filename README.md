# 博客api接口自动化测试（基于requests和pytest）
> 📖 This document is Chinese version, click to read **[English Version](./README_EN.md)**
## 项目介绍
本项目基于 Requests + Pytest 实现博客后端接口自动化测试。
完整覆盖登录模块各类正向、异常场景接口用例；
通过二次封装 requests 实现统一请求处理与全链路日志埋点；
采用 YAML 完成数据驱动测试；使用 JsonSchema 做响应 JSON 结构强校验；
基于 logging 实现单例日志组件，区分控制台输出、info 日志文件、error 错误日志文件，可快速定位接口报错；可对接 Allure 生成可视化测试报告。

## 环境要求
- Python >= 3.8
- 网络可访问被测博客后端服务接口地址

## 运行测试方法
**在项目根目录执行下面命令**
```bash
pytest Test/ -v
pytest Test/ --alluredir=allure-results
allure generate allure-results -o allure-report --clean
```
## 项目目录说明
```
blog_api_auto/
├── Test/                      # 业务模块测试用例目录
│   └── test_login_api_auto.py # 登录模块接口自动化用例
├── utils/                     # 公共工具模块
│   ├── __init__.py
│   ├── logging_util.py        # 单例日志封装工具
│   └── request_util.py        # requests请求二次封装
├── data/                      # yaml测试数据目录
│   └── login_cases.yaml       # 登录场景测试数据
├── logs/                      # 运行自动生成日志目录
├── pytest.ini                 # pytest全局配置文件
├── requirements.txt           # 第三方依赖清单
└── README.md                  # 中文项目说明
```
## 测试用例设计
本项目自动化用例参考接口文档提炼，覆盖登录正向成功场景，账号为空、密码为空、账号密码错误等异常入参场景，采用@pytest.mark.parametrize实现数据驱动。后续可扩展文章发布、查询、越权校验等业务接口。

## 注意事项
1. 日志文件夹logs程序运行时会自动创建，无需手动新建。
2. 被测博客为公共测试服务器，存在网络抖动、限流、响应延迟情况，属于正常外部环境问题。
3. 执行测试命令必须在项目根目录运行，否则会出现模块导入失败、用例收集失败问题。
4. logs、allure‑results、allure‑report属于运行产出目录，建议配置 gitignore，不要提交到代码仓库。
5. 修改代码中接口地址为你的实际被测服务地址，否则用例无法正常执行。
