# -*- coding: utf-8 -*-
from huggingface_hub import snapshot_download
import os

MODEL_NAME = "ibm-granite/granite-3.3-2b-instruct"
LOCAL_MODEL_DIR = "./base_model"

if __name__ == "__main__":
    print(f"Downloading model '{MODEL_NAME}' to '{LOCAL_MODEL_DIR}'...")
    os.makedirs(LOCAL_MODEL_DIR, exist_ok=True)
    snapshot_download(
        repo_id=MODEL_NAME,
        local_dir=LOCAL_MODEL_DIR,
        local_dir_use_symlinks=False
    )
    print("Download complete.")
