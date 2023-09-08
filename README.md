## Thing to archive content from someone's JustFor.Fans

With thanks to https://github.com/nichtmax/justfor.fans.ripper & https://github.com/whats-happening-rightnow/justfor.fans.ripper who made the initial versions this is forked from.

The primary changes with this version are:
- Sometimes a videoid is not returned. The old versions of the script would still try to add metadata to a video file that didn't exist and thus error. Sorted that with a 3 time check loop and tweaked the metadata service to not try and add metadata unless the actual scrape was successful.
- Added a Dockerfile as that's my preferred way to run things and I really can't be bothered to deal with issues relating to users random versions of Python everywhere. Got an issue with the container feel free to log it here. Got an issue with python then you're on your own!

1. To Run
    1. Follow the Dockerfile if you don't want to use Docker
    2. Run `docker run -d --name jff -v /downloads:/downloads jff:latest 000000 1a1a1a1a1a1a1a1a` (where 000 is your UserID and 1a1a is your UserHash4 value) 
2. To Configure
    1. `overwrite_existing` - will skip download if file exists
    2. `save_path` - destination folder - will save to same location as script folder if none provided
    3. `save_full_text` - will save text file with full description
    4. `file_name_format` - filename format, following values are available:
        * `name`
        * `post_date`
        * `post_id`
        * `desc`
3. How to get UserID and UserHash values
    1.  Log into your JustFor.Fans account
    2.  Select performer's page
    3.  (in Chrome), hit F12 to open dev-console
    4.  Refresh page to view network activity
    5.  Locate `getPost.php` call, extract `UserID` and `UserHash4` values (in yellow)
    6.  Pass in as params when running script
        * `python app.py [UserID] [UserHash]`

![image](https://user-images.githubusercontent.com/12958294/115130004-859a5580-9fa0-11eb-9275-235d4ec51967.png)
