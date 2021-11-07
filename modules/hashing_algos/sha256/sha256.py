from hashlib import sha256
from memory_profiler import memory_usage


class RunSha256:
    def __init__(self, data_stream):
        self.string = data_stream

    def run(self):
        return sha256(self.string)


if __name__ == "__main__":
    print(max(memory_usage(RunSha256(b'n6QTx9GqJ79FqfhfnBVF2E2AvI1vpBgBySM1iJ89KNG1foPXI5YKBBgw7dIjJeXNrU33XCJlEWhUmN29KXdcfl3PIGY3BwaeED1tLkPqjdpHwQGmNSYxl3GrgrA22hJBOKUueT6Th4qsY2Ttg2ztZWwKsUI17qAbbv1vnOu3TMUgMGjU0EleB637W40FM1tTf19Vbrmd9thVjNiCbRmPFicp7GmhI8g2LMqBmEZ6eyt28vY6bmOhOcnCcwXcerN02zPh2uHlLgPxP8BSGE05hl8OJ1f0rz2Vtw9JVZk9TbS1pgv1HykHoqI25rswweL7ysEyGdplyDbnGnNfBwNJsQwPlMCMukjIoMN8MculZplnYbIirR7zDfUIEdumiER47DT5GunZZAZqmweLHRCfY5Gl5lwkAg2ZNcHbFWxBmfnjcIPMQOMXOY0jaxjrGnRNs1tkWLEysFIDfBwzdgS4e28BdUILH8EqJzThQy0h0H8wtTLnD').run)))
