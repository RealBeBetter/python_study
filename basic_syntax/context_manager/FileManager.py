class FileManager:
    def __init__(self, name, mode):
        print("calling __init__ method")
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("calling __enter__ method")
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, *args):
        print("calling __exit__ method")
        if self.file:
            self.file.close()
        for arg in args:
            print("arg: argType:{}, argVal:{}".format(type(arg), arg))
        return True


with FileManager('test.txt', "w") as f:
    print("ready to write file")
    f.write("hello, world!")
    raise Exception('exception raised').with_traceback(None)

# calling __init__ method
# calling __enter__ method
# ready to write file
# calling __exit__ method
# arg: argType:<class 'type'>, argVal:<class 'Exception'>
# arg: argType:<class 'Exception'>, argVal:exception raised
# arg: argType:<class 'traceback'>, argVal:<traceback object at 0x000001EBAD931380>
