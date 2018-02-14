# docker-image-api-reference
This is a docker deployment of the IIIF Image API reference implementation.

This is currently using the [image api implementation](https://github.com/zimeon/iiif) created by [@zimeon](https://github.com/zimeon). This repo is intended to wrap up Simeon's code in docker and manage the deployment to Amazon.

Note the URLs for accessing IIIF images is as follows:

 * http://localhost:8000/api/image/1.0/example/reference/67352ccc-d1b0-11e1-89ae-279075081939/full/full/0/native.jpg
 * http://localhost:8000/api/image/1.1/example/reference/67352ccc-d1b0-11e1-89ae-279075081939/full/full/0/native.jpg
 * http://localhost:8000/api/image/2.0/example/reference/67352ccc-d1b0-11e1-89ae-279075081939/full/full/0/default.jpg
 * http://localhost:8000/api/image/2.1/example/reference/67352ccc-d1b0-11e1-89ae-279075081939/full/full/0/default.jpg

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

## Testing

To get a list of URLs from the IIIF api website you can run the following:

```find ~/development/iiif/api/ -name "*.json" -exec grep 'api/image' {} \; |grep -v profile |grep reference |grep -o 'http://.*"'|sort |uniq|sed 's/"//g'```

which currently gives:

 * http://iiif.io/api/image/2.0/example/reference/detail
 * http://iiif.io/api/image/2.0/example/reference/detail/10,10,153,153/full/0/default.jpg
 * http://iiif.io/api/image/2.0/example/reference/detail/full/full/0/default.jpg
 * http://iiif.io/api/image/2.0/example/reference/detail/full/full/0/gray.jpg
 * http://iiif.io/api/image/2.0/example/reference/page1-full
 * http://iiif.io/api/image/2.0/example/reference/page1-full/100,100,1000,1600/full/0/default.jpg
 * http://iiif.io/api/image/2.0/example/reference/page1-full/full/full/0/default.jpg
 * http://iiif.io/api/image/2.0/example/reference/page1-full/full/full/0/gray.jpg
 * http://iiif.io/api/image/2.0/example/reference/page1-full/full/full/180/default.jpg
 * http://iiif.io/api/image/2.1/example/reference/detail
 * http://iiif.io/api/image/2.1/example/reference/detail/10,10,153,153/full/0/default.jpg
 * http://iiif.io/api/image/2.1/example/reference/detail/full/full/0/default.jpg
 * http://iiif.io/api/image/2.1/example/reference/detail/full/full/0/gray.jpg
 * http://iiif.io/api/image/2.1/example/reference/page1-full
 * http://iiif.io/api/image/2.1/example/reference/page1-full/100,100,1000,1600/full/0/default.jpg
 * http://iiif.io/api/image/2.1/example/reference/page1-full/full/full/0/default.jpg
 * http://iiif.io/api/image/2.1/example/reference/page1-full/full/full/0/gray.jpg
 * http://iiif.io/api/image/2.1/example/reference/page1-full/full/full/180/default.jpg
