from typing import Dict, List, Tuple


BLOCKS: Dict[str, List[Tuple[List[int], ...]]] = {
    "O": [([1, 1], [1, 1])],
    "I": [
        ([0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]),
        ([0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]),
    ],
    "S": [([0, 1, 1], [1, 1, 0]), ([1, 0], [1, 1], [0, 1])],
    "Z": [
        ([1, 1, 0], [0, 1, 1]),
        ([0, 1], [1, 1], [1, 0]),
    ],
    "J": [
        ([0, 1], [0, 1], [1, 1]),
        ([1, 0, 0], [1, 1, 1]),
        ([1, 1], [1, 0], [1, 0]),
        ([1, 1, 1], [0, 0, 1]),
    ],
    "L": [
        ([1, 0], [1, 0], [1, 1]),
        ([1, 1, 1], [1, 0, 0]),
        ([1, 1], [0, 1], [0, 1]),
        ([0, 0, 1], [1, 1, 1]),
    ],
    "T": [
        ([1, 1, 1], [0, 1, 0]),
        ([0, 1], [1, 1], [0, 1]),
        ([0, 1, 0], [1, 1, 1]),
        ([1, 0], [1, 1], [1, 0]),
    ],
}
