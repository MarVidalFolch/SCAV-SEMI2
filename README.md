# SCAV-SEMI2

## Mar Vidal-Folch Angerri - NIA: 204751

In this seminar we have worked with the Big Bunk Bunny video and ffmpeg:

### Exercise 1
---
We have cut the first 10 seconds of the BBB video and we saved in a new mp4 file. In the ex1 folder you can find the commands used in a screenchot and the ouput mp4 video. 
### Exercise 2
---
From the output in exercise 1, we have extracted its YUV histogram which you can find in ex2.mp4 file. Then, we have created a new video where the histogram and the 10 seconds video are displayed simultaneously. All the output files and the screenshots showing the commands used can be found in the ex2 folder. 

### Exercise 3
---
We have resized the output video of exercise 1 into 4 different video outputs:

- 720p (which corresponds to 1280x720 pixels)
- 480p (whose standard corresponds to 640x480 pixels) 
- 360x240
- 160x120

In the ex3 folder you can find the different output videos and the screnshoots with the commands used. If we play the different videos, we can really see the differences between them. 

### Exercise 4
---
We have changed the audio into mono output and in a different audio codec. We have done it in two steps. First of all, we have only changed the audio into mono. Once this was done, we changed the audio codec. In this case, we used the Variable Bit Rate (VBR) model setting the VBR level at 3 (medium quality). From the mono.mp4 video, we converted only the audio stream to AAC and copied the audio stream.
In the ex4 folder, you can find the outputs and commands of the two steps. 

### Exercise 5
---
We have created a pyhton script with all the previous exercises. For each exercise, we have created one or two functions. By calling them, we obtain exactly the same aoutputs than in all previous exercises. 
In all functions, we mus give as parameters the input video and the name for the output video. In the case of the scaling function, we also must input the desired resolution for each case. 
In the ex5 folder, you can find the python script and the outputs obtained from it. If we have a look at these new outputs, we see that, obviously, they are the same obtained doing the 4 first exercises. 
