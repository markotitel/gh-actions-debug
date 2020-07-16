import os

ref = os.environ['GITHUB_REF'].split('/')[2]
sha = os.environ['GITHUB_SHA'][:8]
run_id = os.environ['GITHUB_RUN_ID']


print(ref)
print(sha)
print(run_id)

if 'tag-test' in ref:
    print("Tag commit")
