
import argparse

from .analyzer import analyze_trend
from .comparator import compare_trends
from trendwatch.visualizer import plot_trends


def main():
    parser = argparse.ArgumentParser(
        description="TrendWatch - Trend Analysis Tool"
    )

    parser.add_argument(
        "command",
        choices=["analyze", "compare", "plot"],
        help="Command to run"
    )

    parser.add_argument(
        "topics",
        nargs="+",
        help="Topics to analyze or compare"
    )

    args = parser.parse_args()

    if args.command == "analyze":
        if len(args.topics) != 1:
            parser.error("Analyze requires one topic")

        result = analyze_trend(args.topics[0])

        print("\n--- TrendWatch Analysis ---")
        print(f"Topic: {result['topic']}")
        print(f"Score: {result['score']}")
        print(f"Status: {result['status']}")
        print(f"Direction: {result['direction']}")

    elif args.command == "compare":
        if len(args.topics) != 2:
            parser.error("Compare requires two topics")

        result = compare_trends(
            args.topics[0],
            args.topics[1]
        )

        if result is None:
            print("No comparison data found.")
            return

        print("\n--- TrendWatch Comparison ---")
        print(f"{result['topic1']}: {result['score1']}")
        print(f"{result['topic2']}: {result['score2']}")
        print(f"Higher search interest: {result['winner']}")


    elif args.command == "plot":
        if len(args.topics) != 2:
            parser.error("Plot requires two topics")

        plot_trends(
            args.topics[0],
            args.topics[1]
        )


if __name__ == "__main__":
    main()
