import argparse

# Conversion functions

def convert_length(from_unit, to_unit, value):
    units = {'m': 1.0, 'km': 1000.0, 'ft': 0.3048, 'mi': 1609.34}
    try:
        meters = float(value) / units[from_unit]
        return meters * units[to_unit]
    except KeyError:
        raise ValueError("Invalid units. Supported units are: m, km, ft, mi.")
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid number.")

# Command-line interface setup

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Measurement Converter")
    parser.add_argument('type', choices=['length', 'weight', 'volume', 'temperature'], help='Type of conversion')
    parser.add_argument('from_unit', help='From unit')
    parser.add_argument('to_unit', help='To unit')
    parser.add_argument('value', help='Value to convert')

    args = parser.parse_args()

    if args.type == 'length':
        try:
            result = convert_length(args.from_unit, args.to_unit, args.value)
            print(f"{args.value} {args.from_unit} is equal to {result} {args.to_unit}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    # Add similar logic for other types of conversions (weight, volume, temperature)
