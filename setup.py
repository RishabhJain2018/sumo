import subprocess

def bash_command(cmd):
    subprocess.Popen(cmd, shell=True, executable='/bin/bash')

bash_command('pip install sumo-api/requirements.txt')
bash_command('pip install sumo-api/.')
