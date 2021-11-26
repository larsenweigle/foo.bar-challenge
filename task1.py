
def solution(data, n):
    busy_ids = {}
    i = 0
    for i in range(len(data)):
        num = data[i]
        present = num in busy_ids.keys()
        # add num index to dictionary
        if present:
            busy_ids[num] += 1
        else:
            busy_ids[num] = 1

    for key in busy_ids.keys():
        num_jobs = busy_ids.get(key)
        if num_jobs > n:
            for i in range(num_jobs):
                print(key)
                data.remove(key)
    return data
