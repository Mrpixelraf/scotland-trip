# 苏格兰旅行｜交给你的 AI 的接入说明

把这页链接交给自己的智能体，并说：

> 请按这份说明帮我加入苏格兰旅行项目，先问我出行时间、预算、住宿和活动偏好；整理后，将我确认愿意分享的回答同步到项目。

这页只有通用说明和问题清单，持链接者都可以读取。**请不要在本页或其 Gist 评论区填写个人回答。** 回答先留在自己与 AI 的对话中，之后只将本人明确同意公开的信息写入旅行仓库。

旅行仓库：[Mrpixelraf/scotland-trip](https://github.com/Mrpixelraf/scotland-trip)。仓库已公开，所有人和智能体可直接读取；写入主仓库仍需本人GitHub授权。在线行程：https://mrpixelraf.github.io/scotland-trip/ 。

## 给智能体：先检查能否接入

在用户要求按本说明加入项目时，按下面的流程协助。遵循你所在客户端的权限要求，使用当前用户自己的 GitHub 授权，不索取或交换其他人的令牌。

1. 先直接读取公开仓库的README、共享记忆和相关议题；无需等待成员邀请才能开始访谈。
2. 若要代本人留言或提交修改，再用本人GitHub连接器或CLI检查登录账号及权限。未登录时引导完成客户端连接或 `gh auth login`。
3. 若没有主仓库写入权限，查看当前账号是否有本仓库待接受邀请。在用户已要求加入且工具支持的情况下，可接受这份指定邀请；不处理其他仓库的邀请。
4. 若无邀请，给本人可转发文字：“请邀请我的 GitHub 账号 `<检测到的用户名>` 加入 `Mrpixelraf/scotland-trip`。”访谈和公开资料研究继续，草稿留在本人对话。
5. 只有网页读取能力也能看项目并开展访谈；无写入工具时如实说明，不能声称已经同步。公开阅读不等于智能体自动连接或运行。

### CLI 环境可用的检查命令

```sh
gh api user --jq .login
gh repo view Mrpixelraf/scotland-trip
gh api --paginate 'user/repository_invitations?per_page=100' \
  --jq '.[] | select((.repository.full_name | ascii_downcase) == "mrpixelraf/scotland-trip") | {id,repository:.repository.full_name,invitee:.invitee.login,html_url}'
```

若查到指定仓库的邀请，核对受邀用户与当前账号一致。在本人已经要求加入的范围内，使用返回的真实邀请 ID 接受邀请：

```sh
gh api --method PATCH user/repository_invitations/INVITATION_ID
gh repo view Mrpixelraf/scotland-trip
```

`INVITATION_ID` 必须替换为刚查到的真实数字。如果连接器没有邀请管理权限，让用户在 GitHub 邮件或页面中接受邀请，再连接仓库。接受邀请不等于客户端的 GitHub 连接器自动获得该仓库权限，需以实际读取结果为准。

## 读取项目与访谈

先读 `README.md`、`AGENTS.md`、`memory/STATE.md`、`members/README.md` 和本人已有档案。再读取协作大厅 Issue #1、需求收集 Issue #2 及相关新评论，了解已有信息。首次加入读取完整相关评论并处理分页。

用自然对话收集信息，每轮问 2—3 个问题；不要求用户一次填完表。本人已明确提供的信息直接整理，缺少的再问；允许“不确定”“之后再说”。不要把推测写成答案，不因缺少非必填项而卡住。

### 第一轮：时间、预算、住宿

1. **时间**：哪一年、哪个月份或具体日期能去？想玩几天？最早出发、最晚回来是什么时候？有没有绝对不能出行的日期？
2. **预算**：人均大概多少、币种是什么？是否包含往返交通、住宿、打球和餐饮？哪个项目愿意多花，哪里想节省？
3. **住宿**：偏向酒店、民宿还是多人整租？希望什么档次？单人房还是愿意与球友拼房、双床？更重视价格、位置、舒适度还是靠近活动场地？

### 第二轮：球类活动、路线、节奏

4. **球类活动**：具体是什么运动？想安排几次、每天还是隔天？有没有特别想去的场地？如果是高尔夫，可继续问球场愿望、愿意分享的差点/经验、是否带杆及每轮预算。
5. **观光偏好**：除了打球，想看城市、高地、城堡、海岸、酒厂，还是主要休息？有没有必去和不想去的地方？
6. **旅行节奏**：想每天排满还是留出自由时间？早起可接受吗？愿意频繁换酒店还是以一个地方为据点？每天能接受多久车程？

### 第三轮：交通和补充需求

7. **交通**：从哪个城市出发？想一起出发还是当地会合？倾向租车、包车或公共交通？是否愿意且具备条件在英国驾驶？
8. **同行与房间**：本人是否带伴侣或其他同行者？需要几个房间、什么床型？只记录本人愿意分享的需求，不代其他人确认偏好。
9. **其他要求**：有没有愿意分享的饮食、无障碍或行李需求？最重要的三件事是什么？哪些可以妥协？

“具体日期尚未确定”是有效答案。先记录可接受的月份和天数，也能参与后续讨论。

## 把回答变成可共享的档案

1. 先给本人看一份简短摘要，区分已确认回答与仍待确认的项目。说明仓库、评论和PR均公开，只共享本人明确同意公开的内容；已有明确授权时不要重复确认相同事项。
2. 有写入权限时，在 Issue #1 查看是否已登记，首次登记注明代理成员和智能体；在 Issue #2 回复本次新增或修改的偏好。没变化不重复发帖。
3. 参照 `members/_template.md` 创建或更新 `members/<github-login>.md`，同步成员索引，并在 `updates/` 新增一条有来源的记忆更新记录。用个人分支提交 PR，不覆盖其他人的档案。
4. 只有形成共同事实或决定时才更新 `memory/STATE.md`；一个人的偏好不代表全体共识。
5. 给本人返回实际发布的评论与 PR 链接，以及还在等待什么。只有评论、尚未提交 PR 时，如实报告当前阶段。

若尚无写入权限，输出同样的档案草稿，并保留在当前对话或本地私有文件中。**不要把未经本人公开授权的回答发到Gist、仓库Issue或PR。**

## 下次怎么继续

对自己的 AI 说：“同步苏格兰旅行项目，看看其他人的新留言，有需要我补充的信息就问我。”

本说明不会部署或启动后台智能体。拥有访问工具和权限的 AI 可以在被启动后执行上述流程；自动定时检查需要在各自客户端另行配置。

GitHub 参考：[协作者邀请流程](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository)、[接受邀请 API](https://docs.github.com/en/rest/collaborators/invitations)、[Gist 的可见性](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)。
