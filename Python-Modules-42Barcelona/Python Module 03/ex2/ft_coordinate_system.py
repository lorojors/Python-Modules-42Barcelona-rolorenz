import sys
import math

def parse_coordinate(coord_str):
    """Parse a coordinate string like '1,2,3' into a tuple (x, y, z)"""
    try:
        parts = coord_str.split(',')
        if len(parts) != 3:
            raise ValueError(f"Coordinate must have exactly 3 values, got {len(parts)}")
        
        x = float(parts[0].strip())
        y = float(parts[1].strip())
        z = float(parts[2].strip())
        
        return tuple((x, y, z))
    except ValueError as e:
        raise ValueError(f"Invalid coordinate '{coord_str}': {e}")

def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two 3D points"""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def main():
    print("=== Game Coordinate System ===")
    
    # Check if user provided coordinates
    if len(sys.argv) == 3:
        # User provided two coordinates
        try:
            position1 = parse_coordinate(sys.argv[1])
            position2 = parse_coordinate(sys.argv[2])
            distance = calculate_distance(position1, position2)
            print(f"Position 1: {position1}")
            print(f"Position 2: {position2}")
            print(f"Distance between {position1} and {position2}: {distance:.2f}")
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
        return
    
    # Default demonstration if no arguments provided
    origin = (0, 0, 0)
    position1 = (10, 20, 5)
    coord_str1 = "3,4,0"
    coord_str_invalid = "abc,def,ghi"
    
    # Display created position and distance from origin
    print(f"Position created: {position1}")
    distance1 = calculate_distance(origin, position1)
    print(f"Distance between {origin} and {position1}: {distance1:.2f}")
    
    # Parse valid coordinates
    print(f"Parsing coordinates: \"{coord_str1}\"")
    try:
        position2 = parse_coordinate(coord_str1)
        print(f"Parsed position: {position2}")
        distance2 = calculate_distance(origin, position2)
        print(f"Distance between {origin} and {position2}: {distance2}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
    
    # Parse invalid coordinates
    print(f"Parsing invalid coordinates: \"{coord_str_invalid}\"")
    try:
        invalid_position = parse_coordinate(coord_str_invalid)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details- Type: {type(e).__name__}, Args: {e.args}")
    
    # Demonstrate tuple unpacking
    print("Unpacking demonstration:")
    x, y, z = position2
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")

if __name__ == "__main__":
    main()