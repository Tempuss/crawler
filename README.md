
## Crawler 
* URL {YOUR_OWN_URL} 

### 1. Get URL List with javascript

Open URL Link -> Open Chrome Developer Tool->Console 

```
var url_list = [];

var size = document.getElementsByTagName('a').length;

var data = document.getElementsByTagName('a');

for(var i=5;i<size;i++) {

	url_list.push(data[i].href);
}

JSON.stringify(url_list);
```

It Will Print Json String

```
[
   "{URL}"
]
```

Copy The List and Save it(File)

ex) url.json

### 2.Turn On Your Own AWS EC2 Instance (5개)

```
sudo su
apt-get update
apt-get install python3

cd ~
mkdir craw
cd craw

```
Move This Source code to *craw*

* Look Like This Structure

```
.
├── craw.log
├── crawler.py
├── url.json
├── key
|   └── REAMEME.md
└── url.json
```


### 3. Run Crawler

* Run Python Module In Background

```
./python crawler.py &

```


* You can check your log

```
tail -f craw.log
```


### 4. Result
* It WORKED!
