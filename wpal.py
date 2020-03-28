#!/usr/bin/env python

"""
wpal (workout pal is command-line tool to generate different exercises based on
user input. It serves (or will serve) as a quick inventory of exercises for:
1. body-weight exercises
2. resistance band exercises
3. weighted exercises
"""

import sys

TRICEPS = [
    # TRICEPS[0] = resistance band triceps exercises
    ["reverse grip triceps band kickback",
     "hammer grip triceps band kickback",
     "palms up triceps band kickback",
     "standing single arm triceps band extensions",
     "standing triceps band pushdowns",
     "kneeling triceps band pushdowns",
     "overhead triceps band extensions"],

    # TRICEPS[1] = body-weight exercises for triceps
    ["triceps bench dips",
     # note: name needs to be fixed
     "triceps bench push aways"]
]

BICEPS = [
    # BICEPS[0] = resistance band biceps exercises
    ["seated resistance band bicep curl",
     "standing resistance band bicep curl",
     "resistance band bicep curl to reverse lunge",
     "standing single arm triceps band extensions"],

    # BICEPS[1] = body-weight biceps exercises
    ["chin-ups",
     "inverted bicep curls"]
]

TRAPS = [
    # TRAPS[0] = resistance band trap exercises
    ["wide stance resistance band shrugs",
     "resistance band shrugs",
     "resistance band Y raises",
     "resistance band seated W raises",
     "resistance band face pulls"],

    # TRAPS[1] = Weighted Plate raises
    [
        "weighted plate raises"
    ]
]

SHOULDERS = [
    # SHOULDERS[0] resistance band shoulder exercises
    ["standing resistance band lateral raises",
     "resistance band shoulder press",
     "resistance band real delt flyes",
     "seated reverse flyes"],

    # SHOULDERS[1] = body-weight shoulder exercises
    ["pike push-ups"]
]

CHEST = [
    # CHEST[0] resistance band exercices
    ["resistance band push-ups",
     "incline resistance band push-ups",
     "resistance band chest press",
     "banded crossover push up",
     "resistance band low to high crossovers"],

    # CHEST[1] = body-weight chest exercises
    ["push-ups",
     "incline push-ups"]
]

LEGS = [
    # LEGS[0] resistance band exercices
    ["resistance band overhead squat",
     "resistance band deadlift",
     "resistance band stiff-legged deadlift",
     "resistance band lunge to squat"],

    # CHEST[1] = body-weight chest exercises
    ["bodyweight squats",
     "body-weight split squats",
     "body-weight reverse lunges"]
]

CALVES = [
    # CALVES[0] resistance band exercices
    ["anchored resistance band calf raises"],

    # CALVES[1] = body-weight chest exercises
    ["staircase calf raises",
     "seated calf raises"]
]


def triceps_workout(workout_mean):
    """Return triceps workouts based on the requested workout means"""
    if workout_mean == "bands":
        print("-" * 80 + "\nRes. band exercises for triceps:\n" + "-" * 80)
        for item in TRICEPS[0]:
            print(item)
    if workout_mean == "bodyweight":
        print("-" * 80 + "\nBody-weight exercises for triceps:\n" + "-" * 80)
        for item in TRICEPS[1]:
            print(item)


def biceps_workout(workout_mean):
    """Return bicep workouts based on the requested workout means"""
    if workout_mean == "bands":
        print("-" * 80 + "\nRes. band exercises for biceps:\n" + "-" * 80)
        for item in BICEPS[0]:
            print(item)
    if workout_mean == "bodyweight":
        print("-" * 80 + "\nBody-weight exercises for biceps:\n" + "-" * 80)
        for item in BICEPS[1]:
            print(item)


def shoulders_workout(workout_mean):
    """Return shoulders workouts based on the requested workout means"""
    if workout_mean == "bands":
        print("-" * 80 + "\nRes. band exercises for shoulders:\n" + "-" * 80)
        for item in SHOULDERS[0]:
            print(item)
    if workout_mean == "bodyweight":
        print("-" * 80 + "\nBody-weight exercises for shoulders:\n" + "-" * 80)
        for item in SHOULDERS[1]:
            print(item)


def chest_workout(workout_mean):
    """Return chest workouts based on the requested workout means"""
    if workout_mean == "bands":
        print("-" * 80 + "\nRes. band exercises for the chest:\n" + "-" * 80)
        for item in CHEST[0]:
            print(item)
    if workout_mean == "bodyweight":
        print("-" * 80 + "\nBody-weight exercises for the chest:\n" + "-" * 80)
        for item in CHEST[1]:
            print(item)


def legs_workout(workout_mean):
    """Return leg workouts based on the requested workout means"""
    if workout_mean == "bands":
        print("-" * 80 + "\nRes. band exercises for legs:\n" + "-" * 80)
        for item in LEGS[0]:
            print(item)
    if workout_mean == "bodyweight":
        print("-" * 80 + "\nBody-weight exercises for legs:\n" + "-" * 80)
        for item in LEGS[1]:
            print(item)


def calves_workout(workout_mean):
    """Return calves workouts based on the requested workout means"""
    if workout_mean == "bands":
        print("-" * 80 + "\nRes. band exercises for calves:\n" + "-" * 80)
        for item in CALVES[0]:
            print(item)
    if workout_mean == "bodyweight":
        print("-" * 80 + "\nBody-weight exercises for calves:\n" + "-" * 80)
        for item in CALVES[1]:
            print(item)


def usage():
    """print usage and exit"""
    print("{} [SUBCOMMAND] [BODY_PART]".format(sys.argv[0]))
    print("SUBCOMMANDS: band, bodyweight ]")
    bd_parts = "biceps, triceps, shoulders, traps, legs, calves, chest, back"
    print("BODY_PART: {}".format(bd_parts))


def main():
    """Our main func, start here"""

    # if len(sys.argv) == 1 or len(sys.argv) != 3:
    #     usage()
    if len(sys.argv) != 3:
        usage()

    # print(len(sys.argv))
    if len(sys.argv) == 3:
        if sys.argv[1] != "band" and sys.argv[1] != "bodyweight":
            usage()
            sys.exit(1)

        if sys.argv[2] == "triceps":
            if sys.argv[1] == "band":
                triceps_workout("bands")
            elif sys.argv[1] == "bodyweight":
                triceps_workout("bodyweight")
        if sys.argv[2] == "biceps":
            if sys.argv[1] == "band":
                biceps_workout("bands")
            elif sys.argv[1] == "bodyweight":
                biceps_workout("bodyweight")
        if sys.argv[2] == "shoulders":
            if sys.argv[1] == "band":
                shoulders_workout("bands")
            elif sys.argv[1] == "bodyweight":
                shoulders_workout("bodyweight")
        if sys.argv[2] == "chest":
            if sys.argv[1] == "band":
                chest_workout("bands")
            elif sys.argv[1] == "bodyweight":
                chest_workout("bodyweight")
        if sys.argv[2] == "legs":
            if sys.argv[1] == "band":
                legs_workout("bands")
            elif sys.argv[1] == "bodyweight":
                legs_workout("bodyweight")
        if sys.argv[2] == "calves":
            if sys.argv[1] == "band":
                calves_workout("bands")
            elif sys.argv[1] == "bodyweight":
                calves_workout("bodyweight")


if __name__ == "__main__":
    main()
