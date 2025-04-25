import hashlib
from colorama import Fore, Style, init

init(autoreset=True)

def convert_md5_to_int(md5_hash: str) -> int:
    """Chuyển MD5 thành số nguyên (lấy 8 ký tự cuối)"""
    return int(md5_hash[-8:], 16) 

def predict_tai_xiu(md5_hash: str) -> str:
    num = convert_md5_to_int(md5_hash)
    return "TÀI" if num % 2 == 0 else "XỈU"  # Chẵn → Tài, Lẻ → Xỉu

def analyze_md5(md5_hash: str):
    num = convert_md5_to_int(md5_hash)
    prediction = predict_tai_xiu(md5_hash)
    
    color = Fore.GREEN if prediction == "TÀI" else Fore.RED
    
    print(f"\n🔮 {Fore.CYAN}MD5: {md5_hash}")
    print(f"🔢 {Fore.YELLOW}Giá trị: {num:,}")
    print(f"🎯 {color}DỰ ĐOÁN: {prediction} {Style.BRIGHT}{color}← {'🚀' if prediction == 'TÀI' else '💀'}")

# Demo
if __name__ == "__main__":
    print(f"\n{Fore.MAGENTA}🎲 {Style.BRIGHT}TOOL DỰ ĐOÁN TÀI XỈU MD5 {Fore.MAGENTA}🎲")
    print(f"{Fore.WHITE}-------------------------------")
    
    while True:
        md5_input = input(f"\n{Fore.WHITE}Nhập MD5 (hoặc 'exit' để thoát): ").strip()
        
        if md5_input.lower() == "exit":
            print(f"\n{Fore.CYAN}👋 Kết thúc chương trình!")
            break
        
        if len(md5_input) != 32:
            print(f"{Fore.RED}❌ MD5 phải có 32 ký tự!")
            continue
        
        analyze_md5(md5_input)