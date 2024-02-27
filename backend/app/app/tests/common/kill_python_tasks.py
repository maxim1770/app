from subprocess import Popen, PIPE

if __name__ == '__main__':
    a = [line.decode('cp866', 'ignore') for line in Popen('tasklist', stdout=PIPE).stdout.readlines()]
    for i in [i_ for i_ in a if 'python.exe' in i_]:
        print(f'taskkill /F /IM {i.split()[1]}')

    # 'taskkill /F /IM {}'
    # В Windows PowerShell
    # taskkill /F /IM 12064
