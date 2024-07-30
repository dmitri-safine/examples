### Build docker image

```
docker build -t image-size-detector:0.0.1 .
```

### Place an image into a local folder

In this example we will use local directory:
`C:\Users\DmitriSafine\tmp\images`

### Run application in the docker container

```
docker run --rm -v //c/Users/DmitriSafine/tmp/images:/images  image-size-detector:0.0.1 funny-cat.jpg
```

> Note: You can change your local directory, but don't change the `/images` directory inside the container, because it is hard-coded in the app. To clarify, after `-v` argument change `//c/Users/DmitriSafine/tmp/images` before the `:`, but don't change `/images` after the `:`.
