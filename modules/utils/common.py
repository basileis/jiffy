import hashlib

def get_sha224_hex_digest(string):
    """Returns the hexdigest of the string"""
    h = hashlib.new('sha224')
    h.update(string)
    return h.hexdigest()

if __name__ == '__main__':
    print get_sha224_hex_digest('bhupesh is the dev')
