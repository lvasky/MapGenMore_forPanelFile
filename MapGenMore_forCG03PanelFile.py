import re

# p_width的值
p_width = 16

# 1. 实现按行分割字符串
def split_string_by_newline(input_string):
    return input_string.splitlines()

# 2. 对每一行中的数字加上 p_width，并返回处理后的新字符串列表
def process_lines(input_lines, offset, icmax):
    updated_lines = []
    for i, line in enumerate(input_lines):
        # 对每一行中的数字加上 p_width
        line = re.sub(r'\((\d{3}),(\d{3})\)', lambda m: f"({int(m.group(1)):03},{int(m.group(2)) + offset:03})", line)
        
        # 替换芯片名
        line = re.sub(r'([A-Za-z0-9_]+_CHIP)(\d+)', lambda m: f"{m.group(1)}{int(m.group(2)) + icmax}", line)
        
        # 替换每行中的 "data1_chipN"
        line = re.sub(r'data1_chip(\d)', lambda m: f"data1_chip{i + icmax}", line)
        
        updated_lines.append(line)
    
    return updated_lines

# 提取括号中的第二个数字
def calculate_p_width(input_string):
    # 使用正则表达式提取所有的 "(xxx,yyy)" 中的 yyy
    matches = re.findall(r'\(\d{3},(\d{3})\)', input_string)
    # 转换为整数列表并找到最大值
    return max(int(num) for num in matches) + 1

########################################################################
# 灯板map表
src_str = ""
print("请输入灯板map表: (输入空行结束)")

while True:
    line = input()
    if line == "":  # 如果输入为空行，则结束输入
        break
    src_str += line + "\n"

# 灯板级联数量
panel_num = int(input("请输入灯板级联数量:"))

lines = split_string_by_newline(src_str)
p_width = calculate_p_width(src_str)
p_icmax = len(lines)   # 灯板芯片数量为列表数量
# 计算 p_width
print("灯板芯片数量为列表数量是" + str(p_icmax))

# 处理每个灯板级联的情况
result = lines
newlines = lines
for _ in range(panel_num - 1):
    newlines = process_lines(newlines, p_width, p_icmax)
    result.extend(newlines)

# 把结果打印出来
for line in result:
    print(line)
