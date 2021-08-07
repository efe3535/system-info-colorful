import platform
import distro
from bicim import *
import getpass

os = " ".join(distro.linux_distribution(full_distribution_name=False)).capitalize()
system = platform.system()
kernel_version = platform.release()
# username = platform.uname() Shows computer name instead of username. 
username = getpass.getuser()

print(f"Merhaba, {kirmizi} {username} {sıfır}\n{mavi}bu işletim sistemini: {os},{sıfır}\n{pembe}bu çekirdeği: {system},{sıfır}\n{yesil}bu çekirdek versiyonunu: {kernel_version}, {sıfır}\nkullanıyor olmalısın.")
