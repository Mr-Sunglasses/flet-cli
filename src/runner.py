import os

def runner():
    if os.path.isdir('src'):
        try:
            os.system('pip3 install -r requirements.txt')
            os.chdir('src')
            os.system('python3 main.py')
        except:
            print("ERROR")
    else:
        print('No src folder found')

if __name__ == '__main__':
    runner()