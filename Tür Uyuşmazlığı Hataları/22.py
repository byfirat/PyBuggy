#internet hızını ölçme
import speedtest
speed = speedtest.Speedtest()
download_speed = speed.download()
upload_speed = float("speed.upload()")
print(f'The download speed is {download_speed}')
print(f'The uplaod speed is {upload_speed}')