"""

    Ben Schedin
    Statistical Theory
    Standard Error

"""

import math
from matplotlib import pyplot as plt


def main():
    # TODO: Specify with/out replacement
    # TODO: Specify in/dependent trials
    # Given a specified event probability, how many events must occur to guarantee positive outcome? (dependent events)
    desirable_outcomes = 2
    total_outcomes = 256

    # probability of event occurring naturally
    event_prob = desirable_outcomes / total_outcomes

    # probability of not-event
    not_event_prob = 1 - event_prob

    curr_prob = not_event_prob
    curr_event = 1
    x = []
    y = []

    while curr_prob > 0.001:
        print("Event: {}, Cumulative Probability: {}".format(curr_event, curr_prob))
        x.append(curr_event)
        y.append(curr_prob)

        curr_event += 1
        curr_prob = curr_prob * curr_prob

    print(x)
    print(y)

    plt.cla()
    plt.plot(x, y)
    plt.title("Cumulative Probability for Sequential Non-Events\nDesirable Outcomes: {}, Total Outcomes: {}".format(desirable_outcomes, total_outcomes))
    plt.xlabel("Trial")
    plt.ylabel("Cumulative Probability")
    plt.show()


if __name__ == "__main__":
    main()
