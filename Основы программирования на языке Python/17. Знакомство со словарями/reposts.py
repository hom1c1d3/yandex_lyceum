posts = {}
n = int(input())

name, views = input().split()[::5]
posts[name] = [int(views), 'origin']
for i in range(n - 1):
    repost = input().split()
    name, author, views = repost[0], repost[4][:-1], int(repost[-1])
    posts[name] = [views, author]
    while author != 'origin':
        posts[author][0] += views
        author = posts[author][1]

print(*map(lambda a: a[0], posts.values()), sep='\n')