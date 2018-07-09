#AES-demo

import base64
from Crypto.Cipher import AES

'''
采用AES对称加密算法
'''
# str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return value.encode(encoding='UTF-8')  # 返回bytes

#加密方法
def encrypt(value):
    # 秘钥
    key = '123456'
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    #先进行aes加密
    encrypt_aes = aes.encrypt(add_to_16(value))
    #用base64转成字符串形式
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    return encrypted_text

#解密方法
def decrypt(value):
    # 秘钥
    key = '123456'
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    #优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(value.encode(encoding='utf-8'))
    #
    decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8') # 执行解密密并转码返回str
    return decrypted_text

if __name__ == '__main__':
    #encrypt("我是中国人！")
    print(decrypt(encrypt("aaaa是")))
