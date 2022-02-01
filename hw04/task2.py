origin_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# result_list = []
# for i, e in enumerate(origin_list):
#     if origin_list[i-1] < origin_list[i] and i != 0:
#         result_list.append(e)

result_list = [e for i, e in enumerate(origin_list) if origin_list[i-1] < origin_list[i] and i != 0]

print(result_list)
