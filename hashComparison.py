import hashlib

file1 = 'first.txt'
file2 = 'second.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(file1,'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(file2,'rb').read())

if hash1.digest() != hash2.digest():
    print(f'The file: {file1} is different of {file2}')
    print(f'The hash of {file1} is:  ',hash1.hexdigest())
    print(f'The hash of {file2} is: ', hash2.hexdigest())

else:
    print(f'The file: {file1} is equal to {file2}')