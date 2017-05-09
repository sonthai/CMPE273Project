# -*- coding: utf-8 -*-
import boto3

def handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    body = event.get("data")

    course = body.get("course")
    tableName =  body.get("table")
    field = body.get("field")
    #condition = body.get("condition")
    response_format = body.get("answer")

    print "Course %s Table %s field %s " %(course, tableName, field)

    tableDB = dynamodb.Table(tableName)

    response = tableDB.get_item(
        Key = {
            'course': course
        }
    )

    item = response["Item"]
    answer = response_format % (course, item[field])
    print "Answer %s " % answer

    return {
        "status": 200,
        "response": answer

    }




