import os

# 指定当前目录
current_directory = os.getcwd()

# 创建一个新的TXT文件来汇总内容
output_file_path = os.path.join(current_directory, 'combined_output.txt')

# 打开输出文件
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # 遍历当前目录中的所有文件
    for filename in os.listdir(current_directory):
        # 只处理TXT文件
        if filename.endswith('.txt'):
            file_path = os.path.join(current_directory, filename)
            # 打开并读取TXT文件
            with open(file_path, 'r', encoding='utf-8') as input_file:
                content = input_file.read()
                # 写入输出文件
                output_file.write(f'内容来自文件: {filename}\n')
                output_file.write(content)
                output_file.write('\n\n')  # 分隔不同文件的内容

print(f'所有TXT文件的内容已汇总到 {output_file_path}')
