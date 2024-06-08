以下是一个详细的安装CUDA和NVIDIA驱动程序的过程，以及可能出现的Bug和对应的解决方法的Markdown文件内容。


# Ubuntu 上安装 CUDA 和 NVIDIA 驱动程序指南

本文档详细介绍了在 Ubuntu 上安装 CUDA 和 NVIDIA 驱动程序的步骤，以及可能出现的问题和对应的解决方法。

## 系统更新

首先，确保系统是最新的。打开终端并运行以下命令：

```bash
sudo apt update
sudo apt upgrade
```

## 安装依赖项

安装 CUDA 和 NVIDIA 驱动程序所需的依赖项：

```bash
sudo apt install build-essential dkms linux-headers-$(uname -r)
```

## 添加 NVIDIA 的官方 PPA

添加 NVIDIA 的官方 PPA 源，以获取最新的驱动程序：

```bash
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
```

## 检查可用的 NVIDIA 驱动程序

检查你可以安装的 NVIDIA 驱动程序：

```bash
ubuntu-drivers devices
```

## 安装 NVIDIA 驱动程序

安装适合你显卡型号的驱动程序（以下命令中的数字是示例，请根据上一步的输出选择合适的版本）：

```bash
sudo apt install nvidia-driver-535
```

## 安装 CUDA

前往 NVIDIA 的 [CUDA 下载页面](https://developer.nvidia.com/cuda-downloads) 并选择相应的 CUDA 版本和 Ubuntu 版本。然后按照页面上的指示下载并安装 CUDA。

假设你下载了一个名为 `cuda-repo-ubuntu2004_11.4.2-1_amd64.deb` 的文件，可以使用以下命令进行安装：

```bash
sudo dpkg -i cuda-repo-ubuntu2004_11.4.2-1_amd64.deb
sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
sudo apt update
sudo apt install cuda
```

## 设置环境变量

添加 CUDA 路径到你的环境变量中。打开 `~/.bashrc` 文件：

```bash
nano ~/.bashrc
```

在文件末尾添加以下内容：

```bash
export PATH=/usr/local/cuda-11.4/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-11.4/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

保存并关闭文件，然后使其生效：

```bash
source ~/.bashrc
```

## 验证安装

重启你的计算机，然后运行以下命令以验证 CUDA 是否安装成功：

```bash
nvcc -V
```

运行以下命令以验证 NVIDIA 驱动程序是否安装成功：

```bash
nvidia-smi
```

## 可能出现的问题和解决方法

### 问题 1: `nvidia-smi` 报错

错误信息：`NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.`

#### 解决方法：

1. **移除现有的 NVIDIA 驱动程序**：

    ```bash
    sudo apt remove --purge '^nvidia-.*'
    sudo apt autoremove
    ```

2. **更新系统和软件包**：

    ```bash
    sudo apt update
    sudo apt upgrade
    ```

3. **重新安装 NVIDIA 驱动程序**：

    ```bash
    sudo apt install nvidia-driver-535
    ```

4. **重建 initramfs（可选）**：

    ```bash
    sudo update-initramfs -u
    ```

5. **禁用 nouveau 驱动**：

    ```bash
    sudo nano /etc/modprobe.d/blacklist-nouveau.conf
    ```

    添加以下内容：

    ```
    blacklist nouveau
    options nouveau modeset=0
    ```

    更新 initramfs：

    ```bash
    sudo update-initramfs -u
    ```

6. **重启系统**：

    ```bash
    sudo reboot
    ```

7. **检查内核模块**：

    ```bash
    sudo modprobe nvidia
    ```

### 问题 2: 内核模块未加载

使用 `lsmod | grep nvidia` 命令检查内核模块是否加载。如果没有输出，表示内核模块未加载。

#### 解决方法：

1. **安装 DKMS 和内核头文件**：

    ```bash
    sudo apt install dkms linux-headers-$(uname -r)
    ```

2. **重新安装 NVIDIA 驱动**：

    ```bash
    sudo apt remove --purge '^nvidia-.*'
    sudo apt install nvidia-driver-535
    ```

3. **重启系统**：

    ```bash
    sudo reboot
    ```

4. **确认禁用 Secure Boot**：

    在 BIOS/UEFI 设置中禁用 Secure Boot。你可以通过以下命令确认其状态：

    ```bash
    mokutil --sb-state
    ```

    确保输出显示 `SecureBoot disabled`。

5. **重新加载 NVIDIA 模块**：

    ```bash
    sudo modprobe nvidia
    ```

6. **验证 NVIDIA 驱动**：

    ```bash
    nvidia-smi
    ```

### 其他可能的问题

1. **检查驱动安装日志**：

    ```bash
    dmesg | grep nvidia
    ```

2. **检查 Xorg 日志**：

    ```bash
    cat /var/log/Xorg.0.log | grep NVIDIA
    ```

通过以上步骤，你应该能够解决驱动程序安装问题。如果仍有问题，可根据系统日志和 Xorg 日志的输出信息以便进一步诊断。
