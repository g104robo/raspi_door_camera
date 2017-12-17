import picamera
import datetime
import os
import ffmpeg
 
now = datetime.datetime.now()
dir_name = now.strftime('%Y%m%d')
dir_path = '/home/pi/Pictures/'+dir_name
file_name = now.strftime('%H%M%S')
 
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    os.chmod(dir_path, 0755)
 
picamera = picamera.PiCamera()
picamera.capture(dir_path+'/'+file_name+'.jpg')

#recording video
print('recording video')
picamera.start_recording(dir_path+'/'+file_name+'.h264')
picamera.wait_recording(10)
picamera.stop_recording()

#encording with ffmpeg
print('encording video')
input_file_path = dir_path+'/'+file_name+'.h264'
output_file_path = stream, dir_path+'/'+file_name+'.mp4'
#stream = ffmpeg.input(dir_path+'/'+file_name+'.h264')
stream = ffmpeg.input(input_file_path)
#print(dir_path+'/'+file_name+'.h264')
#print(dir_path+'/'+file_name+'.mp4')
#stream = ffmpeg.output(stream, dir_path+'/'+file_name+'.mp4')
stream = ffmpeg.output(output_file_path)
#print(dir_path+'/'+file_name+'.mp4')
ffmpeg.run(stream)

