# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容自行完成
def main()：
    input_file = 'random_int.py'
    output_file = 'random_int_uppercase.py'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        def replace_word(match):
            word = match.group(0)
            if word in reserved_words:
                return word
            return word.upper()
        converted_content = re.sub(r'\b[a-zA-Z_]\w*\b', replace_word, content)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(converted_content)
        
        print(f"处理完成！结果已保存到 {output_file}")
        
    except FileNotFoundError:
        print(f"错误：找不到文件 {input_file}")
        # 创建示例文件
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write('import random\ndef get_random(min_val=1, max_val=100):\n    return random.randint(min_val, max_val)\n\nresult = get_random()\nprint("随机数:", result)')
        print("已创建示例文件，请重新运行程序")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()
