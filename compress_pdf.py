import sys
import os
import subprocess
import shutil
import tempfile

def get_ghostscript_path():
    """获取系统中 Ghostscript 的执行路径"""
    if os.name == 'nt':
        # Windows 系统可能的执行文件名
        for cmd in ['gswin64c', 'gswin32c']:
            if shutil.which(cmd):
                return cmd
        return None
    else:
        # macOS/Linux
        return 'gs' if shutil.which('gs') else None

def compress_pdf(input_path):
    gs_cmd = get_ghostscript_path()
    if not gs_cmd:
        print("错误: 未找到 Ghostscript。请确保已安装并将其添加到了系统环境变量中。")
        sys.exit(1)

    original_size = os.path.getsize(input_path)
    
    # 创建安全的临时文件
    fd, temp_path = tempfile.mkstemp(suffix='.pdf')
    os.close(fd)

    try:
        # 使用 /ebook 预设 (150 dpi)，在清晰度和体积间取得最佳平衡
        subprocess.run([
            gs_cmd,
            '-sDEVICE=pdfwrite',
            '-dCompatibilityLevel=1.4',
            '-dPDFSETTINGS=/ebook',
            '-dNOPAUSE',
            '-dQUIET',
            '-dBATCH',
            f'-sOutputFile={temp_path}',
            input_path
        ], check=True)

        new_size = os.path.getsize(temp_path)
        
        # 覆盖原文件
        shutil.move(temp_path, input_path)
        
        # 计算并打印压缩效果
        mb_original = original_size / (1024 * 1024)
        mb_new = new_size / (1024 * 1024)
        ratio = (1 - (new_size / original_size)) * 100 if original_size > 0 else 0
        
        print(f"✅ 成功压缩: {os.path.basename(input_path)}")
        print(f"   体积变化: {mb_original:.2f} MB -> {mb_new:.2f} MB (减少了 {ratio:.1f}%)")
        return True

    except subprocess.CalledProcessError:
        print(f"❌ 压缩失败 (进程错误): {input_path}")
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return False
    except Exception as e:
        print(f"❌ 发生意外错误 [{input_path}]: {e}")
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return False

if __name__ == "__main__":
    # 获取命令行传入的所有文件参数
    files = sys.argv[1:]
    
    if not files:
        print("用法: python compress_pdf.py <file1.pdf> <file2.pdf> ...")
        sys.exit(1)

    print(f"找到 {len(files)} 个文件，开始处理...\n" + "-"*40)
    
    for pdf_file in files:
        if os.path.isfile(pdf_file) and pdf_file.lower().endswith('.pdf'):
            compress_pdf(pdf_file)
        else:
            print(f"⚠️ 跳过无效文件或非 PDF 文件: {pdf_file}")
            
    print("-" * 40 + "\n处理完成！")