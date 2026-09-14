# 把自己的智能体接入旅行项目

仓库地址：<https://github.com/Mrpixelraf/scotland-trip>。

## 成员先做一次

1. 使用自己的 GitHub 账号。私有仓库需由管理者邀请，接受邀请后才能访问。
2. 在智能体的运行环境连接 GitHub：可以使用客户端提供的 GitHub 连接器，也可以使用 Git 和 GitHub CLI。
3. 让连接器能读取仓库、Issue、评论和 PR。要发言需具备对应写入权限；要更新共享文件需能创建分支和 PR。只有网页搜索或没有登录状态的智能体不能读取私有仓库。
4. 告诉自己的智能体：你是谁、允许分享哪些旅行偏好、是否授权它在项目中留言并提交草稿。

每个人使用自己的授权，不交换令牌。GitHub 读取仓库文件与读取议题评论是不同操作；克隆仓库不会把评论一起下载。

## 可以直接发给自己 AI 的提示词

```text
请接入我的苏格兰旅行协作项目：
https://github.com/Mrpixelraf/scotland-trip

我的 GitHub 用户名是：<填写你的用户名>。
我授权你读取项目，并在本次旅行范围内代表我讨论方案、回复议题、提交共享记忆更新 PR。
可分享的个人偏好仅限：<填写日期、预算、活动等你愿意分享的信息>。

先读取 README.md、AGENTS.md、memory/STATE.md、members/README.md，
再读取与我有关的成员档案、决策、Issues/PRs 及完整相关评论。
告诉我当前共识、尚未确定的问题和需要我提供的信息。
我给出信息后，用它更新我的档案，按项目规则在对应议题回复并提交 PR。
不要复制我无关的私人记忆；不要替其他成员确认偏好，也不要把建议写成已确认决定。
如当前环境无法访问仓库或发表评论，明确说明缺少的能力，不假装已接入。
```

请先替换尖括号内容，并按自己的意愿调整授权范围。

## 使用 GitHub CLI

以下命令使用本机已登录的账号。先确认账号正确；未登录时运行 `gh auth login`。

```sh
gh api user --jq .login
gh repo view Mrpixelraf/scotland-trip
gh repo clone Mrpixelraf/scotland-trip
cd scotland-trip
```

读取议题和 PR 索引，注意分页；Issues API 也会包含 PR，下列过滤器只保留议题：

```sh
gh api --paginate 'repos/Mrpixelraf/scotland-trip/issues?state=open&per_page=100' \
  --jq '.[] | select(.pull_request == null) | {number,title,body,html_url,updated_at}'
gh api --paginate 'repos/Mrpixelraf/scotland-trip/pulls?state=open&per_page=100' \
  --jq '.[] | {number,title,body,html_url,updated_at}'
```

对相关议题读取正文和评论。下面的 `123` 只是示例，替换为真实编号：

```sh
gh issue view 123 --repo Mrpixelraf/scotland-trip --comments
gh api --paginate 'repos/Mrpixelraf/scotland-trip/issues/123/comments?per_page=100' \
  --jq '.[] | {id,user:.user.login,body,html_url,created_at,updated_at}'
```

上下文涉及已关闭议题时读取其链接；历史检索将 `state=open` 改为 `state=all`。PR 还需读取审阅意见、行内评论及 diff，不能仅依赖上述 Issue 评论端点。首次接入没有同步记录时读取所有相关评论；有可靠游标后再按新增或编辑的评论做增量同步。

按 `templates/agent-comment.md` 写好本地 `.local/reply.md` 后，在本人授权范围内发送：

```sh
gh issue comment 123 --repo Mrpixelraf/scotland-trip --body-file .local/reply.md
```

不要通过 shell 拼接未经处理的评论正文。使用连接器时，同样把正文作为结构化参数传入。

## 更新记忆

在干净且同步过的 `main` 上创建个人分支，修改相关档案、规划和独立更新记录。用真实的用户名、主题和唯一后缀替换示例：

```sh
git switch main
git pull --ff-only
git switch -c agent/YOUR_LOGIN/travel-preferences-UNIQUE_SUFFIX
```

修改后检查 `git diff`，仅暂存本次相关文件，再提交、推送此分支。写好本地 `.local/pr.md` 后创建 PR：

```sh
gh pr create --repo Mrpixelraf/scotland-trip --base main \
  --title '更新出行偏好' --body-file .local/pr.md
```

可用 GitHub 连接器的“创建分支 → 编辑文件 → 创建 PR”执行同一流程。本人偏好由本人确认，共同行程由受影响成员明确确认；保留确认来源。仓库管理者或获授权成员合并后，其他智能体下次同步即可读取。

## 自动讨论的边界

当前没有配置定时任务、Webhook、GitHub Actions 调用模型或后台机器人。留言是一条持久消息，并不保证对方智能体正在运行。

按需使用时，对自己的智能体说：“同步苏格兰旅行项目，读取新留言，处理与我有关的问题。”

以后需要自动跟进，可由每位成员在自己的环境明确授权定时检查。调度任务先读最新内容，只在有新事实、请求或决定时回复；本地记录评论 ID、编辑时间和已经发出的响应，避免重复处理；没有变化保持安静。不要建立智能体无限互相回复的循环。

## 常见情况

- 链接显示 404：确认登录账号、是否接受私有仓库邀请、连接器是否有该仓库权限。
- 能读不能写：确认账号和连接器具有相应的 Issues / Contents / Pull requests 权限。
- 另一位智能体没回复：先让该成员启动智能体同步，或检查其已经授权的调度任务。
- GitHub 连接器只支持查询：先整理建议交给本人，或使用支持写入的 CLI 环境；不要声称已发布。

GitHub 官方参考：[GitHub CLI](https://cli.github.com/manual/)、[议题评论](https://cli.github.com/manual/gh_issue_comment)、[讨论区](https://docs.github.com/en/discussions/quickstart)。
