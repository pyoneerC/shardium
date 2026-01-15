import secrets
import sys
import argparse

# --- Shamir's Secret Sharing Implementation ---
# We use a massive Mersenne prime to handle long seed phrases (up to ~550 characters)
PRIME = 2**4423 - 1 

def _eval_at(poly, x, prime):
    """Evaluates a polynomial at x in a finite field."""
    accum = 0
    for coeff in reversed(poly):
        accum = (accum * x + coeff) % prime
    return accum

def split(secret_int, n, k, prime):
    """Splits a secret into n shares, k of which are required to recover."""
    if k > n:
        raise ValueError("k must be <= n")
    # Secret is the constant term (poly[0])
    poly = [secret_int] + [secrets.randbelow(prime) for _ in range(k - 1)]
    points = [(i, _eval_at(poly, i, prime)) for i in range(1, n + 1)]
    return points

def _inverse(n, prime):
    """Modular inverse."""
    return pow(n, prime - 2, prime)

def recover(shares, prime):
    """Recovers the secret from shares using Lagrange interpolation."""
    if len(shares) < 2:
        raise ValueError("Need at least 2 shares")
    
    secret = 0
    for i, (x_i, y_i) in enumerate(shares):
        numerator = 1
        denominator = 1
        for j, (x_j, y_j) in enumerate(shares):
            if i == j:
                continue
            numerator = (numerator * (0 - x_j)) % prime
            denominator = (denominator * (x_i - x_j)) % prime
        
        lagrange = (y_i * numerator * _inverse(denominator, prime)) % prime
        secret = (secret + lagrange) % prime
        
    return secret

# --- CLI Tool ---

def main():
    parser = argparse.ArgumentParser(description="Shardium SSS Tool - Split your seed phrase into shards.")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Split command
    split_parser = subparsers.add_parser("split", help="Split a secret into 3 shards (2 required)")
    split_parser.add_argument("secret", help="The seed phrase or text to split")

    # Recover command
    recover_parser = subparsers.add_parser("recover", help="Recover secret from 2 shards")
    recover_parser.add_argument("shard1", help="First shard (format: index-value)")
    recover_parser.add_argument("shard2", help="Second shard (format: index-value)")

    args = parser.parse_args()

    if args.command == "split":
        # Convert string to large integer
        secret_bytes = args.secret.encode('utf-8')
        secret_int = int.from_bytes(secret_bytes, byteorder='big')
        
        if secret_int >= PRIME:
            print("Error: Secret is too long for this implementation. Keep it under 550 characters.")
            return

        points = split(secret_int, 3, 2, PRIME)
        
        print("\n--- SHARDIUM SSS SPLIT (2-of-3) ---")
        print("Keep these shards in separate physical locations.")
        print("Any TWO are required to recover your original seed.\n")
        for i, (x, y) in enumerate(points):
            # Encode share as a string: x-y_hex
            share_str = f"{x}-{hex(y)}"
            print(f"Shard {chr(65+i)}: {share_str}")
        print("\n----------------------------------")

    elif args.command == "recover":
        try:
            x1, y1_hex = args.shard1.split('-')
            x2, y2_hex = args.shard2.split('-')
            
            shares = [
                (int(x1), int(y1_hex, 16)),
                (int(x2), int(y2_hex, 16))
            ]
            
            secret_int = recover(shares, PRIME)
            
            # Convert back to string
            secret_bytes = secret_int.to_bytes((secret_int.bit_length() + 7) // 8, byteorder='big')
            print(f"\nRecovered Secret: {secret_bytes.decode('utf-8')}")
        except Exception as e:
            print(f"Error during recovery: {e}")
            print("Usage example: python seed_split.py recover 1-0xabc... 2-0xdef...")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
