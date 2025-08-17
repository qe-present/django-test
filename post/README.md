# 2025-08-17
# Django + MySQL 后端题目

## 题目：构建一个简单的博客系统后端

### 要求：
1. 使用 Django 框架和 MySQL 数据库
2. 实现以下功能：
   - 用户注册、登录和认证
   - 博客文章的创建、读取、更新和删除(CRUD)
   - 文章分类功能
   - 文章评论功能

### 具体任务：

1. **模型设计**：
   - 创建适当的 Django 模型，包括：
     - 用户模型(扩展 Django 的默认用户模型)
     - 文章模型(Article)
     - 分类模型(Category)
     - 评论模型(Comment)
   - 建立正确的模型关系(外键、多对多等)

2. **API 端点**：
   - 实现以下 RESTful API 端点：
     - `POST /api/register/` - 用户注册
     - `POST /api/login/` - 用户登录
     - `GET /api/articles/` - 获取文章列表
     - `POST /api/articles/` - 创建新文章(需要认证)
     - `GET /api/articles/<id>/` - 获取单个文章详情
     - `PUT /api/articles/<id>/` - 更新文章(需要认证且是作者)
     - `DELETE /api/articles/<id>/` - 删除文章(需要认证且是作者)
     - `GET /api/categories/` - 获取所有分类
     - `POST /api/articles/<id>/comments/` - 为文章添加评论(需要认证)
     - `GET /api/articles/<id>/comments/` - 获取文章的所有评论

3. **认证与权限**：
   - 使用 Django REST framework 的认证系统
   - 确保只有登录用户才能创建、更新和删除文章
   - 确保用户只能修改或删除自己创建的文章和评论

4. **数据库优化**：
   - 为常用查询字段添加适当的数据库索引
   - 实现分页功能，避免一次返回过多数据
   - 考虑使用 `select_related` 或 `prefetch_related` 优化查询

5. **额外要求(选做)**：
   - 实现文章搜索功能
   - 添加文章点赞功能
   - 实现简单的推荐系统(如根据分类推荐相关文章)

### 提交要求：
- 完整的 Django 项目代码
- 包含必要的迁移文件
- 提供 API 文档(可以使用 Swagger 或简单的 Markdown 文档)
- 包含一个 `requirements.txt` 文件列出所有依赖
- 提供数据库 schema 设计的简要说明

### 评分标准：
1. 功能完整性(40%)
2. 代码结构与质量(30%)
3. 数据库设计与优化(20%)
4. 文档完整性(10%)

> 提示：可以使用 Django REST framework 来简化 API 开发，确保处理好模型关系和序列化器。
