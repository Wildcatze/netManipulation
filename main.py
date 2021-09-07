import os
import subprocess
import sys

def main():
    print('Setting work directory to: ', os.getcwd())
    with open('output.txt', 'w') as f:
        output = (os.getcwd() + '\output.txt')
        print("The newly created output file path is: " + output)

    cmd = ("cd " + os.getcwd())
    cmd = "ping -n 1 8.8.8.8 > output.txt"
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
    print(p.stderr.read(1))

main()

