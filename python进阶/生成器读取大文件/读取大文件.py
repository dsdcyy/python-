# def my_read_lines(file, delimiter):
#     buf = ''
#     while True:
#         while delimiter in buf:
#             pos = buf.index(delimiter)
#             yield buf[:pos]
#             buf = buf[pos + len(delimiter):]
#         chunk = f.read(4096)
#         if not chunk:
#             yield buf
#             break
#         buf += chunk
#
#
# with open('test.txt', 'r', encoding='utf-8') as f:
#     for line in my_read_lines(f, '|'):
#         print(line)

class Readfile(object):
    """
    说明:适用于一行内容特别长且有特定分隔内容的使用场景。
    filename:输入文件
    delimiter:分行读取分隔符
    """

    def __init__(self, filename, delimiter):
        self.filename = filename
        self.delimiter = delimiter

    def __read(self, f):
        # 读取的文件内容
        buf = ''
        # 一值循环直到文件被读取完毕
        while True:

            while self.delimiter in buf:
                # 判断分隔符在本次buf中的索引位置
                pos = buf.index(self.delimiter)
                # 返回分隔符前的读取内容
                yield buf[:pos]
                # 从新赋值buf内容至
                buf = buf[pos + len(self.delimiter):]
                # print('buf2:', buf)
            # 每次循环读取的字节数
            chunk = f.read(10)
            # 判断chunk是否为空，为空则文件读取完毕，可以结束while循环
            if not chunk:
                # 将本次buf返回
                yield buf
                break
            buf += chunk
            # print('buf:', buf)

    def print_line(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            for line in self.__read(f):
                print(line)

    def save_file(self, output_filename):
        """Save the split file to work directory"""
        with open(self.filename, 'r', encoding='utf-8') as f, open(output_filename, 'w', encoding='utf-8') as f2:
            for line in self.__read(f):
                f2.write(line + "\n")


if __name__ == '__main__':
    read = Readfile('test.txt', '|')
    # read.print_line()
    read.save_file('test_out.txt')
