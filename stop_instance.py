import boto3
from pprint import pprint

client = boto3.client('ec2')

response = client.describe_instances(MaxResults=5)

check = True

get_details = {}
get_running_instances = {}

while check:
    for item in response["Reservations"]:
        instance_name = ""
        for name_list in item["Instances"][0]["Tags"]:
            if name_list["Key"] == "Name":
                instance_name = name_list["Value"]
        get_details.update({item["Instances"][0]["InstanceId"]: [instance_name, item["Instances"][0]["State"]["Name"]]})
        #print(item["Instances"][0]["InstanceId"],instance_name, item["Instances"][0]["State"]["Name"])
    if "NextToken" in response:
        response = client.describe_instances(MaxResults=5,NextToken=response["NextToken"])
    else:
        check = False

print(get_details)


for i_item in get_details.keys():
    if get_details[i_item][1] == "running":
        get_running_instances.update({i_item: [get_details[i_item][0],get_details[i_item][1]]})

print(get_running_instances)