**Git版本控制**

git和svn一个是分布式一个是集中式，集中式中所有的版本数据都存在服务器上，用户需要从中央服务器中下载和上传，并且需要联网；分布式可以直接控制整个项目，用户同步所有版本信息。可以离线提交，在联网时Push到中央服务器

![image-20240719202148861](C:\Users\dragon\AppData\Roaming\Typora\typora-user-images\image-20240719202148861.png)

**git的工作的几个区的基本讲解**

工作区是当前存放工程文件的根目录，日常使用的代码区；暂存区是.git文件中的index文件（并不合适是所有的.git文件） 这里保存的是你通过 `git add` 命令选择纳入下一次提交的文件修改。只有这些文件会被打包成一次提交；本地仓库就是.git文件，执行 `git commit` 后，暂存区中的内容会被保存到本地仓库中，形成一次新的提交。此时，对工作区的其他未暂存修改不会影响这一提交。当你执行 `git push` 时，Git 会把本地仓库的提交推送到远程仓库，而远程仓库中的内容只反映已经提交的内容。因此，如果你在工作区有更改但没有通过 `git add` 添加到暂存区，那么这些更改不会出现在提交中，自然也不会随推送传到远程仓库。

```
git config -l //查看配置
git status //查看git跟踪的文件
git log //显示仓库的提交历史信息
git tag //查看仓库中的所有标签 
git init newrepo//在newrepo目录下生成一个.git目录
git add . //将目录下文件添加暂存区
git commit //将暂存区文件添加到本地git仓库
git push //将本地仓库添加到远程仓库中
git commit -m "消息内容" //提交暂存区中的内容到本地仓库 -m 提交信息
git rm //将文件从暂存区和工作区中删除
git pull //获取最新代码库并自动合并到当前的分支，是fetch、merge的组合操作
git remote //查看远程仓库
```

**分支管理：**

master主分支应该非常稳定，用来发布新版本，一般情况下不允许在上面工作，工作一般情况下在新建的dev分支上工作，工作完后，比如上要发布，或者说dev分支代码稳定后可以合并到主分支master上来。

```
git branch # 列出所有本地分支
git branch -r # 列出所有远程分支
git branch [branch] # 新建一个分支，但依然停留在当前分支
git branch -d [branch] # 删除一个分支
git push origin --delete [branch] # 删除远程origin的分支
git branch -dr [remote/branch] #删除本地对远程分支的引用，不影响远程仓库
git checkout [branch] # 切换到某一个分支
git checkout 文件名 # 回退到之前修改后未提交的文件内容
git checkout -b [branch] # 新建一个分支，并切换到该分支
git merge [branch] # 合并指定分支到当前分支，比其他更加安全
```

**未提交的更改会在分支间保留**，因此在切换分支前最好提交更改，以避免不同分支间的混淆。

**提交更改后再切换分支**，可以确保分支间的隔离，不会将新分支的更改带到主分支。

**解释**：在主分支上创建一个新分支后，切换到新分支上时，在新分支上更改文件后如果不提交到本地仓库或者存到暂存区，这时切换到主分支就会保留更改的信息，所以在新分支上要提交到本地仓库中，然后切换到主分支才不会保留新分支的更改数据

**合并冲突**：主分支和新分支对同一个文件的同一个部分进行了不同的修改，git无法自动合并这些更改，需要人工干预，则打开修改的文件，在某一个分支中手动编辑保留更改的内容，然后添加到暂存区中提交就可以消除了

提交到远程仓库

```
在你想提交的文件目录下运行如下命令，一般是在主文件夹下
git init //初始化仓库
git remote -v //查看所有远程仓库
git remote add origin git@github.com:gsfcv/git_study.git //将一个远程仓库添加到本地仓库，并命名为origin，建立与远程仓库的连接
git remote set-url origin git@github.com:gsfcv/git_study.git //修改现有本地origin和远程仓库url的连接
git add . //数据添加到暂存区
git commit -m "push" //将暂存区修改保留到本地仓库，push自己可改
git push origin master //将本地的master分支内容推送到连接远程仓库的origin服务器中
git remote //查看当前的远程库
```

从远程拉取数据并更新本地仓库(一般用于从拉取同事已经写好的项目分支内容) git pull origin master //直接从orgin获取数据到master分支，可以分为如下两步？

```
git pull origin master //更改仓库内容时要先拉取远程仓库的最新更新， 确保本地仓库是最新的
git fetch origin //默认拉取到orgin/master分支
git merge origin/master //默认从orgin/master分支合并到master
```
