import sys
import logging
import boto3


s3 = boto3.resource('s3')

#bucketName = 'yrassessmentbucket'
#key = 'sample1.txt'
bucketName = sys.argv[1]
key = sys.argv[2]

logging.debug(bucketName)
logging.debug(key)
try:
    bucket = s3.Bucket(bucketName)
except Exception e:
    logging.warning(e)
    exit()
versions = list(bucket.object_versions.filter(Prefix=key).all())
try:
    VersionId = versions[1].get().get('VersionId')
except Exception e:
    logging.warning(e)
    exit()
    
bucket.download_file(key, key, ExtraArgs={'VersionId' : VersionId})

# Output:
# ubuntu@ip-172-31-92-62:~$ python3 Problem2.py yrassessmentbucket sample1.txt
# ubuntu@ip-172-31-92-62:~$ ls
# Problem2.py  Problem8.py  index.html  sample1.txt
# ubuntu@ip-172-31-92-62:~$ cat sample1.txt
# This is a sample text file.
# Another line added to it.

