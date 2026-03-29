#!/bin/bash

# 1. 扫描当前目录下所有的 .pdf 和 .html 文件
# 使用 find 命令，-o 表示 "或者"，-type f 确保只找文件
files=$(find . -maxdepth 1 -name "*.pdf" -o -name "*.html")

# 检查是否存在相关文件
if [ -z "$files" ]; then
    echo "未发现任何 pdf 或 html 文件。"
    exit 0
fi

echo "即将清理以下文件："
echo "-------------------"
# 2. 输出文件名
echo "$files"
echo "-------------------"

# 3. 打印提示并等待输入
read -p "请输入 y 确认删除，按其他任意键取消: " confirm

# 4. 判断输入并执行删除
if [ "$confirm" == "y" ] || [ "$confirm" == "Y" ]; then
    # 直接将变量传递给 rm 执行
    rm $files
    echo "清理完成。"
else
    echo "操作已取消，未删除任何文件。"
fi