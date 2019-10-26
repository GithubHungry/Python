# from threading import Thread, Lock
# from concurrent.futures import ThreadPoolExecutor

# to_test = [
#     ('1.0.0', '2.0.0'),
#     ('1.0.0', '1.42.0'),
#     ('1.2.0', '1.2.42'),
#     ('1.1.0-alpha', '1.2.0-alpha.1'),
#     ('1.0.1b', '1.0.10-alpha.beta'),
#     ('1.0.0-rc.1', '1.0.0'),
# ]
#
# for version_1, version_2 in to_test:
#     assert version_1 < version_2, 'le failed'
#     assert version_2 > version_1, 'ge failed'
#     assert version_2 != version_1, 'neq failed'

# class Version:
#     def __init__(self, version):
#         pass
#
#
# def main():
#     to_test = [
#         ('1.0.0', '2.0.0'),
#         ('1.0.0', '1.42.0'),
#         ('1.2.0', '1.2.42'),
#         ('1.1.0-alpha', '1.2.0-alpha.1'),
#         ('1.0.1b', '1.0.10-alpha.beta'),
#         ('1.0.0-rc.1', '1.0.0'),
#     ]
#
#     for version_1, version_2 in to_test:
#         assert Version(version_1) < Version(version_2), 'le failed'
#         assert Version(version_2) > Version(version_1), 'ge failed'
#         assert Version(version_2) != Version(version_1), 'neq failed'
#
#
# if __name__ == "__main__":
#     main()

# class Noop:
#     def __new__(cls, *args, **kwargs):
#         print("Creating instance with {} and {}".format(args, kwargs))
#         instance = super().__new__(cls)
#         return instance
#
#     def __init__(self, *args, **kwargs):
#         print("Initializing instance with {} and {}".format(args, kwargs))
#
#
# noop = Noop(42, attr='value')


# a = 0
# mutex = Lock()
#
#
# def function(arg):
#     global a
#     for _ in range(arg):
#         mutex.acquire()
#         a += 1
#         mutex.release()
#
#
# def main():
#     threads = []
#
#     for i in range(5):
#         thread = Thread(target=function, args=(10,))
#         thread.start()
#         threads.append(thread)
#
#     [t.join() for t in threads]
#     print("----------------------", a)  # ???
#
#
# main()

# a = 0
# mutex = Lock()
#
#
# def function(arg):
#     global a
#     for _ in range(arg):
#         mutex.acquire()
#         a += 1
#         mutex.release()
#
#
# def main():
#     with ThreadPoolExecutor(5) as executor:
#         executor.map(function, [100000, 100000, 100000, 100000, 100000])
#     print("----------------------", a)  # ???
#
#
# main()
