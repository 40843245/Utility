class ListHandler():
    class String():
        @staticmethod
        def EndsWith(src : str, target : list[str]):
            r = [src.endswith(elem) for elem in target]
            return any(r)
if __name__ == '__main__':
    r = ListHandler.String.EndsWith("src.py", [".py",".pym"])
    print(r)
