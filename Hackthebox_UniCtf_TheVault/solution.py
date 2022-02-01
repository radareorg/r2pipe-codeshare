#!/usr/bin/python3
import r2pipe

#Opens binary with r2pipe in debug mode, and analyzes it
r = r2pipe.open('./vault')

flag = ""

#Enter debug mode and analyze the binary
r.cmd('doo;aaaaa')

#Find the target function where we will be stepping over until we hit the breakpoint
target_func = r.cmd('pdf @ main~[4]~:4')

print("[+] ----------------------------------------------- [+]")
print(f"          Target functions is {target_func}")
print("[+] ----------------------------------------------- [+]")

#Set breakpoint at that target function and step over to find first character 'H'
r.cmd(f'dcu {target_func}')
r.cmd('dso 65')

#Append the character 'H' to the flag
flag += r.cmd('px 6 @ rsp~[4]~:1 | tail -c 2').strip('\n')

#Iterate 24 times to print remaining 24 characters of the flag
for i in range(24):
    r.cmd('dso 45')
    flag += r.cmd('px 20 @ rsp~[3]~:2 | tail -c 2').strip('\n')
print("[+] ----------------------------------------------- [+]")
print("              "+flag)
print("[+] ----------------------------------------------- [+]")

