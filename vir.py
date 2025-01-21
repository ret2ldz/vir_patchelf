#!/usr/bin/env python3
import argparse
import subprocess
import re
import os

def get_elf_architecture(elf_path):
    """ Check if the ELF file is 32-bit or 64-bit """
    try:
        result = subprocess.run(["file", elf_path], capture_output=True, text=True, check=True)
        # Check the output for 32-bit or 64-bit
        if "32-bit" in result.stdout:
            return "i386"
        elif "64-bit" in result.stdout:
            return "amd64"
        else:
            print("Could not determine architecture.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error checking ELF architecture: {e}")
        return None

def get_glibc_version(libc_path):
    result = subprocess.run(["strings", libc_path], capture_output=True, text=True)
    
    # find the version of libc
    match = re.search(r'Ubuntu GLIBC (\d+\.\d+-\d+ubuntu[\d\.]+)', result.stdout)
    
    if match:
        return match.group(1)  # return version
    else:
        return None

def call_glibc_all_in_one(version):
    """ Call glibc_all_in_one to download the specified version """
    try:
        original_dir = os.getcwd()
        # Change to the directory containing glibc_all_in_one scripts
        os.chdir("./glibc")  # Enter the glibc_all_in_one directory
        
        # Run 'cat list' to get the list of available versions
        result = subprocess.run(["cat", "list"], capture_output=True, text=True, check=True)
        available_versions = result.stdout.splitlines()  # Get the list of available versions
        
        # Check if the desired version is in the 'list'
        if version in available_versions:
            print(f"Version {version} found in 'list'. Proceeding to download...")
            download_command = f"./download {version}"  # Run the download command for the specified version
            subprocess.run(download_command, shell=True, check=True)
            print(f"Successfully downloaded glibc version {version}")
            return True
        else:
            # If version is not in 'list', check 'old' for available versions
            print(f"Version {version} not found in 'list'. Checking 'old_list'...")
            result_old = subprocess.run(["cat", "old_list"], capture_output=True, text=True, check=True)
            old_versions = result_old.stdout.splitlines()  # Get the list of old versions
            
            if version in old_versions:
                print(f"Version {version} found in 'old_list'. Proceeding to download...")
                download_command = f"./download {version}"  # Run the download command for the specified version
                subprocess.run(download_command, shell=True, check=True)
                print(f"Successfully downloaded glibc version {version}")
                os.chdir(original_dir) 
                return True
            else:
                print(f"Version {version} not found in either 'list' or 'old_list'.")
                return False
    except subprocess.CalledProcessError as e:
        print(f"Failed to download glibc version: {e}")
        return False
def get_ld_path(version):
    match = re.match(r"(\d+\.\d+)", version)
    if match:
        main_version = match.group(1)  
        ld_path = f"./glibc/libs/{version}/ld-{main_version}.so"
        return ld_path
    else:
        print(f"Error: Failed to extract main version from {version}")
    return None

def set_patchelf(elf_file, ld_version_path):
    """ 使用 patchelf 修改 ELF 文件的 RPATH 和动态链接器 """
    try:
        # 构建 patchelf 命令
        patchelf_command = [
            "patchelf", 
            "--set-rpath", ".",  # set rpath
            "--set-interpreter", ld_version_path,  # set-interpreter
            elf_file  # ELF path
        ]
        original_dir = os.getcwd()
        print(original_dir)
        os.chdir("..")
        print(f"Running: {' '.join(patchelf_command)}")
        result = subprocess.run(patchelf_command, capture_output=True, text=True, check=True)

        # success
        print(f"Successfully set interpreter and rpath for {elf_file}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error during patchelf execution: {e.stderr}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Automated pwn vir tools ")
    parser.add_argument("libc", type=str, help="/path/to/libc.so.6")
    parser.add_argument("elf", type=str, help="/path/to/target ELF file")
    args = parser.parse_args()

    arch = get_elf_architecture(args.elf)
    print(f"this is a {arch} file")
    # get the libc versions
    version = get_glibc_version(args.libc)
    version += "_"
    version += arch
    if version:
        print(f"the libc version is : {version}")
    else:
        print("Could not find the GLIBC version.")
    call_glibc_all_in_one(version)
    ld_path = get_ld_path(version)
    print(ld_path)
    set_patchelf(args.elf, ld_path)
    print("DONE!")

if __name__ == "__main__":
    main()
