n=int(input())
guerreiros=[int(t) for t in input().split()]

guerreiros.sort(reverse = True)

print (' '.join(map(str, guerreiros)))