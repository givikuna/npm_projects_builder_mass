import os
import subprocess

root_directory = '.'

for root, dirs, files in os.walk(root_directory):
    if 'package.json' in files and 'node_modules' not in dirs:
        print(f"Found an npm project in {root}")
        os.chdir(root)

        try:
            print("Running 'npm install'...")
            subprocess.run(['npm', 'install'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running 'npm install': {e}")
            continue

        try:
            print("Running 'npm build'...")
            subprocess.run(['npm', 'run', 'build'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running 'npm build': {e}")
            continue

        print("Completed npm install and build.\n")
