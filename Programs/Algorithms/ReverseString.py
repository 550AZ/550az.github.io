# 写一个函数实现字符串反转

def reverse(content):
    if len(content) <= 1:
        return content
    return reverse(content[1:]) + content[0]

def main():
    str1 = "Hello world!"
    print(str1)
    str2 = reverse(str1)
    print(str2)

if __name__ == '__main__':
    main()