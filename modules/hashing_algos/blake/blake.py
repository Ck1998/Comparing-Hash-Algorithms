from hashlib import blake2s


class RunBlake:
    def __init__(self, data_stream):
        self.string = data_stream

    def run(self):
        return blake2s(self.string)


if __name__ == "__main__":
    RunBlake(b"This is nice").run()
