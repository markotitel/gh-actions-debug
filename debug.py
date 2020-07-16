import os

print(os.environ['GITHUB_REF'].split('/')[2] + os.environ['GITHUB_RUN_ID'])
