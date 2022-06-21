import pymeow
from ReadWriteMemory import ReadWriteMemory
import time

hl2 = pymeow.process_by_name("hl2.exe")
rwm = ReadWriteMemory()
process = rwm.get_process_by_name('hl2.exe')
process.open()

clinetDLL = hl2['modules']['client.dll']['baseaddr']
vgui2DLL = hl2['modules']['vgui2.dll']['baseaddr']


while True:
    attack = process.get_pointer(clinetDLL+0x000F761C, offsets=[0x4, ])
    cross = process.get_pointer(vgui2DLL+0x0006C8D4, offsets=[0x120, ])
    if pymeow.read_int(hl2, cross) in range(1, 64):
        pymeow.write_int(hl2, attack, 5)
        time.sleep(0.1)
        pymeow.write_int(hl2, attack, 4)

