from hashlib import sha512


class RunSha512:
    def __init__(self, data_stream):
        self.string = data_stream

    def run(self):
        return sha512(self.string)


if __name__ == "__main__":
    RunSha512(b"This is good").run()


