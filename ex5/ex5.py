import subprocess


# define and call function to cut the first 10 seconds of the BBB video (ex1)
def cut_10_init_sec(video, output):
    command = f"ffmpeg -ss 00:00:0.0 -i {video} -c copy -t 00:00:10.0 {output}"
    subprocess.call(command, shell=True)


cut_10_init_sec('BBB.mp4', 'script_cut.mp4')


# create a video with the histogram of the cut video (ex2)
def create_histogram(video, output):
    command = f"ffmpeg -i {video} -vf histogram {output}"
    subprocess.call(command, shell=True)


create_histogram('script_cut.mp4', 'script_histogram.mp4')


# join the cut video and its histogram (ex2)
def join_two_videos(video1, video2, output):
    command = f'ffmpeg -i {video1} -i {video2} -filter_complex "[0:v] setpts=PTS-STARTPTS, scale=qvga [a0];[1:v]setpts=PTS-STARTPTS, scale=qvga [a1];[a0][a1]xstack=inputs=2:layout=0_0|w0_0[out]" -map "[out]" -c:v libx264 -f matroska {output}'
    subprocess.call(command, shell=True)


join_two_videos('script_cut.mp4', 'script_histogram.mp4', 'script_joined.mp4')


# scale the cut video in different resolutions (ex3)
def scale(video, w, h, output):
    command = f"ffmpeg -i {video} -vf scale={w}:{h} {output}"
    subprocess.call(command, shell=True)


scale('script_cut.mp4', '160', '120', 'script_scaled_160x120.mp4')
scale('script_cut.mp4', '360', '240', 'script_scaled_360x240.mp4')
scale('script_cut.mp4', '640', '480', 'script_scaled_480p.mp4')
scale('script_cut.mp4', '1280', '720', 'script_scaled_720p.mp4')


# convert the cut video from stereo to mono (ex4)
def mono(video, output):
    command = f"ffmpeg -i {video} -ac 1 {output}"
    subprocess.call(command, shell=True)


mono('script_cut.mp4', 'script_mono.mp4')


# change the audio codec of the mono video (ex4)
def aac(video, output):
    command = f"ffmpeg -i {video} -c:v copy -c:a libfdk_aac -vbr 3 {output}"
    subprocess.call(command, shell=True)


aac('script_cut.mp4', 'script_mono_aac.mp4')
