#crie um programa que recebe o nome de dois aquivo como parametros de linha de comando e que gere um aquivo
# de saida  com as linhas do primeiro e do segundo aquivo.
import sys

def merge_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        for line in f1:
            out.write(line)
        for line in f2:
            out.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python merge_files.py file1.txt file2.txt output.txt")
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file = sys.argv[3]

    merge_files(file1, file2, output_file)
    print(f"Files {file1} and {file2} merged into {output_file}.")