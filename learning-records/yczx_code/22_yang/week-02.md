# 第 1 周学习记录

> GitHub 用户名：asjklflad ( 22届杨睿衡 )
>
> 日期：2026年7月25日

## 本周学习内容

    hello-agents: 第三章 3.2《与大语言模型交互》 第三章 3.3.2《模型幻觉》 第四章 4.2.1《ReAct 的工作流程》
    learn-claude-code: 复习 s01_agent_loop ，逐段解释循环  阅读 s02_tool_use ，重点理解工具注册和分发
    # 目前hello_agents4.2.1还未看完，今天应该搞定

## 我用自己的话理解了什么
    单次模型调用为什么还不是 Agent
        单次模型调用只是一次性问答，use_tool不会把数据回传给模型进行思考,流程上没有形成闭环
        agent_loop:
            user_input --> thinking --> use_tool or text
                                    --> if use_tool --> thinking --> use_tool or text ( cycle )

    模型决策与 Harness 执行的区别
        模型决策: 接受用户的需求，根据历史对话自主判断是否调用工具或输出结果(高自主性，可自主决定执行方案)
                 thinking --> use_tool or text
        Harness执行: 结合模型决策串成完整发布流程，环境、失败补救、日志归档告警，全程自动化闭环
                    (无自主性，仅根据模型决策运行)

## 我运行或修改了什么
    01_first_chat.py
    02_first_tool_call.py
    03_agent_loop.py
    # 前三个都是运行，只有轻微修改
        例: 
            try:
                DEFAULT_BASE_URL = "https://api.deepseek.com/anthropic"
                DEFAULT_MODEL = "deepseek-v4-pro"
            except ImportError:
                DEFAULT_BASE_URL = args.DEFAULT_BASE_URL
                DEFAULT_MODEL = args.model
    # 目前正在学习exercises/yczx_code/yanchuaner/week-01/1.3.py，比Hello agent功能更美观，功能更健全

## 验证命令与结果
    01_first_chat.py
        AI Agent 是一种能够自主感知环境、制定计划并执行动作以达成特定目标的智能系统。它能够独立完成任务，而无需人类进行每一步的直接干预或指令。
    02_first_tool_call.py
        模型请求工具：calculate
        工具参数：{'expression': '(23 + 19) * 7'}
        本地执行结果：294
    03_agent_loop.py
        === 第 1 轮：请求模型 ===
        Action：calculate({'expression': '(23 + 19) * 7'})
        Observation：294
        Action：get_current_time({})
        Observation：2026-07-23T21:44:42+08:00
        === 第 2 轮：请求模型 ===
        (23 + 19) * 7 = **294**，当前本地时间为 **2026年7月23日 21:44:42**。

        Agent 没有继续请求工具，循环结束。

## 仍然困惑的问题（学习缺口自检清单）
    若示例3到达 MAX_STEPS 最大循环模型仍未完成思考，应该怎么进一步处理?
    是在prompt还是agent_loop上进行完善？


