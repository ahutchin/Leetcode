# The Problem
# Many companies use HubSpot for its calling capabilities. Sales reps use the HubSpot product throughout the day to make phone calls to prospects.

# We've found that certain customers using HubSpot have a large number of sales reps concurrently making calls with HubSpot, and this puts heavy load on our systems. In response to this, we'd like to bill our customers based on their peak calling load. In other words, we'd like to bill customers based on their maximum number of concurrent calls.

# You're provided with an HTTP GET endpoint that returns phone call records represented as JSON: https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=5872e8be7715481f3c640f4d6789

# Each call looks something like this:

# {
#   "customerId": 123,
#   "callId": "2c269d25-deb9-42cf-927c-543112f7a76b",
#   "startTimestamp": 1707314726000,
#   "endTimestamp": 1707317769000
# }

# customerId is a unique identifier for one customer. One customer may have many sales reps concurrently making calls.
# callId is a unique identifier for a single phone call. No two phone calls will have the same callId.
# startTimestamp is when the call started. This value is given as a UNIX timestamp in milliseconds. In other words, it's the number of milliseconds that passed between the UNIX epoch (1970-01-01 00:00:00 UTC) and the start of the call.
# endTimestamp is when the call ended. This value is also given as a UNIX timestamp in milliseconds. endTimestamp will always be greater than startTimestamp for a given call record.
# For the billing team to charge our customers correctly, they need to know the maximum number of concurrent calls for each customer for each day. The billing team has asked you to POST this information to the following endpoint: https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=5872e8be7715481f3c640f4d6789. The POST body must be in the following format:

# {
#   "results": [
#     {
#       "customerId": 123,
#       "date": "2024-02-07",
#       "maxConcurrentCalls": 1,
#       "timestamp": 1707314726000,
#       "callIds": [
#         "2c269d25-deb9-42cf-927c-543112f7a76b"
#       ]
#     }
#   ]
# }
# date is a UTC date in the format YYYY-MM-DD. So the example date refers to February 7th 2024.
# maxConcurrentCalls is the maximum number of simultaneous calls that occurred at any time during the corresponding date for this customer.
# timestamp is a UNIX timestamp (in milliseconds) at which maxConcurrentCalls was reached for this customer and date. There could be multiple time periods during this date where maxConcurrentCalls is reached. A timestamp during any of these time periods can be chosen.
# callIds is an array of calls that were happening for this customer at timestamp. The length of this array should equal maxConcurrentCalls. The order of callIds does not matter.
# This example response only has one entry in the results array, but we expect the actual answer to have multiple results.

# Note
# The startTimestamp of a call is inclusive, and the endTimestamp of a call is exclusive. This means that:
# If call A has an endTimestamp of 123, and call B has a startTimestamp of 123, they never overlapped.
# For a given results entry, the timestamp should always be less than the endTimestamp of each call in callIds.
# A single call may span multiple UTC dates, and calls can be arbitrarily long.
# The order of results posted does not matter.
# For a given customerId and date, if no phone calls occurred during that date, there should be no results entry with that customerId and date combination.
# No two entries in the results array should have identical values for both customerId and date. In other words, for a given customerId and date combination, there should be at most one entry in the array.
# Example 1
# Let's say that for some customer, the diagram below is a visual representation of their call records.


# For this customer, for the date 2024-02-07, maxConcurrentCalls should equal 3, since that's the largest number of calls that were concurrently happening on that date. The given timestamp for this customer on date 2024-02-07 can be any UNIX timestamp in the time period highlighted in red.

# Example 2
# Let's say that for some other customer, the diagram below is a visual representation of their call records.


# Call MNO starts on February 10th and ends on February 11th. For this customer:

# For the date 2024-02-10, maxConcurrentCalls should equal 1. The given timestamp can be any UNIX timestamp in the time period highlighted in red.
# For the date 2024-02-11, maxConcurrentCalls should equal 1. The given timestamp can be any UNIX timestamp in the time period highlighted in yellow.
# For the date 2024-02-12, no result should be given.
# For the date 2024-02-13, maxConcurrentCalls should equal 1. The given timestamp can be any UNIX timestamp in the time period highlighted in green.
# API Guidelines
# If your answer is correct, the API will return 200 OK. If the request is malformatted or incorrect, the API will return 400 along with a message indicating if the response is of the wrong structure or incorrect. If you submit an incorrect response that is close or on the right track, the error message will tell you so.

# If you get a 5xx response, let us know and we’ll help you out.

# The candidate.hubteam.com domain is set up with a permissive cross-origin policy, so you can POST to it from any location in a browser if you choose to implement in an in-browser JS solution.

# Testing Guidelines
# If you want help testing and debugging your solution, you can use the these endpoints:

# GET https://candidate.hubteam.com/candidateTest/v3/problem/test-dataset?userKey=5872e8be7715481f3c640f4d6789

# This endpoint above returns a small example dataset for testing.
# GET https://candidate.hubteam.com/candidateTest/v3/problem/test-dataset-answer?userKey=5872e8be7715481f3c640f4d6789

# This endpoint above returns a correct answer corresponding to the test dataset.
# POST https://candidate.hubteam.com/candidateTest/v3/problem/test-result?userKey=5872e8be7715481f3c640f4d6789

# This endpoint above accepts a request body with a JSON answer. A 200 status code is returned if the given answer is correct for the test dataset. A 400 status code is returned if the given answer is incorrect for the test dataset.
# If you use the response body from the test-dataset-answer endpoint as the body of your test-result request, a 200 status code will be returned. The test-result endpoint exists just to help you debug your solution. A 200 response from that endpoint does not mean you have passed the full assessment. You still need to POST a correct answer to the https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=5872e8be7715481f3c640f4d6789 endpoint to pass the full assessment.
# Evaluation
# When you’re done, this page will update with a form to upload your code. We’ll evaluate you based on two things:

# First and foremost, if you complete the project within three hours.
# Next, the time from when you started the assessment to the time you submit a correct solution.


import json
import requests
from datetime import datetime, timedelta

# add only relevant emails, country, and available dates to array. names can be ignored. convert the available dates to datetime format
filtered_arr = []
# countries is
countries = {}

# fetch the data from the api
data = requests.get(
    "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=7e744a7ce1e27cba5cc581e51e4d",
    timeout=5,
)
jsonRes = data.json()

for user in jsonRes["partners"]:
    filtered_arr.append(
        [
            user["country"],
            user["email"],
            [
                datetime.strptime(date, "%Y-%m-%d").date()
                for date in user["availableDates"]
            ],
        ]
    )

# sort all dates in filtered_array in case they are not chronological
sortedData = [
    [country, name, sorted(numbers)] for country, name, numbers in filtered_arr
]

def find_longest_consecutive_seq(dates: list) -> []:
    """This function finds the longest consecutive pair of sequences for each attendee"""
    max_seq = []
    curr = []

    for date in dates[2]:
        if not curr or date == curr[-1] + timedelta(days=1):
            curr.append(date)
        # if the curr has an array of 2 then we know there is a consecutive pair
        if len(curr) == 2:
            max_seq.append(curr)
        # update the curr array to reflect the curr date
        curr = [date]

    # check if there is still a consecutive pair in curr
    if len(curr) == 2:
        max_seq.append(curr)

    # if no consecutive dates then set array as empty
    if len(max_seq) < 2:
        max_seq = []
    dates[2] = max_seq
    return dates


def add_to_dict(attendee: list) -> None:
    """This function adds all the attendees to their respective country,
        thus filtering them by country now
    """
    if attendee[0] not in countries:
        countries[attendee[0]] = {"attendee": [attendee[1]], "available": [attendee[2]]}
    else:
        countries[attendee[0]]["attendee"].append(attendee[1])
        countries[attendee[0]]["available"].append(attendee[2])


def find_most_common(key: str):
    """This function finds the max consecutive pair of dates for each country"""
    # we only care about what the starting date because we know it will end the next day after
    # the key param represents the country name
    longest = {}
    for i in range(len(countries[key]["available"])):
        date_arr = countries[key]["available"][i]
        if len(date_arr) == 0:
            # skip non consequtive dates
            continue
        for time in date_arr:
            if time[0] not in longest:
                longest[time[0]] = [1, [countries[key]["attendee"][i]]]
            else:
                longest[time[0]][0] += 1
                longest[time[0]][1].append(countries[key]["attendee"][i])

    # return null if there are no consecutive pairs
    if not longest:
        return None, None
    most_common_key = max(longest.items(), key=lambda x: x[1][0])
    # iterate through longest again just in case there is an earlier date
    longest_value = most_common_key[1][0]
    min_date = most_common_key[0]
    for key, value in longest.items():
        if value[0] == longest_value:
            min_date = min(min_date, key)
    return min_date, longest[min_date]


for attendee in sortedData:
    findConseq = find_longest_consecutive_seq(attendee)
    add_to_dict(findConseq)

# print("countries arr", countries["Japan"])
finale_arr = {}
for country in countries:
    date, longest_test = find_most_common(country)
    finale_arr[country] = {
        "start_date": date,
        "attendees": longest_test,
    }

# print(finale_arr)

postBody = {"countries": []}

for key, value in finale_arr.items():
    # if there are no attendees
    if not value["attendees"]:
        tempBody = {
            "attendeeCount": 0,
            "attendees": [],
            "name": key,
            "startDate": None,
        }
        postBody["countries"].append(tempBody)
        continue
    tempBody = {
        "attendeeCount": value["attendees"][0],
        "attendees": value["attendees"][1],
        "name": key,
        "startDate": value["start_date"].strftime("%Y-%m-%d"),
    }
    postBody["countries"].append(tempBody)

#send post request
headers = {
    "Content-Type": "application/json",
}
json_content = json.dumps(postBody)
post_url = "https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=7e744a7ce1e27cba5cc581e51e4d"
send_post = requests.post(post_url, data=json_content, headers=headers, timeout=5)

if send_post.status_code == 400:
    print("bad response")
    print(send_post.text)
