# docker-image-api-reference
This is a docker deployment of the IIIF Image API reference implementation.

This is currently using the [image api implementation](https://github.com/zimeon/iiif) created by [@zimeon](https://github.com/zimeon). This repo is intended to wrap up Simeon's code in docker and manage the deployment to Amazon.

Note the URLs for accessing IIIF images is as follows:

 * http://localhost:8000/1.0_pil/67352ccc-d1b0-11e1-89ae-279075081939/full/full/0/native.jpg
 * http://localhost:8000/1.1_pil/67352ccc-d1b0-11e1-89ae-279075081939/full/full/0/native.jpg
 * http://localhost:8000/2.0_pil/67352ccc-d1b0-11e1-89ae-279075081939/full/full/0/native.jpg

and the directory for storing images is:

```
/app/iiif/testimages
```

## Build

To build the docker image run:

```
 docker build -t iiif-image .
 ```

To run the image:

```
 docker run -it --rm -p 8000:80 --name iiif-image iiif-image:latest
```

To run the above on one line:

```
docker build -t iiif-image . && docker run -it --rm -p 8000:80 --name iiif-image iiif-image:latest
```

Documentation on deploying to AWS: https://docs.aws.amazon.com/AWSGettingStartedContinuousDeliveryPipeline/latest/GettingStarted/ECS_CD_Pipeline.html
