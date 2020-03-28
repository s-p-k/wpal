# wpal
Workout pal - A CLI tool written in python to server as an exercises inventory
based on available means (body-weight, resistance bands, full gym etc).

#### Usage:

```bash
$ ./wpal.py [SUBCOMMAND] [BODY_PART]
SUBCOMMANDS: band, bodyweight ]
BODY_PART: biceps, triceps, shoulders, traps, legs, calves, chest, back
```

#### Examples
```bash
$ ./wpal.py bodyweight triceps
--------------------------------------------------------------------------------
Body-weight exercises for triceps:
--------------------------------------------------------------------------------
triceps bench dips
triceps bench push aways
```

```bash
$ ./wpal.py band shoulders
--------------------------------------------------------------------------------
Res. band exercises for shoulders:
--------------------------------------------------------------------------------
standing resistance band lateral raises
resistance band shoulder press
resistance band real delt flyes
seated reverse flyes
```
