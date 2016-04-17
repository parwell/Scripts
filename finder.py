# Finds all files of an extension in a directory

import os

class Finder(object):
    def __init__(self):
        print('Finder.')

    def __str__(self):
        return 'Extension Finder'

    def getInfo(self):
        ext = input('Enter extension to search (.flac is default): ')
        if not ext:
            ext = '.flac'
        direct = input('Enter directory to search (/Users/Pawel/Music is default): ')
        if not direct:
            direct = '/Users/Pawel/Music'
        return ext, direct

    
    def find(self):
        ext, direct = self.getInfo()
        results = []
        for root, dirs, files in os.walk(direct):
            for file in files:
                if file.endswith(ext):
                    results.append(str(root)[len(direct)+1:])
                    break
        return results


    def run(self):
        results = self.find()
        with open('finder.txt', 'w') as f:
            for result in results:
                f.write(result + '\n')
                print(result)
        print('Results saved to finder.txt')
        input('Enter to exit.')


if __name__ == '__main__':
    f = Finder()
    f.run()