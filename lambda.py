import urllib
import urllib2
import json
import re
import datetime

API_BASE = "https://dailyprophet.alphaparticle.com/"

def lambda_handler(event, context):
    if (event['session']['application']['applicationId'] != "amzn1.ask.skill.2d0c2f9d-7910-47a7-b8fe-645bd00f4abf"):
        raise ValueError("Invalid Application ID")
        
    ## Handle the bare launch intent
    if(event["request"]["type"] == "LaunchRequest"):
        return build_response("Daily Prophet", "Welcome to the Daily Prophet Quote of the Day. Ask me about the quote of the day.", False)
        
    intent_name = event["request"]["intent"]["name"]

    ## Handle the help intent
    if intent_name == "AMAZON.HelpIntent" or intent_name == "TroubleshootIntent":
        return build_response("Daily Prophet", "Welcome to the Daily Prophet Quote of the Day. Ask me about the quote of the day.", False)
    
    ## Handle the stop intent
    elif intent_name == "AMAZON.StopIntent" or intent_name == "AMAZON.CancelIntent":
        return build_response( "Thanks!", "Thanks for using Daily Prophet Quote of the Day. Goodbye!", True)
    
    elif intent_name == "QuoteOfTheDay":
        return query_quote()
        
def query_quote():
    should_end_session = True
    
    api_url = API_BASE + "wp-json/dailyprophet/qotd"
    
    try:
        response = urllib2.urlopen(api_url)
    except urllib2.HTTPError, e:
        return build_response("Quote of the Day", "Sorry, I didn't quite get that. Ask me about the quote of the day.", False)
    
    quote_of_the_day = json.load(response)

    if(quote_of_the_day and quote_of_the_day != ''):
        quote_of_the_day = "The quote of the day is: '" + quote_of_the_day + "'"
    else:
        quote_of_the_day = "No quote of the day was found."

    return build_response("Quote of the Day", quote_of_the_day, should_end_session)
    
def build_response( title, output_text, should_end_session ):
    return {
      "version": "1.0",
      "response": {
        "outputSpeech": {
          "type": "PlainText",
          "text": output_text
        },
        "card": {
          "content": output_text,
          "title": title,
          "type": "Simple"
        },
        "reprompt": {
          "outputSpeech": {
            "type": "PlainText",
            "text": ""
          }
        },
        "shouldEndSession": should_end_session
      },
      "sessionAttributes": {}
    }