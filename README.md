# MAC-Generator

Simple MAC addresses generator.

### Generate one full random MAC address

```bash
./macgen.py
```
```
6b:ad:8f:24:4b:f5
```

### Generate five full random MAC addresses

```bash
./macgen.py 5
```
```
b1:a3:24:cc:ff:40
43:57:23:9a:52:c3
3f:ab:be:38:50:46
8d:06:5b:3a:6c:59
7a:e7:7d:8d:fa:86
```

### Generate five random MAC addresses with a prefix

```bash
./macgen.py 5 -p 5C:26:0A       # Dell Inc.
```
```
5c:26:0a:62:83:29
5c:26:0a:d1:7e:f7
5c:26:0a:52:e9:46
5c:26:0a:61:34:16
5c:26:0a:1a:a2:a4
```

### Generate five MAC addresses with a prefix by incrementing from 00

```bash
./macgen.py 5 -p 5C:59:48 -i    # Apple, Inc.
```
```
5c:59:48:00:00:00
5c:59:48:00:00:01
5c:59:48:00:00:02
5c:59:48:00:00:03
5c:59:48:00:00:04
```

### Generate one full random Uppercased MAC address

```bash
./macgen.py -u
```
```
3A:05:ED:02:52:37
```

### Check MAC addresses vendors

```bash
cat vendor.lst | grep -i apple
```

MAC vendors list has been retrieved from:
- https://gist.github.com/aallan/b4bb86db86079509e6159810ae9bd3e4
