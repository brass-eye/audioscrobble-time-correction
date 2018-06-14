import unittest
from audioscrobble_time_offset import *

class AudioScrobbleTimeOffsetTests(unittest.TestCase):

    def test_offset_audioscrobbler_line(self):
        old_time = 946705463
        old_scrobble = "Boris\tAmplifier Worship\tGanbou-Ki\t2\t969\tL\t946705463"
        ten_hours = 60*60*10
        expected_time = old_time + ten_hours
        expected_scrobble = "Boris\tAmplifier Worship\tGanbou-Ki\t2\t969\tL\t{}".format(expected_time)
        self.assertEqual(offset_audioscrobbler_line(old_scrobble, ten_hours), expected_scrobble)

if __name__ == '__main__':
    unittest.main()