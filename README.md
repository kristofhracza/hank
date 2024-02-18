# Hank
The commonn man's OSINT tools

## Usage
```
        Usage: hank.py -u [username] -r [other names]
        
        REQUIRED:
        -u or --username
        -r or --real-name

        OPTIONAL:
        -c or --count\t[Iteration count]
```
The `real-name` parameter is used by the search engine, so any known aliases can be added as well as the person's real name.

```bash
python hank.py -u "johndoe" -r "John Doe bigjohnny421 johndoe"
```

## Search engine crawling
By giving multiple names under which the target is know, the script will search for those partcular words in the specified search engine.

### To-Do list
- Add more search engines

## Site lookup
Integrated into this *hank* is the old binoculars tool.

It will check sites for the presence of a username.

### To-Do list
- Fix false positive / negatives
- Add new site list processor an system