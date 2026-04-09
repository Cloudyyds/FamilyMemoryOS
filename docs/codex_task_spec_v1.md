# FamilyMemoryOS - Codex 编程需求文档 v1

## 1. 文档目的

本文档用于约束 Codex 在 FamilyMemoryOS 项目中的编码行为，确保生成代码符合项目定位、环境约束与阶段目标。

Codex 在执行任何开发任务前，应优先遵守本文档，而不是自行扩展需求或引入额外复杂度。

---

## 2. 项目定位

FamilyMemoryOS 是一个本地优先（local-first）、隐私优先（privacy-by-default）的家族数字记忆开源框架。

项目目标包括：

- 管理家族成员与亲缘关系
- 记录人物事件与家族时间线
- 导入和整理本地家族资料
- 基于本地资料进行检索问答
- 构建受约束、可追溯的数字人格交互能力

本项目不是：
- 复活逝者系统
- 意识上传系统
- 默认联网的云端产品
- 以高拟真“人格扮演”为第一目标的项目

---

## 3. 核心约束

### 3.1 隐私约束
- 默认假设部署环境可以完全离线
- 默认不依赖公网服务
- 默认不上传原始家族资料到云端
- 不自动接入任何在线 API
- 如需外部服务，必须设计为明确可选、默认关闭的插件能力

### 3.2 数据约束
- 原始资料默认保留在本地
- 数据导入主要通过本地文件或安全介质完成
- 不实现联网抓取
- 不实现自动同步

### 3.3 生成约束
- 所有问答与人格交互应尽量基于现有资料
- 回答应支持来源展示或证据等级
- 必须能够区分：
  - 直接引用
  - 资料综合
  - 约束推断
  - 纪念性生成

### 3.4 工程约束
- 一次只处理一个明确任务
- 不进行未经要求的大规模重构
- 不擅自替换技术栈
- 不引入与当前目标无关的复杂工程设施
- 不为“未来可能需要”而提前实现复杂能力

---

## 4. 当前开发环境约束

### 后端
- 使用现有 Conda Python 3.10 环境
- Python 版本：3.10.x
- 当前基础依赖：
  - fastapi
  - uvicorn
  - sqlalchemy
  - pydantic
  - pytest
  - python-multipart
  - aiofiles

### 前端
- Node.js 18.x
- npm 9.x
- 前端预计使用：
  - Vue 3
  - TypeScript
  - Vite

### 当前阶段
- 以本地开发为主
- 暂不要求 Docker
- 暂不要求 pnpm / yarn
- 暂不接入云模型或外部在线服务

---

## 5. 当前技术选型

### 后端
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite（MVP 默认数据库）

### 前端
- Vue 3
- TypeScript
- Vite
- UI 组件库可后续确定，当前无需擅自引入复杂依赖

### 数据与检索
- 当前阶段仅需为后续检索能力预留结构
- 不在第一批任务中实现复杂向量检索或 LLM 管线

---

## 6. 当前阶段目标（MVP 起步）

当前阶段只做以下事情：

1. 初始化后端工程骨架
2. 初始化前端工程骨架
3. 定义核心数据模型
4. 实现人物管理基础 API
5. 支持最基础的本地文本资料导入
6. 为后续记忆片段和检索能力预留结构

当前阶段暂不做：

- 复杂权限系统
- 数字人格高级逻辑
- 语音克隆
- 多模态自动解析
- 外部模型接入
- 联网同步
- 复杂部署编排

---

## 7. 核心数据对象（第一版）

第一版建议围绕以下核心实体建模：

### Person
用于表示家族人物。

建议字段：
- id
- name
- display_name
- aliases
- birth_date
- death_date
- bio
- tags
- privacy_level
- created_at
- updated_at

### Relationship
用于表示人物关系。

建议字段：
- id
- from_person_id
- to_person_id
- relation_type
- note
- confidence
- created_at
- updated_at

### Event
用于表示人物事件或家庭事件。

建议字段：
- id
- title
- description
- event_type
- start_date
- end_date
- created_at
- updated_at

### Artifact
用于表示原始资料。

建议字段：
- id
- artifact_type
- title
- file_path
- original_filename
- source_kind
- owner_person_id
- created_time
- imported_time
- privacy_level

### MemorySegment
用于表示切分后的记忆片段。

建议字段：
- id
- artifact_id
- person_id
- content
- summary
- source_type
- timestamp
- evidence_level
- privacy_level

---

## 8. 目录结构约束

建议遵循以下后端目录结构：

backend/
- app/
  - main.py
  - api/
  - core/
  - models/
  - schemas/
  - services/
  - repositories/
  - imports/
  - retrieval/
  - persona/
  - utils/

Codex 在当前阶段应尽量保持结构清晰，但不要引入过度设计。

---

## 9. 编码要求

- 使用清晰、可维护的模块划分
- 核心函数添加类型标注
- 保持命名清晰
- 避免硬编码路径
- 使用配置集中管理
- 所有 API 应有明确输入输出 schema
- 适当添加基础测试
- 注释应简洁，避免无意义注释

---

## 10. 任务执行输出要求

Codex 在执行每个任务时，应按如下格式输出：

### 在编码前
1. 说明本次将修改哪些文件
2. 说明本次任务的实现思路
3. 明确哪些内容不在本次任务范围内

### 在编码后
1. 列出实际修改的文件
2. 说明如何运行
3. 说明如何测试
4. 说明未完成项或后续建议
5. 不要擅自扩展任务边界

---

## 11. 第一批任务优先级

优先级从高到低如下：

1. 初始化 FastAPI 后端骨架
2. 增加基础配置管理
3. 定义核心数据模型
4. 实现 Person CRUD
5. 实现基础文本导入接口
6. 为后续 MemorySegment 预留切块结构

---

## 12. 明确禁止事项

当前阶段禁止以下行为：

- 默认接入任何外部联网服务
- 擅自引入复杂微服务架构
- 擅自引入消息队列
- 擅自引入大型 DevOps 工具链
- 擅自加入 Docker 强依赖
- 擅自实现云同步
- 擅自引入与当前任务无关的第三方重依赖
- 擅自重命名核心项目结构
- 擅自把项目目标改为“AI 复活”或类似叙事

---

## 13. 当前推荐的第一条 Codex 任务

建议首先执行以下任务：

**任务名称：初始化 FastAPI 后端骨架**

任务要求：
- 仅修改 backend 目录相关内容
- 创建最小可运行 FastAPI 项目结构
- 提供 `GET /health` 接口
- 提供清晰的本地启动方式
- 暂不实现数据库逻辑
- 暂不实现业务实体
- 暂不修改 frontend