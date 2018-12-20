import hashlib

def my_hash(new_temp):
    m = hashlib.sha256()
    m.update(new_temp)
    # 获取sign
    sign = m.hexdigest()
    return sign