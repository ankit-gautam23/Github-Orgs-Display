import json
import sys

orgs_file = sys.argv[1]

with open(orgs_file, 'r') as f:
    orgs = json.load(f)

org_links = [f"- [{org['login']}]({org['html_url']})" for org in orgs]

markdown_content = f"""### Contributions to Organizations{'\n'.join(org_links)}"""

print(markdown_content)
