import pandas as pd

data = pd.read_csv('output.csv')

print("Data Overview:")
print(data.info())

# analysing the most common pages
print("\nMost Common Pages:")
common_pages = data['path'].value_counts().head(30)
print(common_pages.to_markdown())

# analysing the most common IP addresses
print("\nMost Common IP Addresses:")
common_ips = data['ip'].value_counts().head(20)
print(common_ips.to_markdown())

# analysing the most common countries
print("\nMost Common Countries:")
common_countries = data['country'].value_counts().head(15)
print(common_countries.to_markdown())

# analysing the user agents
print("\nUser Agents:")
common_user_agents = data['useragent'].value_counts()
print(common_user_agents.to_markdown())

# after researching about bot detection and user agents, i found the most common bot user agents
bots_user_agents = ['Wget', 'curl', 'HTTPie', 'python-requests', 'sqlmap', 'okhttp/4.9.3',
                    'Postman', 'PostmanRuntime/7.32.3', 'OWASP ZAP', 'nikto', 'Burp Suite Professional',
                    'Mozilla/5.0 (compatible; Nmap Scripting Engine)', 'Apache-HttpClient/4.5.13',]
bot_traffic = data[data['useragent'].str.contains('|'.join(bots_user_agents), case=False)]
bot_analysis = bot_traffic.groupby(['useragent', 'ip']).size().reset_index(name='count').sort_values(by='count', ascending=False)
print("\nBot Traffic Analysis:")
print(bot_analysis.to_markdown())

# total number of bot requests
total_bot_requests = bot_traffic.shape[0]
print(f"\nTotal Bot Requests: {total_bot_requests}")

# counting the number of bots and their corresponding IPs
bot_count_by_ip = bot_traffic['ip'].value_counts().reset_index()
bot_count_by_ip.columns = ['ip', 'bot_count']
print("\nBot Count by IP:")
print(bot_count_by_ip.to_markdown())

# identifying the top countries with bot traffic
top_bot_countries = bot_traffic['country'].value_counts().reset_index()
top_bot_countries.columns = ['country', 'bot_count']
print("\nTop Countries with Bot Traffic:")
print(top_bot_countries.to_markdown())