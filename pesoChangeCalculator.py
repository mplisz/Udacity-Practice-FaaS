# import libraries
import json
import decimal

def lambda_handler(event, context):
    ''' Accepts some Pesos input and returns the amount of change
        needed to make up that value.
        :param event: a request that has a JSON input with some "amount" value
        :return: a response with the correct Peso change to make up the amount,
            formatted in JSON as the number of 5centavos, 10centavos, 20centavos, 50centavos.
    '''
    print (event) #log in the AWS Lambda for CloudWatch

    # check that the request has some input body
    if 'body' in event:
        event = json.loads(event["body"])
    #find amount from event body
        amount = float(event["amount"])
    #set up the possible values of centavos
        coins = [5,10,20,50]
        coins_lookup = {50:"50 centavos", 20:"20 centavos", 10:"10 centavos", 5:"5centavos"}
    #set up the variable for result
    result = []

    # divide the amount*100 (the amount in cents) by a coin value
    # record the number of coins that evenly divide and the remainder
    coin = coins.pop()
    num, rem  = divmod(int(amount*100), coin)
    # append the coin type and number of coins that had no remainder
    res.append({num:coin_lookup[coin]})
    
    # while there is still some remainder, continue adding coins to the result
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num:coin_lookup[coin]})

    # format the response as JSON and return the result
    response = {
        "statusCode": "200",
        "headers": { "Content-type": "application/json" },
        "body": json.dumps({"res": res})
    }

    return response
