class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image

        queue = []
        originalPoint = (sr, sc)
        queue.append(originalPoint)

        while len(queue) > 0:
            visiting = queue.pop()
            image[visiting[0]][visiting[1]] = newColor
            if (visiting[0] - 1 >= 0 and image[visiting[0] - 1][visiting[1]] == oldColor):
                queue.append((visiting[0] - 1, visiting[1]))
            if (visiting[0] + 1 < len(image) and image[visiting[0] + 1][visiting[1]] == oldColor):
                queue.append((visiting[0] + 1, visiting[1]))
            if (visiting[1] - 1 >= 0 and image[visiting[0]][visiting[1] - 1] == oldColor):
                queue.append((visiting[0], visiting[1] - 1))
            if (visiting[1] + 1 < len(image[0]) and image[visiting[0]][visiting[1] + 1] == oldColor):
                queue.append((visiting[0], visiting[1] + 1))

        return image
