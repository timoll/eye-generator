#!/bin/bash

if [ ! -d "videos" ]; then
    mkdir videos
fi
ffmpeg -framerate 60 -i leftup/%04d.png -c:v libx264 -r 60 videos/leftup.mp4
ffmpeg -framerate 60 -i leftdown/%04d.png -c:v libx264 -r 60 videos/leftdown.mp4
ffmpeg -framerate 60 -i rightup/%04d.png -c:v libx264 -r 60 videos/rightup.mp4
ffmpeg -framerate 60 -i rightdown/%04d.png -c:v libx264 -r 60 videos/rightdown.mp4
