def fun(s):
    # consider the case where there isn't either @, then the split function will throw error.
    freq_attherate = 0
    freq_dot = 0
    for i in range(len(s)):
        if (s[i] == "@"):
            freq_attherate += 1

    if (freq_attherate != 1):
        return False
    user, domain = s.split("@")

    if (len(user) > 20 or len(user) <= 0):
        return False

    if (len(domain) <= 0):
        return False
    return True


def filter_mail(emails):
    return list(filter(fun, sorted(emails)))

list1 = ['sara@scaler.com','brian-23@scaler.com','brute_54@scaler.com']
print(filter_mail(list1))
