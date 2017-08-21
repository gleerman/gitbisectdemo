# Git Bisect demo
This mini project serves as a demo for the Git bisect feature. See the docs of [Git bisect](https://git-scm.com/docs/git-bisect) for more information.

## The demo
By running `script.py`, a process is started that creates numbereous commits. Each commit adds one line with the word `good` to `file.txt`. Only once, a line with the word `bad` is inserted - this is considered a bug.

The script cleans up all commits at startup, so it can just be used over again for demo purposes. The entire demo should consist of the following steps:

1. Run the script
```
$ ./script.py
```

2. Start the bisecting process to pinpoint where the script introduced the bug. Use the following command to indicate that `master` does not contain the bug, but `feature` does
```
$ git bisect start feature master --
```

3. Git will iteratively checkout a commit for which you can indicate if the bug is present by using `git bisect good` or `git bisect bad`. Alternatively, you can automate the process using the secondary script in the repo:
```
$ git bisect run ./wrongfinder.py
```

After these steps, HEAD is at the commit that inserted the `bad` line into `file.txt`.
Reset the HEAD using `git bisect reset`.
