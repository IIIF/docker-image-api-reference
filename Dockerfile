FROM grahamdumpleton/mod-wsgi-docker:python-3.5-onbuild

WORKDIR /app
RUN git clone https://github.com/zimeon/iiif.git iiif

# WORKDIR /app/iiif
# RUN pip install iiif

WORKDIR /app/iiif/

CMD [ "iiif/iiif_testserver.wsgi" ]
