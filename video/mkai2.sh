#!/bin/bash
IMG=$1; DUR=$2; CAP=$3; MOVE=$4; OUT=$5
F=$(echo "$DUR*25" | bc | cut -d. -f1)
case $MOVE in
  in)  Z="zoompan=z='1+0.10*in/$F':d=1:x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':s=1920x1080:fps=25";;
  out) Z="zoompan=z='1.10-0.10*in/$F':d=1:x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':s=1920x1080:fps=25";;
  pan) Z="zoompan=z='1.08':d=1:x='(iw-iw/zoom)*in/$F':y='(ih-ih/zoom)/2':s=1920x1080:fps=25";;
esac
ffmpeg -y -loop 1 -t $DUR -framerate 25 -i ai/$IMG.jpg -vf "$Z,unsharp=5:5:0.5,eq=gamma=1.02:saturation=1.1:contrast=1.03,drawbox=y=ih-170:h=170:color=black@0.45:t=fill,drawtext=fontfile=mont.ttf:text='$CAP':fontcolor=white:fontsize=52:x=(w-text_w)/2:y=h-118,fade=t=in:st=0:d=0.35,fade=t=out:st=$(echo "$DUR-0.35"|bc):d=0.35" -an -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p segs2/$OUT.mp4 -loglevel error
