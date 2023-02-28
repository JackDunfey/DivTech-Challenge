N, T = [int(i) for i in input("").split(" ")]
print("NO" if any(t <= 0 for t in (v-T*i for i, v in enumerate(sorted(int(input("")) for i in range(N))))) else "YES")