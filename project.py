import hashlib
# # print(hashlib.algorithms_available)
# write a program in python to generate MD5 of string data 
name=input("Please Enter your name :\n")
print("MD5 ALGORITHM EXAMPLE:")
hashvalue=hashlib.md5(name.encode())
print("Output:")
print("The hexadecimal equivalent of hash:\n",hashvalue.hexdigest())
print("-------------------------------------------------------------")
# write a program in python to generate hashes of string data using any 3 algorithm
print("SHA-1 ALGORITHM EXAMPLE:")
hashvalue=hashlib.sha1(name.encode())
print("Output:")
print("The hexadecimal equivalent of hash:\n",hashvalue.hexdigest())
print("-------------------------------------------------------------")
print("SHA-224 ALGORITHM EXAMPLE:")
hashvalue=hashlib.sha224(name.encode())
print("Output:")
print("The hexadecimal equivalent of hash:\n",hashvalue.hexdigest())
print("-------------------------------------------------------------")
print("SHA-512 ALGORITHM EXAMPLE:")
hashvalue=hashlib.sha512(name.encode())
print("Output:")
print("The hexadecimal equivalent of hash:\n",hashvalue.hexdigest())
