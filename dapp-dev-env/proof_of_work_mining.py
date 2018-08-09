from sha3 import keccak_256
import sys
import time


def mine_block(difficulty):
    target = 2**256 // difficulty

    # Pad the number to 32 bytes, 64 hex, withe leading 0x
    print('New block target:', '{0:#0{1}x}'.format(target, 66))

    # Randomly guess numbers
    for i in range(100000000):
        print('Trying: ', i)

        # Generate the hash and see if you have found the answer
        hashed_value = keccak_256(bytes(i)).digest()
        int_hash = int.from_bytes(hashed_value, byteorder='big')  # conver to int to compare against target

        # Answer found return the solution
        if int_hash <= target:
            return {
                'nonce': i,
                'hash': int_hash,
                'target': target
            }

    return bytes(0)


# Timer to measure mining vs. validating
class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start


if __name__ == '__main__':
    # Difficulty is computed... simulated with command line arg
    difficulty = int(sys.argv[1])

    # Miner races to find the solution
    with Timer() as t:
       solution = mine_block(difficulty)

    mining_time = t.interval

    print('Block Target:   ', '{0:#0{1}x}'.format(solution['target'], 66))
    print('Solution Nonce: ', '{0:#0{1}x}'.format(solution['nonce'], 66))
    print('Solution Hash:  ', '{0:#0{1}x}'.format(solution['hash'], 66))
    print('Mining the block took %.09f sec.' % mining_time)