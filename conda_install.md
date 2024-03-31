# Miniconda使用教程

## 安装Miniconda

首先，访问[Miniconda官网](https://docs.conda.io/en/latest/miniconda.html)下载适合您操作系统的安装程序。

### Windows

在Windows上，下载`.exe`文件并双击运行安装程序。安装过程中，根据指示选择安装路径和配置选项。

### macOS和Linux

在macOS或Linux上，使用终端窗口。首先，通过`cd`命令导航到包含下载的安装脚本的目录。然后，运行以下命令：

```bash
bash Miniconda3-latest-MacOSX-x86_64.sh  # macOS
bash Miniconda3-latest-Linux-x86_64.sh   # Linux
```

按照屏幕上的指示完成安装过程。

## 基本Conda命令

### 查看Conda版本

```bash
conda --version
```

### 获取帮助

```bash
conda --help
```

### 管理Conda环境

**创建环境**：

```bash
conda create --name myenv python=3.8
```

**激活环境**：

```bash
conda activate myenv
```

**退出环境**：

```bash
conda deactivate
```

**查看所有环境**：

```bash
conda env list
```

或

```bash
conda info --envs
```

**删除环境**：

```bash
conda env remove --name myenv
```

### 管理包

**安装包**：

```bash
conda install numpy
```

安装指定版本的包：

```bash
conda install numpy=1.18
```

**更新包**：

```bash
conda update numpy
```

**卸载包**：

```bash
conda remove numpy
```

**查看已安装的包**：

```bash
conda list
```

### 通过`environment.yml`安装环境

首先，创建一个`environment.yml`文件，内容如下：

```yaml
name: myenv
dependencies:
  - numpy=1.18
  - pandas
  - python=3.8
```

然后，使用以下命令创建环境：

```bash
conda env create -f environment.yml
```

### 清理Conda

```bash
conda clean --all
```

### 关于仓库给出的yaml与文档中的yml不一样的解释

在处理Conda环境文件时，您可能会遇到两种文件扩展名：`.yml`和`.yaml`。实际上，这两种扩展名在功能上没有区别。它们都被用来表示YAML（YAML Ain't Markup Language）格式的文件，这是一种用于配置文件和数据交换的人类可读的数据序列化标准。Conda环境文件使用YAML格式来定义环境的名称、包含的包及其版本等信息。

尽管`.yml`和`.yaml`在技术上可以互换使用，但在Conda文档和社区中，`.yml`扩展名更为常见。这种偏好主要是由于历史原因和个人习惯决定的。在早期，`.yml`是更常见的扩展名，但随着时间的推移，官方YAML网站和规范开始推荐使用`.yaml`作为标准扩展名，以更清楚地表明文件格式。

### 编写Conda环境文件

无论您选择`.yml`还是`.yaml`作为文件扩展名，编写环境文件的方式都是相同的。以下是一个示例环境文件`environment.yaml`（或`environment.yml`），定义了一个名为`myenv`的环境，包含了`numpy`和`pandas`两个包，以及指定的Python版本：

```yaml
name: myenv
dependencies:
  - python=3.8
  - numpy=1.18
  - pandas
```

### 使用环境文件

要使用这个环境文件创建Conda环境，您可以运行以下命令：

```bash
conda env create -f environment.yml
```

或者，如果您的文件名为`environment.yaml`：

```bash
conda env create -f environment.yaml
```

Conda将解析该文件并创建一个包含所有指定包和版本的环境。

### 总结

`.yml`和`.yaml`扩展名在功能上没有区别，都可以用来创建和管理Conda环境文件。选择哪一个主要取决于个人偏好或项目规范。在编写和使用这些文件时，最重要的是保持一致性，以避免混淆。
