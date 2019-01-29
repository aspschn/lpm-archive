lpm-archive
============
archive.lpmpkg.tk

Simple directory listing.

Build and run with docker
-------------------------
- Create or link to `static` directory.
- Build docker image and run server.

```sh
docker build -t lpm-archive .
docker run -d -p 5000:5000 -v static:/srv/www/static lpm-archive
```
