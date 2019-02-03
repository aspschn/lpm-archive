lpm-archive
============
archive.lpmpkg.tk

Simple directory listing.

Build and run with docker
-------------------------
- Build docker image and run server.

```sh
docker build -t lpm-archive .
docker run -d -p 5000:5000 -v $CONTENTS_ROOT:/srv/www/static lpm-archive
```
