# build the image
docker build -t pong . 

# allow connections from host to container
xhost + 

# run the image
docker run --rm -e DISPLAY=$DISPLAY -v /dev/snd:/dev/snd \
           -v /tmp/.X11-unix/:/tmp/.X11-unix/ --privileged \
           --name pong-plus pong