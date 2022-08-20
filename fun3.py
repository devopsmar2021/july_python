import boto3



def cb(bname):
    client = boto3.client('s3')
    response = client.create_bucket(ACL='private',Bucket=bname)

def db(bname):
    client = boto3.client('s3')
    del_response = client.delete_bucket(Bucket=bname)

def upload_file(input_file,bname,upload_file):
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(input_file, bname, upload_file)

# cb('auganu123')
# cb('auganu1234')
# cb('auganu12345')

file_names = ['f1','f2','f3','f4','f5',]

for i in file_names:
    upload_file(i,'auganu123',f'upload/{i}')
