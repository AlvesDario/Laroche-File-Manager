import sys, base64

def help():
    print("usage: b64.py <command> [<arg1>] [<arg2>]\n\tencode\tEncode a file to another file.\n\tdecode\tDecode a file to another file.")


def encod(entrada, saida):
    encoded_string=""
    with open(entrada, "rb") as originalFile:
        encoded_string = base64.b64encode(originalFile.read())
        originalFile.close()
    with open(saida, "wb") as resultFile:
        resultFile.write(encoded_string)
    print("encoded sucessfuly!")

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
