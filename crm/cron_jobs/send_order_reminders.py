#!/usr/bin/env python3

import sys
import os
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime

# GraphQL endpoint URL
GRAPHQL_ENDPOINT = "http://localhost:8000/graphql/"

# GraphQL client setup
transport = RequestsHTTPTransport(url=GRAPHQL_ENDPOINT, verify=True, retries=3)
client = Client(transport=transport, fetch_schema_from_transport=True)

# Optional: Check hello field to ensure endpoint is live
query = gql("""
{
  hello
}
""")
response = client.execute(query)

# Log the hello check
with open("/tmp/order_reminders_log.txt", "a") as f:
    f.write(f"{datetime.now()}: GraphQL hello field says: {response}\n")

# TODO: Replace with your real reminder query later
print("GraphQL order reminder ran OK.")
