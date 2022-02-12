max_road = 0
max_high = 0
roads_num = int(input())
for r in range(roads_num):
    tunnels_num = int(input())
    min_tunnel = 0
    for t in range(tunnels_num):
        tunnel = int(input())
        if min_tunnel == 0:
            min_tunnel = tunnel
        else:
            if tunnel < min_tunnel:
                min_tunnel = tunnel
    if min_tunnel > max_high:
        max_high = min_tunnel
        max_road = r + 1

print(max_road, max_high)

# tunnels = [
#     [
#         [
#             int(input())
#         ]
#         for tunnel in range(int(input()))
#     ]
#     for road in range(int(input()))
# ]
