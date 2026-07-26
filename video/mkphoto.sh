#!/bin/bash
# mkphoto img dur caption out
IMG=$1; DUR=$2; CAP=$3; OUT=$4
F=$(echo "$DUR*25" | bc | cut -d. -f1)
ffmpeg -y -loop 1 -t $DUR -i ../products/$IMG.jpg -filter_complex "[0:v]scale=1920:1080,gblur=sigma=40,eq=brightness=-0.18[bg];[0:v]scale=-2:1080[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,zoompan=z='1+0.05*in/$F':d=1:x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':s=1920x1080:fps=25,eq=gamma=1.02:saturation=1.12,drawbox=y=ih-170:h=170:color=black@0.45:t=fill,drawtext=fontfile=mont.ttf:text='$CAP':fontcolor=white:fontsize=52:x=(w-text_w)/2:y=h-118,fade=t=in:st=0:d=0.35,fade=t=out:st=$(echo "$DUR-0.35"|bc):d=0.35" -an -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -t $DUR segs/$OUT.mp4 -loglevel error
