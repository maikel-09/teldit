**Application**
teldit

**Description**

Teldit is a simple telegram bot which can be used for downloading media using the pyhton redvid library

**Usage**
```
 docker run -d \
	    -e TELEGRAMTOKEN='<telegram bot token>' \
	    -v=<path to media files>:/media \
	    --name=teldit \
	    maikel09/teldit:latest
```
---
