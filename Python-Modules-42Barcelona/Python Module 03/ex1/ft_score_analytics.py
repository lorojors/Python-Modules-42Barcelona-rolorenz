import sys

def main():
    print("=== PixelMetrics 3000 Score Cruncher ===")
    print("Analyzing player scores from the command line...\n")
    
    scores = []
    
    # Process command line arguments
    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            if score < 0:
                print(f"Warning: Negative score '{arg}' detected - including anyway")
            scores.append(score)
        except ValueError:
            print(f"Invalid score: '{arg}' is not a number - skipping")
    
    # Check if we have any valid scores
    if not scores:
        print("No valid scores found! Please provide numeric scores as arguments.")
        print("Example: python ft_score_analytics.py 1500 2300 1800")
        return
    
    # Calculate statistics
    total_scores = len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)
    total_sum = sum(scores)
    average_score = total_sum / total_scores
    
    # Display results
    print("📊 SCORE ANALYSIS RESULTS 📊")
    print("=" * 40)
    print(f"Total Scores Processed: {total_scores}")
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")
    print(f"Total Sum: {total_sum}")
    print(f"Average Score: {average_score:.2f}")
    print("=" * 40)
    print("🎮 Game dev approved! Ready for the leaderboard! 🎮")

if __name__ == "__main__":
    main()