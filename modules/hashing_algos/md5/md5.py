from hashlib import md5


class RunMd5:
    def __init__(self, data_stream):
        self.string = data_stream

    def run(self):
        return md5(self.string)


if __name__ == "__main__":
    RunMd5(b"This is nice").run()
