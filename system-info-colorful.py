import platform
import distro
from bicim import *

os = " ".join(distro.linux_distribution(full_distribution_name=False)).capitalize()
system = platform.system()
kernel_version = platform.release()
username = platform.uname()

print(f"Merhaba, {kirmizi} {username.node} {sıfır}\n{mavi}bu işletim sistemini: {os},{sıfır}\n{pembe}bu çekirdeği: {system},{sıfır}\n{yesil}bu çekirdek versiyonunu: {kernel_version}, {sıfır}\nkullanıyor olmalısın.")
