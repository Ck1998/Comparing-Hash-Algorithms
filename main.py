from modules.utils.generator import generate_key_array, generate_rand_bytes
from json import dumps
from datetime import datetime
from uuid import uuid4
from modules.hashing_algos.sha256.sha256 import RunSha256
from modules.hashing_algos.sha512.sha512 import RunSha512
from modules.hashing_algos.md5.md5 import RunMd5
from modules.hashing_algos.blake.blake import RunBlake
from memory_profiler import memory_usage
from psutil import Process
import matplotlib.pyplot as plt
from threading import Thread
from os import makedirs
import pandas as pd


class Driver:
    def __init__(self):
        # Data storing dictionary
        self.RUN = {}
        self.KEYS = []
        self.SHA256_T = []
        self.SHA512_T = []
        self.MD5_T = []
        self.BLAKE_T = []
        self.SHA256_M = []
        self.SHA512_M = []
        self.MD5_M = []
        self.BLAKE_M = []
        self.SHA256_C = []
        self.SHA512_C = []
        self.MD5_C = []
        self.BLAKE_C = []
        self.RUN_DATE = datetime.now().strftime('%Y-%m-%d')
        self.RUN_UUID = str(uuid4()).split('-')[0]
        self.SAVE_PATH = f"output/{self.RUN_DATE}/{self.RUN_UUID}"

    def make_save_dir(self):
        makedirs(name=self.SAVE_PATH, exist_ok=True)

    @staticmethod
    def run_sha256(string):
        obj = RunSha256(data_stream=string).run
        # Running time
        st = datetime.now()
        obj()
        et = datetime.now()
        rt = (et - st).microseconds
        # Memory Used
        mm = max(memory_usage(obj))

        # CPU Usage
        t = Thread(target=obj)
        cu = (Process(t.start()).cpu_percent()) * 100
        t.join()

        return rt, mm, cu

    @staticmethod
    def run_sha512(string):
        obj = RunSha512(data_stream=string).run
        # Running time
        st = datetime.now()
        obj()
        et = datetime.now()
        rt = (et - st).microseconds
        # Memory Used
        mm = max(memory_usage(obj))

        # CPU Usage
        t = Thread(target=obj)
        cu = (Process(t.start()).cpu_percent()) * 100
        t.join()

        return rt, mm, cu

    @staticmethod
    def run_md5(string):
        obj = RunMd5(data_stream=string).run
        # Run time
        st = datetime.now()
        obj()
        et = datetime.now()
        rt = (et - st).microseconds

        # Memory Used
        mm = max(memory_usage(obj))

        # CPU Usage
        t = Thread(target=obj)
        cu = (Process(t.start()).cpu_percent()) * 100
        t.join()

        return rt, mm, cu

    @staticmethod
    def run_blake(string):
        obj = RunBlake(data_stream=string).run
        # Run time
        st = datetime.now()
        obj()
        et = datetime.now()
        rt = (et - st).microseconds
        # Memory Used
        mm = max(memory_usage(obj))

        # CPU Usage
        t = Thread(target=obj)
        cu = (Process(t.start()).cpu_percent()) * 100
        t.join()

        return rt, mm, cu

    def runtime_vs_is(self):
        plt.plot(self.KEYS, self.SHA256_T, "-o")
        plt.plot(self.KEYS, self.SHA512_T, "-o")
        plt.plot(self.KEYS, self.MD5_T, "-o")
        plt.plot(self.KEYS, self.BLAKE_T, "-o")
        plt.savefig(f"{self.SAVE_PATH}/runtime_vs_input_size_{self.RUN_DATE}_{self.RUN_UUID}.png")

    def memory_vs_is(self):
        plt.plot(self.KEYS, self.SHA256_M, "-o")
        plt.plot(self.KEYS, self.SHA512_M, "-o")
        plt.plot(self.KEYS, self.MD5_M, "-o")
        plt.plot(self.KEYS, self.BLAKE_M, "-o")
        plt.savefig(f"{self.SAVE_PATH}/memory_vs_input_size_{self.RUN_DATE}_{self.RUN_UUID}.png")

    def cpu_vs_is(self):
        plt.plot(self.KEYS, self.SHA256_C, "-o")
        plt.plot(self.KEYS, self.SHA512_C, "-o")
        plt.plot(self.KEYS, self.MD5_C, "-o")
        plt.plot(self.KEYS, self.BLAKE_C, "-o")
        plt.savefig(f"{self.SAVE_PATH}/cpu_vs_input_size_{self.RUN_DATE}_{self.RUN_UUID}.png")

    def sort_arrays(self):
        for variable, value in vars(self).items():
            if type(value) == list:
                self.__setattr__(name=variable, value=sorted(value))

    def save_graphs(self):
        self.runtime_vs_is()
        self.memory_vs_is()
        self.cpu_vs_is()

    def save_run_to_json(self):
        with open(f"{self.SAVE_PATH}/hash_run_{self.RUN_DATE}_{self.RUN_UUID}.json", "w+") as wo:
            wo.write(dumps(self.RUN, indent=4))

    def save_to_excel(self):
        df_t = pd.DataFrame(list(zip(self.KEYS, self.SHA256_T, self.SHA512_T, self.MD5_T, self.BLAKE_T)),
                            columns=["Input Size", "SHA 256 Runtime", "SHA 512 Runtime",
                                     "MD5 Runtime", "BLAKE Runtime"])

        df_m = pd.DataFrame(list(zip(self.KEYS, self.SHA256_M, self.SHA512_M, self.MD5_M, self.BLAKE_M)),
                            columns=["Input Size", "SHA 256 Memory Usage", "SHA 512 Memory Usage",
                                     "MD5 Memory Usage", "BLAKE Memory Usage"])

        df_c = pd.DataFrame(list(zip(self.KEYS, self.SHA256_C, self.SHA512_C, self.MD5_C, self.BLAKE_C)),
                            columns=["Input Size", "SHA 256 CPU Usage", "SHA 512 CPU Usage",
                                     "MD5 CPU Usage", "BLAKE CPU Usage"])

        df_t.to_excel(f"{self.SAVE_PATH}/runtime_vs_input_size_{self.RUN_DATE}_{self.RUN_UUID}.xlsx", index=False)
        df_m.to_excel(f"{self.SAVE_PATH}/memory_vs_input_size_{self.RUN_DATE}_{self.RUN_UUID}.xlsx", index=False)
        df_c.to_excel(f"{self.SAVE_PATH}/cpu_vs_input_size_{self.RUN_DATE}_{self.RUN_UUID}.xlsx", index=False)

    def main(self):
        self.make_save_dir()
        test_cases = int(input("[+] Enter number of test cases you want to run - "))
        count = 1
        print(f"[+] Generating {test_cases} key lengths at random")
        self.RUN["test cases"] = test_cases
        self.RUN["Run statistics"] = {}
        key_array = generate_key_array(test_cases)
        for key in key_array:
            print(f"[+] Test case #: {count}")
            print(f"\t[+] Generating {key} sized random bytes string")
            string = bytes(generate_rand_bytes(size=key))

            # SHA 256
            print(f"\t[+] Running Sha256 Algorithm on a {key} sized input")
            sha256_rt, sha256_mm, sha256_cu = self.run_sha256(string)

            # SHA 512
            print(f"\t[+] Running Sha512 Algorithm on a {key} sized input")
            sha512_rt, sha512_mm, sha512_cu = self.run_sha512(string)

            # MD5
            print(f"\t[+] Running MD5 Algorithm on a {key} sized input")
            md5_rt, md5_mm, md5_cu = self.run_md5(string)

            # Blake
            print(f"\t[+] Running Blake Algorithm on a {key} sized input")
            blake_rt, blake_mm, blake_cu = self.run_blake(string)

            # Populating graphing  arrays
            self.KEYS.append(key)

            # SHA 256 Arrays
            self.SHA256_T.append(sha256_rt)
            self.SHA256_M.append(sha256_mm)
            self.SHA256_C.append(sha256_cu)

            # SHA 512 Arrays
            self.SHA512_T.append(sha512_rt)
            self.SHA512_M.append(sha512_mm)
            self.SHA512_C.append(sha512_cu)

            # MD5 Arrays
            self.MD5_T.append(md5_rt)
            self.MD5_M.append(md5_mm)
            self.MD5_C.append(md5_cu)

            # Blake Arrays
            self.BLAKE_T.append(blake_rt)
            self.BLAKE_M.append(blake_mm)
            self.BLAKE_C.append(blake_cu)

            # Adding data to dict
            self.RUN["Run statistics"][count] = {
                "Input size": key,
                "Input": string.decode("utf-8"),
                "SHA 256 Run time": sha256_rt,
                "SHA 256 memory usage": sha256_mm,
                "SHA 256 cpu usage": sha256_cu,
                "SHA 512 Run time": sha512_rt,
                "SHA 512 memory usage": sha512_mm,
                "SHA 512 cpu usage": sha512_cu,
                "MD5 Run time": md5_rt,
                "MD5 memory usage": md5_mm,
                "MD5 cpu usage": md5_cu,
                "Blake Run time": blake_rt,
                "Blake max memory usage": blake_mm,
                "Blake cpu usage": blake_cu,
            }
            count += 1

        # Save graphs
        self.save_graphs()

        # Save to excel
        self.save_to_excel()

        # saving RUN to json
        self.save_run_to_json()


if __name__ == "__main__":
    Driver().main()
