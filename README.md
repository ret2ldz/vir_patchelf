### vir - Automated GLIBC Version Download and Link Tool|vir - 自动化 GLIBC 版本下载和链接工具

#### Introduction|简介

`vir` 是一个用于自动化下载指定版本 GLIBC 并为 ELF 文件设置正确链接的命令行工具。它会根据提供的 `libc.so.6` 文件确定对应的 GLIBC 版本，并从 `glibc-all-in-one` 中自动下载所需版本的 GLIBC 库和 `ld` 文件，然后使用 `patchelf` 工具设置 ELF 文件的解释器和 RPATH。它支持 32 位和 64 位的 ELF 文件，简化了 GLIBC 配置的过程。

`vir` is a command-line tool for automating the download of the specified GLIBC version and setting the correct links for ELF files. It determines the corresponding GLIBC version based on the provided `libc.so.6` file and automatically downloads the required GLIBC libraries and `ld` files from `glibc-all-in-one`. Then, it uses the `patchelf` tool to set the ELF file's interpreter and RPATH. It supports both 32-bit and 64-bit ELF files, streamlining the GLIBC setup process.

#### Features|特性

- 自动检测并下载与 `libc.so.6` 对应的 GLIBC 版本。
- 支持为 ELF 文件设置正确的解释器和 RPATH。
- 支持 32 位与 64 位 ELF 文件。
- 自动从 `glibc-all-in-one` 下载并配置所需的库和 `ld` 文件。
- 简化了 `patchelf` 工具的使用。
- Automatically detects and downloads the GLIBC version corresponding to `libc.so.6`.
- Supports setting the correct interpreter and RPATH for ELF files.
- Supports both 32-bit and 64-bit ELF files.
- Automatically downloads and configures the required libraries and `ld` files from `glibc-all-in-one`.
- Simplifies the use of the `patchelf` tool.

#### Installation|安装

克隆本仓库到本地 | Clone the repository:

```
git clone https://github.com/askdfkd/vir.git
cd vir
```

============================================================

Install and configure the global command using `setup.sh`:

通过 `setup.sh` 安装并配置全局命令:

```
chmod+x setup.sh
./setup.sh
```

<img src="C:\Users\0629\AppData\Roaming\Typora\typora-user-images\image-20250121163031203.png" alt="image-20250121163031203" style="zoom:67%;" />

#### Usage|使用方法

Basic command format:

基本命令格式 :

```
vir ./libc.so.6 ./you_file_names
```

#### EXAMPLE|例子

<img src="C:\Users\0629\Downloads\p1\Screenshot_2025-01-21_04_18_14.png" alt="Screenshot_2025-01-21_04_18_14" style="zoom:80%;" />

#### Contributing|贡献 

欢迎提出问题和贡献代码！如果你有任何建议或发现 bug，欢迎通过 [GitHub issues](https://github.com/your-username/vir/issues) 提交反馈。| Contributions are welcome! If you have any suggestions or find any bugs, feel free to submit feedback via [GitHub issues](https://github.com/your-username/vir/issues).

#### License

MIT License. See the LICENSE file for more detail