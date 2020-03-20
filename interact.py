def request(options):
    res = input(options)
    if res.isdigit():
        return int(res)
    else:
        return 0
