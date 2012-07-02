import bencode

class BitTorrentFile(object):
    def __init__(self, torrent):
        if isinstance(torrent, basestring):
            with open(torrent, "rb+") as fh:
                self.contents = bencode.bdecode(fh.read().rstrip("\n"))
        else:
            self.contents = bencode.bdecode(torrent.read().rstrip("\n"))

    def add_tracker(self, tracker):
        self.trackers.append(tracker)

    @property
    def name(self):
        return self.contents['info']['name']

    @property
    def main_tracker(self):
        return self.contents['announce']

    @property
    def comment(self):
        return self.contents['comment']

    @property
    def files(self):
        return self.contents['info']['files']

    @property
    def trackers(self):
        try:
            return self.contents['announce-list']
        except KeyError:
            self.contents['announce-list'] = [ ]
            return self.contents['announce-list']

    def __str__(self):
        return bencode.bencode(self.contents)


