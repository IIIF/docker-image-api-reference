FROM grahamdumpleton/mod-wsgi-docker:python-3.5-onbuild

RUN apt-get update
RUN apt-get -y install unzip

WORKDIR /app
RUN curl -LO https://github.com/zimeon/iiif/archive/master.zip
RUN unzip master
RUN mv iiif-master iiif

# test with validator
RUN apt-get -y install libmagic-dev libwebp-dev
RUN pip install iiif_validator coveralls pep8 pep257 testfixtures boto3 pytz tzlocal
#RUN python setup.py install
#RUN python setup.py test

WORKDIR /app/iiif/testimages
RUN rm -rf *
ADD images/* /app/iiif/testimages/
RUN chmod 777 /app/iiif/testimages
ADD iiif_reference_server.cfg /app/iiif/

COPY src/* /app/iiif/
RUN echo "import SyncS3" >> /app/iiif/iiif_reference_server.wsgi
RUN echo "SyncS3.loadApp(application)" >> /app/iiif/iiif_reference_server.wsgi

CMD [ "iiif/iiif_reference_server.wsgi" ]
