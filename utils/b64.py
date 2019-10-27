import sys, base64, os, math

MEMORY_MAX = 15
MEMORY_MAX_MB = MEMORY_MAX * 1048576

def help():
    print("usage: b64.py <command> [<arg1>] [<arg2>]\n\tencode\tEncode a file to another file.\n\tdecode\tDecode a file to another file.")

def printPercentage(atual, fim):
    status = atual/fim
    sys.stdout.write('\r')
    sys.stdout.write(f'{math.floor(status*100)}% {atual}/{fim}')
    sys.stdout.flush()

def encod(entrada, saida):
    encoded_string=""
    originalFile = open(entrada, "rb")
    iterations = math.ceil(os.stat(sys.argv[2]).st_size/MEMORY_MAX_MB)
    print(f'you will have {iterations} iterations')
    for i in range(0,iterations):
        originalFile.seek(i*MEMORY_MAX_MB)
        encoded_string = originalFile.read(MEMORY_MAX_MB)
        resultFile = open(saida+str(i), "wb")
        resultFile.write(encoded_string)
        resultFile.close()
        printPercentage(i,iterations)
    originalFile.close()
    print("all files encoded sucessfuly!")

def decod(entrada, saida):
    encoded_string=""
    with open(entrada, "rb") as codedFile:
        encoded_string = base64.b64decode(codedFile.read())
    with open(saida, "wb") as outputFile:
        outputFile.write(encoded_string)
    print("decoded sucessfuly!")


if sys.argv[1] == "encode":
    encod(sys.argv[2], sys.argv[3])
    sys.exit(0)
elif sys.argv[1] == "decode":
    decod(sys.argv[2], sys.argv[3])
    sys.exit(0)
