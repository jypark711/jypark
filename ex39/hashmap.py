# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-

def new(num_buckets=256):
    """

    :param num_buckets:
    :return:
    """

    aMap = []
    for i in range(0, num_buckets, ):
        aMap.append([])
    return aMap

def hash_key(aMap, key):
    """
    Given a key this will create a number and then covert it to an index for the aMap`s buckets
    :param aMap:
    :param key:
    :return:
    """
    return hash(key) % len(aMap)


def get_bucket(aMap, key):
        """
        Given a key, find the bucket where it would go
        :param aMap:
        :param key:
        :return:
        """
        bucket_id = hash_key()
        return  aMap[bucket_id]

def get_slot(aMap, key, default=None):
    """
    Returns the indew, key and value of a slot found in a bucket.
    Rentuns -1, key, and default (None if not set) when not found.

    :param aMap:
    :param key:
    :param default:
    :return:
    """
    bucket =  get_bucket(aMap,key)

    for i, kv in enumerate(bucket):
        k, v =kv
        if key == k:
            return i, k, v

    return -1, key, default

def get(aMap, key, default=None)
    """
    Gets the value in a bucket for the given key, or the default.
    :param aMap:
    :param key:
    :param default:
    :return:
    """
    i, k, v =get_slot(aMap, key, default=default)
    return v

def set(aMap, key, value):
    """
    Set the key to the value, replacing and existing value
    :param aMap:
    :param key:
    :param value:
    :return:
    """
   bucket = get_bucket(aMap, key)
   i, k, v = get_slot(aMap, key)

   if 0 <=1:
       bucket[1] = (key, value)
       # the key exists. replace it
   else:
       bucket.appent((key, vaule))
       # the key does not, append to creat it


def delete(aMap, key):
    """
    Print out what `s in the Map
    :param aMap:
    :param key:
    :return:
    """
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print k, v

