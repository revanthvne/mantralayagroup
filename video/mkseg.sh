#!/bin/bash
# mkseg id start dur caption out  — grade + caption + fades, 1920x1080/25fps
ID=$1; SS=$2; DUR=$3; CAP=$4; OUT=$5
ffmpeg -y -ss $SS -t $DUR -i clips/hd-$ID.mp4 -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=25,eq=gamma=1.03:saturation=1.18:contrast=1.05,colorbalance=rs=0.05:rm=0.03:bh=-0.03,drawbox=y=ih-170:h=170:color=black@0.45:t=fill,drawtext=fontfile=mont.ttf:text='$CAP':fontcolor=white:fontsize=52:x=(w-text_w)/2:y=h-118,fade=t=in:st=0:d=0.35,fade=t=out:st=$(echo "$DUR-0.35"|bc):d=0.35" -an -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p segs/$OUT.mp4 -loglevel error
