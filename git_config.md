在配置Git时使用的用户名和邮箱确实应该与您的GitHub账户信息相匹配。这样做可以确保您的Git提交正确地与您的GitHub账户关联。

---

# GitHub注册教程
```
Copyright 2024 Pixiu

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

1. 访问 [GitHub官网](https://github.com/).
2. 点击右上角的"Sign up"按钮。
3. 输入您的用户信息：
    - **用户名**：选择一个独特的用户名，其他GitHub用户将通过这个用户名识别您。
    - **邮箱地址**：输入一个有效的邮箱地址，GitHub将发送验证邮件到这个地址。
    - **密码**：创建一个强密码用于GitHub账户。
4. 验证您的账户。
5. 选择一个订阅计划，您可以从免费和各种付费计划中选择。
6. 完成设置后，检查您的邮箱，并点击验证邮件中的链接来验证您的GitHub账户。



## 安装Git

### Windows

1. 下载Git的安装程序从 [Git官网](https://git-scm.com/download/win)。
2. 运行下载的安装程序，并按照指示完成安装。

### macOS

使用Homebrew安装Git：

```bash
brew install git
```

### Linux

使用包管理器安装Git，例如，在Ubuntu上：

```bash
sudo apt-get update
sudo apt-get install git
```

## 配置Git

配置用户信息（替换`Your Name`为你的GitHub用户名 `your.email@example.com`为你的GitHub注册邮箱）：

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```
## 以下确保在初次安装时候应该正确的内容
```
git config --global init.defaultBranch main
git config credential.helper
```

## 配置Git代理

如果您需要通过代理服务器连接到互联网，可以配置Git使用代理：

```bash
git config --global http.proxy 'http://proxyserver:port'
git config --global https.proxy 'https://proxyserver:port'
```

### 关于git代理的详细解释

#### 1. 代理服务器

代理服务器是一种网络服务，允许客户端通过它发送请求到其他服务器。它作为客户端和外部服务器之间的中介，可以提供多种功能，包括内容缓存、访问控制、以及通过隐藏客户端真实IP地址提高安全性等。

#### 2. 配置Git使用HTTP代理

```bash
git config --global http.proxy 'http://proxyserver:port'
```

这条命令设置Git使用HTTP协议的代理服务器。其中：

- `http.proxy`：是Git配置项，指示Git使用HTTP代理。
- `'http://proxyserver:port'`：应该替换为您的代理服务器的地址和端口。例如，如果您的代理服务器地址是`proxy.example.com`，端口是`8080`，那么您应该输入`http://proxy.example.com:8080`。

#### 3. 配置Git使用HTTPS代理

```bash
git config --global https.proxy 'https://proxyserver:port'
```

这条命令设置Git使用HTTPS协议的代理服务器。配置方式与HTTP代理相同，但适用于使用HTTPS协议的通讯。

#### 4. `--global`选项

- `--global`选项意味着这个代理配置是全局有效的，会应用到当前用户的所有Git仓库上。如果您只想为特定的仓库配置代理，可以在仓库的根目录下运行相同的命令，但不加`--global`选项。

#### 5. 移除代理配置

如果您想要取消代理设置，可以使用以下命令：

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

这些命令会从您的Git配置中移除HTTP和HTTPS代理设置。

#### 总结

通过适当配置代理，可以帮助处于特定网络环境中的用户正常使用Git进行远程仓库的操作，包括克隆、推送、拉取等。这是一个在特定情况下解决网络访问问题的有效方法。

如果你使用的是clash那么请将git与clash配置保持一致

## 创建SSH密钥

1. 打开终端或命令提示符。
2. 输入以下命令，替换`your.email@example.com`为您的GitHub邮箱地址：

```bash
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
```
你也可以通过下面这种方式创建另一种密钥，但是以下的操作需要微调
```bash
ssh-keygen -t ed25519 -C "1831768457@qq.com"
```

3. 当提示“Enter a file in which to save the key”时，按`Enter`键接受默认文件位置。输入密码建议为空直接按几次回车，否则以后使用会一直提示输入密码


## 绑定SSH密钥到GitHub

1. 在终端中，输入以下命令将SSH密钥复制到剪贴板：

    - Windows:

    ```bash
    clip < ~/.ssh/id_rsa.pub
    ```

    - macOS:

    ```bash
    pbcopy < ~/.ssh/id_rsa.pub
    ```

    - Linux (需要安装xclip)：

    ```bash
    xclip -sel clip < ~/.ssh/id_rsa.pub
    ```
或者在C盘用户文件夹中找到你的用户名点进去的.ssh文件夹，打开ssh密钥

2. 登录到您的GitHub账户，进入Settings > SSH and GPG keys > New SSH key。
3. 在"Title"字段中，输入描述性名称。在"Key"字段中，粘贴您的密钥。
4. 点击“Add SSH key”。

## 通过HTTPS测试SSH连接
GitHub支持通过HTTPS端口443进行SSH连接。这对于在某些网络环境下，标准SSH端口22被阻塞的情况特别有用。使用以下命令测试SSH连接：
```
ssh -T -p 443 git@ssh.github.com
```

## 使用Git Clone

使用SSH URL克隆仓库：

```bash
git clone ssh_url_of_repository
```

将`ssh_url_of_repository`替换为仓库的SSH URL。

## 使用VSCode打开文件夹

1. 打开VSCode。
2. 选择File > Open Folder，然后选择克隆的仓库文件夹。

# 使用VSCode进行Git操作

在VSCode中，您可以利用内置的图形用户界面进行Git操作，而不需要使用命令行。这些操作包括提交更改、拉取远程仓库的更新、推送本地更改到远程仓库等。
记得打开vscode的自动拉取

## 克隆仓库

1. 在VSCode中，打开命令面板（`Ctrl+Shift+P`或`Cmd+Shift+P`）。
2. 输入`Git: Clone`，选择此命令。
3. 输入仓库的SSH或HTTPS URL，然后按`Enter`。
4. 选择一个本地目录存储克隆的仓库。
5. 克隆完成后，VSCode会提示您打开克隆的仓库。

## 拉取最新更改

1. 打开VSCode中的源代码管理面板（SCM）（侧边栏的第三个图标或`Ctrl+Shift+G` `Cmd+Shift+G`）。
2. 点击“...”更多操作按钮，选择“拉取”从当前分支的上游拉取最新更改。

## 创建提交

1. 在源代码管理面板（SCM），您会看到所有未提交的更改。
2. 选择文件并点击“+”将其添加到暂存区。
3. 在提交消息框中输入提交信息。
4. 点击勾选图标提交更改到您的本地仓库。

## 推送更改到远程仓库

1. 在源代码管理面板，点击“...”更多操作按钮。
2. 选择“推送”将本地更改推送到远程仓库。

## 合并分支

1. 在源代码管理面板，点击“...”更多操作按钮。
2. 选择“分支”然后“合并分支…”。
3. 选择要合并进当前分支的分支。





# git如何提交空文件夹
在Git中，空文件夹本身是不会被跟踪或提交到仓库的。这是因为Git是基于文件的版本控制系统，它跟踪文件的变化，而不是文件夹。如果你想在版本控制中保持一个空的文件夹结构，你需要在这些空文件夹中添加一个文件。最常见的做法是添加一个名为`.gitkeep`的空文件。`.gitkeep`并不是Git的官方文件，但它是一个被广泛接受的约定，用来允许空文件夹被提交到仓库。

以下是如何解决VSCode中空文件夹无法提交的问题的步骤：

### 1. 在空文件夹中创建`.gitkeep`文件

你可以在每个需要保留的空文件夹中手动创建一个`.gitkeep`文件。这可以通过VSCode的文件浏览器或使用命令行来完成。

#### 使用VSCode:

1. 在VSCode的文件浏览器中，右击空文件夹。
2. 选择"新建文件"。
3. 命名文件为`.gitkeep`。

#### 使用命令行:

如果你更喜欢使用命令行，可以打开终端（在VSCode中，你可以使用`Ctrl+``或是通过菜单`视图` > `终端`打开），然后使用`touch`命令在每个空文件夹中创建`.gitkeep`文件，如下所示：

```bash
touch path/to/your/empty-folder/.gitkeep
```

确保将`path/to/your/empty-folder/`替换成实际的文件夹路径。

### 2. 提交`.gitkeep`文件

创建了`.gitkeep`文件后，你就可以使用Git的常规流程来添加和提交这些文件了，这样空文件夹就会被保留在版本控制中。

```bash
git add .
git commit -m "Add .gitkeep files to keep empty folders"
git push
```

### 注意

- `.gitkeep`文件只是一个约定，它本身对Git没有任何特殊意义。Git只是因为这个文件存在而允许文件夹被包含进版本控制。
- 另一种常见的做法是使用`.gitignore`文件排除不需要的文件，但请注意，`.gitignore`用于忽略那些你不希望提交的文件，而不是用来保留空文件夹。
- 如果你的空文件夹是为了将来添加文件，那么只需在添加了实际文件后提交即可，无需使用`.gitkeep`。

通过这种方式，你就可以在使用VSCode和Git时保持空文件夹的结构了。
