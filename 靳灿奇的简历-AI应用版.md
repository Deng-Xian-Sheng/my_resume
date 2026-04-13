# 靳灿奇的简历

## 目录

- [靳灿奇的简历](#靳灿奇的简历)
  - [目录](#目录)
  - [一句话自我介绍](#一句话自我介绍)
  - [目标岗位](#目标岗位)
  - [我的亮点](#我的亮点)
  - [速览本简历](#速览本简历)
  - [工作经历](#工作经历)
    - [AI 应用研发（2024.10 - 至今）](#ai-应用研发202410---至今)
    - [山东尼诺智能科技有限公司](#山东尼诺智能科技有限公司)
    - [济南黑马网络技术有限公司](#济南黑马网络技术有限公司)
  - [我的项目](#我的项目)
    - [cmd-ai-dev AI编程工具](#cmd-ai-dev-ai编程工具)
      - [特点](#特点)
    - [深度学习相关GitHub库](#深度学习相关github库)
    - [用于LLM SFT训练的小说/文章数据清洗与合成](#用于llm-sft训练的小说文章数据清洗与合成)
      - [概述](#概述)
    - [DayLog](#daylog)
    - [coding-daylog-skill](#coding-daylog-skill)
    - [burn-after-reading（阅后即焚）](#burn-after-reading阅后即焚)
    - [make\_data\_set\_so-vits-svc](#make_data_set_so-vits-svc)
    - [call-to-llm](#call-to-llm)
  - [工作地点](#工作地点)
  - [工资要求](#工资要求)
  - [远程面试](#远程面试)
  - [出差](#出差)
  - [核心技能](#核心技能)
  - [学历](#学历)
  - [其他信息\&联系](#其他信息联系)

## 一句话自我介绍

我有 2.5 年 Golang 商业后端开发经验，做过接口实现和部署上线。

过去 1.5 年主要在做 AI 应用独立研发和开源实践，涉及 Agent、模型微调、量化部署和 LLM 应用工具开发。

我希望找的是偏工程落地的岗位，比如 AI 应用开发或模型部署方向，能比较快上手并产出结果。

## 目标岗位

- AI 应用工程师
- LLM 应用工程师
- Agent 开发工程师
- 模型部署工程师
- AIGC 工程师（偏应用）
- 智能体应用开发

## 我的亮点

- Agent 流程设计
- LoRA 微调
- Qwen / DeepSeek / Flux / YOLO 相关实践
- vLLM / ollama / llama.cpp 部署
- 低资源环境量化优化
- 开源贡献
- 作品 demo

## 速览本简历

* **我工作时的照片**：
* <img src="3D8210E8971541410295786A2FCEAD64.png" width="300">
* <img src="6694DDB3B5F03FF60BF216AA1FF2BFA8.png" width="300">

* **基本情况**：23岁，2年在校开发经验，2.5年 Golang 商业后端经验，1.5年 AI 独立研发与开源实践，工作地点**全国皆可**（无城市偏好）。

* **核心竞争力**：不仅掌握 LLM/Agent 落地实战，还拥有Golang/Linux 服务端开发这样的**工程化**能力。

* **AI 技能**：
  * **Agent 开发**：了解流程编排、熟悉提示词工程、了解函数调用/智能体记忆/RAG/skill/MCP/上下文压缩/多模态/深度研究/联网搜索。
  
  * **模型微调与训练**：基于 Qwen / DeepSeek / Flux / YOLO 完成多类模型微调与量化实践，覆盖文本、视觉理解、图像生成与目标检测场景，具备低显存部署与特定任务适配经验
  
  * **本地部署**：了解 ollama/vllm/llama.cpp 等推理库，具备在 CPU/低显存环境下进行量化部署与性能优化的能力。

* **开源贡献**：活跃的开源贡献者，曾向 Deepin 操作系统([迁移方案](https://github.com/Deng-Xian-Sheng/deepin-v23-to-v25-python-script)/[壁纸](https://github.com/Deng-Xian-Sheng/DeepinV25-desktop-wallpaper))、DiffSynth-Studio([int8微调](https://github.com/modelscope/DiffSynth-Studio/pull/1101)) 、QwenCode([qwen3.5-plus bug](https://github.com/QwenLM/qwen-code/pull/2300))等知名项目提交代码，拥有多个有价值个人开源项目。

* **工作风格**：极简实用主义，解决问题为导向，有单兵作战与技术攻关能力。

* **联系信息**：
  * **邮箱**：daylog@qq.com

  * **哔哩哔哩**：https://space.bilibili.com/507940635

  * **github**：https://github.com/Deng-Xian-Sheng

  * **huggingface**：https://huggingface.co/likewendy

  * **魔塔社区**：https://modelscope.cn/profile/likewendy

## 工作经历

### AI 应用研发（2024.10 - 至今）

工作内容：

1. 跟踪人工智能前沿模型进展情况，探究实际应用落地可能性。
2. 编写ipynb，推理/微调小模型。
3. 发布模型和代码，公开有价值的成果，为开源做贡献。
4. 研究模型应用落地具体方案，编写实施计划。
5. 与开源社区和相关研究人员深入探讨交换意见。

内容：

- 发布了一个基于yolo用于识别闲鱼网页上消息红点的模型：[链接](https://huggingface.co/likewendy/red-dot_yolov12n_object_detection)
- 发布了一个基于流浪地球2图丫丫角色训练的Flux lora：[链接](https://huggingface.co/likewendy/flux-dev-tu-ya-ya)
- 为modelscope开源的国产文生图模型推理训练框架DiffSynth-Studio添加Qwen-Image-Edit-2509模型的int8量化微调方法，大幅度降低显存占用：[链接](https://github.com/modelscope/DiffSynth-Studio/pull/1101)
- 为国产操作系统Deepin社区贡献v23～v25大版本系统迁移方案：[链接](https://github.com/Deng-Xian-Sheng/deepin-v23-to-v25-python-script)、基于DeepinV25的无图标遮挡视频壁纸实现方案：[链接](https://github.com/Deng-Xian-Sheng/DeepinV25-desktop-wallpaper)
- 更新10余篇有价值的 大模型微调/推理/智能体 实施方法：[链接](https://github.com/Deng-Xian-Sheng/Real-technology)
- 修改Meta公司音频分割模型sam-audio的开源仓库，降低了推理时显存需求与多模型依赖，并编写了gradio以方便的使用模型：[链接](https://cnb.cool/CanQiJin/sam-audio-large)
- DayLog软件所需模型的数据集爬取、合成和模型训练。
- 为知名开源项目QwenCode贡献代码（修复了`qwen3.5-plus`和`Qwen3.5-397B-A17B`模型bug，导致的文件路径损坏问题：[链接](https://github.com/QwenLM/qwen-code/pull/2300)）
- coding-daylog-skill，一个 Agent skill，它让 Agent 根据 git 提交，统计你今天做了什么：[链接](https://github.com/Deng-Xian-Sheng/coding-daylog-skill)
- burn-after-reading（阅后即焚），一个“阅后即焚”的图片分享 Web 应用：[链接](https://github.com/Deng-Xian-Sheng/burn-after-reading)

### 山东尼诺智能科技有限公司

工资：月薪5k，到手4850 + 300元公积金

岗位：Golang后端开发

日期：2022-01～2024-10（2.5年）

工作内容：
- 参与某管理系统多个业务模块的后端开发，负责接口设计、数据处理、部署上线及问题排查，支持项目从原型到交付落地。
- git仓库和构建部署流水线用的阿里云云效

业绩：
- 年底老板给了我13薪。
- 上司夸我“让人眼前一亮”。

离职原因：
- 开发周期与工作量与员工数量不符
- 工资没有上升空间

### 济南黑马网络技术有限公司

工资：每月，试用期3500元，正式工4500元。

岗位：全栈工程师（基本啥都干）

日期：2021-07～2021-12（约4个月）

工作内容：
1. 开发和部署PHP网页与CMS

业绩：
- 公司节假日奖励了个充电宝。
- 领导评价我不错。
- 为公司培训了一个新人。

离职原因：
- 薪资待遇不高
- 工作流程混乱

## 我的项目

### cmd-ai-dev AI编程工具

一个命令行 AI 编程工具，它在 Docker 容器里运行，模型通过命令行来完成编程任务，用左右分栏 TUI 提升 16:9 屏幕下的可用性。

![cmd ai dev 运行的图片](cmd-ai-dev.png)

#### 特点

- 支持skills
- 支持用playwright操作浏览器
- 不依赖函数调用，即使模型不支持 function calling 也能工作
- 通过划分AI工作区，让项目文件夹更干净

链接：https://github.com/Deng-Xian-Sheng/cmd-ai-dev

### 深度学习相关GitHub库

![仓库图片](Real-technology.png)

- 在模型训练和实现需求（主要是个人idea）的过程中，有时会遇到一些不错的实现，开源出来增加个人影响力。
- 这些技术对于需要的人来说千金不换。

链接：https://github.com/Deng-Xian-Sheng/Real-technology

### 用于LLM SFT训练的小说/文章数据清洗与合成

#### 概述

借助LLM，基于纯文本的小说/文章，合成符合OpenAI API message 格式的数据集，该数据集可用于小说/文章生成模型的微调。

支持长上下文分段，添加了段落摘要和总摘要用于缓解主题偏离，添加了段落标题用于优化视觉呈现。

对于训练部分，探索了利用grpo让模型产生思维链以优化小说生成的方法，但该方法有一定的局限性。（具体来说，通过Qwen3-Embedding-0.6B把模型回答和数据集中的答案转换成向量，然后计算它们之间的距离，近则正奖励，远则负奖励。）

链接：https://github.com/Deng-Xian-Sheng/Novel-cleaning-synthesis

### DayLog

- DayLog偷偷记录你今天做了什么，一个PC软件，通过屏幕画面记录人类的工作内容，当一天结束之后以便回顾工作内容。
- 基座模型基于qwen系列，本地运行一个小VLM，该模型经过高质量数据集微调，特点是无API花费、隐私安全。
- 部署时int4 gguf llama.cpp量化部署，由于经过微调，模型性能不会损失太多。
- 仍在开发：模型已训练完成，许可证服务和桌面端正在开发。

![ide截图](daylog.png)

### coding-daylog-skill

![代码截图](1776064808708.png)

这是一个 Agent skill，它让 Agent 根据 git 提交，统计你今天做了什么

链接：https://github.com/Deng-Xian-Sheng/coding-daylog-skill

### burn-after-reading（阅后即焚）

- 主界面
![界面](1776064473940.png)

- 加载中
![界面2](1776064548307.png)

- 链接失效
![界面3](1776064585616.png)

- 切换标签页或将浏览器放到后台，会焚毁
![界面4](1776064698250.png)

一个“阅后即焚”的图片分享 Web 应用

> 这是一个 100% vibe coding 项目。
> 
> 我一行代码都没写，完全由 codex 进行开发、部署。
> 
> 我负责项目设计，探索并选择技术栈。

在线demo：https://burn.daylog.top

链接：https://github.com/Deng-Xian-Sheng/burn-after-reading

### make_data_set_so-vits-svc

![运行示例](1776064351854.png)

这个项目实现了语音的气口切分、增益均衡，并提供了一个 GUI 的音频片段审核界面。

用于辅助 so-vits-svc(音色迁移) 数据集制作，它实现了数据集制作环节的音频切分与检查。

链接：https://github.com/Deng-Xian-Sheng/make_data_set_so-vits-svc

### call-to-llm

![演示图片-ipad](IMG_2870.png)

![演示图片-iphone](IMG_2871.png)

一个 html 文件，通过 VAD 和 OpenAI Audio API 实现了语音对话。

通过调用 gpt4o 等带视觉的模型实现解读画面。

演示视频：[实现OpenAI的ChatGPT视频聊天-哔哩哔哩](https://b23.tv/UN5KB9i)

代码仓库链接：https://github.com/Deng-Xian-Sheng/call-to-llm

这个项目大部分是使用AI开发的。

## 工作地点

我没有城市偏好，因为我没有房子，所以全国都可。

## 工资要求

<!-- 高 -->
<!-- 工资可谈，期望，月收入，税前，12k～15k人民币。 -->
<!-- 12-1=11，15-1=14，税后11k～14k -->

<!-- 中 -->
<!-- 工资可谈，期望，月收入，税前，10k～14k人民币。 -->
<!-- 10-1=9，14-1=13，税后9k～13k -->

<!-- 低 -->
工资可谈，期望，月收入，税前，10k～12k人民币。
<!-- 10-1=9，12-1=11，税后9k～11k -->

## 远程面试

目前人在山东省泰安市宁阳县。

由于跨城面试差旅成本较高，希望初试/技术面优先线上进行；若双方在终面阶段已基本确认意向，我可以配合到场。若需跨省现场面试，也想确认贵司是否支持差旅报销。

## 出差

接受短途高铁出差。

## 核心技能

核心技能：Agent开发(智能体)、模型训练&微调、模型部署

- Agent开发(智能体)
  + 针对**特定任务**，使用Lora微调模型

    提高模型对该任务的**稳定性**，或者使模型具有执行该任务的能力。

  + 提示词微调
    
    在少样本的情况下改善模型的输出结果，使其适用于特定任务。
  
  + 量化部署
  
    通过选择较小规模的模型+量化，使其能够在CPU、OpenGL环境下正常推理。

  + 函数调用
    
    无论模型是否支持函数调用，我都可以对接模型外的服务&接口，为模型提供额外的能力。
  
  + 流程编排
  
    针对特定任务设计提示词、添加外部文档、设计模型间的信息传递结构，通过多次模型调用完成特定任务。
  
  + 多种类模型API调用经验
  
    符合OpenAI API规范的接口（带有图像、文本、think），图像生成/编辑，文本转语音(tts)，翻译，人脸识别。
  
  + milvus向量数据库的基本使用
    
    添加数据和相似搜索

  + 文本、图片、视频向量化

    将文本、图片、视频等非结构化数据转换成向量实现相似搜索等需求。

- 模型训练&微调
  + Qwen系列
  
    使用Lora微调Qwen2、Qwen2.5、Qwen3的纯文本、`-VL`、`-Thinking`模型。以及DeepSeek-R1的qwen变体。
  
  + 目标检测
    
    针对目标检测任务，训练yolo11、yolo12，支持主动学习、0样本半自动化标注。
  
  + 图像生成
    
    使用Lora微调Flux-dev、Kolors，支持少样本，能够让模型学习新概念。

- 模型部署
  + ollama(个人或试验使用)
  + llama.cpp（推理GGUF）
  + vllm(LLM、VLM高性能推理库)
  + 本地推理的人脸核身库

    我能够部署这个库，它拥有寻找人脸位置和人脸核身功能，并且凭借我独特的算法优化，能够加快处理速度。

## 学历

- 齐鲁工业大学，非全日制，大专，艺术设计业余，成人高考学历。
- 山东新华电脑学院，2018～2021，网络安全专业。

  2018年6月份就读于山东新华电脑学院—网络信息安全专业(后成人高考获大专学历)，21年6月份毕业；在校主要学习Python编程基础、MySQL、Linux、TCP/IP、Web服务安全。


## 其他信息&联系
- 出生日期&年龄：2002年，今年23岁。
- 邮箱：daylog@qq.com
- 哔哩哔哩：https://space.bilibili.com/507940635
- github：https://github.com/Deng-Xian-Sheng
- huggingface：https://huggingface.co/likewendy
- 魔塔社区：https://modelscope.cn/profile/likewendy
- [INTJ-A](https://www.16personalities.com/ch/档案/e3a6c8bc6ca93)
- 我心目中的好工作是，个人与公司共同前进，公司在发展，个人在进步。

---

**简历结束**，你居然看完了我的简历🎉！

♥️♥️辛苦了，你真的是太棒了🏆！都看到这里了，不妨约个面试❓

---

在Github上打开本简历：[链接](https://github.com/Deng-Xian-Sheng/my_resume)

<!-- 链接部分 -->

<!-- [ida]: https://github.com/modelscope/DiffSynth-Studio/pull/1101 "Qwen-Image-Edit-2509模型的int8量化微调方法，大幅度降低显存占用"
[idb]: https://github.com/Deng-Xian-Sheng/deepin-v23-to-v25-python-script "v23～v25大版本系统迁移方案"
[idc]: https://github.com/Deng-Xian-Sheng/DeepinV25-desktop-wallpaper "基于DeepinV25的无图标遮挡视频壁纸实现方案"
[idd]: https://github.com/QwenLM/qwen-code/pull/2300 "修复了`qwen3.5-plus`和`Qwen3.5-397B-A17B`模型bug，导致的文件路径损坏问题" -->