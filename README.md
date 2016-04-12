# timelapse
Script to periodically save the image at a url. Designed for webcams on a local server.

## Simple example
```bash
python puppy-saver dir-of-puppies http://animaliaz-life.com/data_images/dog/dog5.jpg
```

## Sample output file output
By default the files are saved in a directory structure of /YYYY/MM/DD and the file name is HHMMSS.jpg
```
/dir-of-puppies
+---/2016
    +---/04
        +---/12
        |   +---000229.jpg
        |   +---000240.jpg
        |   ...
        +---/13
            +---000230.jpg
            +---000240.jpg
            ...
```

## Example bash script
Something like this could be useful if you want to run this task as a background operation.
```bash
#!/bin/bash 
EYEDIR="$HOME/webcam-eye"
python "$EYEDIR/timelapse.py" eye-1 "$EYEDIR/eye-1" http://eyeball1.local:8081/ >> "$EYEDIR/LOG-eye-1.txt" 2>&1 &
```


### Arguments

#### name
Unique name to be used for process tracking to verify that another instance of the script with the same name isn't already running. This could be useful if you plan on running this with a cronjob.

#### output_dir
The path to the directory where the images will be saved

#### url
Url of the image to be saved

### Options

#### --poll_freq
How often (in seconds) to poll for image
