"""
Description

在某重大保障行动中，你作为防守方成员，负责每天处理攻击日志并进行统计和汇报。

每条攻击日志都包含时间戳、攻击类型、攻击次数三种信息，而你需要写一个程序来统计一段时间内某个攻击类型的攻击次数。


Input
第一行有两个数 N 和 M。

N 表示日志行数，M 表示查询次数。

接下来的 N 行是攻击日志，每一行根据顺序依次为时间戳、攻击类型、攻击次数。

再接下来的 M 行是查询，每一行根据顺序依次为查询起始时间、查询终止时间、攻击类型。


Output
输出 M 行，每一行表示该查询所查询到的总攻击次数。
"""
"""
5 3
1575562565 sqli 3
1575562567 xss 10
1575562572 csrf 2
1575562579 sqli 5

0 1575562571 xss
1575562565 1575562579 sqli
1575562565 1575562579 none



"""
"""
10
8
0
"""


def is_cur_pos_ok(log_list_, idx_, start_time_, end_time_):
    if idx_ >= len(log_list_) or idx_ < 0:
        return False
    if not (start_time_ <= log_list_[idx][0] <= end_time_):
        return False
    return True


def bin_find_first_ok_time(log_list_, start_time_, end_time_):
    if not log_list_:
        return -1
    start_idx_ = 0
    end_idx_ = len(log_list_) - 1
    while start_idx_ + 1 < end_idx_:
        if start_idx_ > end_idx_:
            mid = end_idx_ + (start_idx_ - end_time_) // 2
        else:
            mid = start_idx_ + (end_time_ - start_idx_) // 2
        if log_list_[mid][0] > end_time_:
            end_idx_ = mid
        elif log_list_[mid][0] < start_time_:
            start_idx_ = mid
        else:
            end_idx_ = mid
    if is_cur_pos_ok(log_list_, start_idx_, start_time_, end_time_):
        return start_idx_
    if is_cur_pos_ok(log_list_, end_idx_, start_time_, end_time_):
        return end_idx_
    return -1


def bin_find_last_ok_time(log_list_, start_time_, end_time_):
    if not log_list_:
        return -1
    start_idx_ = 0
    end_idx_ = len(log_list_) - 1
    while start_idx_ + 1 < end_idx_:
        if start_idx_ > end_idx_:
            mid = end_idx_ + (start_idx_ - end_time_) // 2
        else:
            mid = start_idx_ + (end_time_ - start_idx_) // 2
        if log_list_[mid][0] > end_time_:
            end_idx_ = mid
        elif log_list_[mid][0] < start_time_:
            start_idx_ = mid
        else:
            start_idx_ = mid
    if is_cur_pos_ok(log_list_, end_idx_, start_time_, end_time_):
        return end_idx_
    if is_cur_pos_ok(log_list_, start_idx_, start_time_, end_time_):
        return start_idx_
    return -1


def is_valid(atk_type_):
    for character in atk_type_:
        if character.isalpha() and character.islower():
            continue
        if character == "_":
            continue
        return False
    return True


first_line = input()

if first_line:
    log_num, query_num = first_line.split()
    log_num = int(log_num)
    query_num = int(query_num)
    log_list = []
    # 初始化log_list
    for _ in range(log_num):
        temp_line = input()
        if not temp_line:
            continue
        time_, atk_type, atk_times = temp_line.split(" ")
        time_ = int(time_)
        atk_times = int(atk_times)
        log_list.append((time_, atk_type, atk_times))

    res = []

    for _ in range(query_num):
        current_query = input()
        if not current_query or not log_list:
            print(0)
            continue
        try:
            query_command_list = current_query.split(" ")
            if len(query_command_list) < 3:
                print(0)
                continue
            if len(query_command_list) > 3:
                print(0)
                continue
            start_time, end_time, query_atk_type = query_command_list[0], query_command_list[1], query_command_list[-1]
            if not is_valid(query_atk_type):
                print(0)
                continue
            start_time = int(start_time)
            end_time = int(end_time)
        except Exception:
            print(0)
            continue
        if start_time > end_time:
            print(0)
            continue
        current_atk_time = 0
        # 二分搜索开始结束idx
        start_idx = bin_find_first_ok_time(log_list, start_time, end_time)
        end_idx = bin_find_last_ok_time(log_list, start_time, end_time)
        if start_idx > end_idx or start_idx == -1 or end_idx == -1:
            print(0)
        # start_idx = 0
        # end_idx = len(log_list) - 1
        for idx in range(start_idx, end_idx + 1):
            log_time, atk_type, atk_times = log_list[idx]
            if start_time <= log_time <= end_time and atk_type == query_atk_type:
                current_atk_time += atk_times
        print(current_atk_time)
