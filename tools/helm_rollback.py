import subprocess
subprocess.run(["helm", "rollback", "sample-app", "0"])