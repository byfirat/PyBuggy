#Python ile Pil yüzdesi öğrenme
import psutil
from plyer import notification
import time
pil = psutil.sensors_battery()
while(True)
   yuzde=pil.percent
   notification.notify(
       title="Pil yüzdesi",
       message=str(yuzde)"% Kalan pil",
       timeout=10
   )
   time.sleep(60*60)
   continue