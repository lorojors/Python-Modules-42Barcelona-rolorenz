from typing import Generator
import time

def game_event_stream(num_events: int) -> Generator[dict, None, None]:
    """Generate game events on-demand"""
    players = ["alice", "bob", "charlie", "diana", "eve"]
    events = ["killed monster", "found treasure", "leveled up", "defeated boss", "discovered dungeon"]
    
    for i in range(num_events):
        event_type = events[i % len(events)]
        player = players[i % len(players)]
        level = 5 + (i % 20)
        
        yield {
            "id": i + 1,
            "player": player,
            "level": level,
            "event": event_type
        }

def fibonacci_generator(limit: int) -> Generator[int, None, None]:
    """Generate Fibonacci numbers up to limit"""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

def prime_generator(limit: int) -> Generator[int, None, None]:
    """Generate prime numbers up to limit"""
    count = 0
    num = 2
    while count < limit:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1

def main():
    print("=== Game Data Stream Processor ===")
    
    num_events = 1000
    print(f"Processing {num_events} game events...\n")
    
    # Create the event stream generator
    event_stream = game_event_stream(num_events)
    
    # Show first few events
    for i in range(3):
        event = next(event_stream)
        print(f"Event {event['id']}: Player {event['player']} (level {event['level']}) {event['event']}")
    
    print("...")
    
    # Process remaining events and collect statistics
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0
    total_processed = 3  # Already processed 3 events
    
    start_time = time.time()
    
    for event in event_stream:
        total_processed += 1
        if event["level"] >= 10:
            high_level_count += 1
        if "treasure" in event["event"]:
            treasure_count += 1
        if "leveled up" in event["event"]:
            levelup_count += 1
    
    end_time = time.time()
    processing_time = end_time - start_time
    
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_processed}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print(f"Memory usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.3f} seconds")
    
    # Generator demonstrations
    print("\n=== Generator Demonstration ===")
    
    # Fibonacci sequence
    fib_gen = fibonacci_generator(10)
    fib_numbers = list(fib_gen)
    print(f"Fibonacci sequence (first 10): {', '.join(map(str, fib_numbers))}")
    
    # Prime numbers
    prime_gen = prime_generator(5)
    primes = list(prime_gen)
    print(f"Prime numbers (first 5): {', '.join(map(str, primes))}")

if __name__ == "__main__":
    main()