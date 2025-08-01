import json

def lambda_handler(event, context):
    # Extract name from event, default to 'PyCharm' if not provided
    name = event.get('name', 'PyCharm')
    
    # Use a breakpoint in the code line below to debug your script.
    message = f'Asak Bhaisaab, {name}'  # Press Ctrl+F8 to toggle the breakpoint.
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': message
        })
    }
