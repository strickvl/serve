import os
import platform
import sys

nvidia_smi_cmd = {'Windows': 'nvidia-smi.exe',
                         'Darwin': 'nvidia-smi',
                         'Linux': 'nvidia-smi'}

def is_gpu_instance():
    return os.system(nvidia_smi_cmd[platform.system()]) == 0

def is_conda_build_env():
    return os.system("conda-build") == 0

def is_conda_env():
    return os.system("conda") == 0


def check_python_version():
    req_version = (3, 6)
    cur_version = sys.version_info

    if (
        cur_version.major != req_version[0]
        or cur_version.minor < req_version[1]
    ):
        print(f"System version{str(cur_version)}")
        print("TorchServe supports Python 3.6 and higher only. Please upgrade")
        exit(1)