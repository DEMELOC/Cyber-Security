

msg = input("Please enter your message: ")

key = "abcdefghijklmnopqrstuwxyz0123456789 !"

val = key[:: -1]

e_msg = dict(zip(key, val))
#print(e_msg)

enc_msg = "".join([e_msg[words] for words in msg.lower()])

print((enc_msg))
