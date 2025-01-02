# 1. 初始化Git仓库

git init

# 2. 克隆远程仓库

git clone `<repository-url>`

# 3. 查看仓库的当前状态

git status

# 4. 添加文件到暂存区

git add `<file>`  # 添加指定文件
git add .       # 添加所有文件

# 5. 提交更改

git commit -m "commit message"  # 使用提交信息进行提交

# 6. 查看提交历史

git log

# 7. 创建新的分支

git branch `<branch-name>`

# 8. 切换到指定分支

git checkout `<branch-name>`

# 9. 创建并切换到新的分支

git checkout -b `<branch-name>`

# 10. 合并分支

git merge `<branch-name>`

# 11. 删除分支

git branch -d `<branch-name>`

# 12. 查看远程仓库

git remote -v

# 13. 添加远程仓库

git remote add origin `<repository-url>`

# 14. 推送本地分支到远程仓库

git push origin `<branch-name>`

# 15. 拉取远程仓库的更新

git pull origin `<branch-name>`

# 16. 查看差异

git diff `<file>`  # 查看指定文件的差异
git diff         # 查看所有文件的差异

# 17. 暂存当前工作进度

git stash

# 18. 恢复之前的暂存进度

git stash pop

# 19. 重置文件或提交

git reset `<file>`         # 取消暂存区中的文件
git reset --hard `<commit>`  # 回退到指定提交

# 20. 标签管理

git tag `<tag-name>`             # 创建标签
git push origin `<tag-name>`     # 推送标签
