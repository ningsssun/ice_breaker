import json
from ice_breaker import ice_break_with


def handler(event, context):
    body = json.loads(event["body"])
    name = body["name"]

    summary_and_facts, interests, ice_breakers, profile_pic_url = ice_break_with(name)

    # Return the response as a JSON object
    return {
        "statusCode": 200,
        "body": json.dumps({
            "summary_and_facts": summary_and_facts.to_dict(),
            "interests": interests.to_dict(),
            "ice_breakers": ice_breakers.to_dict(),
            "picture_url": profile_pic_url,
        }),
        "headers": {
            "Content-Type": "application/json"
        }
    }
