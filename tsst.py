print("######开始执行网络自动化脚本####")
#最基础的打印：把东西喊出来
print('python 3.7.21')
#字符串（一定要加引号，单双引号都可以）
print('这是一台华为交换机')
print('123')
print(456)
print('如果带引号的10',10)
print('数字运算,比如2的8次方:',2**8)
#数字（千万不要用引号）
device="s5700"
ip="192.168.1.1"
#变量（贴了标签的盒子）
print(f"发现设备：{device},管理ip是:{ip}")
#把变量塞进一句话里面（f-string)
device='s12700'
print(f'刚才那台设备升级了,现在变成了：{device}')
#变量是可以换的！
device='s6700'
interface='g0/0/1'
description='连接交换机'
print(f'配置接口 {interface} 连接交换机{device},状态为：{description}')
devices=['S5700','S12700','S6700','S3200']
#定义设备列表（框）
for device in devices:
    #此时device 依此是s5700,s12700,s6700,s3200
    #注意：print前面有4个空格，表示它在循环里
    print(f'开始登录设备 {device}')
    print(f'开始保存配置 {device}')