tree = [
  {
    "title": "Chapter 1: Sorting Spells",
    "chapters": [
      {
        "title": "1.1 Bubble Sort"
      },
      {
        "title": "1.2 Insertion Sort"
      },
      {
        "title": "1.3 Merge Sort"
      },
      {
        "title": "1.4 Quick Sort"
      }
    ]
  },
  {
    "title": "Chapter 2: Graphical Charms",
    "chapters": [
      {
        "title": "2.1 Graph Traversal",
        "chapters": [
          {
            "title": "2.1.1 Breadth-First Search"
          },
          {
            "title": "2.1.2 Depth-First Search"
          }
        ]
      },
      {
        "title": "2.2 Shortest Path",
        "chapters": [
          {
            "title": "2.2.1 Dijkstra's Algorithm"
          },
          {
            "title": "2.2.2 Bellman-Ford Algorithm"
          }
        ]
      }
    ]
  },
  {
    "title": "Chapter 3: Enchanting Trees",
    "chapters": [
      {
        "title": "3.1 Binary Trees",
        "chapters": [
          {
            "title": "3.1.1 Preorder Traversal"
          },
          {
            "title": "3.1.2 Inorder Traversal"
          },
          {
            "title": "3.1.3 Postorder Traversal"
          }
        ]
      },
      {
        "title": "3.2 Balanced Trees",
        "chapters": [
          {
            "title": "3.2.1 AVL Trees"
          },
          {
            "title": "3.2.2 Red-Black Trees"
          }
        ]
      }
    ]
  },
  {
    "title": "Chapter 4: Hexadecimal Hexes",
    "chapters": [
      {
        "title": "4.1 Hash Tables",
        "chapters": [
          {
            "title": "4.1.1 Linear Probing"
          },
          {
            "title": "4.1.2 Quadratic Probing"
          }
        ]
      },
      {
        "title": "4.2 Bloom Filters",
        "chapters": [
          {
            "title": "4.2.1 False Positive Probability"
          },
          {
            "title": "4.2.2 Optimal Parameters"
          },
          {
            "title": "4.2.3 Deletion Operations"
          }
        ]
      }
    ]
  }
]


def solution(book):
    collection = ''

    def walk(node):
        keys = node['title']
        chapters = node.get('chapters')
        if isinstance(chapters, list):
            return keys, solution(chapters)
        return "*" + keys, chapters

    for item in book:
        key, value = walk(item)
        collection += f"\n{key} {value if value else ""}"
    return collection


print(solution(tree))
