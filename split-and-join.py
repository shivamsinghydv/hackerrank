def split_and_join(line):
    # write your code here
    linout = line.split(" ")
    newline = "-".join(linout)
    return newline
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
