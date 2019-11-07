from mergeJson import mergeJsonFiles
import sys


def main():
	filePath = sys.argv[1]
	baseInFile = sys.argv[2]
	baseOutFile = sys.argv[3]
	maxFileSize = int(sys.argv[4])
	
	mergeJsonFiles().mergeJson(filePath, baseInFile, baseOutFile, maxFileSize)

if __name__ == '__main__':
    main()