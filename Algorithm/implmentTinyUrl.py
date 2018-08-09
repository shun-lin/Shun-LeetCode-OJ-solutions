class Codec:

    tinyURLRoot = 'http://tinyurl.com/'

    # the key for this storage is the longUrl and value is shortUrl
    encodingStorage = dict()
    # vise versa
    decodingStorage = dict()
    nextAvailableShortURL = "1"

    def updateNextAvailableShortURL(self):
        strip_zs = self.nextAvailableShortURL.rstrip('z')
        if strip_zs:
            self.nextAvailableShortURL =  strip_zs[:-1] + chr(ord(strip_zs[-1]) + 1) + 'a' * (len(self.nextAvailableShortURL) - len(strip_zs))
        else:
            self.nextAvailableShortURL =  'a' * (len(self.nextAvailableShortURL) + 1)

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.encodingStorage:
            return tinyURLRoot + self.encodingStorage[longUrl]

        shortUrl = self.tinyURLRoot + self.nextAvailableShortURL
        self.encodingStorage[longUrl] = shortUrl
        self.decodingStorage[shortUrl] = longUrl
        self.updateNextAvailableShortURL()

        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        if (shortUrl in self.decodingStorage):
            return self.decodingStorage[shortUrl]

        return ''





# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
