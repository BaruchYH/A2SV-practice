class Solution:
    def simplifyPath(self, path: str) -> str:
        store = []
        for file in path.split("/"):
            if file:
                if file == ".":
                    continue
                elif file == "..":
                    if store:
                        store.pop()
                    else:
                        continue
                else:
                    store.append(file)
        return "/" + "/".join(store)
