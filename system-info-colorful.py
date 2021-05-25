import platform
from bicim import *

os = " ".join(platform.linux_distribution()).capitalize()
system = platform.system()
kernel_version = platform.release()
username = platform.uname()

print(f"Merhaba, {kirmizi} {username.node} {sıfır}\n{mavi}bu işletim sistemini: {os},{sıfır}\n{pembe}bu çekirdeği: {system},{sıfır}\n{yesil}bu çekirdek versiyonunu: {kernel_version}, {sıfır}\nkullanıyor olmalısın.")
